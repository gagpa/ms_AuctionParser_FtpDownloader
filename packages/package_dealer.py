from packages.ftp_downloader import downloaders


class PackageDealer:

    __downloaders = downloaders

    @classmethod
    def get_downloader(cls, ftpd_name):
        try:
            parser = cls.__downloaders[ftpd_name]
            return parser
        except KeyError:
            print(f'Ваш ключ: {ftpd_name} не подходит. Возможные ключи: {cls.__downloaders.keys()}')
            raise KeyError
