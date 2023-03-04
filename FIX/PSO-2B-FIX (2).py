import random
#fungsi f(X,y)
def func(x,y):
    return (1.5-x+x*y)**2+(2.25-x+x*y**2)**2+(2.625-x+x*y**3)**2
#inisialisasi variabel xi awal untuk iterasi pertama
xi = {
    "x1" : random.uniform(-4.5,4.5),
    "x2" : random.uniform(-4.5,4.5),
    "x3" : random.uniform(-4.5,4.5),
    "x4" : random.uniform(-4.5,4.5),
    "x5" : random.uniform(-4.5,4.5),
    "x6" : random.uniform(-4.5,4.5),
    "x7" : random.uniform(-4.5,4.5),
    "x8" : random.uniform(-4.5,4.5),
    "x9" : random.uniform(-4.5,4.5),
    "x10": random.uniform(-4.5,4.5)
}
#inisialisasi penampungan variabel xi-1 untuk perbandingan mencari Pbestix
xi_before={
    "x1" : 0,
    "x2" : 0,
    "x3" : 0,
    "x4" : 0,
    "x5" : 0,
    "x6" : 0,
    "x7" : 0,
    "x8" : 0,
    "x9" : 0,
    "x10": 0
}
#inisialisasi variabel yi awal untuk iterasi pertama
yi = {
    "y1" : random.uniform(-4.5,4.5),
    "y2" : random.uniform(-4.5,4.5),
    "y3" : random.uniform(-4.5,4.5),
    "y4" : random.uniform(-4.5,4.5),
    "y5" : random.uniform(-4.5,4.5),
    "y6" : random.uniform(-4.5,4.5),
    "y7" : random.uniform(-4.5,4.5),
    "y8" : random.uniform(-4.5,4.5),
    "y9" : random.uniform(-4.5,4.5),
    "y10": random.uniform(-4.5,4.5)
}
#inisialisasi penampungan variabel yi-1 untuk perbandingan mencari Pbestiy
yi_before={
    "y1" : 0,
    "y2" : 0,
    "y3" : 0,
    "y4" : 0,
    "y5" : 0,
    "y6" : 0,
    "y7" : 0,
    "y8" : 0,
    "y9" : 0,
    "y10": 0
}
#inisialisasi vo
v0 = 0
#inisialisasi vix setelah terjadi iterasi
vix = {
    "v1":v0,
    "v2":v0,
    "v3":v0,
    "v4":v0,
    "v5":v0,
    "v6":v0,
    "v7":v0,
    "v8":v0,
    "v9":v0,
    "v10":v0
}
##inisialisasi vix setelah terjadi iterasi
viy = {
    "v1":v0,
    "v2":v0,
    "v3":v0,
    "v4":v0,
    "v5":v0,
    "v6":v0,
    "v7":v0,
    "v8":v0,
    "v9":v0,
    "v10":v0
}
#inisialisasi variabel-variabel lainnya
c1=1/2
c2=1
r1=random.randint(0,1)
r2=random.randint(0,1)
w=1
Gbest=0
besti=0
Pbestix=[]
Pbestiy=[]

