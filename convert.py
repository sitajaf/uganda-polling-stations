import os

from uganda_voter_register.converter.excel_to_json_converter import ExcelToJsonConverter


def convert():
    converter = ExcelToJsonConverter()

    json = converter.excel_to_json('register.xlsx')

    if not os.path.exists('dist'):
        os.makedirs('dist', 0755, True)

    with open('register.json', 'w') as _writer:
        _writer.write(json)

    print 'Conversion completed! Check in register.json in dist :)'


convert()
