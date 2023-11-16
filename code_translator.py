import json
import re
from typing import Union, Tuple, List
from config import START_KEYWORDS, END_KEYWORDS, GENERAL_KEYWORDS, CALC_KEYWORDS, ALL_KEYWORDS

'''
This file is responsible for converting PyJSON code to Python code.
'''


class Translator:
    def __init__(self, raw_code: Union[str, dict]) -> None:
        self.json_code = raw_code

        if isinstance(raw_code, str):
            self.json_code = json.loads(raw_code)

        self.python_code = ''
        self.indentation = '\t'

        self.start_keywords = START_KEYWORDS.copy()
        self.end_keywords = END_KEYWORDS.copy()
        self.general_keywords = GENERAL_KEYWORDS.copy()
        self.calc_keywords = CALC_KEYWORDS.copy()
        self.all_keywords = ALL_KEYWORDS.copy()

    def convert(self) -> Tuple[str, str]:
        try:
            converted_code = ''
            indent = 0
            for key, value in self.json_code.items():
                # read key until first number
                pattern = r'[a-zA-Z]+'
                start_term = re.search(pattern, key)
                start_term = str(start_term.group())
                current_indentation = self.indentation * indent

                if start_term not in self.all_keywords:
                    raise Exception(f'Keyword {key} is not supported')

                if indent < 0:
                    raise Exception('Indentation is less than 0')

                # start translating
                
                # Check if the current line is a calculation
                if start_term in self.calc_keywords:
                    formatted_code = self.calc_code_convert(keyword=start_term, expression=value)
                else:
                    formatted_code = self.general_keywords[start_term] % value

                # Add non-empty line to the converted code
                if formatted_code:
                    converted_code += f'{current_indentation}{formatted_code}\n'

                # Modify the indentation
                if start_term in self.start_keywords:
                    indent += 1
                elif start_term in self.end_keywords:
                    indent -= 1

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
