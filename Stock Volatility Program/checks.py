#Checks if the interval is valid based on being divisible by 5 and greater than or equal to 5
def checkInterval(timeInterval):
    if timeInterval >= 5 and  timeInterval %5 == 0:
        return True
    return False

def checkAmountOfStocksOutputted(stockAmount):
    if stockAmount >= 1 and stockAmount <= 19000 and stockAmount %1 == 0:
        return True
    return False

def checkMinimumPrice(minimumPrice):
    if minimumPrice >= 0:
        return True
    return False

def checkMaximumPrice(maximumPrice, minimumPrice):
    if maximumPrice >= 0 and maximumPrice >= minimumPrice:
        return True
    return False