#fungsi untuk mencari Gbestx dan Gbesty dengan membandingkan semua fungsi(x,y) lalu mengambil nilai x & y dari fungsi yang menghasilkan nilai paling kecil
def xy_mininum(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10):
    global Gbestx
    global Gbesty
    if func(x1,y1)<=func(x2,y2) and func(x1,y1)<=func(x3,y3) and func(x1,y1)<=func(x4,y4) and func(x1,y1)<=func(x5,y5) and func(x1,y1)<=func(x6,y6) and func(x1,y1)<=func(x7,y7) and func(x1,y1)<=func(x8,y8) and func(x1,y1)<=func(x9,y9) and func(x1,y1)<=func(x10,y10) :
        Gbestx = x1
        Gbesty = y1
    if func(x2,y2)<=func(x1,y1) and func(x2,y2)<=func(x3,y3) and func(x2,y2)<=func(x4,y4) and func(x2,y2)<=func(x5,y5) and func(x2,y2)<=func(x6,y6) and func(x2,y2)<=func(x7,y7) and func(x2,y2)<=func(x8,y8) and func(x2,y2)<=func(x9,y9) and func(x2,y2)<=func(x10,y10) :
        Gbestx = x2
        Gbesty = y2
    if func(x3,y3)<=func(x2,y2) and func(x3,y3)<=func(x1,y1) and func(x3,y3)<=func(x4,y4) and func(x3,y3)<=func(x5,y5) and func(x3,y3)<=func(x6,y6) and func(x3,y3)<=func(x7,y7) and func(x3,y3)<=func(x8,y8) and func(x3,y3)<=func(x9,y9) and func(x3,y3)<=func(x10,y10) :
        Gbestx = x3
        Gbesty = y3
    if func(x4,y4)<=func(x2,y2) and func(x4,y4)<=func(x3,y3) and func(x4,y4)<=func(x1,y1) and func(x4,y4)<=func(x5,y5) and func(x4,y4)<=func(x6,y6) and func(x4,y4)<=func(x7,y7) and func(x4,y4)<=func(x8,y8) and func(x4,y4)<=func(x9,y9) and func(x4,y4)<=func(x10,y10) :
        Gbestx = x4
        Gbesty = y4
    if func(x5,y5)<=func(x2,y2) and func(x5,y5)<=func(x3,y3) and func(x5,y5)<=func(x4,y4) and func(x5,y5)<=func(x1,y1) and func(x5,y5)<=func(x6,y6) and func(x5,y5)<=func(x7,y7) and func(x5,y5)<=func(x8,y8) and func(x5,y5)<=func(x9,y9) and func(x5,y5)<=func(x10,y10) :
        Gbestx = x5
        Gbesty = y5
    if func(x6,y6)<=func(x2,y2) and func(x6,y6)<=func(x3,y3) and func(x6,y6)<=func(x4,y4) and func(x6,y6)<=func(x5,y5) and func(x6,y6)<=func(x1,y1) and func(x6,y6)<=func(x7,y7) and func(x6,y6)<=func(x8,y8) and func(x6,y6)<=func(x9,y9) and func(x6,y6)<=func(x10,y10) :
        Gbestx = x6
        Gbesty = y6
    if func(x7,y7)<=func(x2,y2) and func(x7,y7)<=func(x3,y3) and func(x7,y7)<=func(x4,y4) and func(x7,y7)<=func(x5,y5) and func(x7,y7)<=func(x6,y6) and func(x7,y7)<=func(x1,y1) and func(x7,y7)<=func(x8,y8) and func(x7,y7)<=func(x9,y9) and func(x7,y7)<=func(x10,y10) :
        Gbestx = x7
        Gbesty = y7
    if func(x8,y8)<=func(x2,y2) and func(x8,y8)<=func(x3,y3) and func(x8,y8)<=func(x4,y4) and func(x8,y8)<=func(x5,y5) and func(x8,y8)<=func(x6,y6) and func(x8,y8)<=func(x7,y7) and func(x8,y8)<=func(x1,y1) and func(x8,y8)<=func(x9,y9) and func(x8,y8)<=func(x10,y10) :
        Gbestx = x8
        Gbesty = y8
    if func(x9,y9)<=func(x2,y2) and func(x9,y9)<=func(x3,y3) and func(x9,y9)<=func(x4,y4) and func(x9,y9)<=func(x5,y5) and func(x9,y9)<=func(x6,y6) and func(x9,y9)<=func(x7,y7) and func(x9,y9)<=func(x8,y8) and func(x9,y9)<=func(x1,y1) and func(x9,y9)<=func(x10,y10) :
        Gbestx = x9
        Gbesty = y9
    if func(x10,y10)<=func(x2,y2) and func(x10,y10)<=func(x3,y3) and func(x10,y10)<=func(x4,y4) and func(x10,y10)<=func(x5,y5) and func(x10,y10)<=func(x6,y6) and func(x10,y10)<=func(x7,y7) and func(x10,y10)<=func(x8,y8) and func(x10,y10)<=func(x9,y9) and func(x10,y10)<=func(x1,y1) :
        Gbestx = x10
        Gbesty = y10
        
#fungsi untuk yang akan mengambil langsung nilai xi & yi dan menympannya kedalam array Pbestix dan Pbestiy jika sedang dalam iterasi pertama
def fxy_minimum_iterasi1(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10):
    Pbestix.append(x1)
    Pbestix.append(x2)
    Pbestix.append(x3)
    Pbestix.append(x4)
    Pbestix.append(x5)
    Pbestix.append(x6)
    Pbestix.append(x7)
    Pbestix.append(x8)
    Pbestix.append(x9)
    Pbestix.append(x10)
    Pbestiy.append(y1)
    Pbestiy.append(y2)
    Pbestiy.append(y3)
    Pbestiy.append(y4)
    Pbestiy.append(y5)
    Pbestiy.append(y6)
    Pbestiy.append(y7)
    Pbestiy.append(y8)
    Pbestiy.append(y9)
    Pbestiy.append(y10)
