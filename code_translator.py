import re
from utils import read_json
from typing import Union, Tuple, List
from config import START_KEYWORDS, END_KEYWORDS, GENERAL_KEYWORDS, CALC_KEYWORDS, BLOCK_KEYWORDS, ALL_KEYWORDS

'''
This file is responsible for converting PyJSON code to Python code.
'''


class Translator:
    def __init__(self, raw_code: Union[str, dict]) -> None:
        self.json_code = raw_code

        if isinstance(raw_code, str):
            self.json_code = read_json(raw_code)

        self.python_code = ''
        self.indentation = '\t'
        self.indent = 0

        self.start_keywords = START_KEYWORDS.copy()
        self.end_keywords = END_KEYWORDS.copy()
        self.general_keywords = GENERAL_KEYWORDS.copy()
        self.calc_keywords = CALC_KEYWORDS.copy()
        self.block_keywords = BLOCK_KEYWORDS.copy()
        self.all_keywords = ALL_KEYWORDS.copy()

    def convert(self, json_code: Union[str, dict] = None) -> Tuple[str, str]:
        try:
            if json_code is None:
                json_code = self.json_code

            if isinstance(json_code, str):
                json_code = read_json(json_code)

            converted_code = ''
            for key, value in json_code.items():
                # * KEYWORD VALIDATION
                pattern = r'[a-zA-Z]+'
                start_term = re.search(pattern, key)
                start_term = str(start_term.group())
                current_indentation = self.indentation * self.indent

                if start_term not in self.all_keywords:
                    raise Exception(f'Keyword {key} is not supported')

                if self.indent < 0:
                    raise Exception('Indentation is less than 0')

                # * START TRANSLATION

                # Process block keywords by recursively calling the convert function
                if start_term in self.block_keywords:
                    converted_code += f'{current_indentation}{self.block_keywords[start_term] % value[0]}'
                    self.indent += 1
                    converted_code += f'{self.convert(value[1])[1]}\n'
                    self.indent -= 1
                    continue

                # Check if the current line is a calculation
                if start_term in self.calc_keywords:
                    formatted_code = self.calc_code_convert(
                        keyword=start_term, expression=value)
                else:
                    formatted_code = self.general_keywords[start_term] % value

                # Add non-empty line to the converted code
                if formatted_code:
                    converted_code += f'{current_indentation}{formatted_code}\n'

                # * INDENTATION HANDLING
                if start_term in self.start_keywords:
                    self.indent += 1
                elif start_term in self.end_keywords:
                    self.indent -= 1

            return 'success', converted_code

        except Exception as e:
            # get the line of error
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            lineno = exc_tb.tb_lineno
            print('Error converting code')
            print(e)
            print(f"Line of error: {lineno}")

            return 'error', str(e)

    # Convert PyJSON expression to Python expression
    def calc_code_convert(self, keyword: str, expression: List[str]) -> str:
        # TODO: Implement the calculation for PyJSON code
        try:
            output = ''

            # Get properties of the expression
            var_type: str = keyword
            var_name: str = expression[0]
            var_value: str = expression[1]

            # Check if the variable type is valid
            if var_type not in self.calc_keywords:
                raise Exception(f'Invalid variable type: {var_type}')

            # Check if the variable name is valid
            pattern = r'[a-zA-Z_][a-zA-Z0-9_]*'
            if not re.match(pattern, var_name):
                raise Exception(f'Invalid variable name: {var_name}')

            # Convert the variable value to Python code
            output = self.calc_keywords[var_type] % (var_name, var_value)

            return output

        except Exception as e:
            print('Error converting calculation code')
            print(e)
            return ''


if __name__ == '__main__':
    code = ''
    filename = input('Enter filename: ')
    # read from file
    with open(filename, 'r') as f:
        code = f.read()

    translator = Translator(code)
    translated_code = translator.convert()

    print(translated_code)
