import os
from uganda_polling_stations.converter.excel_to_json_converter import ExcelToJsonConverter


def convert():
    converter = ExcelToJsonConverter()

    json = converter.excel_to_json('files/register_test_mini.xlsx')

    if not os.path.exists('dist'):
        os.makedirs('dist', 0755, True)

    with open('dist/polling-stations-test-mini.json', 'w') as _writer:
        _writer.write(json)

    print 'Conversion completed! Check in uganda-polling-stations.json in dist :)'


convert()
