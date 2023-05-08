"""state functions"""

"""status text functions"""


def show_bourse_market(data):
    """bourse market state text"""
    out_text = ""
    queue = data["bourse"]
    out_text += f'market : بورس' + f' ({queue["index_change_percent"]}%)' + "\n"
    out_text += f'state : {queue["state"]}' + "\n"
    out_text += f'index : {queue["index"]}' + "\n"
    out_text += f'Index changes : {queue["index_change"]}' + "\n"
    out_text += f'Eq index : {queue["index_h"]}' + "\n"
    out_text += f'Eq index changes : {queue["index_h_change"]}' + "\n"
    out_text += f'Market value : {queue["market_value"]}' + "\n"
    out_text += f'Number of trade : {queue["trade_number"]}' + "\n"
    out_text += f'Value of trade : {queue["trade_value"]}' + "\n"
    out_text += f'Volume of trade : {queue["trade_volume"]}' + "\n"

    return out_text


def show_farabourse_market(data):
    """farabourse market state text"""
    out_text = ""
    queue = data["fara-bourse"]
    out_text += 'market : فرابورس' + f' ({queue["index_change_percent"]}%)' + "\n"
    out_text += f'state : {queue["state"]}' + "\n"
    out_text += f'index : {queue["index"]}' + "\n"
    out_text += f'Index changes : {queue["index_change"]}' + "\n"
    out_text += f'Market value : {queue["market_value"]}' + "\n"
    out_text += f'Number of trade : {queue["trade_number"]}' + "\n"
    out_text += f'Value of trade : {queue["trade_value"]}' + "\n"
    out_text += f'Volume of trade : {queue["trade_volume"]}' + "\n"

    return out_text


def show_fav_namad(data):
    """most view namad"""
    out_list = []
    for i in data:
        text = ""
        text += f'Name : {i["name"]}' + "\n"
        text += f'Final price : {i["final_price"]} ({i["final_price_change"]}%)' + "\n"
        text += f'Close price : {i["close_price"]} ({i["close_price_change"]}%)' + "\n"
        text += f'Lowest price : {i["lowest_price"]}' + "\n"
        text += f'Highest price : {i["highest_price"]}' + "\n"
        text += f'Highest price : {i["highest_price"]}' + "\n"
        text += f'Number of trade : {i["n"]}' + "\n"
        text += f'Volume of trade : {i["volume"]}' + "\n"
        text += f'Value of trade : {i["value"]}' + "\n"
        out_list.append(text)
    return out_list


def show_ind_namad(data):
    """most impact on the index"""
    out_list = []
    for i in data:
        text = ""
        text += f'Name : {i["name"]}' + "\n"
        text += f'Final price : {i["final_price"]}' + "\n"
        text += f'Effect : {i["effect"]}' + "\n"
        out_list.append(text)
    return out_list


def show_market_indices(data):
    """indices market state"""
    out_list = []
    for i in data:
        text = ""
        text += f'Name : {i["name"]}' + "\n"
        text += f'Value : {i["value"]}' + "\n"
        text += f'Change : {i["change"]} ({i["percent"]}%)' + "\n"
        text += f'Max : {i["max"]}' + "\n"
        text += f'Min : {i["min"]}' + "\n"
        out_list.append(text)
    return out_list


"""single namad functions"""


def search_list(data):
    """search list prepare"""
    out_list = []
    for i in data:
        if str(i["full_name"]).find("ح") != 0 and str(i["name"]).isalpha():
            out_list.append([f'{i["full_name"]} ({i["name"]})', i["instance_code"]])
    return out_list


