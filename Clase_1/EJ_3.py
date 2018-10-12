def mayor_divisor(n):
    numero = n
    maxDivisor = 2
    divisor = 2

    while numero%2==0:
        maxDivisor = divisor
        numero = numero/divisor
    divisor = 3
    maxFactor = numero**0.5
    #print(maxFactor)

    while divisor<= numero and  divisor <= maxFactor:
        while numero%divisor ==0:
            maxDivisor = divisor
            numero = numero/divisor
        divisor+= 2
    print(divisor-2)
    #print(numero)
    if divisor>maxFactor and numero>maxDivisor:
        maxDivisor = numero
    return maxDivisor


mayor_divisor(600851475143)

