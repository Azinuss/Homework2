
def polindrome(str) -> bool:
    for i in range(len(str)):
        if str[i] != str[-i-1]:
            return False     
    return True

mass = 'дед'
if polindrome(mass):
    print('Строка является палиндромом')
else:
    print('Строка не является палиндромом')