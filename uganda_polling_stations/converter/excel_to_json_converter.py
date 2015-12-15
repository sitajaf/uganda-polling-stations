import json

from openpyxl import load_workbook
from uganda_polling_stations.models.polling_station import PollingStation


class ExcelToJsonConverter:
    def __init__(self):
        pass

    def excel_to_json(self, file_path):
        work_book = load_workbook(file_path)
        work_book._active_sheet_index = 0
        work_sheet = work_book.active

        polling_stations = []
        for row in work_sheet.rows:
            if self.is_valid(row):
                polling_station = PollingStation(row[0].value, row[1].value, row[2].value, row[3].value, row[4].value,
                                                 row[5].value, row[6].value, row[7].value, row[8].value,
                                                 # TODO: an unknown cell is added in the 9th position, so skip it
                                                 row[10].value, row[11].value)
                polling_stations.append(polling_station.to_dict())

        return json.dumps(polling_stations)

    def is_valid(self, row):
        row_values = [cell.value for cell in row]
        if 'Table 1' in row_values or 'No' in row_values or 'DIST CODE' in row_values or 'DISTRICT NAME' in row_values \
                or 'EA CODE' in row_values or 'EA NAME' in row_values or 'SUB COUNTY CODE' in row_values \
                or 'SUB COUNTY NAME' in row_values or 'PARISH CODE' in row_values \
                or 'PARISH NAME' in row_values or 'PS CODE' in row_values or 'POLLING STATION NAME' in row_values \
                or row_values[0] is None:
            return False
        return True
