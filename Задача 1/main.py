
def polindrome(str):
    for i in range(len(str)):
        if (str[i] != str[-i-1]):
            print('Эта строка  не полином')      
            return
    print('Эта строка полином')        
    return

mass = 'дед'
polindrome(mass)