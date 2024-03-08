from datetime import timedelta

from fastapi import Response
from tinkoff.invest import CandleInterval, Client
from tinkoff.invest.utils import now

from Helpos.HistoricCandel_to_DF import create_df

TOKEN = ""


def get_candles_share():
    with Client(TOKEN) as client:
        candles = list(client.get_all_candles(
            figi="BBG004S68B31",
            from_=now() - timedelta(days=50),
            interval=CandleInterval.CANDLE_INTERVAL_DAY,
        ))
        df = create_df(candles)

    return df


