txt = input()
t = int(txt[0])

for i in range(t):
    txt1 = input()
    if txt1.count("T") == 1 \
            and txt1.count("I") == 1 \
            and txt1.count("N") == 1 \
            and txt1.count("K") == 1 \
            and txt1.count("O") == 1 \
            and txt1.count("F") == 2 \
            and len(txt1) == 7:
        print("Yes")

    else :
        print("No")
