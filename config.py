from utils import read_json

filename = 'pyjson.cofig.json'
data = read_json(filename)

KEYWORDS = data['KEYWORDS']
START_KEYWORDS = data['START_KEYWORDS']
END_KEYWORDS = data['END_KEYWORDS']

ALL_KEYWORDS = {
    **KEYWORDS,
    **START_KEYWORDS,
    **END_KEYWORDS
}

if __name__ == '__main__':
    print(KEYWORDS['print'] % 'Hello World')