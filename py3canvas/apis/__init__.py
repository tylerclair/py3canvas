import os
import requests
ACCESS_TOKEN = os.environ.get('CANVAS_TOKEN', None)
URL_INSTANCE = 'https://usu.instructure.com'


class AccessTokenMissingError(Exception):
    pass

if ACCESS_TOKEN is None:
    raise AccessTokenMissingError('There is no access token specified. You need to specify an '
                                  'access token in order to use the Canvas API.')
session = requests.session()
session.headers.update({'Authorization': 'Bearer {}'.format(ACCESS_TOKEN)})