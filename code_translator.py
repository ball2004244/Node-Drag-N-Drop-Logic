import json
from typing import Union

class Translator:
    def __init__(self, raw_code: str) -> None:
        self.json_code = json.loads(raw_code)
        self.python_code = ''
        self.indentation = '\t'
        
        self.variables = {}
        self.keywords = {
            'print': 'print("%s")',
            'if': 'if %s:',
            'else': 'else:',
            'for': 'for %s:',
            'in': 'in %s',
            'while': 'while %s:',
            'range': 'range(%s)',
        }
        
        self.pseudo_keywords = {
            'do': '%s',
            'then': '%s',
            'condition': '%s',
            'variable': '%s',
        }
        
        self.code_block_keywords = {
            'if',
            'for',
            'while'
        }
        
    def handle_if(self, raw_code: str) -> str:
        pass
    
    def handle_for(self, raw_code: str) -> str:
        pass

    def convert(self) -> str:
        try:
            converted_code = ''
            for key, value in self.json_code.items():
                if key not in self.keywords and key not in self.pseudo_keywords:
                    raise Exception(f'Keyword {key} is not supported')

                # start translating
                formatted_keyword = self.format_keyword(key, value)
                converted_code += f'{formatted_keyword}\n'

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

    
    def format_keyword(self, keyword: str, value: Union[str, dict, None]) -> str:
        formatted_value = self.format_value(keyword, value)
        
        # Return code block directly from format_value function
        if self.is_code_block(value):
            return str(formatted_value)

        if keyword in self.keywords:
            return self.keywords[keyword] % str(formatted_value)
        
        if keyword in self.pseudo_keywords:
            return self.pseudo_keywords[keyword] % str(formatted_value)

        return keyword
    
    def format_value(self, key: str, value: Union[str, dict, None]) -> str:
        if not self.is_code_block(value):
            return value
        
        code_block = f'{key} - This is a code-block'
        
        #TODO: Implement if-else

        #TODO: Implement for loop
        
        #TODO: Implement while loop
        
        
        #TODO: Implement def
        
        #TODO: Implement class

        return code_block

    
    def is_code_block(self, code: Union[str, dict, None]) -> bool:
        if isinstance(code, dict):
            return True
        return False
    
if __name__ == '__main__':
    code = ''
    filename = input('Enter filename: ')
    # read from file
    with open(filename, 'r') as f:
        code = f.read()
    
    translator = Translator(code)
    translated_code = translator.convert()
    
    print(translated_code)
