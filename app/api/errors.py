from flask import jsonify
from werkzeug.exceptions import HTTPException

from . import api


@api.app_errorhandler(404)
def handle_not_found(e):
    response = jsonify({'status': False,
                        'message': 'Страница не найдена'})
    response.status_code = 404
    return response


@api.errorhandler(Exception)
def handle_internal_error(e):
    if isinstance(e, HTTPException):
        response = jsonify({'status': False,
                            'message': 'HTTP ошибка'})
        response.status_code = 400

    elif isinstance(e, KeyError):
        response = jsonify({'status': False,
                            'message': 'Внутрення ошибка'})
        response.status_code = 501

    else:
        response = jsonify({'status': False,
                            'message': 'Внутрення ошибка сервера'})
        response.status_code = 500

    return response
