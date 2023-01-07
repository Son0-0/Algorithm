for target in [str(num) for num in range(1, int(input()) + 1)]:
    temp = ""
    for i in range(len(target)):
        if target[i] in ("3", "6", "9"):
            temp += "-"
    
    print(temp, end=' ') if temp != "" else print(target, end=' ')