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
    **(shortcuts.get('KEYWORDS', {}) if shortcuts.get('KEYWORDS') else {})
}

# # Pair keywords
START_KEYWORDS = {
    **config['START_KEYWORDS'],
    **(shortcuts.get('START_KEYWORDS', {}) if shortcuts.get('START_KEYWORDS') else {})
}
END_KEYWORDS = {
    **config['END_KEYWORDS'],
    **(shortcuts.get('END_KEYWORDS', {}) if shortcuts.get('END_KEYWORDS') else {})
}

# Keywords for data types
VAR_KEYWORDS = {
    **config.get('VAR_KEYWORDS', {}),
    **(shortcuts.get('VAR_KEYWORDS', {}) if shortcuts.get('VAR_KEYWORDS') else {})
}

# Keywords for advanced data types
ADVANCED_TYPES_KEYWORDS = {
    **config['ADV_DATA_TYPES'],
    **(shortcuts.get('ADV_DATA_TYPES', {}) if shortcuts.get('ADV_DATA_TYPES') else {})
}

CALC_KEYWORDS = {
    **VAR_KEYWORDS,
    **ADVANCED_TYPES_KEYWORDS,
}

# Keywords for handling blocks
BLOCK_KEYWORDS = {
    **config['BLOCK_KEYWORDS'],
    **(shortcuts.get('BLOCK_KEYWORDS', {}) if shortcuts.get('BLOCK_KEYWORDS') else {})
}

# Keyword for bracket syntaxs
BRACKET_KEYWORDS = {
    **config['BRACKET_KEYWORDS'],
    **(shortcuts.get('BRACKET_KEYWORDS', {}) if shortcuts.get('BRACKET_KEYWORDS') else {})
}

# Non param keywords
NON_PARAM_KEYWORDS = {
    **config['NON_PARAM_KEYWORDS'],
    **(shortcuts.get('NON_PARAM_KEYWORDS', {}) if shortcuts.get('NON_PARAM_KEYWORDS') else {})
}

# * Define all general keywords here

GENERAL_KEYWORDS = {
    **KEYWORDS,
    **START_KEYWORDS,
    **END_KEYWORDS,
}

ALL_KEYWORDS = {
    **GENERAL_KEYWORDS,
    **CALC_KEYWORDS,
    **BLOCK_KEYWORDS,
    **BRACKET_KEYWORDS,
    **NON_PARAM_KEYWORDS,
}

# template for compiler response
RESPONSE_TEMPLATE = {
    'status': 'success',
    'stdout': '',
    'stderr': ''
}
if __name__ == '__main__':
    print(KEYWORDS)
