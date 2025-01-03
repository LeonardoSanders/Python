def contagem_regressiva(start=10, end=0):
    print(start)

    if start <= end:
        return start
    
    return contagem_regressiva(start-1)

contagem_regressiva()