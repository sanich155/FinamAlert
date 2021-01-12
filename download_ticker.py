import requests

URL_figi = ''
URL_download = 'https://api-invest.tinkoff.ru/openapi/sandbox/market/candles'
TOKEN = 't.A2okbChoC7bsayzra72SaLWEv4EOr3XJkBF58rhHcRyDnlvANCnxIsxBRedmSbmgA8VRKba_Nlw5uiL-0R9iuw'


def find_figi(TOKEN, ticker):
      return figi

def download_ticker(TOKEN, figi, date_from, date_to):
    #скачивает инфу о тикере в json, создает .csv и записывает в него всё, что необходимо




headers = {'Authorization': 'Bearer ' + TOKEN}
pararams = {'Authorization': 'Bearer ' + TOKEN,
          'figi': 'BBG006G2JVL2',
            'from': '2019-08-07T15:35:00.029721253Z',
            'to': '2019-09-07T15:35:00.029721253Z',
            'interval': 'day'}

r = requests.get(URL, headers=headers, params=pararams)
print(r.json())