# !coding=utf-8
import datetime
import pytz
import analyzedutil as aul
class node:
    ip = ""
    AS = ""
    next = ""
    isp = ""
    cou = ""
    couCode = ""
    prov = ""
    lat = ""
    lng = ""
    FindTime = ""
    dataOK = ""
    owner = ""

    def __init__(self, ip,lang="ch"):
        self.ip = ip
        record = aul.getrecord(ip,lang)
        if record == 1:
            self.dataOK = False
            return
        self.dataOK = True
        self.isp = aul.filterNull(record.get('isp', b'').decode("utf-8"))
        self.lat = aul.filterNull(record.get('latwgs', b'').decode("utf-8"))
        self.lng = aul.filterNull(record.get('lngwgs', b'').decode("utf-8"))
        self.prov = aul.filterNull(record.get('province', b'').decode("utf-8"))
        self.AS = "ASN"+str(aul.filterNull(record.get('asnumber', b'').decode("utf-8")))
        self.couCode = aul.filterNull(record.get('areacode', b'').decode("utf-8"))
        self.cou = aul.filterNull(record.get('country', b'').decode("utf-8"))
        self.FindTime = datetime.datetime.now(pytz.UTC)
        self.owner = aul.filterNull(record.get('owner', b'').decode("utf-8"))