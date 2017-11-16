import urllib.request
import zlib
import json


class HttpClient:
    URL_BASE = "https://api.stackexchange.com/2.2"

    @classmethod
    def get(cls, entity, ids=[], params={}):
        identification = '/'.join([cls.URL_BASE, entity, cls._ids(ids)])
        query = '&'.join([cls._params(params), "site=stackoverflow"])
        url = '?'.join([identification, query])

        body = urllib.request.urlopen(url).read()
        content_json = zlib.decompress(body, 16+zlib.MAX_WBITS)
        content = json.loads(content_json)

        return content

    def _ids(ids):
        return ';'.join(str(_id) for _id in ids)

    def _params(params_dict):
        elements = \
            list(f"{key}={value}" for key, value in params_dict.items())

        return '&'.join(str(element) for element in elements)
