str = 'hello '
symbol = input('Enter symbol:')
n = 0
for i in str:
    if  i == symbol:
        n +=1

print("Symbol {0} is {1} times in string {2}".format(symbol, n, str))
