dct = {}
dct_1 = {}

txt = input()
array = txt.split(" ")
n = int(array[0])
k = int(array[1])
lst = []

for i in range(k):
    txt = input()
    lst.append(txt)

for i in range(n):
    txt = input()
    array = txt.split(" ")

    p = int(array[0])
    a = int(array[1])
    c = str(array[2])

    if p in dct:
        dct[p].append([a, c])
    else:
        dct.update({p: [[a, c]]})

o = 0

opssina = []
for key in dct:
    for element in lst:
        if not any(element in sublist for sublist in dct.get(key)):
            opssina.append(key)
            break

for element in opssina:
    del dct[element]

if len(dct) == 0:
    print(-1)
else:
    summ = 0
    ops = []

    for key in dct:
        for element in lst:
            for array_value in dct.get(key):
                if array_value[1] == element:
                    ops.append(array_value[0])

            min_el = min(ops)
            summ = summ + min_el
            ops = []

    print(summ)


