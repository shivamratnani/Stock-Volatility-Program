import subprocess, os
import checks, stocksAPI

# Clear the terminal
subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)

if __name__ == "__main__":
    stocksAPI
    
    print("Welcome to the Stock Screener!")
    
        # Daily Stock
    try:
        stock = input("What stock would you like to see: ")
        stocksAPI.getDailyStocks(stock)
    except Exception as e:
        print (e)
    
    # set interval to be screened at
    try:
        timeInterval = float(input("What interval would you like stocks screened at in minutes: "))
        while not checks.checkInterval(timeInterval):
            print("The interval must be divisible by 5 and greater than or equal to 5!")
            timeInterval = float(input("What interval would you like stocks screened at in minutes: "))
    except Exception as e:
        print (e)
        
    # amount of stocks to be outputted
    try:
        stockAmount = float(input("How many stocks would you like outputted: "))
        while not checks.checkAmountOfStocksOutputted(stockAmount):
            print("The amount of stocks outputted must be greater than or equal to 1 and less than or equal to 19000!")
            stockAmount = float(input("How many stocks would you like outputted: "))
    except Exception as e:
        print (e)
    
    # minimum stock price
    try:
        minumumPrice = float(input("What should be the minimum price of the stock in dollars: "))
        while not checks.checkMinimumPrice(minumumPrice):
            print("The minimum price must be greater than or equal to 0!")
            minumumPrice = float(input("What should be the minimum price of the stock in dollars: "))
    except Exception as e:
        print (e)
    
    # Maximum stock price
    try:
        maximumPrice = float(input("What should be the maximum price of the stock in dollars: "))
        while not checks.checkMaximumPrice(maximumPrice, minumumPrice):
            print("The maximum price must be greater than or equal to 0 and greater than or equal to the minimum price!")
            maximumPrice = float(input("What should be the maximum price of the stock in dollars: "))
    except Exception as e:
        print (e)
        
        
        

