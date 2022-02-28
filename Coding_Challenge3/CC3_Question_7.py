#We have a list of companies with their face values in the stock market. 
#Now, I want to get the company's name along with its face value for the company, which has the maximum and the minimum face values.
#I also want you all to sort this list based on face values in increasing order.
#In this example, you have the flexibility to go ahead and google for some hints.
stock_market = {'AXIS BANK' : 7,
        'BHARTI AIRTEL' : 5,
        'COAL INDIA' : 10,
        'ITC' : 1,
        'TCS' : 3,
        'L&T' : 2,
        'RELIANCE' : 9,
        'KOTAK BANK' : 8,
        'AMERICAN EXPRESS' : 11}
result_lst = [(value, key) for key, value in stock_market.items()]
print(min(result_lst))
print(max(result_lst))
print(sorted(result_lst))