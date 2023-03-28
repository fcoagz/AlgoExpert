def smallestDifference(arrayOne, arrayTwo):
    # Ordenara los dos Arrays
    arrayOne.sort()
    arrayTwo.sort()
    # Inicializamos las Variables
    menorPar = []
    puntero1 = 0
    puntero2 = 0
    diferencia = float("inf")
    diferenciaMenor = float("inf")
    
    # Comparara los Elementos de los Arrays
    while puntero1 < len(arrayOne) and puntero2 < len(arrayTwo):
        primerNum = arrayOne[puntero1]
        segundoNum = arrayTwo[puntero2]
        
        # Calcula la diferencia de los dos numeros. Examples: (5, 10) | (10 - 5)
        if primerNum < segundoNum:
            diferencia = segundoNum - primerNum
            puntero1 +=1
        elif primerNum > segundoNum:
            diferencia =  primerNum - segundoNum
            puntero2 +=1
        else: 
            return [primerNum, segundoNum] # Si son iguales, la diferencia es cero

        if diferenciaMenor > diferencia: # Si finito es mayor que infinito, devolvera el par con su menor diferencia
            diferenciaMenor = diferencia
            menorPar = [primerNum, segundoNum]
    
    return menorPar
            
