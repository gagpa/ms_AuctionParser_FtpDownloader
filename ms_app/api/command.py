from . import api
from ms_app import api_links, ConfigFtp44

from ftp_downloader import Fz44 as Ftp
from threading import Thread
import requests
from flask import jsonify, request
from datetime import datetime


@api.route('/download')
def download():
    def do_work(start, days):
        config = ConfigFtp44()
        ftp = Ftp(config)
        status, count = ftp.download(start, days)
        local_link = config.zips
        link = api_links['autofiller']
        if status:
            requests.get(link, {'local_link': local_link,
                                'status': status,
                                'count': count
                                })
        requests.get(link, {'local_link'})
    status = False  # TODO
    start_date = request.args.get('start', None)
    days = request.args.get('days', 1)
    th = Thread(target=do_work, kwargs={'start': start_date,
                                        'days': days})
    th.start()
    status = True
    return jsonify({'status': status,
                    'time': datetime.now()})
