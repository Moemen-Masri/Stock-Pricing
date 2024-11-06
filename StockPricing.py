def max_profit(prices):
    Price = len(prices) #price stores the nb of prices in the list
    Result = 0 #it will accumulate to total profit
    i = 0 #will be used as index to traverse through rhe list
    for i in range(Price - 1):#for loop that iterates over the indices of the list
        #finding Minimum priceprice
        if i < Price -1 and prices[i] >= prices[i+1]:#check if the curr price is greater than or equal to the next price
            while i < Price -1 and prices[i] >= prices[i+1]: 
                i += 1
            Min_price = prices[i]
        else:
            continue
        #finding Maximum price
        if i < Price -1 and prices[i] <=prices[i +1]:#check if the curr price is less than or equal to the next price
            while i < Price -1 and prices[i] <= prices[i+1]:
                i +=1
            Max_price = prices[i]
            Result += (Max_price - Min_price) #adding current profit
    return Result

prices = [100, 180, 260, 310, 40, 535, 695]
print(max_profit(prices))