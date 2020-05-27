import calendar
from datetime import datetime, timedelta

from .IDownloader import IDownloader
from .LimitReachedException import LimitReachedException
from .base import Base
from .regions import get_regions


class Fz44(IDownloader, Base):
    """
    Парсер ftp для 44ФЗ. Реализует функционал
    согласно особенностям структуры FTP для заданного закона.
    """

    _ROOT = 'fcs_regions'
    __total: int = 0  # Общее кол-во скаченных архивов
    limit: int = None  # Ограничение на кол-во архивов (для тестирования)

    def __init__(self, conf):
        self.init_config(conf)
        super(Fz44, self).__init__()

    def init_config(self, conf):
        self._HOST = conf.host
        print(self._HOST, conf.host)
        self._USER = conf.login
        self._PASSWORD = conf.password
        self._ZIPS = conf.zips

    def download(self, start_date: datetime = None, days: int = 1) -> (bool, int):
        """Скачивание за заданный срок"""
        if days < 1:
            raise ArithmeticError('days должен быть >= 1')

        if not self._prepare_save_dir():
            return False, self.__total

        today = datetime.now()

        if not start_date:
            start_date = today + timedelta(days=-1)

        active_date = start_date
        self.__total = 0
        status = False
        self._regions = get_regions()
        try:
            while days > 0:
                month_diff = today.month - active_date.month
                year_diff = today.year - active_date.year

                if not year_diff and not month_diff:
                    self._download_day(active_date, 'curr')
                    delta = 1
                elif not year_diff and month_diff == 1:
                    self._download_day(active_date, 'prev')
                    delta = 1
                else:
                    self._download_month(active_date)
                    delta = calendar.mdays[active_date.month]

                days -= delta
                active_date += timedelta(days=-delta)

            status = True
        except LimitReachedException:
            status = True

        return status, self.__total

    def _download_day(self, date: datetime, subdir):
        """Скачивание одного дня"""
        print('Downloading', date)

        day = datetime.strftime(date, '%Y%m%d')
        total = 0

        for region in self._regions:
            total += self._download_region(region, day, subdir)

        print('Downloaded', total)

    def _download_month(self, date: datetime):
        """Скачивание месяца"""
        print('Downloading', date)

        day = datetime.strftime(date, '%Y%m01')
        total = 0

        for region in self._regions:
            total += self._download_region(region, day)

        print('Downloaded', total)

        if not total:
            raise FileNotFoundError('Not found notification.zip')

    def _download_region(self, region: str, day: str, subdir: str = None) -> int:
        """Скачивание региона"""
        total = 0
        self._dir(region + '/notifications')
        zip_prefix = 'notification_{}_{}'.format(region, day)

        if self.debug:
            print(zip_prefix)

        if subdir == 'curr':
            total += self._download_path(zip_prefix, 'currMonth')
            self._dir('..')
            self._dir('..')
            return total

        if subdir == 'prev':
            total += self._download_path(zip_prefix, 'prevMonth')
            self._dir('..')
            self._dir('..')
            return total

        total += self._download_path(zip_prefix)
        self._dir('..')
        self._dir('..')

        return total

    def _download_path(self, zip_prefix: str, dir_name: str = None) -> int:
        """Скачивание пути"""
        if dir_name:
            self._dir(dir_name)

        filenames = self._ftp.nlst()
        total = 0
        for filename in filenames:
            part = filename[:len(zip_prefix)]
            if part == zip_prefix:
                if self.debug:
                    print('Match', part, zip_prefix)

                if self._download_file(filename):
                    self.__total += 1
                    total += 1
                    if self.limit and self.__total == self.limit:
                        raise LimitReachedException('Limit was ' + str(self.limit))

            elif self.debug:
                print('Not match', part, zip_prefix)

        if dir_name:
            self._dir('..')

        return total
