import random

# Fungsi f(x)
def func(x):
    return (2*x**2+16)

#inisialisasi variabel xi awal untuk iterasi pertama
xi = {
    "x1" : 1/2,
    "x2" : 1,
    "x3" : 3,
}

#inisialisasi penampungan variabel xi-1 untuk perbandingan mencari Pbestix
xi_before={
    "x1" : 0,
    "x2" : 0,
    "x3" : 0,
}

#inisialisasi vo
v0 = 0

#inisialisasi vi setelah terjadi iterasi
vi = {
    "v1":v0,
    "v2":v0,
    "v3":v0,
}

#inisialisasi variabel-variabel lainnya
c1 = 1/2
c2 = 1
r1 = 1/2
r2 = 1/2
w = 1
Gbest = 0
Pbesti = []

#fungsi untuk mencari Gbest dengan membandingkan semua fungsi(x) lalu mengambil nilai x dari fungsi yangmenghasilkan nilai paling kecil
def x_minimum(x1,x2,x3):
    global Gbest
    if func(x1)<=func(x2) and func(x1)<=func(x3):
        Gbest = x1
    elif func(x2)<=func(x1) and func(x2)<=func(x3):
        Gbest = x2
    elif func(x3)<=func(x1) and func(x3)<=func(x2):
        Gbest = x3

#fungsi untuk yang akan mengambil langsung nilai xi dan menympannya kedalam array Pbesti jika sedang dalam iterasi pertama
def fx_minimum_iterasi1(x1,x2,x3):
    Pbesti.append(x1)
    Pbesti.append(x2)
    Pbesti.append(x3)

# fungsi untuk mengambil nilai xi dan menyimpannya kedalam Pbesti dengan cara membandikan antara nilai fungsi f(x) iterasi sekarang dengan iterasi sebelumnya
def fx_minimum_selanjutnya(x1_before,x1,x2_before,x2,x3_before,x3):
    if func(x1)<=func(x1_before):
        Pbesti.append(x1)
    else :
        Pbesti.append(x1_before)
    if func(x2)<=func(x2_before):
        Pbesti.append(x2)
    else :
        Pbesti.append(x2_before)

    if func(x3)<=func(x3_before):
        Pbesti.append(x3)
    else :
        Pbesti.append(x3_before)
    
#fungsi untuk mencari nilai vi
def vi_func(vimin1,xi,i):
    return (w * vimin1)+(c1*r1*((Pbesti[i]) - xi))+(c2*r2*((Gbest) - xi))

n = int(input("masukkan jumlah iterasi: "))
print()

#Looping berdasarkan jumlah iterasi yang diinginkan
for index in range(n):
    print("\033[0;31m"+f"iterasi ke-{index+1}"+"\033[0m")
    print(f"nilai (x1): {xi['x1']}")
    print(f"nilai (x2): {xi['x2']}")
    print(f"nilai (x3): {xi['x3']}")
    print()
    print(f"nilai f(x1): {func(xi['x1'])}")
    print(f"nilai f(x2): {func(xi['x2'])}")
    print(f"nilai f(x3): {func(xi['x3'])}")
    print()
    #Pengosongan array Pbesti
    Pbesti.clear()

    #Kondisional statetement yang mana jika index nya sama dengan 0 fungsi fx_minimum_iterasi1 akan dijalankan jika tidak terpenuhi fx_minimum_selanjutnya yang dijalankan
    if index == 0 :
        fx_minimum_iterasi1(xi["x1"],xi["x2"],xi["x3"])
    else:
        fx_minimum_selanjutnya(xi_before["x1"],xi["x1"],xi_before["x2"],xi["x2"],xi_before["x3"],xi["x3"])

    #Memanggil fungsi x_minimum
    x_minimum(Pbesti[0],Pbesti[1],Pbesti[2])

    #update nilai vi berdasarkan fungsi vi_func
    vi["v1"]= vi_func(vi["v1"],xi["x1"],0)
    vi["v2"] = vi_func(vi["v2"],xi["x2"],1)
    vi["v3"] = vi_func(vi["v3"],xi["x3"],2)

    #Update nilai xi penampungan (xi_before) dengan nilai dari xi iterasi sekarang
    xi_before["x1"] = xi["x1"]
    xi_before["x2"] = xi["x2"]
    xi_before["x3"] = xi["x3"]
    

    #update nilai dari xi iterasi sekarang
    xi["x1"] = xi_before["x1"] + vi["v1"]
    xi["x2"] = xi_before["x2"] + vi["v2"]
    xi["x3"] = xi_before["x3"] + vi["v3"]

print(f"Nilai Gbest: {Gbest}")
print(f"Nilai minimum f(x): {func(Gbest)}")