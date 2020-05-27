from configs.app_configs import main_configs, api_links
from configs.package_configs import ConfigFtp44


class ConfigDealer:
    __main = main_configs
    __package = {'ftpd44': ConfigFtp44}
    __api_links = api_links

    @classmethod
    def get_main(cls, config_name):
        try:
            config = cls.__main[config_name]
            return config()
        except KeyError:
            print(f'Ваш ключ: {config_name} не подходит. Возможные ключи: {cls.__main.keys()}')
            raise KeyError

    @classmethod
    def get_package(cls, package_name):
        try:
            config = cls.__package[package_name]
            return config()
        except KeyError:
            print(f'Ваш ключ: {package_name} не подходит. Возможные ключи: {cls.__package.keys()}')
            raise KeyError

    @classmethod
    def get_api_link(cls, api_name):
        try:
            link = cls.__api_links[api_name]
            return link
        except KeyError:
            print(f'Ваш ключ: {api_name} не подходит. Возможные ключи: {cls.__api_links.keys()}')
            raise KeyError
