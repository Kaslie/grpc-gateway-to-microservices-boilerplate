import json
import requests

from flask import request, Response

def build_url(dns, port="", is_test=False):
    if dns == "" or dns is None:
        raise Exception("DNS cannot be null")
    result = "%s%s%s"
    _protocol = "http://"
    _port = ""
    if port == "443":
        _protocol = "https://"
        _port = ""
    elif not (port == "" or port is None or port is "80" or port is "8080"):
        _port = ":" + port
    else:
        _port = ""
    _dns = dns
    _dns = _dns if _dns[-1] != "/" else _dns[:-1]
    _protocol = "" if ("http://" in _dns or "https://" in _dns) else _protocol
    result = result % (_protocol, _dns, _port)
    if not is_test:
        print("URL Builded: %s" % (result))
    return result

def parse_byte_as_json(rd):
    try:
        result_data = json.loads(rd.decode())
        return result_data
    except json.decoder.JSONDecodeError as e:
        # return str(rd.decode()), "", {}
        return {}
    except Exception as e:
        raise e

def clean_mh(mh={}):
    def is_mh_valid(key, val):
        valid1 = key != "Transfer-Encoding" and val != "chunked"
        valid2 = key != "Content-Encoding" and val != "gzip"
        return valid1 and valid2

    return {k: v for k, v in dict(mh).items() if is_mh_valid(k, v)}


def mirror_request(url):
    # for now, only GET supported
    # BUG headers are not passed
    headers = {k: v for k, v in request.headers.items() if k not in ["Host"]}
    params = {k: v for k, v in request.args.items()}
    data = parse_byte_as_json(request.data)
    method = request.method

    # LOGGER.info('Mirror request to %s' % (json.dumps({'url':url, 'headers':headers, 'params':params})))

    if method == "GET":
        mirror_response = requests.get(url, headers=headers, params=params)
    elif method == "POST":
        mirror_response = requests.post(url, headers=headers, params=params, data=data)
    else:
        raise Exception("Method '%s' is not supported" % (method))

    mirror_headers = clean_mh(mirror_response.headers)
    mirror_status_code = mirror_response.status_code
    mirror_text = mirror_response.text
    response = Response(mirror_text, headers=mirror_headers, status=mirror_status_code)
    return response
