txt = input()
t = int(txt[0])

for i in range(t):
    txt1 = input()
    txt2 = input()
    lst = []

    n = int(txt1)
    array = txt2.split(" ")
    for element in array:
        lst.append(int(element))

    summs = sum(lst)

    if summs >= (n-1)*2:
        print("Yes")
    else:
        print("No")




