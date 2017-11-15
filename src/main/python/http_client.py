import urllib.request
import zlib
import json


class HttpClient:
    URL_BASE = "https://api.stackexchange.com/2.2"

    @classmethod
    def get(cls, entity, params_dict = {}):
        params_string_elements = list (f"{key}={value}" for key, value in params_dict.items())
        params_string = '&'.join(str(element) for element in params_string_elements)

        url = f"{cls.URL_BASE}/{entity}?{params_string}&site=stackoverflow"

        body = urllib.request.urlopen(url).read()
        content_json = zlib.decompress(body, 16+zlib.MAX_WBITS)
        content = json.loads(content_json)

        return content
