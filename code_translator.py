import json
import re
from typing import Union

class Translator:
    def __init__(self, raw_code: Union[str, dict]) -> None:
        self.json_code = raw_code
        
        if isinstance(raw_code, str):
            self.json_code = json.loads(raw_code)

        self.python_code = ''
        self.indentation = '\t'

        self.variables = {}
        
        self.keywords = {
            'print': 'print(%s)',
        }
        
        self.start_keywords = {
            'for': 'for %s:',
            'while': 'while %s:',
            'if': 'if %s:',
        }
        
        self.end_keywords = {
            'endfor': '%s',
            'endwhile': '%s',
            'endif': '%s',
        }

        self.all_keywords = {
            **self.keywords,
            **self.start_keywords,
            **self.end_keywords,
        }

    def convert(self) -> str:
        try:
            converted_code = ''
            indent = 0
            for key, value in self.json_code.items():
                # read key until first number
                pattern = r'[a-zA-Z]+'
                start_term = re.search(pattern, key)
                start_term = str(start_term.group())
                print('Converting key:%s to %s' % (key, start_term))
                current_indentation = self.indentation * indent

                if start_term not in self.all_keywords:
                    raise Exception(f'Keyword {key} is not supported')

                if indent < 0:
                    raise Exception('Indentation is less than 0')

                # start translating
                formatted_code = self.all_keywords[start_term] % value
                converted_code += f'{current_indentation}{formatted_code}\n'

                if start_term in self.start_keywords:
                    indent += 1
                elif start_term in self.end_keywords:
                    indent -= 1

            return converted_code

        except Exception as e:
            # get the line of error
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            lineno = exc_tb.tb_lineno
            print('Error converting code')
            print(e)
            print(f"Line of error: {lineno}")

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
