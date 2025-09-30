def decidir_operacao(df):
    sinais = []
    for i in range(1, len(df)):
        compra = (
            df['sma_20'][i] > df['sma_50'][i] and
            df['rsi'][i] < 30 and
            df['Close'][i] < df['bb_lower'][i] and
            df['macd'][i] > df['macd_signal'][i]
        )
        venda = (
            df['sma_20'][i] < df['sma_50'][i] and
            df['rsi'][i] > 70 and
            df['Close'][i] > df['bb_upper'][i] and
            df['macd'][i] < df['macd_signal'][i]
        )
        if compra:
            sinais.append('COMPRA')
        elif venda:
            sinais.append('VENDA')
        else:
            sinais.append('MANTER')
    df['sinal'] = ['MANTER'] + sinais
    return df

def simular_operacoes(df, valor_inicial=1000):
    saldo = valor_inicial
    posicao = 0
    for i in range(len(df)):
        preco = df['Close'][i]
        sinal = df['sinal'][i]
        if sinal == 'COMPRA' and posicao == 0:
            posicao = saldo / preco
            saldo = 0
        elif sinal == 'VENDA' and posicao > 0:
            saldo = posicao * preco
            posicao = 0
    return saldo + (posicao * df['Close'].iloc[-1])
