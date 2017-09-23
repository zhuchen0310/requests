# coding=utf-8

from retrying import retry
import requests
@retry(stop_max_attempt_number=3)
def _pares_url(url,headers):
    response = requests.get(url=url,headers=headers)
    assert response.status_code == 200
    return response.content.decode()


def pares_url(url,headers):
    try:
        return _pares_url(url=url,headers=headers)
    except:
        return None