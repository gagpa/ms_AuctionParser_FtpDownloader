import os
from datetime import datetime
from threading import Thread
from time import sleep

import requests
from flask import jsonify, request

from configs import ConfigDealer
from packages import PackageDealer
from . import api


def download(start, days, ftpd_name, config_name, api_name):
    config = ConfigDealer.get_package(config_name)
    api_link = ConfigDealer.get_api_link(api_name)
    ftpd = PackageDealer.get_downloader(ftpd_name)(config)
    status, count = ftpd.download(start, days)
    requests.get(api_link, {'local_path': config.zips,
                            'status': status,
                            'count': count})


@api.route('/download')
def api_download():
    """Api скачки файлов аукциона"""
    start_date = request.args.get('start', None)
    days = request.args.get('days', 1)

    config_name = 'FTPD44'
    ftpd_name = 'FTPD44'
    api_name = 'AFILLER'

    download_path = ConfigDealer.get_package(config_name).zips
    if os.path.exists(download_path):
        first_measure = os.path.getsize(download_path)
    else:
        first_measure = 0

    th = Thread(target=download, kwargs={'start': start_date,
                                         'days': days,
                                         'ftpd_name': ftpd_name,
                                         'config_name': config_name,
                                         'api_name': api_name})
    th.start()

    sleep(1)
    second_measure = os.path.getsize(download_path)
    status = (second_measure - first_measure) > 0
    return jsonify({'first': first_measure,
                    'second': second_measure,
                    'status': status,
                    'time': datetime.now()})
