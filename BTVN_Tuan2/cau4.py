import os

ten_file = input("Nhap ten tap tin nguon:")

if os.path.exists(ten_file):
    print("Tap tin da ton tai")

    f = open(ten_file, 'r', encoding="utf-8")
    noi_dung = f.read()
    f.close()

    ds_so = noi_dung.split()

    f_chan = open("chan.txt", "w", encoding="utf-8")
    f_le = open("le.txt", "w", encoding="utf-8")
    
    tong_chan = 0
    tong_le = 0
    
    for so in ds_so:
        so = int(so)
        if so % 2 == 0:
            tong_chan += so
            f_chan.write(str(so) + " ")
        else:
            tong_le += so
            f_le.write(str(so) + " ")
            
    f_chan.close()
    f_le.close()
    
    print("Tong so chan:", tong_chan)
    print("Tong so le:", tong_le)
else:
    print("Tap tin khong ton tai")