from pandas import DataFrame
from tinkoff.invest import HistoricCandle

def cast_money(c):
    return c.units + c.nano / 1e9

def create_df(candels: [HistoricCandle]):
    df = DataFrame([{
        'time': c.time,
        'volume': c.volume,
        'open': cast_money(c.open),
        'close': cast_money(c.close),
        'high': cast_money(c.high),
        'low': cast_money(c.low),
    } for c in candels])

    return df