def show_single_namad(data):
    """single namad data"""
    out_text = ""
    if "state" in data.keys():
        if data["state"] == "مجاز":
            out_text = "🟢"
        elif data["state"] == "مجاز-محفوظ":
            out_text = "🟡"
        elif data["state"] == "مجاز-متوقف":
            out_text = "🟠"
        elif data["state"] == "ممنوع":
            out_text = "🔴"
        elif data["state"] == "ممنوع-متوقف":
            out_text = "⚫"
    if "full_name" in data.keys():
        out_text += f'{data["full_name"]} ({data["name"]})' + "\n"
    else:
        out_text += f'{data["name"]}' + "\n"
    out_text += f'Type : {data["type"]} ({data["market"]})' + "\n"
    out_text += f'Subtype : {data["sub_type"]}' + "\n"
    out_text += f'Yesterday price : {data["yesterday_price"]}' + "\n"
    out_text += f'First price : {data["first_price"]}' + "\n"
    out_text += f'Min price : {data["min_price"]} | Max price : {data["max_price"]}' + "\n"
    out_text += f'Close price : {data["close_price"]} [{data["close_price_change"]}] ' \
                + f'({data["close_price_change_percent"]}%)' + "\n"
    out_text += f'Final price : {data["final_price"]} [{data["final_price_change"]}] ' \
                + f'({data["final_price_change_percent"]}%)' + "\n"
    out_text += f'EPS : {data["eps"]} | P:E {data["P:E"]}' + "\n"
    out_text += f'Period : min={data["daily_price_low"]} max={data["daily_price_high"]}' + "\n"
    out_text += f'Real person count buy={data["real_buy_count"]} sell={data["real_sell_count"]}' + "\n"
    out_text += f'Real person value buy={data["real_buy_value"]} sell={data["real_sell_value"]}' + "\n"
    out_text += f'Real person volume buy={data["real_buy_volume"]} sell={data["real_sell_volume"]}' + "\n"
    out_text += f'Co person count buy={data["co_buy_count"]} sell={data["co_sell_count"]}' + "\n"
    out_text += f'Co person value buy={data["co_buy_value"]} sell={data["co_sell_value"]}' + "\n"
    out_text += f'Co person volume buy={data["co_buy_volume"]} sell={data["co_sell_volume"]}' + "\n"
    out_text += f'Trade value:{data["trade_value"]} volume:{data["trade_volume"]} number:{data["trade_number"]}' + "\n"
    out_text += f'All stocks : {data["all_stocks"]} | basis_volume {data["basis_volume"]}'
    return out_text


def show_namad_stockholder(data):
    """namad stockholder"""
    out_list = []
    for i in data:
        text = f'Name : {i["name"]}' + "\n"
        text += f'Percent : {i["percent"]}' + "\n"
        text += f'Change : {i["change"]}'
        out_list.append(text)
    return out_list


def show_namad_stats(data):
    """single namad state"""
    out_text = ""
    out_text += f'Negative days in 3M : {data["n_day_3m"]}' + "\n"
    out_text += f'Negative days in 12M : {data["n_day_12m"]}' + "\n"
    out_text += f'Percentage of negative days in 12M : {data["n_percent_12m"]}' + "\n"
    out_text += f'Rating of negative days in 3M : {data["n_rank_3m"]}' + "\n"
    out_text += f'Rating of negative days in 12M : {data["n_rank_12m"]}' + "\n"
    out_text += f'Number of positive days in 3M : {data["p_day_3m"]}' + "\n"
    out_text += f'Number of positive days in 12M : {data["p_day_12m"]}' + "\n"
    out_text += f'Rank of positive days in 3M : {data["p_rank_3m"]}' + "\n"
    out_text += f'Rank of positive days in 12M : {data["p_rank_12m"]}' + "\n"
    out_text += f'Days without a deal in 3M : {data["trade_nday_3m"]}' + "\n"
    out_text += f'Days without a deal in 12M : {data["trade_nday_12m"]}' + "\n"
    out_text += f'Days with a deal in 3M : {data["trade_day_3m"]}' + "\n"
    out_text += f'Days with a deal in 12M : {data["trade_day_12m"]}' + "\n"
    out_text += f'Rank the days with the deal in 3M : {data["trade_rank_3m"]}' + "\n"
    out_text += f'Rank the days with the deal in 12M : {data["trade_rank_12m"]}' + "\n"
    out_text += f'Average number of daily trade in 3M : {data["tn_average_3m"]}' + "\n"
    out_text += f'Average number of daily trade in 12M : {data["tn_average_12m"]}' + "\n"
    out_text += f'Rank the number of daily trades in 3M : {data["tn_rank_3m"]}' + "\n"
    out_text += f'Rank the number of daily trades in 12M : {data["tn_rank_12m"]}' + "\n"
    out_text += f'Count trades on the last day : {data["tn_last_day"]}' + "\n"
    out_text += f'Average trading value last day : {data["tval_last_day"]}' + "\n"
    out_text += f'Average trading value in 3M : {data["tval_average_3m"]}' + "\n"
    out_text += f'Average trading value in 12M : {data["tval_average_12m"]}' + "\n"
    out_text += f'Trading value rating in 3M : {data["tval_rank_3m"]}' + "\n"
    out_text += f'Trading value rating in 12M : {data["tval_rank_12m"]}'

    return out_text


