# --- Exercise 4.1 ---

def FactorialInt(number):
    FinalValue = int(number)
    for n in range((number-1), 1, -1):
        FinalValue *= int(n)
        #print('DBG: n={0} && FinalValue={1}'.format(n, FinalValue))
    
    return FinalValue
    
def FactorialFloat(number):
    FinalValue = float(number)
    for n in range((number-1), 1, -1):
        FinalValue *= float(n)
        #print('DBG: n={0} && FinalValue={1}'.format(n, FinalValue))
    
    return FinalValue

Input = input('Enter a number to calculate a factorial for: ')

print('Factorial for int({0}) is: {1}'.format(int(Input), FactorialInt(Input)))
print('Factorial for float({0}) is: {1}'.format(float(Input), FactorialFloat(Input)))