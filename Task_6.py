# import qrcode
# import cv2
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data('Some data')
# qr.make(fit=True)
#
# img = qr.make_image(fill_color="black", back_color="white")
#
# detector = cv2.QRCodeDetector()
# data,bbox,clear_qr = detector.detectAndDecode(img)
#


# lst = ["00","01","20","02","11","10"]
# lst.sort()
#
# if data != "":
#     stroke = data
#     if stroke_old != stroke:
#         r = requests.post(f'http://127.0.0.1:8000/warehouse/add_pallet?unparsed={data}')
#         seq = lst[i]
#         seq = str(seq[0]) + str(seq[1])
#         str_0 = requests.get(f'http://127.0.0.1:8000/warehouse/check?id_cell={seq}')
#         lst[i] = [int(str_0[0]), int(str_0[1])]
#
#         stroke_old = stroke
#
# cv2.waitKey(3)

lst = []
def add(txt: str):
    array = txt.split(" ")
    l = int(array[1])
    r = int(array[2])
    x = float(array[3])
    for i in range(l,r+1):
        lst[i] = lst[i] + x

def out(txt: str):
    array = txt.split(" ")
    l = int(array[1])
    r = int(array[2])
    k = float(array[3])
    b = float(array[4])
    arr = []
    for i in range(l, r):
        arr.append(min(lst[i],k*i + b))
    print(int(max(arr)))

txt = input()
array = txt.split(" ")
n = int(array[0])
q = int(array[1])
txt = input()
array = txt.split(" ")
for element in array:
    lst.append(int(element))
for i in range(q):
    txt = input()
    if txt[0] == '+':
        add(txt)
    if txt[0] == '?':
        out(txt)