# fungsi untuk mengambil nilai xi & yi dan menyimpannya kedalam Pbestix dan Pbestiy dengan cara membandikan antara nilai fungsi f(x,y) iterasi sekarang dengan iterasi sebelumnya
def fxy_minimum_selanjutnya(x1_before,x1,x2_before,x2,x3_before,x3,x4_before,x4,x5_before,x5,x6_before,x6,x7_before,x7,x8_before,x8,x9_before,x9,x10_before,x10,y1_before,y1,y2_before,y2,y3_before,y3,y4_before,y4,y5_before,y5,y6_before,y6,y7_before,y7,y8_before,y8,y9_before,y9,y10_before,y10):
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
    if func(x4,y4)<=func(x4_before,y4_before):
        Pbestix.append(x4)
        Pbestiy.append(y4)
    else :
        Pbestix.append(x4_before)
        Pbestiy.append(y4_before)
    if func(x5,y5)<=func(x5_before,y5_before):
        Pbestix.append(x5)
        Pbestiy.append(y5)
    else :
        Pbestix.append(x5_before)
        Pbestiy.append(y5_before)
    if func(x6,y6)<=func(x6_before,y6_before):
        Pbestix.append(x6)
        Pbestiy.append(y6)
    else :
        Pbestix.append(x6_before)
        Pbestiy.append(y6_before)
    if func(x7,y7)<=func(x7_before,y7_before):
        Pbestix.append(x7)
        Pbestiy.append(y7)
    else :
        Pbestix.append(x7_before)
        Pbestiy.append(y7_before)
    if func(x8,y8)<=func(x8_before,y8_before):
        Pbestix.append(x8)
        Pbestiy.append(y8)
    else :
        Pbestix.append(x8_before)
        Pbestiy.append(y8_before)
    if func(x9,y9)<=func(x9_before,y9_before):
        Pbestix.append(x9)
        Pbestiy.append(y9)
    else :
        Pbestix.append(x9_before)
        Pbestiy.append(y9_before)
    if func(x10,y10)<=func(x10_before,y10_before):
        Pbestix.append(x10)
        Pbestiy.append(y10)
    else :
        Pbestix.append(x10_before)
        Pbestiy.append(y10_before)
#fungsi untuk mencari nilai vix
def vix_func(vixmin1,xi,i):
    return (w * vixmin1)+(c1*r1*(Pbestix[i] - xi)) +(c2*r2*(Gbestx-xi))
#fungsi untuk mencari nilai viy
def viy_func(viymin1,yi,i):
    return (w * viymin1)+(c1*r1*(Pbestiy[i] - yi)) +(c2*r2*(Gbesty-yi))

n = int(input("masukkan jumlah iterasi: "))
#Looping berdasarkan jumlah iterasi yang diinginkan
print(f"nilai x1,y1,f(x1,y1) pada iterasi ke-1: [{xi['x1']}],[{yi['y1']}],[{func(xi['x1'],yi['y1'])}]")
print(f"nilai x2,y2,f(x2,y2) pada iterasi ke-1: [{xi['x2']}],[{yi['y2']}],[{func(xi['x2'],yi['y2'])}]")
print(f"nilai x3,y3,f(x3,y3) pada iterasi ke-1: [{xi['x3']}],[{yi['y3']}],[{func(xi['x3'],yi['y3'])}]")
print(f"nilai x4,y4,f(x4,y4) pada iterasi ke-1: [{xi['x4']}],[{yi['y4']}],[{func(xi['x4'],yi['y4'])}]")
print(f"nilai x5,y5,f(x5,y5) pada iterasi ke-1: [{xi['x5']}],[{yi['y5']}],[{func(xi['x5'],yi['y5'])}]")
print(f"nilai x6,y6,f(x6,y6) pada iterasi ke-1: [{xi['x6']}],[{yi['y6']}],[{func(xi['x6'],yi['y6'])}]")
print(f"nilai x7,y7,f(x7,y7) pada iterasi ke-1: [{xi['x7']}],[{yi['y7']}],[{func(xi['x7'],yi['y7'])}]")
print(f"nilai x8,y8,f(x8,y8) pada iterasi ke-1: [{xi['x8']}],[{yi['y8']}],[{func(xi['x8'],yi['y8'])}]")
print(f"nilai x9,y9,f(x9,y9) pada iterasi ke-1: [{xi['x9']}],[{yi['y9']}],[{func(xi['x9'],yi['y9'])}]")
print(f"nilai x10,y10,f(x10,y10) pada iterasi ke-1: [{xi['x10']}],[{yi['y10']}],[{func(xi['x10'],yi['y10'])}]")
print()

