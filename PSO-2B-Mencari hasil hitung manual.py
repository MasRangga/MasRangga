import random

#fungsi f(X,y)
def func(x,y):
    return (1.5-x+x*y)**2+(2.25-x+x*y**2)**2+(2.625-x+x*y**3)**2

#inisialisasi variabel xi awal untuk iterasi pertama
xi = {
    "x1" : 1,
    "x2" : -1,
    "x3" : 2
}

#inisialisasi penampungan variabel xi-1 untuk perbandingan mencari Pbestix
xi_before={
    "x1" : 0,
    "x2" : 0,
    "x3" : 0,
}

#inisialisasi variabel yi awal untuk iterasi pertama
yi = {
    "y1" : 1,
    "y2" : 2,
    "y3" : 1
}

#inisialisasi penampungan variabel yi-1 untuk perbandingan mencari Pbestiy
yi_before={
    "y1" : 0,
    "y2" : 0,
    "y3" : 0,
}

#inisialisasi vo
v0 = 0

#inisialisasi vix setelah terjadi iterasi
vix = {
    "v1":v0,
    "v2":v0,
    "v3":v0,
}

##inisialisasi vix setelah terjadi iterasi
viy = {
    "v1":v0,
    "v2":v0,
    "v3":v0,
}

#inisialisasi variabel-variabel lainnya
c1 = 1
c2 = 1/2
r1=1
r2=1
w = 1
Gbestx = 0
Gbesty = 0
Pbestix=[]
Pbestiy=[]

#fungsi untuk mencari Gbestx dan Gbesty dengan membandingkan semua fungsi(x,y) lalu mengambil nilai x & y dari fungsi yang menghasilkan nilai paling kecil
def xy_mininum(x1,x2,x3,y1,y2,y3):
    global Gbestx
    global Gbesty
    if func(x1,y1)<=func(x2,y2) and func(x1,y1)<=func(x3,y3):
        Gbestx = x1
        Gbesty = y1
    if func(x2,y2)<=func(x1,y1) and func(x2,y2)<=func(x3,y3):
        Gbestx = x2
        Gbesty = y2
    if func(x3,y3)<=func(x2,y2) and func(x3,y3)<=func(x1,y1):
        Gbestx = x3
        Gbesty = y3

#fungsi untuk yang akan mengambil langsung nilai xi & yi dan menympannya kedalam array Pbestix dan Pbestiy jika sedang dalam iterasi pertama
def fxy_minimum_iterasi1(x1,x2,x3,y1,y2,y3):
    Pbestix.append(x1)
    Pbestix.append(x2)
    Pbestix.append(x3)
    Pbestiy.append(y1)
    Pbestiy.append(y2)
    Pbestiy.append(y3)

# fungsi untuk mengambil nilai xi & yi dan menyimpannya kedalam Pbestix dan Pbestiy dengan cara membandikan antara nilai fungsi f(x,y) iterasi sekarang dengan iterasi sebelumnya
def fxy_minimum_selanjutnya(x1_before,x1,x2_before,x2,x3_before,x3,y1_before,y1,y2_before,y2,y3_before,y3):
    if func(x1,y1)<=func(x1_before,y1_before):
        Pbestix.append(x1)
        Pbestiy.append(y1)
    else :
        Pbestix.append(x1_before)
        Pbestiy.append(y1_before)
    if func(x2,y2)<=func(x2_before,y2_before):
        Pbestix.append(x2)
        Pbestiy.append(y2)
    else :
        Pbestix.append(x2_before)
        Pbestiy.append(y2_before)
    if func(x3,y3)<=func(x3_before,y3_before):
        Pbestix.append(x3)
        Pbestiy.append(y3)
    else :
        Pbestix.append(x3_before)
        Pbestiy.append(y3_before)

#fungsi untuk mencari nilai vix
def vix_func(vixmin1,xi,i):
    return (w * vixmin1)+(c1*r1*(Pbestix[i] - xi))+(c2*r2*(Gbestx-xi))

#fungsi untuk mencari nilai viy
def viy_func(viymin1,yi,i):
    return (w * viymin1)+(c1*r1*(Pbestiy[i] - yi))+(c2*r2*(Gbesty-yi))

n = int(input("masukkan jumlah iterasi: "))
print()

#Looping berdasarkan jumlah iterasi yang diinginkan
for index in range(n):
    print("\033[0;31m"+f"iterasi ke-{index+1}"+"\033[0m")
    print(f"nilai (x1,y1): ({xi['x1']},{yi['y1']})")
    print(f"nilai (x2,y2): ({xi['x2']},{yi['y2']})")
    print(f"nilai (x3,y3): ({xi['x3']},{yi['y3']})")
    print()
    print(f"nilai f(x1,y1): {func(xi['x1'],yi['y1'])}")
    print(f"nilai f(x2,y2): {func(xi['x2'],yi['y2'])}")
    print(f"nilai f(x3,y3): {func(xi['x3'],yi['y3'])}")
    print()
    #Pengosongan array Pbestix dan Pbestiy
    Pbestix.clear()
    Pbestiy.clear()

    #Kondisional statetement yang mana jika index nya sama dengan 0 fungsi fxy_minimum_iterasi1 akan dijalankan jika tidak terpenuhi fxy_minimum_selanjutnya yang dijalankan
    if index == 0 :
        fxy_minimum_iterasi1(xi["x1"],xi["x2"],xi["x3"],yi["y1"],yi["y2"],yi["y3"])
    else:
        fxy_minimum_selanjutnya(xi_before["x1"],xi["x1"],xi_before["x2"],xi["x2"],xi_before["x3"],xi["x3"],yi_before["y1"],yi["y1"],yi_before["y2"],yi["y2"],yi_before["y3"],yi["y3"])

    #Memanggil fungsi xy_minimum
    xy_mininum(Pbestix[0],Pbestix[1],Pbestix[2],Pbestiy[0],Pbestiy[1],Pbestiy[2])

    #update nilai vix berdasarkan fungsi vix_func
    vix["v1"] = vix_func(vix["v1"],xi["x1"],0)
    vix["v2"] = vix_func(vix["v2"],xi["x2"],1)
    vix["v3"] = vix_func(vix["v3"],xi["x3"],2)
    
    #update nilai viy berdasarkan fungsi viy_func
    viy["v1"] = viy_func(viy["v1"],yi["y1"],0)
    viy["v2"] = viy_func(viy["v2"],yi["y2"],1)
    viy["v3"] = viy_func(viy["v3"],yi["y3"],2)
    
    #Update nilai xi penampungan (xi_before) dengan nilai dari xi iterasi sekarang
    xi_before["x1"] = xi["x1"]
    xi_before["x2"] = xi["x2"]
    xi_before["x3"] = xi["x3"]
    
    #updata nilai dari xi iterasi sekarang
    xi["x1"] = xi_before["x1"] + vix["v1"]
    xi["x2"] = xi_before["x2"] + vix["v2"]
    xi["x3"] = xi_before["x3"] + vix["v3"]
    
    #Update nilai yi penampungan (yi_before) dengan nilai dari yi iterasi sekarang
    yi_before["y1"] = yi["y1"]
    yi_before["y2"] = yi["y2"]
    yi_before["y3"] = yi["y3"]
    
    #update nilai dari yi iterasi sekarang
    yi["y1"] = yi_before["y1"] + viy["v1"]
    yi["y2"] = yi_before["y2"] + viy["v2"]
    yi["y3"] = yi_before["y3"] + viy["v3"]

print(f"Nilai Gbest: ({Gbestx}, {Gbesty})")
print(f"Nilai minimum f(x,y): {func(Gbestx,Gbesty)}")