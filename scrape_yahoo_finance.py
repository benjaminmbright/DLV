# reference http://wern-ancheta.com/blog/2015/04/05/getting-started-with-the-yahoo-finance-api/

import pandas as pd

url = 'http://finance.yahoo.com/d/quotes.csv?'
symbols = ['CRUS', 'AAPL']
parameters = ['a', 'b', 'o', 'e7']
request = url + 's=' + '+'.join(symbols) + '&f=' + ''.join(parameters)

print(request)

data = pd.read_csv(request)

print(data)