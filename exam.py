import kis_api as kis
import time

def getStock(stknum, company):
    res = kis.get_current_price(stknum)
    priceChange = res["prdy_ctrt"]
    symbol = "▲" if float(priceChange) > 0 else "▼" if float(priceChange) < 0 else "-"
    print(f"{company}: ", res["stck_prpr"], symbol, "(", priceChange, ")")

stocks = {"005930":"삼성전자", "035720":"카카오"}

kis.auth()

for i in range(0, 100):
    for stock in stocks.keys():
        getStock(stock, stocks[stock])
    time.sleep(1)
