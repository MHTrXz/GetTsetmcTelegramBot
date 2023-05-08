import requests
import secret

"""status requests functions"""


def market_bourse():
    """get bourse market state"""
    patameters = {
        'token': secret.bors_api_key,
        "market": "market_bourse"
    }
    data = requests.get(secret.bors_api_url, params=patameters).json()
    return data


def market_farabourse():
    """get bourse market state"""
    patameters = {
        'token': secret.bors_api_key,
        "market": "market_farabourse"
    }
    data = requests.get(secret.bors_api_url, params=patameters).json()
    return data


def fav_namad_bourse():
    """"get most view namad in bourse market"""
    patameters = {
        'token': secret.bors_api_key,
        "market": "fav_namad_bourse"
    }
    data = requests.get(secret.bors_api_url, params=patameters).json()
    return data


def fav_namad_farabourse():
    """"get most view namad in farabourse market"""
    patameters = {
        'token': secret.bors_api_key,
        "market": "fav_namad_farabourse"
    }
    data = requests.get(secret.bors_api_url, params=patameters).json()
    return data


def ind_namad_bourse():
    """get most impact on the index in bourse market"""
    patameters = {
        'token': secret.bors_api_key,
        "market": "ind_namad_bourse"
    }
    data = requests.get(secret.bors_api_url, params=patameters).json()
    return data


def ind_namad_farabourse():
    """get most impact on the index in farabourse market"""
    patameters = {
        'token': secret.bors_api_key,
        "market": "ind_namad_farabourse"
    }
    data = requests.get(secret.bors_api_url, params=patameters).json()
    return data


def market_indices():
    """get indices market data"""
    patameters = {
        'token': secret.bors_api_key,
        "market": "indices"
    }
    data = requests.get(secret.bors_api_url, params=patameters).json()
    return data


"""show single namad requests functions"""


def namad_search(search):
    """search in all namad"""
    patameters = {
        'token': secret.bors_api_key,
        "search": search
    }
    data = requests.get(secret.bors_api_url, params=patameters).json()
    return data


def single_namad_data(namad):
    """get single namad data"""
    patameters = {
        'token': secret.bors_api_key,
        "name": namad
    }
    data = requests.get(secret.bors_api_url, params=patameters).json()
    return data


def namad_stockholder(namad):
    """get namad stockholder data"""
    patameters = {
        'token': secret.bors_api_key,
        "stockholder": namad
    }
    data = requests.get(secret.bors_api_url, params=patameters).json()
    return data


def namad_stats(namad):
    """get namad state data"""
    patameters = {
        'token': secret.bors_api_key,
        "stats": namad
    }
    data = requests.get(secret.bors_api_url, params=patameters).json()
    return data


def namad_codal(namad):
    """fet namad codal alert data"""
    patameters = {
        'token': secret.bors_api_key,
        "codal": namad,
        "p": 1
    }
    data = requests.get(secret.bors_api_url, params=patameters).json()
    return data


def co_real_power(namad):
    """get company or real person buy or sell power data"""
    patameters = {
        'token': secret.bors_api_key,
        "power": namad,
        "days": 30
    }
    data = requests.get(secret.bors_api_url, params=patameters).json()
    return data


def namad_nday_history(namad, day):
    """get price history in n days"""
    patameters = {
        'token': secret.bors_api_key,
        "name": namad,
        "days": day
    }
    data = requests.get(secret.bors_api_url, params=patameters).json()
    return data


"""watch req functions"""


def search_code(codes):
    """search a namad with instance code"""
    data = requests.get(secret.bors_api_url + "?token=" + secret.bors_api_key + "&all&type=0").json()
    out_list = []
    for i in data:
        if i["instance_code"] in codes:
            out_list.append([f'{i["full_name"]} ({i["name"]})', i["instance_code"]])
    return out_list


def search_code_name(codes):
    """search a namad with instance code"""
    data = requests.get(secret.bors_api_url + "?token=" + secret.bors_api_key + "&all&type=0").json()
    out_list = []
    for i in data:
        if i["instance_code"] in codes:
            out_list.append(i["name"])
    return out_list


def all_namad_data():
    """get all namad data"""
    data = requests.get(secret.bors_api_url + "?token=" + secret.bors_api_key + "&all&type=0").json()
    return data
