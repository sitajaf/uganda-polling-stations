import json
from unittest import TestCase

from uganda_voter_register.converter.excel_to_json_converter import ExcelToJsonConverter
from uganda_voter_register.models.polling_station import PollingStation

expectedMiniJson = json.dumps(
    [PollingStation(1, 01, "APAC", 002, "KWANIA COUNTY", 01, "ADUKU", 01, "ADYEDA", 01, "ADYEDA CENTRE").to_dict(),
     PollingStation(2, 01, "APAC", 002, "KWANIA COUNTY", 01, "ADUKU", 01, "ADYEDA", 02,
                    "APORWEGI P.7 SCHOOL").to_dict()])

expectedJson = json.dumps(
    [PollingStation(1, 01, "APAC", 002, "KWANIA COUNTY", 01, "ADUKU", 01, "ADYEDA", 01, "ADYEDA CENTRE").to_dict(),
     PollingStation(2, 01, "APAC", 002, "KWANIA COUNTY", 01, "ADUKU", 01, "ADYEDA", 02,
                    "APORWEGI P.7 SCHOOL").to_dict(),
     PollingStation(3, 01, "APAC", 002, "KWANIA COUNTY", 01, "ADUKU", 01, "ADYEDA", 03, "ADYEDA IMALO").to_dict(),
     PollingStation(4, 01, "APAC", 002, "KWANIA COUNTY", 01, "ADUKU", 02, "ALIRA", 01, "ALIRA B").to_dict(),
     PollingStation(5, 01, "APAC", 002, "KWANIA COUNTY", 01, "ADUKU", 02, "ALIRA", 02, "AKOT A").to_dict()])


class ExcelToJsonConverterTest(TestCase):
    def test_should_return_json_file(self):
        converter = ExcelToJsonConverter()

        converted_json = converter.excel_to_json('files/register_test_mini.xlsx')

        self.assertEqual(converted_json, expectedMiniJson)

    def test_should_return_corrected_json(self):
        converter = ExcelToJsonConverter()

        converted_json = converter.excel_to_json('files/register_test.xlsx')

        self.assertEqual(converted_json, expectedJson)
