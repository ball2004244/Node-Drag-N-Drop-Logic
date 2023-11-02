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
            'range': 'range(%s)',
        }
        
        self.if_keywords = {
            'if': 'if %s:',
            'then': '%s',
            'condition': '%s',
            'else': 'else:\n%s%s' % (self.indentation, '%s'),
        }
        
        self.for_keywords = {
            'for': 'for %s:',
            'variable': '%s ',
            'in': 'in %s',
            'do': '%s',
        }
        
        self.while_keywords = {
            'while': 'while %s:',
            'do': '%s',
            'condition': '%s',
        }
        
        # merge all keywords
        self.all_keywords = {
            **self.keywords,
            **self.if_keywords,
            **self.for_keywords,
            **self.while_keywords,
        }

    def convert(self) -> str:
        try:
            converted_code = ''
            for key, value in self.json_code.items():
                if key not in self.all_keywords:
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
            return self.handle_basic(keyword, formatted_value)
        
        # return the same keyword if not in keywords
        return keyword
    
    def format_value(self, key: str, value: Union[str, dict, None]) -> Union[str, dict, None]:
        if not self.is_code_block(value):
            return value        
        code_block = f''
        
        #TODO: Implement if-else
        code_block += self.handle_if(key, value)

        #TODO: Implement for loop
        code_block += self.handle_for(key, value)

        #TODO: Implement while loop
        code_block += self.handle_while(key, value)
        
        #TODO: Implement def later
        
        #TODO: Implement class later

        return value

    
    def is_code_block(self, code: Union[str, dict, None]) -> bool:
        if isinstance(code, dict):
            return True
        return False
    
    def handle_basic(self, key: str, raw_code: Union[str, dict, None]) -> str:
        if key in self.keywords:
            return self.keywords[key] % raw_code
        
        return ''

    def handle_if(self, key: str, raw_code: Union[str, dict, None]) -> str:
        if key != 'if':
            return ''

        output = ''

        # get the condition
        condition = self.if_keywords['condition'] % raw_code['condition']
        if_code = self.if_keywords['if'] % condition
        then_code = self.if_keywords['then'] % raw_code['then']
        else_code = ''

        if 'else' in raw_code:
            else_code = self.if_keywords['else'] % raw_code['else']
        
        # format the condition
        # add to output
        output += f'{if_code}\n'
        output += f'{self.indentation}{then_code}\n'
        output += f'{else_code}\n'

        return output

    def handle_for(self, key: str, raw_code: Union[str, dict, None]) -> str:
        if key != 'for':
            return ''

        output = ''

        # get the condition
        condition = self.for_keywords['variable'] % raw_code['variable']
        in_code = self.for_keywords['in'] % raw_code['in']
        do_code = self.for_keywords['do'] % raw_code['do']
        for_code = self.for_keywords['for'] % (condition + in_code)

        # format the condition
        # add to output
        output += f'{for_code}\n'
        output += f'{self.indentation}{do_code}\n'

        return output

    def handle_while(self, key: str, raw_code: Union[str, dict, None]) -> str:
        if key != 'while':
            return ''

        output = ''

        # get the condition
        condition = self.while_keywords['condition'] % raw_code['condition']
        while_code = self.while_keywords['while'] % condition
        do_code = self.while_keywords['do'] % raw_code['do']

        # format the condition
        # add to output
        output += f'{while_code}\n'
        output += f'{self.indentation}{do_code}\n'

        return output

if __name__ == '__main__':
    code = ''
    filename = input('Enter filename: ')
    # read from file
    with open(filename, 'r') as f:
        code = f.read()
    
    translator = Translator(code)
    translated_code = translator.convert()
    
    # print(translated_code)
