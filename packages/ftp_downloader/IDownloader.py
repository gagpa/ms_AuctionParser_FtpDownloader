from abc import ABC, abstractmethod


class IDownloader(ABC):
    """
    Интерфейс парсера аукциона.
    """

    @abstractmethod
    def download(self, start_date=None, end_date=None) -> [bool, int]:
        """
        Скачивание за заданный срок

        Если не не педедан start_date, то скачивается за вчерашний день.
        Если не передан end_date, то скачивается только за день указанный в start_date
        """
        pass
