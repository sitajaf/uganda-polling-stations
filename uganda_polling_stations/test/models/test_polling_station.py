from unittest import TestCase

from uganda_polling_stations.models.polling_station import PollingStation


class PollingStationTest(TestCase):
    def test_should_convert_to_dictionary(self):
        polling_station = PollingStation(1, 01, "APAC", 002, "KWANIA COUNTY", 01, "ADUKU", 01, "ADYEDA", 01,
                                         "ADYEDA CENTRE")
        self.expected_dict = {"no": 1, "distCode": 1, "districtName": "APAC", "eaCode": 2,
                              "eaName": "KWANIA COUNTY", "subCountyCode": 1, "subCountyName": "ADUKU",
                              "parishCode": 1, "parishName": "ADYEDA",
                              "psCode": 1, "pollingStationName": "ADYEDA CENTRE"}

        self.assertEqual(polling_station.to_dict(), self.expected_dict)

    def test_should_convert_to_correct_dictionary(self):
        polling_station = PollingStation(2, 01, "APAC", 002, "KWANIA COUNTY", 01, "ADUKU", 01, "ADYEDA", 02,
                                         "APORWEGI P.7 SCHOOL")
        self.expected_dict = {"no": 2, "distCode": 1, "districtName": "APAC", "eaCode": 2,
                              "eaName": "KWANIA COUNTY", "subCountyCode": 1, "subCountyName": "ADUKU",
                              "parishCode": 1, "parishName": "ADYEDA",
                              "psCode": 2, "pollingStationName": "APORWEGI P.7 SCHOOL"}

        self.assertEqual(polling_station.to_dict(), self.expected_dict)

