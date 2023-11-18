from utils import read_json, dump_json

'''
This file contains all the configuration for the API.
It reads configs from saved json files,
Then use their syntaxes as template to convert PyJSON to Python.
'''

# Load configuration
config_file = 'pyjson.config.json'
shortcut_file = 'pyjson.shortcut.json'
config = read_json(config_file)
shortcuts = read_json(shortcut_file)
dumped_config = dump_json(config)

# * Define keywords
# 1-word keywords
KEYWORDS = {
    **config['KEYWORDS'],
    **shortcuts['KEYWORDS']
}

# # Pair keywords
START_KEYWORDS = {
    **config['START_KEYWORDS'],
    **shortcuts['START_KEYWORDS']
}
END_KEYWORDS = {
    **config['END_KEYWORDS'],
    **shortcuts['END_KEYWORDS']
}

# Keywords for calculation and comparison
VAR_KEYWORDS = {
    **config['VAR_KEYWORDS'],
    **shortcuts['VAR_KEYWORDS']
}
CALC_KEYWORDS = {
    **VAR_KEYWORDS,
}

# Keywords for handling blocks
BLOCK_KEYWORDS = {
    **config['BLOCK_KEYWORDS'],
    **shortcuts['BLOCK_KEYWORDS']
}

# * Define all general keywords here

GENERAL_KEYWORDS = {
    **KEYWORDS,
    **START_KEYWORDS,
    **END_KEYWORDS
}

ALL_KEYWORDS = {
    **GENERAL_KEYWORDS,
    **CALC_KEYWORDS,
    **BLOCK_KEYWORDS
}

# template for compiler response
RESPONSE_TEMPLATE = {
    'status': 'success',
    'stdout': '',
    'stderr': ''
}
if __name__ == '__main__':
    print(KEYWORDS['print'] % 'Hello World')
