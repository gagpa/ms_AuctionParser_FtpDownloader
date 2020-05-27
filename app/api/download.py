from datetime import datetime
from threading import Thread
import os
import requests
from flask import jsonify, request

from configs import ConfigDealer
from packages import PackageDealer
from . import api


def download(start, days, ftpd_name, config_name, api_name):
    config = ConfigDealer.get_package(config_name)
    api_link = ConfigDealer.get_api_link(api_name)
    print(config.host, os.environ.get('FTP_HOST'))
    ftpd = PackageDealer.get_downloader(ftpd_name)(config)
    status, count = ftpd.download(start, days)
    requests.get(api_link, {'local_link': config.zips,
                            'status': status,
                            'count': count})


@api.route('/download')
def api_download():
    start_date = request.args.get('start', None)
    days = request.args.get('days', 1)
    config_name = 'ftpd44'
    ftpd_name = 'ftpd44'
    api_name = 'afiller'
    th = Thread(target=download, kwargs={'start': start_date,
                                         'days': days,
                                         'ftpd_name': ftpd_name,
                                         'config_name': config_name,
                                         'api_name': api_name})
    th.start()

    status = True
    return jsonify({'status': status,
                    'time': datetime.now()})
