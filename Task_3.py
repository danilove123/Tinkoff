dct = {}
txt = input()
array = txt.split(" ")
n = int(array[0])
m = int(array[1])
lst = []
txt = input()
array = txt.split(" ")
for element in array:
    lst.append(int(element))

for i in range(1,m+1):
    ostatok = i
    for price in lst:
        if price > ostatok:
            continue
        else :
            ostatok = ostatok - price

    dct.update({i:ostatok})

lst_0 = []
for key in dct:
    lst_0.append(dct.get(key))

print(max(lst_0))



