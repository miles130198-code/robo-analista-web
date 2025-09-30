import ta

def aplicar_indicadores(df):
    df['rsi'] = ta.momentum.RSIIndicator(df['Close']).rsi()
    df['sma_20'] = ta.trend.SMAIndicator(df['Close'], window=20).sma_indicator()
    df['sma_50'] = ta.trend.SMAIndicator(df['Close'], window=50).sma_indicator()
    bb = ta.volatility.BollingerBands(df['Close'])
    df['bb_upper'] = bb.bollinger_hband()
    df['bb_lower'] = bb.bollinger_lband()
    macd = ta.trend.MACD(df['Close'])
    df['macd'] = macd.macd()
    df['macd_signal'] = macd.macd_signal()
    return df
