# ----------------------------------------------------------------------------
# yahoo_finance_analysts.py
# 2016-07-26
# ----------------------------------------------------------------------------

# imports
# ----------------------------------------------------------------------------
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep, time
# ----------------------------------------------------------------------------

# attributes
# ----------------------------------------------------------------------------
TICKERS = ['AAPL', 'CRUS']

TABLES = [
    'Earnings Estimate',
    'Revenue Estimate',
    'Earnings History',
    'EPS Trend',
    'EPS Revisions',
    'Growth Estimates']
# ----------------------------------------------------------------------------


# script
# ----------------------------------------------------------------------------
start = time()                                                                  # initial time stamp
driver = webdriver.Firefox()                                                    # open the web browser

for ticker in TICKERS:
    print()
    print(ticker)
    url = 'http://finance.yahoo.com/quote/' + ticker + '/analysts?p=' + ticker
    driver.get(url)                                                             # request page
    sleep(3)                                                                    # this is a dumb wait, should find better way to wait for the page to load
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")

    for table in TABLES:
        print()
        print(table)
        a = soup.find(string=table)                                             # Search for table name
        b = a.find_parent("table")                                              # find html table that contains that name
        for row in b.tbody.find_all('tr'):                                      # iterate over the rows in the table body
            c = []
            for data in row.find_all('td'):
                c.append(data.get_text())
            print('{} {}'.format(c[0], c[1:]))

driver.quit()                                                                   # close the web browser

print()
print('Runtime for {} stocks: {}'.format(len(TICKERS), time() - start))
# ----------------------------------------------------------------------------
