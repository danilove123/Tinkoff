dct = {}
dct_1 = {}
def send(txt: str):
    array = txt.split(" ")
    v = int(array[1])
    x = int(array[2])
    lst = []
    for i in dct_1:
        if i == v:
            lst.append(dct_1.get(i))
        if dct_1.get(i) == v:
            lst.append(i)
    for element in lst:
        dct[element] = dct[element] + x

def count(txt: str):
    array = txt.split(" ")
    v = int(array[1])
    print(dct[v])

txt = input()
array = txt.split(" ")
n = int(array[0])
m = int(array[1])
q = int(array[2])
txt = input()
array = txt.split(" ")
i1 = 1
for element in array:
    dct.update({i1:int(element)})
    i1 = i1 + 1

for i in range(m):
    txt = input()
    txt = txt.split(" ")
    dct_1.update({int(txt[0]):int(txt[1])})

for i in range(q):
    txt = input()
    if txt[0] == '+':
        send(txt)
    if txt[0] == '?':
        count(txt)

# dct = {}
# for i in range(1,10):
#     dct.update({i:"o"})



