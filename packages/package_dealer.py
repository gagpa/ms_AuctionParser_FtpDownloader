from packages.ftp_downloader import Fz44


class PackageDealer:
    __ftpd = {'ftpd44': Fz44}

    @classmethod
    def get_downloader(cls, ftpd_name):
        try:
            parser = cls.__ftpd[ftpd_name]
            return parser
        except KeyError:
            print(f'Ваш ключ: {ftpd_name} не подходит. Возможные ключи: {cls.__ftpd.keys()}')
            raise KeyError
