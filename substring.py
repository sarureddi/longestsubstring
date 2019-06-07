num=input()
Len=[]
for k in num:
    if k not in Len:
        Len.append(k)
    else:
        break
print(len(Len))
