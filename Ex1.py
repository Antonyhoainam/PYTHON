def sum_deep(t):
    tong = 0
    for x in t:
        if type(x)==str:
            continue
        elif type(x)== int or type(x) == float:
            tong = tong + x
        else:
            temp = sum_deep(x)
            tong = tong + temp
    return tong

list = [(1, 2),-2,4.3,(3,'thi',5),[2], 'nothing']
test = sum_deep(list)
print(test)