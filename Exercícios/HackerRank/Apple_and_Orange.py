def countApplesAndOranges(s, t, a, b, apples, oranges):
    cont_apple = 0
    cont_orange = 0
    
    for i, apple in enumerate(apples):
        apples[i] = a + apple
        if t >= apples[i] >= s:
            cont_apple += 1
            
    for x, orange in enumerate(oranges):
        oranges[x] = b + orange
        if t >= oranges[x] >= s:
            cont_orange += 1
    
    print(cont_apple)
    print(cont_orange)