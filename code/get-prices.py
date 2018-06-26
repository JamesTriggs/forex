from  forex_python.converter import CurrencyRates
import sys, getopt, csv

"""Class to get value of Currencies in British Sterling based on param of chosen currency or mix"""

def main(argv):
    singleCurrency = ''
    try:
        opts, args = getopt.getopt(argv, "h:c:")
    except getopt.GetoptError:
        print('get-prices.py -c <currency>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('get-prices.py -c <currency>')
            sys.exit()
        elif opt == '-c':
            singleCurrency = arg
    currency_dict = openCurrencyList()
    for abbrv, cur in currency_dict.items():
        print (abbrv + ": " + getSingleGBPConversion(abbrv))

def getSingleGBPConversion(currency):
    c = CurrencyRates()
    conversion = c.get_rate(currency, 'GBP')
    print(conversion)   

def openCurrencyList():
    with open('currencies.csv', mode='r') as infile:
        reader = csv.reader(infile)
        mydict = {rows[0]:rows[1] for rows in reader}
        print(mydict)
        return mydict

if __name__ == '__main__':
    main(sys.argv[1:])