for index in range(n):
    #Pengosongan array Pbestix dan Pbestiy
    Pbestix.clear()
    Pbestiy.clear()
    
#Memanggil fungsi xy_minimum
    xy_mininum(xi["x1"],xi["x2"],xi["x3"],xi["x4"],xi["x5"],xi["x6"],xi["x7"],xi["x8"],xi["x9"],xi["x10"],yi["y1"],yi["y2"],yi["y3"],yi["y4"],yi["y5"],yi["y6"],yi["y7"],yi["y8"],yi["y9"],yi["y10"])

#Kondisional statetement yang mana jika index nya sama dengan 0 fungsi fxy_minimum_iterasi1 akan dijalankan jika tidak terpenuhi fxy_minimum_selanjutnya yang dijalankan
    if index == 0 :
        fxy_minimum_iterasi1(xi["x1"],xi["x2"],xi["x3"],xi["x4"],xi["x5"],xi["x6"],xi["x7"],xi["x8"],xi["x7"],xi["x8"],yi["y1"],yi["y2"],yi["y3"],yi["y4"],yi["y5"],yi["y6"],yi["y7"],yi["y8"],yi["y9"],yi["y10"])
    else:
        fxy_minimum_selanjutnya(xi_before["x1"],xi["x1"],xi_before["x2"],xi["x2"],xi_before["x3"],xi["x3"],xi_before["x4"],xi["x4"],xi_before["x5"],xi["x5"],xi_before["x6"],xi["x6"],xi_before["x7"],xi["x7"],xi_before["x8"],xi["x8"],xi_before["x9"],xi["x9"],xi_before["x10"],xi["x10"],yi_before["y1"],yi["y1"],yi_before["y2"],yi["y2"],yi_before["y3"],yi["y3"],yi_before["y4"],yi["y4"],xi_before["x5"],xi["x5"],xi_before["x6"],xi["x6"],xi_before["x7"],xi["x7"],xi_before["x8"],xi["x8"],xi_before["x9"],xi["x9"],xi_before["x10"],xi["x10"],)

    #update nilai vix berdasarkan fungsi vix_func
    vix["v1"] = vix_func(vix["v1"],xi["x1"],0)
    vix["v2"] = vix_func(vix["v2"],xi["x2"],1)
    vix["v3"] = vix_func(vix["v3"],xi["x3"],2)
    vix["v4"] = vix_func(vix["v4"],xi["x4"],3)
    vix["v5"] = vix_func(vix["v5"],xi["x5"],4)
    vix["v6"] = vix_func(vix["v6"],xi["x6"],5)
    vix["v7"] = vix_func(vix["v7"],xi["x7"],6)
    vix["v8"] = vix_func(vix["v8"],xi["x8"],7)
    vix["v9"] = vix_func(vix["v9"],xi["x9"],8)
    vix["v10"] = vix_func(vix["v10"],xi["x10"],9)

    #update nilai viy berdasarkan fungsi viy_func
    viy["v1"] = viy_func(viy["v1"],yi["y1"],0)
    viy["v2"] = viy_func(viy["v2"],yi["y2"],1)
    viy["v3"] = viy_func(viy["v3"],yi["y3"],2)
    viy["v4"] = viy_func(viy["v4"],yi["y4"],3)
    viy["v5"] = viy_func(viy["v5"],yi["y5"],4)
    viy["v6"] = viy_func(viy["v6"],yi["y6"],5)
    viy["v7"] = viy_func(viy["v7"],yi["y7"],6)
    viy["v8"] = viy_func(viy["v8"],yi["y8"],7)
    viy["v9"] = viy_func(viy["v9"],yi["y9"],8)
    viy["v10"] = viy_func(viy["v10"],yi["y10"],9)

#Update nilai xi penampungan (xi_before) dengan nilai dari xi iterasi sekarang
    xi_before["x1"] = xi["x1"]
    xi_before["x2"] = xi["x2"]
    xi_before["x3"] = xi["x3"]
    xi_before["x4"] = xi["x4"]
    xi_before["x5"] = xi["x5"]
    xi_before["x6"] = xi["x6"]
    xi_before["x7"] = xi["x7"]
    xi_before["x8"] = xi["x8"]
    xi_before["x9"] = xi["x9"]
    xi_before["x10"] = xi["x10"]

