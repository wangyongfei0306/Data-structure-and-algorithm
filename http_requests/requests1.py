import requests
import urllib.request, urllib3
URL_IP = 'http://127.0.0.1:5000/ip'


def use_simple_urllib():
    response = urllib.request.urlopen(URL_IP)
    print(response.info())
    print('------------------')
    print(response.readlines())


if __name__ == '__main__':
    use_simple_urllib()
