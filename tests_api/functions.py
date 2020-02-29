import json


def convert_dist(response):
    res_json = response.text
    res_load = json.loads(res_json)
    return res_load


def check_status(status):
    try:
        assert status == 200, "Status code fail"
        print("Status code = 200")
    except:
        assert status != 200, "Status code = 200"
        print("Status code fail")
