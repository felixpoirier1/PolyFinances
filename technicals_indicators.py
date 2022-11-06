import ta
import pandas as pd
from typing import Callable, Dict


# def addNewIndicator(
#     indicatorFunction: Callable, indicatorName: str, priceDataFrame: pd.DataFrame
# ) -> pd.DataFrame:
#     indicatorDataFrame = priceDataFrame.apply(indicatorFunction, axis=0)
#     name = indicatorName
#     indicatorDataFrame.columns = [name]
#
#     return indicatorDataFrame

def MACD(
    close: pd.Series,
    window_fast: int = 12,
    window_slow: int = 26,
    window_sign: int = 9,
    select: str = "macd",
) -> pd.Series:
    """
    Moving Average Convergence Divergence (MACD)
    Is a trend-following momentum indicator that shows the
    relationship between two moving averages of prices.
    :param close_price:
    :param window_fast:
    :param window_slow:
    :param window_sign:
    :param select:
    :return:
    """

    MACD = ta.trend.MACD(
        close.shift(1),
        window_fast=window_fast,
        window_slow=window_slow,
        window_sign=window_sign,
    )

    if select == "macd":
        return MACD.macd()

    if select == "macdsignal":
        return MACD.macd_signal()


def AddingNewIndicators(newVariableDataFrame: pd.DataFrame,
                        indicators: Dict[str, Callable]= {"MACD": MACD}
                        ) -> pd.DataFrame:
    """
    Fonction qui permet d'ajouter des indicateurs à un dataframe.
    On ajoute aussi ici la variable de lag de 1 jour des rendements.
    :param newVariableDataFrame: DataFrame contenant les nouvelles variables
    créees par la fonction createModifiedVariableForPairTrading.
    :return: DataFrame des nouvelles variables avec les indicateurs ajoutés.
    """
    df_stack = stack_columns(newVariableDataFrame)
    list_of_pairs = list(df_stack["Paire"].unique())

    df_indicators = pd.DataFrame()

    for paire in list_of_pairs:
        df = df_stack[df_stack["Paire"] == paire]
        df_copy = df.copy()
        df_copy["Return"] = df_copy["Prix"].pct_change()
        # Adding a lag of 1 day to the price
        df_copy["Lag_Return_1"] = df_copy["Return"].shift(1)

        for key, value in indicators.items():
            df_copy[key] = value(df["Prix"])

        df_indicators = pd.concat([df_indicators, df_copy], sort=False)

    return df_indicators


def AROON(close: pd.Series,
             window: int = 25,
             fillna: bool = False) -> pd.Series:
    """
    Aroon Indicator (AI)
    Identify when trends are likely to change direction

    :param close:
    :param window:
    :param fillna:
    :return:
    """
    aroon = ta.trend.AroonIndicator(close.shift(1), window=window, fillna=fillna).aroon_indicator()

    return aroon

def AROON_UP(close: pd.Series,
             window: int = 25,
             fillna: bool = False) -> pd.Series:
    """
    Aroon Indicator (AI)
    Identify when trends are likely to change direction (uptrend).
    Aroon Up - ((N - Days Since N-day High) / N) x 100

    :param close:
    :param window:
    :param fillna:
    :return:
    """
    aroon_up = ta.trend.aroon_up(close.shift(1), window=window, fillna=fillna)

    return aroon_up

def AROON_DOWN(close: pd.Series,
             window: int = 25,
             fillna: bool = False) -> pd.Series:
    """
    Aroon Indicator (AI)
    Identify when trends are likely to change direction (downtrend).
    Aroon Down = ((N - Days Since N-day Low) / N) x 100

    :param close:
    :param window:
    :param fillna:
    :return:
    """
    aroon_down = ta.trend.aroon_down(close.shift(1), window=window, fillna=fillna)

    return aroon_down

def EMA(close: pd.Series,
        window: int = 12,
        fillna: bool = False) -> pd.Series:
    """
    Exponential Moving Average (EMA)
    :param close:
    :param window:
    :param fillna:
    :return:
    """
    ema = ta.trend.ema_indicator(close.shift(1), window=window, fillna=fillna)

    return ema

def TSI(close: pd.Series,
        window_slow: int = 12,
        window_fast: int = 13,
        fillna: bool = False) -> pd.Series:
    """
    MOMENTUM : True strength index (TSI)
    Shows both trend direction and overbought/oversold conditions.
    :param close:
    :param window_slow:
    :param window_fast:
    :param fillna:
    :return:
    """
    tsi = ta.momentum.tsi(close.shift(1), window_slow=window_slow,
                          window_fast=window_fast, fillna=fillna)

    return tsi

def ULCER(close: pd.Series,
        window: int = 14,
        fillna: bool = False) -> pd.Series:
    """
    Ulcer Index
    :param close:
    :param window:
    :param fillna:
    :return:
    """
    ulcer_index = ta.volatility.ulcer_index(close.shift(1), window=window, fillna=fillna)

    return ulcer_index

