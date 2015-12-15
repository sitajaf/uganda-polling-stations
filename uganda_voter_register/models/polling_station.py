from simplejson import OrderedDict


class PollingStation:
    # TODO: district, subcounty and parish can be refactored into separate models :P
    def __init__(self, number, dist_code, district_name, ea_code, ea_name,
                 sub_county_code, sub_county_name, parish_code, parish_name, ps_code, ps_name):
        self.number = number
        self.dist_code = dist_code
        self.district_name = district_name
        self.ea_code = ea_code
        self.ea_name = ea_name
        self.sub_county_code = sub_county_code
        self.sub_county_name = sub_county_name
        self.parish_code = parish_code
        self.parish_name = parish_name
        self.ps_code = ps_code
        self.ps_name = ps_name

    def __unicode__(self):
        return 'ps code: %s ps name: %s' % (self.ps_code, self.ps_name)

    def to_dict(self):
        _dict = OrderedDict()
        _dict["NO"] = self.number
        _dict["DIST CODE"] = self.dist_code
        _dict["DISTRICT NAME"] = self.district_name
        _dict["EA CODE"] = self.ea_code
        _dict["EA NAME"] = self.ea_name
        _dict["SUB COUNTY CODE"] = self.sub_county_code
        _dict["SUB COUNTY NAME"] = self.sub_county_name
        _dict["PARISH CODE"] = self.parish_code
        _dict["PARISH NAME"] = self.parish_name
        _dict["PS CODE"] = self.ps_code
        _dict["POLLING STATION NAME"] = self.ps_name

        return _dict
