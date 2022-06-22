def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    menorPar = []
    puntero1 = 0
    puntero2 = 0
    diferencia = float("inf")
    diferenciaMenor = float("inf")

    while puntero1 < len(arrayOne) and puntero2 < len(arrayTwo):
        primerNum = arrayOne[puntero1]
        segundoNum = arrayTwo[puntero2]

        if primerNum < segundoNum:
            diferencia = segundoNum - primerNum
            puntero1 +=1
        elif primerNum > segundoNum:
            diferencia =  primerNum - segundoNum
            puntero2 +=1
        else: 
            return [primerNum, segundoNum]

        if diferenciaMenor > diferencia:
            diferenciaMenor = diferencia
            menorPar = [primerNum, segundoNum]
    
    return menorPar
            