def BOLLINGER(close: pd.Series,
              window: int = 20,
              window_dev: int = 2,
              fillna: bool = False) -> pd.Series:

    """
    Bollinger Channel Band Width
    :param close:
    :param window:
    :param window_dev:
    :param fillna:
    :return:
    """

    bollinger_wband = ta.volatility.bollinger_wband(close.shift(1),
                                            window=window,
                                            window_dev=window_dev,
                                            fillna=fillna)

    return bollinger_wband



def DPO(close: pd.Series,
        window: int = 20,
        fillna: bool = False) -> pd.Series:

    """
    Detrended Price Oscillator (DPO)
    Is an indicator designed to remove trend from price
    and make it easier to identify cycles.

    :param close:
    :param window:
    :param fillna:
    :return:
    """

    dpo = ta.trend.dpo(close.shift(1), window=window, fillna=fillna)

    return dpo




def KST(close: pd.Series,
         roc1: int = 10, roc2: int = 15, roc3: int = 20, roc4: int = 30,
         window1: int = 10, window2: int = 10, window3: int = 10, window4: int = 15,
         nsig: int = 9, fillna: bool = False,
         select: str = "kst") -> pd.Series:
    """
    KST Oscillator (KST Signal)

    It is useful to identify major stock market cycle junctures because
    its formula is weighed to be more greatly influenced by
    the longer and more dominant time spans, in order to better reflect
    the primary swings of stock market cycle.

    """

    KST = ta.trend.KSTIndicator(close.shift(1), roc1=roc1, roc2=roc2,
                                roc3=roc3, roc4=roc4,
                                window1=window1, window2=window2,
                                window3=window3, window4=window4,
                                nsig=nsig, fillna=fillna)
    if select == "kst":
        return KST.kst()

    if select == "kst_diff":
        return KST.kst_diff()

    if select == "kst_sig":
        return KST.kst_sig()

def KAMA(close: pd.Series,
         window: int = 10,
         pow1: int = 2,
         pow2: int = 30,
         fillna: bool = False) -> pd.Series:
    """
    Momentum : Kaufman’s Adaptive Moving Average (KAMA)

    Moving average designed to account for market noise or volatility.
    KAMA will closely follow prices when the price swings are relatively small
    and the noise is low. KAMA will adjust when the price swings widen and
    follow prices from a greater distance. This trend-following indicator
    can be used to identify the overall trend, time turning
    points and filter price movements.
    :param close:
    :param window:
    :param pow1:
    :param pow2:
    :param fillna:
    :return:
    """

    kama = ta.momentum.kama(close.shift(1),
                            window=window,
                            pow1=pow1,
                            pow2=pow2,
                            fillna=fillna)

    return kama

def PPO(close: pd.Series, window_slow: int = 26, window_fast: int = 12,
        window_sign: int = 9, fillna: bool = False) -> pd.Series:
    """
    Momentum : The Percentage Price Oscillator (PPO)
    It is a momentum oscillator that measures the difference between two
    moving averages as a percentage of the larger moving average.
    :param close:
    :param window_slow:
    :param window_fast:
    :param window_sign:
    :param fillna:
    :return:
    """

    ppo = ta.momentum.ppo(close.shift(1), window_slow=window_slow,
                          window_fast=window_fast, window_sign=window_sign,
                          fillna=fillna)

    return ppo

def RSI(close: pd.Series, window: int = 14, fillna: bool = False) -> pd.Series:
    """
    Momentum : Relative Strength Index (RSI)
    :param close:
    :param window:
    :param fillna:
    :return:
    """

    rsi = ta.momentum.rsi(close.shift(1), window=window, fillna=fillna)

    return rsi

def STC(close: pd.Series, window_slow: int = 50, window_fast: int = 23,
        cycle: int = 10, smooth1: int = 3, smooth2: int = 3, fillna: bool = False) -> pd.Series:
    """
    Schaff Trend Cycle (STC)

    The Schaff Trend Cycle is a charting indicator that is commonly used to
    identify market trends and provide buy and sell signals to traders.
    Developed in 1999 by noted currency trader Doug Schaff, STC is a type of
    oscillator and is based on the assumption that, regardless of time frame,
    currency trends accelerate and decelerate in cyclical patterns.
    :param close:
    :param window_slow:
    :param window_fast:
    :param cycle:
    :param smooth1:
    :param smooth2:
    :param fillna:
    :return:
    """

    stc = ta.trend.stc(close.shift(1), window_slow=window_slow,
                            window_fast=window_fast, cycle=cycle,
                            smooth1=smooth1, smooth2=smooth2, fillna=fillna)
    return stc

def STOCHRSI(close: pd.Series, window: int = 14, fillna: bool = False) -> pd.Series:
    """
    Momentum : Stochastic RSI
    :param close:
    :param window:
    :param fillna:
    :return:
    """

    stochrsi = ta.momentum.stochrsi(close.shift(1), window=window, fillna=fillna)

    return stochrsi



def TRIX(close: pd.Series, window: int = 15) -> pd.Series:

    """
    TREND : Trix (TRIX)
    Shows the percent rate of change of a triple exponentially
    smoothed moving average.
    :param close:
    :param window:
    :return:
    """
    trix = ta.trend.trix(close.shift(1), window=window)

    return trix