#updata nilai dari xi iterasi sekarang
    xi["x1"] = xi_before["x1"] + vix["v1"]

    xi["x2"] = xi_before["x2"] + vix["v2"]
    
    xi["x3"] = xi_before["x3"] + vix["v3"]
    
    xi["x4"] = xi_before["x4"] + vix["v4"]
    
    xi["x5"] = xi_before["x5"] + vix["v5"]
    
    xi["x6"] = xi_before["x6"] + vix["v6"]
    
    xi["x7"] = xi_before["x7"] + vix["v7"]

    xi["x8"] = xi_before["x8"] + vix["v8"]
    
    xi["x9"] = xi_before["x9"] + vix["v9"]
    
    xi["x10"] = xi_before["x10"] + vix["v10"]


#Update nilai yi penampungan (yi_before) dengan nilai dari yi iterasi sekarang
    yi_before["y1"] = yi["y1"]
    yi_before["y2"] = yi["y2"]
    yi_before["y3"] = yi["y3"]
    yi_before["y4"] = yi["y4"]
    yi_before["y5"] = yi["y5"]
    yi_before["y6"] = yi["y6"]
    yi_before["y7"] = yi["y7"]
    yi_before["y8"] = yi["y8"]
    yi_before["y9"] = yi["y9"]
    yi_before["y10"] = yi["y10"]

#update nilai dari yi iterasi sekarang 
    # yi["y1"] = yi_before["y1"] + viy["v1"]
    # yi["y2"] = yi_before["y2"] + viy["v2"]
    # yi["y3"] = yi_before["y3"] + viy["v3"]
    # yi["y4"] = yi_before["y4"] + viy["v4"]
    # yi["y5"] = yi_before["y5"] + viy["v5"]
    # yi["y6"] = yi_before["y6"] + viy["v6"]
    # yi["y7"] = yi_before["y7"] + viy["v7"]
    # yi["y8"] = yi_before["y8"] + viy["v8"]
    # yi["y9"] = yi_before["y9"] + viy["v9"]
    # yi["y10"] = yi_before["y10"] + viy["v10"]
    yi["y1"] = yi_before["y1"] + viy["v1"]
    
    yi["y2"] = yi_before["y2"] + viy["v2"]

    yi["y3"] = yi_before["y3"] + viy["v3"]
    
    yi["y4"] = yi_before["y4"] + viy["v4"]

    yi["y5"] = yi_before["y5"] + viy["v5"]
    
    yi["y6"] = yi_before["y6"] + viy["v6"]
    
    yi["y7"] = yi_before["y7"] + viy["v7"]
    
    yi["y8"] = yi_before["y8"] + viy["v8"]
    
    yi["y9"] = yi_before["y9"] + viy["v9"]

    yi["y10"] = yi_before["y10"] + viy["v10"]
    
    print(f"nilai x1,y1,f(x1,y1) pada iterasi ke{index+2}: [{xi['x1']}],[{yi['y1']}],[{func(xi['x1'],yi['y1'])}]")
    print(f"nilai x2,y2,f(x2,y2) pada iterasi ke{index+2}: [{xi['x2']}],[{yi['y2']}],[{func(xi['x2'],yi['y2'])}]")
    print(f"nilai x3,y3,f(x3,y3) pada iterasi ke{index+2}: [{xi['x3']}],[{yi['y3']}],[{func(xi['x3'],yi['y3'])}]")
    print(f"nilai x4,y4,f(x4,y4) pada iterasi ke{index+2}: [{xi['x4']}],[{yi['y4']}],[{func(xi['x4'],yi['y4'])}]")
    print(f"nilai x5,y5,f(x5,y5) pada iterasi ke{index+2}: [{xi['x5']}],[{yi['y5']}],[{func(xi['x5'],yi['y5'])}]")
    print(f"nilai x6,y6,f(x6,y6) pada iterasi ke{index+2}: [{xi['x6']}],[{yi['y6']}],[{func(xi['x6'],yi['y6'])}]")
    print(f"nilai x7,y7,f(x7,y7) pada iterasi ke{index+2}: [{xi['x7']}],[{yi['y7']}],[{func(xi['x7'],yi['y7'])}]")
    print(f"nilai x8,y8,f(x8,y8) pada iterasi ke{index+2}: [{xi['x8']}],[{yi['y8']}],[{func(xi['x8'],yi['y8'])}]")
    print(f"nilai x9,y9,f(x9,y9) pada iterasi ke{index+2}: [{xi['x9']}],[{yi['y9']}],[{func(xi['x9'],yi['y9'])}]")
    print(f"nilai x10,y10,f(x10,y10) pada iterasi ke{index+2}: [{xi['x10']}],[{yi['y10']}],[{func(xi['x10'],yi['y10'])}]")
    print()

print(f"Nilai Gbestx: {Gbestx}")
print(f"Nilai Gbesty: {Gbesty}")
