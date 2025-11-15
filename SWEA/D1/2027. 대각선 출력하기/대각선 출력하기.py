for i in range(5):        
    line = ""
    for j in range(5):      
        if i == j:         
            line += "#"
        else:
            line += "+"
    print(line)
