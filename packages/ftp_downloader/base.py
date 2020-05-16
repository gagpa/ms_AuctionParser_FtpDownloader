from ftplib import FTP
from abc import ABC
from os import path, mkdir


class Base(ABC):
    """
    Базовый класс работы с FTP.
    """

    _ftp: FTP = None       # Соединение с FTP
    _HOST = None           # URL
    _USER = None           # Логин
    _PASSWORD = None       # Пароль
    _ROOT = None           # Начальная директория на FTP
    _ZIPS = None           # Локальная директория для архивов
    _current_path = _ROOT
    _regions = []

    debug: bool = False    # Debug-режим

    def __init__(self):
        self._connect(self._HOST, self._USER, self._PASSWORD)
        if self._ROOT:
            self._dir(self._ROOT)

    def _connect(self, host: str, user: str, password: str):
        """Коннект к FTP"""
        self._ftp = FTP(host, user, password)

    def _reconnect(self):
        """Реконнект к FTP"""
        self._connect(self._HOST, self._USER, self._PASSWORD)
        self._dir(self._current_dir)
        print('Reconnect', self._current_dir)

    def _dir(self, path: str):
        """Смена директории"""
        self._ftp.cwd(path)
        self._current_dir = self._ftp.pwd()
        if self.debug:
            print(self._current_dir)

    def _quit(self):
        """Закрытие соединения"""
        self._ftp.quit()

    def _prepare_save_dir(self) -> bool:
        """Создание директории для загрузки архивов"""
        if not path.isdir(self._ZIPS):
            mkdir(self._ZIPS)
        return True

    def _download_file(self, filename: str) -> bool:
        """Скачивание zip-архива"""
        local_zip = self._ZIPS + '/' + filename
        with open(local_zip, 'wb') as f:
            self._ftp.retrbinary('RETR ' + filename, f.write)

        return True

    def __del__(self):
        self._quit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._quit()
