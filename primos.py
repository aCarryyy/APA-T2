"""
ALEX CARRIÓN GONZÁLEZ
"""

import math

"Devuelve True si el número es primo, False si no lo es"
def esPrimo(num):
    """
    >>> esPrimo(5)
    True

    >>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """

    if num < 2:
        return False
    for i in range(2, num-1):
        if num % i == 0:
            return False
    return True

"Devuelve una tupla de todos los primos hasta el argumento sin incluirlo"
def primos(lim):
    """
    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """

    return tuple(i for i in range(2, lim) if esPrimo(i))

"Devuelve una tupla con la descomposición en factores primos de su argumento."
def descompon(num):
    """
    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """

    factores = []
    divisor = 2
    while divisor ** 2 <= num:  
        if num % divisor == 0:  
            factores.append(divisor)
            num //= divisor     
        else:                   
            divisor += 1        
    if num > 1:                 
        factores.append(num)        
    return tuple(factores)

"Devuelve el mínimo común múltiplo de los dos argumentos"
def mcm(num1, num2):
    """
    >>> mcm(90, 14)
    630
    """

    desc1 = descompon(num1)
    desc2 = descompon(num2)
    mCmList = list(desc1)                   
    for i in range(len(desc2)):             
        quantInDesc1 = mCmList.count(desc2[i])     
        quantInDesc2 = desc2.count(desc2[i])
        if quantInDesc1 < quantInDesc2:     
            n = quantInDesc2 - quantInDesc1 
            for j in range(n):                 
                mCmList.append(desc2[i])       
    return math.prod(mCmList)

"Devuelve el máximo común divisor de los dos argumentos"
def mcd(num1, num2):
    """
    >>> mcd(924, 780)
    12
    """

    desc1 = descompon(num1)
    desc2 = descompon(num2)
    list2 = list(desc2)
    mCdList = []                    
    for i in range(len(desc1)):      
        if desc1[i] in list2:        
            mCdList.append(desc1[i]) 
            list2.remove(desc1[i])   
    return math.prod(mCdList)

"Devuelve el mínimo común múltiplo de todos los argumentos"
def mcmN(*nums):
    """
    >>> mcmN(42, 60, 70, 63)
    1260
    """
    
    MCM = 1
    for i in range(len(nums)):
        MCM = mcm(MCM, nums[i])
    return MCM

"Devuelve el máximo común divisor de todos los argumentos"
def mcdN(*nums):
    """
    >>> mcdN(840, 630, 1050, 1470)
    210
    """
    
    MCD = nums[0]
    for num in nums[1: ]:
        MCD = mcd(MCD, num)
    return MCD

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)