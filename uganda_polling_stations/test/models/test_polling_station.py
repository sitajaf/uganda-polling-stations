from unittest import TestCase

from uganda_polling_stations.models.polling_station import PollingStation


class PollingStationTest(TestCase):
    def test_should_convert_to_dictionary(self):
        polling_station = PollingStation(1, 01, "APAC", 002, "KWANIA COUNTY", 01, "ADUKU", 01, "ADYEDA", 01,
                                         "ADYEDA CENTRE")
        self.expected_dict = {"NO": 1, "DIST CODE": 1, "DISTRICT NAME": "APAC", "EA CODE": 2,
                              "EA NAME": "KWANIA COUNTY", "SUB COUNTY CODE": 1, "SUB COUNTY NAME": "ADUKU",
                              "PARISH CODE": 1, "PARISH NAME": "ADYEDA",
                              "PS CODE": 1, "POLLING STATION NAME": "ADYEDA CENTRE"}

        self.assertEqual(polling_station.to_dict(), self.expected_dict)

    def test_should_convert_to_correct_dictionary(self):
        polling_station = PollingStation(2, 01, "APAC", 002, "KWANIA COUNTY", 01, "ADUKU", 01, "ADYEDA", 02,
                                         "APORWEGI P.7 SCHOOL")
        self.expected_dict = {"NO": 2, "DIST CODE": 1, "DISTRICT NAME": "APAC", "EA CODE": 2,
                              "EA NAME": "KWANIA COUNTY", "SUB COUNTY CODE": 1, "SUB COUNTY NAME": "ADUKU",
                              "PARISH CODE": 1, "PARISH NAME": "ADYEDA",
                              "PS CODE": 2, "POLLING STATION NAME": "APORWEGI P.7 SCHOOL"}

        self.assertEqual(polling_station.to_dict(), self.expected_dict)

