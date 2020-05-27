from os import environ


class ConfigFtp44:
    host = environ.get('FTP_HOST')
    login = environ.get('FTP_LOGIN')
    password = environ.get('FTP_PASSWORD')
    zips = environ.get('FTP_ZIPS')