def show_namad_codal(data):
    """namad codal alert"""
    out_list = []
    for i in data:
        text = list()
        text.append(f'Name : {i["name"]} ({i["symbol"]})')
        text.append(f'Letter number : {i["letter_number"]} | Date : {i["date"]}')
        text.append(f'Title : {i["title"]}')
        if i["link"] != "":
            text.append(f'Link : {i["link"]}')
        if i["pdf"] != "":
            text.append(f'PDF : {i["link"]}')
        if i["excel"] != "":
            text.append(f'Excel : {i["link"]}')
        out_list.append("\n".join(text))
    return out_list


def show_co_real_power(data):
    """real or company person buy or sell power"""
    out_list = []
    for i in data:
        text = f'Date : {i["date"]}' + "\n"
        text += f'Price : close={i["close_price"]} final={i["final_price"]}' + "\n"
        text += f'Real volume : buy={i["real_buy_volume"]} sell={i["real_sell_volume"]}' + "\n"
        text += f'Real count : buy={i["real_buy_count"]} sell={i["real_sell_count"]}' + "\n"
        text += f'Trades : volume={i["trade_volume"]} number={i["trade_number"]} value={i["trade_value"]}' + "\n"
        text += f'Power : buy={i["buy_power"]} sell={i["sell_power"]}' + "\n"
        text += f'Power ratio : buy/sell={i["buy_power_to_sell_power"]} sell/buy={i["sell_power_to_buy_power"]}'
        out_list.append(text)
    return out_list


def show_namad_nday_history(data):
    """namad price history in n days"""
    out_list = []
    for i in data:
        text = f'Date : {i["date"]}' + "\n"
        text += f'Close price : {i["close_price"]}' + "\n"
        text += f'Final price : {i["final_price"]}' + "\n"
        text += f'First price : {i["first_price"]}' + "\n"
        text += f'Highest price : {i["highest_price"]}' + "\n"
        text += f'Lowest price : {i["lowest_price"]}' + "\n"
        text += f'Trade volume : {i["trade_volume"]}' + "\n"
        text += f'Trade number : {i["trade_number"]}' + "\n"
        text += f'Trade value : {i["trade_value"]}'
        out_list.append(text)
    return out_list


"""watch text function"""


def all_namad_search(data, search):
    """search in all namad"""
    out_list = []
    for i in data:
        if str(i['instance_code']) in search:
            text = f'{i["full_name"]} ({i["name"]})' + "\n"
            text += f'First price : {i["first_price"]}' + "\n"
            text += f'Close price : {i["close_price"]} [{i["close_price_change"]}] ' \
                    f'({i["close_price_change_percent"]}%)' + "\n"
            text += f'Final price : {i["final_price"]} [{i["final_price_change"]}] ' \
                    f'({i["final_price_change_percent"]}%)' + "\n"
            text += f'H price : {i["highest_price"]} | L price : {i["lowest_price"]}'
            out_list.append(text)
    return out_list
