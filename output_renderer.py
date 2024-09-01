
# data = {'date': '31.08.2024', 
#  'bank': 'PB', 
#  'baseCurrency': 980, 
#  'baseCurrencyLit': 'UAH', 
#  'exchangeRate': [
#      {'baseCurrency': 'UAH', 'currency': 'UAH', 
#       'saleRateNB': 1.0, 'purchaseRateNB': 1.0}, 
#     {'baseCurrency': 'UAH', 'currency': 'USD', 
#       'saleRateNB': 41.1901, 'purchaseRateNB': 41.1901, 
#       'saleRate': 41.35, 'purchaseRate': 40.75}, 
#     {'baseCurrency': 'UAH', 'currency': 'EUR', 
#      'saleRateNB': 45.7045, 'purchaseRateNB': 45.7045,
#        'saleRate': 45.9, 'purchaseRate': 44.9}, 
# ]}


def finder(currency: str, exchange_rate: list) -> dict:
    '''
    Finds the correct dict from the exchange list.
    '''
    for exchange in exchange_rate:
        if exchange['currency'] == currency:
            return exchange


def output_renderer(currencies: list, input_data: dict) -> list[dict]:
    '''
    Returns the exchange rate in the right form.
    '''
    output = {}
    output[input_data['date']] = {}
    for currency in currencies:
        # currency = currency.upper()
        output[input_data['date']][currency] = {
            'sale': finder(currency, input_data['exchangeRate'])['saleRate'],
            'purchase': finder(currency, input_data['exchangeRate'])['purchaseRate'] }
    return output

if __name__ == '__main__':
    curr = ['EUR', 'USD']
        
    print(output_renderer(curr, data))

    # print(data['date'])
