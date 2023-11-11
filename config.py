from utils import read_json
import json

filename = 'pyjson.cofig.json'
pyjson_data = read_json(filename)
dumped_pyjson_data = json.dumps(pyjson_data)

KEYWORDS = pyjson_data['KEYWORDS']
START_KEYWORDS = pyjson_data['START_KEYWORDS']
END_KEYWORDS = pyjson_data['END_KEYWORDS']

ALL_KEYWORDS = {
    **KEYWORDS,
    **START_KEYWORDS,
    **END_KEYWORDS
}

RESPONSE_TEMPLATE = {
    'status': 'success',
    'stdout': '',
    'stderr': ''
}
if __name__ == '__main__':
    print(KEYWORDS['print'] % 'Hello World')