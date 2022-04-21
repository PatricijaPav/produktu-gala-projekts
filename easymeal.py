class Augli:
    def __init__(self, nosaukums, kaloriju_daudzums, tauku_daudzums, cukura_daudzums ):
        self.nosaukums = nosaukums
        self.kaloriju_daudzums = kaloriju_daudzums
        self.tauku_daudzums = tauku_daudzums
        self.cukura_daudzums = cukura_daudzums

visi_Augli = [
  "ananas-      kcal: 0.5,    tauki: 0.001g,  cukurs: 0.1g",
  "apelsīns-    kcal: 0.471,  tauki: 0.001g,  cukurs: 0.09g",
  "arbūzs-      kcal: 0.304,  tauki: 0.002g,  cukurs: 0.06g",
  "avenes-      kcal: 0.52,   tauki: 0.007g,  cukurs: 0.044g",
  "ābols-       kcal: 0.521,  tauki: 0.002g,  cukurs: 0.1g",
  "banāns-      kcal: 0.887,  tauki: 0.003g,  cukurs: 0.12g",
  "bumbieris-   kcal: 0.571,  tauki: 0.001g,  cukurs: 0.1g",
  "dzērvenes-   kcal: 0.46,   tauki: 0.001g,  cukurs: 0.04g",
  "ērkšķogas-   kcal: 0.43,   tauki: 0.009g,  cukurs: 0.15g",
  "granātābols- kcal: 0.68,   tauki: 0.01g,   cukurs: 0.07g",
  "jāņogas-     kcal: 0.5664, tauki: 0.004g,  cukurs: 0.075g",
  "lācenes-     kcal: 0.5497, tauki: 0.0106,  cukurs: 0.0581",
  "mandarīns-   kcal: 0.533,  tauki: 0.003g,  cukurs: 0.11g",
  "mellenes-    kcal: 0.57,   tauki: 0.003g,  cukurs: 0.1g",
  "melone-      kcal: 0.33,   tauki: 0.002g,  cukurs: 0.12g",
  "nektarīns-   kcal: 0.442,  tauki: 0.003g,  cukurs: 0.08g",
  "persiki-     kcal: 0.47,   tauki: 0.005g,  cukurs: 0.11g",
  "vīnogas-     kcal: 0.66,   tauki: 0.004g,  cukurs: 0.16g",
  "zemenes-     kcal: 0.325,  tauki: 0.003g,  cukurs: 0.049g",
]
a1 = Augli("ābols", 0.521, 0.002, 0.1)
a2 = Augli("ananas", 0.5, 0.001, 0.1)
a3 = Augli("apelsīns", 0.471, 0.001, 0.09)
a4 = Augli("arbūzs", 0.304, 0.002, 0.06)
a5 = Augli("avenes", 0.52, 0.007, 0.044)
a6 = Augli("banāns", 0.887, 0.003, 0.12)
a7 = Augli("bumbieris", 0.571, 0.001, 0.1)
a8 = Augli("dzērvenes", 0.46, 0.001, 0.07)
a9 = Augli("ērkšķogas", 0.43, 0.009, 0.15)
a10 = Augli("jāņogas", 0.5664, 0.004, 0.075)
a11 = Augli("kazenes", 0.43, 0.005, 0.049)
a12 = Augli("kivi", 0.6, 0.005, 0.09)
a13 = Augli("ķirši", 0.5, 0.003, 0.08)
a14 = Augli("mandarīns", 0.533, 0.003, 0.11)
a15 = Augli("mellenes", 0.57, 0.003, 0.1)
a16 = Augli("melone", 0.33, 0.002, 0.12)
a17 = Augli("nektarīns", 0.442, 0.003, 0.08)
a18 = Augli("persiki", 0.47, 0.005, 0.11)
a19 = Augli("upenes", 0.63, 0, 0.015)
a20 = Augli("vīnogas", 0.66, 0.004, 0.16)
a21 = Augli("zemenes", 0.325, 0.003, 0.049)
a22 = Augli("lācenes", 0.5497, 0.0106, 0.0581)

class Darzeni:

    def __init__(self, nosaukums, kaloriju_daudzums, tauku_daudzums, cukura_daudzums ):
        self.nosaukums = nosaukums
        self.kaloriju_daudzums = kaloriju_daudzums
        self.tauku_daudzums = tauku_daudzums
        self.cukura_daudzums = cukura_daudzums

visi_darzeni = [
"Avokado-            kcal: 1,9814  tauki: 0,194g   cukurs: 0,0066g",
"Baklažāns-          kcal: 0.2223, tauki: 0.002g,  cukurs: 0.029g",
"Baravikas-          kcal: 0.3011, tauki: 0.0023g, cukurs: 0.0161g",
"Bietes-             kcal: 0.3824, tauki: 0.002g,  cukurs: 0.068g",
"Brokoļi-            kcal: 0.3489, tauki: 0.003g,  cukurs: 0.0195g",
"Burkāni-            kcal: 0,413,  tauki: 0,002g   cukurs: 0,047g",
"Cukini-             kcal: 0.24,   tauki: 0.003g,  cukurs: 0.025g",
"Gailenes-           kcal: 0.2677, tauki: 0.0069g, cukurs: 0.0144g",
"Gurķis-             kcal: 0,15,   tauki: 0,001g   cukurs: 0,017g",
"Kabacis-            kcal: 0.17,   tauki: 0.004g,  cukurs: 0.003g",
"Kartupeļi-          kcal: 0.76,   tauki: 0.002,   cukurs: 0.006",
"Kāposts-            kcal: 0.2772, tauki: 0.002g,  cukurs: 0.0406g",
"Kukurūza-           kcal: 1.2763, tauki: 0.0129g, cukurs: 0.0342g",
"Ķiploks-            kcal: 1.0827, tauki: 0.006g,  cukurs: 0.016g",
"Ķirbis-             kcal: 0.1577, tauki: 0.001,   cukuri: 0.017g",
"Paprika-            kcal: 0.2103, tauki: 0.003g,  cukuri: 0.024g",
"Redīsi-             kcal: 0.2462, tauki: 0.0003g, cukurs: 0.0307g",
"Saldais kartupelis- kcal: 0.8795, tauki: 0.0005g, cukuri: 0.0454g",
"Sīpols-             kcal: 0.3011, tauki: 0.002g,  cukurs: 0.048g",
"Spārģeļi-           kcal:  0.2,   tauki: 0.001g,  cukurs: 0.019g",
"Tomāti-             kcal: 0.2271, tauki: 0.003g,  cukurs: 0.0335g",
"Zirņi-              kcal: 0.7505, tauki: 0.0079g, cukurs: 0.0531g"]

d1 = Darzeni("burkāni", 0.413, 0.002, 0.047)
d2 = Darzeni("gurķi", 0.15, 0.001, 0.017)
d3 = Darzeni("kartupeļi", 0.76, 0.002, 0.006)
d4 = Darzeni("kāposts", 0.2772, 0.002, 0.0406)
d5 = Darzeni("avokado", 1.9814, 0.194, 0.0066)
d6 = Darzeni("ķirbis", 0.1577, 0.001, 0.017)
d7 = Darzeni("brokoļi", 0.3489, 0.003, 0.0195)
d8 = Darzeni("sīpols", 0.3011, 0.002, 0.048)
d9 = Darzeni("ķiploks", 1.0827, 0.006, 0.016)
d10 = Darzeni("paprika", 0.2103, 0.003, 0.024)
d11 = Darzeni("kabacis", 0.17, 0.004, 0.003)
d12 = Darzeni("kukurūza", 1.2763, 0.0129, 0.0342)
d13 = Darzeni("cukini", 0.24, 0.003, 0.025)
d14 = Darzeni("saldais kartupelis", 0.8795, 0.0005, 0.0454)
d15 = Darzeni("redīsi", 0.2462, 0.0003, 0.0307)
d16 = Darzeni("zirņi", 0.7505, 0.0079, 0.0531)
d17= Darzeni("baklažāns", 0.2223, 0.002, 0.029)
d18 = Darzeni("baravikas", 0.3011, 0.0023, 0.0161)
d19 = Darzeni("gailenes", 0.2677, 0.0069, 0.0144)
d21 = Darzeni("spārģeļi", 0.2, 0.001, 0.019)
d22 = Darzeni("tomāti", 0.2271, 0.003, 0.0335)
d23 = Darzeni("bietes", 0.3824, 0.002, 0.068)
d24 = Darzeni("nav", 0, 0, 0) 

class PienaProdukti:

    def __init__(self, nosaukums, kaloriju_daudzums, tauku_daudzums, cukura_daudzums):
        self.nosaukums = nosaukums
        self.kaloriju_daudzums = kaloriju_daudzums
        self.tauku_daudzums = tauku_daudzums
        self.cukura_daudzums = cukura_daudzums

visi_PienaProdukti = [
"biezpiena sieriņi- kcal: 3.14,   tauki: 0.225g,  cukurs: 0.224g",
"biezpiens-         kcal: 0.8963, tauki: 0.0151g, cukurs: 0.0236g",
"jogurts-           kcal: 0.7098, tauki: 0.0011g, cukurs: 0.142g",
"kausētais siers-   kcal: 2.978,  tauki: 0.24g,   cukurs: 0.025g",
"krējums-           kcal: 1.7615, tauki: 0.17g,   cukurs: 0.031g",
"mozarella-         kcal: 0.33,   tauki: 0.191g,  cukurs: 0.014g",
"saldais krējums-   kcal: 3.3007, tauki: 0.35g,   cukurs: 0.03g",
"siers-             kcal: 2.7701, tauki: 0.1995g, cukurs: 0.0022g",
"svaigais siers-    kcal: 2.63,   tauki: 0.24g,   cukurs: 0.034g",
"sviests-           kcal: 7.2682, tauki: 0.813g,  cukurs: 0.008g",
]

pp1 = PienaProdukti("siers", 2.7701, 0.1995, 0.0022)
pp2 = PienaProdukti("biezpiens", 0.8963, 0.0151, 0.0236)
pp3 = PienaProdukti("jogurts", 0.7098, 0.0011, 0.142)
pp4 = PienaProdukti("krējums", 1.7615, 0.17, 0.031)
pp5 = PienaProdukti("saldais krējums", 3.3007, 0.35, 0.03)
pp6 = PienaProdukti("biezpiena sieriņi", 3.14, 0.225, 0.224)
pp7 = PienaProdukti("kausētais siers", 2.978, 0.24, 0.025)
pp8 = PienaProdukti("mozarella", 0.33, 0.191, 0.014)
pp9 = PienaProdukti("svaigais siers", 2.63, 0.24, 0.034)
pp10 = PienaProdukti("sviests", 7.2682, 0.813, 0.008) 

class GalasProdukti:

    def __init__(self, nosaukums, kaloriju_daudzums, tauku_daudzums, cukura_daudzums):
        self.nosaukums = nosaukums
        self.kaloriju_daudzums = kaloriju_daudzums
        self.tauku_daudzums = tauku_daudzums
        self.cukura_daudzums = cukura_daudzums

visi_GalasProdukti = [
    "cīsiņi-       kcal: 2.26,   tauki: 0.18g,   cukurs: 0.004g",
    "cūkgaļa-      kcal: 1.9503, tauki: 0.134g,  cukurs: 0g",
    "desa-         kcal: 2.8633, tauki: 0.2657g, cukurs: 0g",
    "lielopa gaļa- kcal: 1.4794, tauki: 0.0715g, cukurs: 0g",
    "nageti-       kcal: 2.22,   tauki: 0.12g,   cukurs: 0.05g",
    "olas-         kcal: 1.6372, tauki: 0.1149g, cukurs: 0.0036g",
    "pastēte-      kcal: 3.64,   tauki: 0.35g,   cukurs: 0.0019g",
    "pelmeņi-      kcal: 2.9111, tauki: 0.1561g, cukurs: 0.0055g",
    "vistas gaļa-  kcal: 1.4316, tauki: 0.0265g, cukurs: 0g",
    "zivis-        kcal: 1.4508, tauki: 0.0265g, cukurs: 0g",
    ]

gap1 = GalasProdukti("cīsiņi", 2.26, 0.18, 0.004)
gap2 = GalasProdukti("desa", 2.8633, 0.2657, 0)
gap3 = GalasProdukti("pastēte", 3.64, 0.35, 0.0019)
gap4 = GalasProdukti("cūkgaļa", 1.9503, 0.134, 0)
gap5 = GalasProdukti("lielopa gaļa", 1.4794, 0.0715, 0)
gap6 = GalasProdukti("vistas gaļa", 1.4316, 0.0265, 0)
gap7 = GalasProdukti("pelmeņi", 2.9111, 0.1561, 0.0055)
gap8 = GalasProdukti("olas", 1.6372, 0.1149, 0.0036)
gap9 = GalasProdukti("zivis", 1.4508, 0.0265, 0)
gap10 = GalasProdukti("nageti", 2.22, 0.12, 0.05)

class GrauduProdukti:

    def __init__(self, nosaukums, kaloriju_daudzums, tauku_daudzums, cukura_daudzums):
        self.nosaukums = nosaukums
        self.kaloriju_daudzums = kaloriju_daudzums
        self.tauku_daudzums = tauku_daudzums
        self.cukura_daudzums = cukura_daudzums

visi_GrauduProdukti = [
    "auzu pārslas-    kcal: 0.4804, tauki: 0.0091g, cukurs: 0.0015g",
    "baltmaize-       kcal: 2.3064, tauki: 0.0098g, cukurs: 0.0075g",
    "graudu maize-    kcal: 3.33,   tauki: 0.104g,  cukurs: 0.008g",
    "griķi-           kcal: 1,2906, tauki: 0.008g,  cukurs: 0.0018g",
    "makaroni-        kcal: 0.9799, tauki: 0.0033g, cukurs: 0.0015g",
    "pupiņas-         kcal: 0.3561, tauki: 0.0026g, cukurs: 0.0311g",
    "rīsi-            kcal: 1,3695, tauki: 0.0028g, cukurs: 0.0016g",
    "rudzu maize-     kcal: 2.5,    tauki: 0.0133g, cukurs: 0.0106g",
    "saldskābā maize- kcal: 2.41,   tauki: 0.011g,  cukurs: 0.032g",
    "zirņi-           kcal: 0.7505, tauki: 0.0079g, cukurs: 0.0531g",
]

grp1 = GrauduProdukti("rīsi", 1.3695, 0.0028, 0.0016)
grp2 = GrauduProdukti("griķi", 1.2906, 0.008, 0.0018)
grp3 = GrauduProdukti("auzu pārslas", 0.4804, 0.0091, 0.0015)
grp4 = GrauduProdukti("makaroni", 0.9799, 0.0033, 0.0015)
grp5 = GrauduProdukti("baltmaize", 2.3064, 0.0098, 0.0075)
grp6 = GrauduProdukti("rudzu maize", 2.5, 0.0133, 0.0106)
grp7 = GrauduProdukti("saldskābā maize", 2.41, 0.011, 0.032)
grp8 = GrauduProdukti("graudu maize", 3.33, 0.104, 0.008)
grp9 = GrauduProdukti("zirņi", 0.7505, 0.0079, 0.0531)
grp10 = GrauduProdukti("pupiņas", 0.3561, 0.0026, 0.0311)

while True:
    darbiba = int(input("""Ievadiet vēlamās darbības ciparu:
    1- Izprintēt visu pieejamo produktu sarakstu
    2- Izprintēt augļu pieejamo sarakstu
    3- Izprintēt dārzeņu pieejamo sarakstu
    4- Izprintēt piena produktu pieejamo sarakstu
    5- Izprintēt gaļas produktu pieejamo sarakstu
    6- Izprintēt graudaugu produktu pieejamo sarakstu
    7- Izvēlēties produktus no pieejamajiem un veikt aprēķinu
    8- Manuāli ievadīt produktus un saskaitīt to kaloriju daudzumu, tauku daudzumu un cukura daudzumu \n"""))

    if(darbiba == 1):
        print("Visas vērtības ir norādītas 1g produkta")
        print("_____ Augļi _____")
        for vaugli in visi_Augli:
            print(vaugli)
        print(                      )

        print("_____ Dārzeņi _____")
        for vdarzeni in visi_darzeni:
            print (vdarzeni)
        print(                      )

        print("_____ Piena produkti _____")
        for vPienaProdukti in visi_PienaProdukti:
            print(vPienaProdukti)
        print(                      )

        print("_____ Gaļas Produkti _____")
        for vGalasProdukti in visi_GalasProdukti:
            print(vGalasProdukti)
        print(                      )

        print("_____ Graudaugu Produkti _____")
        for vGraudauguProdukti in visi_GrauduProdukti:
            print(vGraudauguProdukti)
        print(                      )

    elif (darbiba == 2):
        print("Visas vērtības ir norādītas 1g produkta")
        print("Augļu saraksts:")
        for auglu_saraksts in visi_Augli:
            print(auglu_saraksts)
        print("___________________")
        print(                      )

    elif(darbiba == 3):
        print("Visas vērtības ir norādītas 1g produkta")
        print("Darzeņu saraksts:")
        for darzenu_saraksts in visi_darzeni:
            print(darzenu_saraksts)
        print("___________________")
        print(                      )

    elif (darbiba == 4):
        print("Visas vērtības ir norādītas 1g produkta")
        print("Piena produktu saraksts:")
        for Piena_produktu_saraksts in visi_PienaProdukti:
            print(Piena_produktu_saraksts)
        print("___________________")
        print(                      )

    elif (darbiba == 5):
        print("Visas vērtības ir norādītas 1g produkta")
        print("Gaļas produktu saraksts:")
        for Galas_produktu_saraksts in visi_GalasProdukti:
            print(Galas_produktu_saraksts)
        print("___________________")
        print(                      )

    elif (darbiba == 6):
        print("Visas vērtības ir norādītas 1g produkta")
        print("Graudaugu produktu saraksts:")
        for Graudaugu_produktu_saraksts in visi_GrauduProdukti:
            print(Graudaugu_produktu_saraksts)
        print("___________________")
        print(                      )

    elif(darbiba == 7): 
        print("Ievadiet produkta nosaukumu, bet izmantojiet tikai mazos burtus") 
        print("Ievadiet vārdu nav, ja tik daudz produktus nevēlaties izvēlēties")    
        vards = input("Ievadiet produkta nosaukumu: ")
        daudzums = int(input("Ievadiet produkta daudzumu gramos: "))
        print("_____________________")

        if vards == d1.nosaukums:
            kal = d1.kaloriju_daudzums
            tauk = d1.tauku_daudzums
            cuk = d1.cukura_daudzums

        elif vards == d2.nosaukums:
            kal = d2.kaloriju_daudzums
            tauk = d2.tauku_daudzums
            cuk = d2.cukura_daudzums

        elif vards == d3.nosaukums:
            kal = d3.kaloriju_daudzums
            tauk = d3.tauku_daudzums
            cuk = d3.cukura_daudzums

        elif vards == d4.nosaukums:
            kal = d4.kaloriju_daudzums
            tauk = d4.tauku_daudzums
            cuk = d4.cukura_daudzums

        elif vards == d5.nosaukums:
            kal = d5.kaloriju_daudzums
            tauk = d5.tauku_daudzums
            cuk = d5.cukura_daudzums

        elif vards == d6.nosaukums:
            kal = d6.kaloriju_daudzums
            tauk = d6.tauku_daudzums
            cuk = d6.cukura_daudzums

        elif vards == d7.nosaukums:
            kal = d7.kaloriju_daudzums
            tauk = d7.tauku_daudzums
            cuk = d7.cukura_daudzums

        elif vards == d8.nosaukums:
            kal = d8.kaloriju_daudzums
            tauk = d8.tauku_daudzums
            cuk = d8.cukura_daudzums

        elif vards == d9.nosaukums:
            kal = d9.kaloriju_daudzums
            tauk = d9.tauku_daudzums
            cuk = d9.cukura_daudzums

        elif vards == d10.nosaukums:
            kal = d10.kaloriju_daudzums
            tauk = d10.tauku_daudzums
            cuk = d10.cukura_daudzums

        elif vards == d11.nosaukums:
            kal = d11.kaloriju_daudzums
            tauk = d11.tauku_daudzums
            cuk = d11.cukura_daudzums

        elif vards == d12.nosaukums:
            kal = d12.kaloriju_daudzums
            tauk = d12.tauku_daudzums
            cuk = d12.cukura_daudzums

        elif vards == d13.nosaukums:
            kal = d13.kaloriju_daudzums
            tauk = d13.tauku_daudzums
            cuk = d13.cukura_daudzums

        elif vards == d14.nosaukums:
            kal = d14.kaloriju_daudzums
            tauk = d14.tauku_daudzums
            cuk = d14.cukura_daudzums

        elif vards == d15.nosaukums:
            kal = d15.kaloriju_daudzums
            tauk = d15.tauku_daudzums
            cuk = d15.cukura_daudzums

        elif vards == d16.nosaukums:
            kal = d16.kaloriju_daudzums
            tauk = d16.tauku_daudzums
            cuk = d16.cukura_daudzums

        elif vards == d17.nosaukums:
            kal = d17.kaloriju_daudzums
            tauk = d17.tauku_daudzums
            cuk = d17.cukura_daudzums

        elif vards == d18.nosaukums:
            kal = d18.kaloriju_daudzums
            tauk = d18.tauku_daudzums
            cuk = d18.cukura_daudzums

        elif vards == d19.nosaukums:
            kal = d19.kaloriju_daudzums
            tauk = d19.tauku_daudzums
            cuk = d19.cukura_daudzums

        elif vards == d21.nosaukums:
            kal = d21.kaloriju_daudzums
            tauk = d21.tauku_daudzums
            cuk = d21.cukura_daudzums

        elif vards == d22.nosaukums:
            kal = d22.kaloriju_daudzums
            tauk = d22.tauku_daudzums
            cuk = d22.cukura_daudzums

        elif vards == d23.nosaukums:
            kal = d23.kaloriju_daudzums
            tauk = d23.tauku_daudzums
            cuk = d23.cukura_daudzums

        elif vards == d24.nosaukums:
            kal = d24.kaloriju_daudzums
            tauk = d24.tauku_daudzums
            cuk = d24.cukura_daudzums

        elif vards == pp1.nosaukums:
            kal = pp1.kaloriju_daudzums
            tauk = pp1.tauku_daudzums
            cuk = pp1.cukura_daudzums

        elif vards == pp2.nosaukums:
            kal = pp2.kaloriju_daudzums
            tauk = pp2.tauku_daudzums
            cuk = pp2.cukura_daudzums

        elif vards == pp3.nosaukums:
            kal = pp3.kaloriju_daudzums
            tauk = pp3.tauku_daudzums
            cuk = pp3.cukura_daudzums

        elif vards == pp4.nosaukums:
            kal = pp4.kaloriju_daudzums
            tauk = pp4.tauku_daudzums
            cuk = pp4.cukura_daudzums

        elif vards == pp5.nosaukums:
            kal = pp5.kaloriju_daudzums
            tauk = pp5.tauku_daudzums
            cuk = pp5.cukura_daudzums

        elif vards == pp6.nosaukums:
            kal = pp6.kaloriju_daudzums
            tauk = pp6.tauku_daudzums
            cuk = pp6.cukura_daudzums

        elif vards == pp7.nosaukums:
            kal = pp7.kaloriju_daudzums
            tauk = pp7.tauku_daudzums
            cuk = pp7.cukura_daudzums

        elif vards == pp8.nosaukums:
            kal = pp8.kaloriju_daudzums
            tauk = pp8.tauku_daudzums
            cuk = pp8.cukura_daudzums

        elif vards == pp9.nosaukums:
            kal = pp9.kaloriju_daudzums
            tauk = pp9.tauku_daudzums
            cuk = pp9.cukura_daudzums

        elif vards == pp10.nosaukums:
            kal = pp10.kaloriju_daudzums
            tauk = pp10.tauku_daudzums
            cuk = pp10.cukura_daudzums

        elif vards == gap1.nosaukums:
            kal = gap1.kaloriju_daudzums
            tauk = gap1.tauku_daudzums
            cuk = gap1.cukura_daudzums

        elif vards == gap2.nosaukums:
            kal = gap2.kaloriju_daudzums
            tauk = gap2.tauku_daudzums
            cuk = gap2.cukura_daudzums

        elif vards == gap3.nosaukums:
            kal = gap3.kaloriju_daudzums
            tauk = gap3.tauku_daudzums
            cuk = gap3.cukura_daudzums

        elif vards == gap4.nosaukums:
            kal = gap4.kaloriju_daudzums
            tauk = gap4.tauku_daudzums
            cuk = gap4.cukura_daudzums

        elif vards == gap5.nosaukums:
            kal = gap5.kaloriju_daudzums
            tauk = gap5.tauku_daudzums
            cuk = gap5.cukura_daudzums

        elif vards == gap6.nosaukums:
            kal = gap6.kaloriju_daudzums
            tauk = gap6.tauku_daudzums
            cuk = gap6.cukura_daudzums

        elif vards == gap7.nosaukums:
            kal = gap7.kaloriju_daudzums
            tauk = gap7.tauku_daudzums
            cuk = gap7.cukura_daudzums

        elif vards == gap8.nosaukums:
            kal = gap8.kaloriju_daudzums
            tauk = gap8.tauku_daudzums
            cuk = gap8.cukura_daudzums

        elif vards == gap9.nosaukums:
            kal = gap9.kaloriju_daudzums
            tauk = gap9.tauku_daudzums
            cuk = gap9.cukura_daudzums

        elif vards == gap10.nosaukums:
            kal = gap10.kaloriju_daudzums
            tauk = gap10.tauku_daudzums
            cuk = gap10.cukura_daudzums

        elif vards == grp1.nosaukums:
            kal = grp1.kaloriju_daudzums
            tauk = grp1.tauku_daudzums
            cuk = grp1.cukura_daudzums

        elif vards == grp2.nosaukums:
            kal = grp2.kaloriju_daudzums
            tauk = grp2.tauku_daudzums
            cuk = grp2.cukura_daudzums

        elif vards == grp3.nosaukums:
            kal = grp3.kaloriju_daudzums
            tauk = grp3.tauku_daudzums
            cuk = grp3.cukura_daudzums

        elif vards == grp4.nosaukums:
            kal = grp4.kaloriju_daudzums
            tauk = grp4.tauku_daudzums
            cuk = grp4.cukura_daudzums

        elif vards == grp5.nosaukums:
            kal = grp5.kaloriju_daudzums
            tauk = grp5.tauku_daudzums
            cuk = grp5.cukura_daudzums

        elif vards == grp6.nosaukums:
            kal = grp6.kaloriju_daudzums
            tauk = grp6.tauku_daudzums
            cuk = grp6.cukura_daudzums

        elif vards == grp7.nosaukums:
            kal = grp7.kaloriju_daudzums
            tauk = grp7.tauku_daudzums
            cuk = grp7.cukura_daudzums

        elif vards == grp8.nosaukums:
            kal = grp8.kaloriju_daudzums
            tauk = grp8.tauku_daudzums
            cuk = grp8.cukura_daudzums

        elif vards == grp9.nosaukums:
            kal = grp9.kaloriju_daudzums
            tauk = grp9.tauku_daudzums
            cuk = grp9.cukura_daudzums

        elif vards == grp10.nosaukums:
            kal = grp10.kaloriju_daudzums
            tauk = grp10.tauku_daudzums
            cuk = grp10.cukura_daudzums

        elif vards == a1.nosaukums:
            kal = a1.kaloriju_daudzums
            tauk = a1.tauku_daudzums
            cuk = a1.cukura_daudzums

        elif vards == a2.nosaukums:
            kal = a2.kaloriju_daudzums
            tauk = a2.tauku_daudzums
            cuk = a2.cukura_daudzums

        elif vards == a3.nosaukums:
            kal = a3.kaloriju_daudzums
            tauk = a3.tauku_daudzums
            cuk = a3.cukura_daudzums

        elif vards == a4.nosaukums:
            kal = a4.kaloriju_daudzums
            tauk = a4.tauku_daudzums
            cuk = a4.cukura_daudzums

        elif vards == a5.nosaukums:
            kal = a5.kaloriju_daudzums
            tauk = a5.tauku_daudzums
            cuk = a5.cukura_daudzums

        elif vards == a6.nosaukums:
            kal = a6.kaloriju_daudzums
            tauk = a6.tauku_daudzums
            cuk = a6.cukura_daudzums

        elif vards == a7.nosaukums:
            kal = a7.kaloriju_daudzums
            tauk = a7.tauku_daudzums
            cuk = a7.cukura_daudzums

        elif vards == a8.nosaukums:
            kal = a8.kaloriju_daudzums
            tauk = a8.tauku_daudzums
            cuk = a8.cukura_daudzums

        elif vards == a9.nosaukums:
            kal = a9.kaloriju_daudzums
            tauk = a9.tauku_daudzums
            cuk = a9.cukura_daudzums

        elif vards == a10.nosaukums:
            kal = a10.kaloriju_daudzums
            tauk = a10.tauku_daudzums
            cuk = a10.cukura_daudzums

        elif vards == a11.nosaukums:
            kal = a11.kaloriju_daudzums
            tauk = a11.tauku_daudzums
            cuk = a11.cukura_daudzums

        elif vards == a12.nosaukums:
            kal = a12.kaloriju_daudzums
            tauk = a12.tauku_daudzums
            cuk = a12.cukura_daudzums

        elif vards == a13.nosaukums:
            kal = a13.kaloriju_daudzums
            tauk = a13.tauku_daudzums
            cuk = a13.cukura_daudzums

        elif vards == a14.nosaukums:
            kal = a14.kaloriju_daudzums
            tauk = a14.tauku_daudzums
            cuk = a14.cukura_daudzums

        elif vards == a15.nosaukums:
            kal = a15.kaloriju_daudzums
            tauk = a15.tauku_daudzums
            cuk = a15.cukura_daudzums

        elif vards == a16.nosaukums:
            kal = a16.kaloriju_daudzums
            tauk = a16.tauku_daudzums
            cuk = a16.cukura_daudzums

        elif vards == a17.nosaukums:
            kal = a17.kaloriju_daudzums
            tauk = a17.tauku_daudzums
            cuk = a17.cukura_daudzums

        elif vards == a18.nosaukums:
            kal = a18.kaloriju_daudzums
            tauk = a18.tauku_daudzums
            cuk = a18.cukura_daudzums

        elif vards == a19.nosaukums:
            kal = a19.kaloriju_daudzums
            tauk = a19.tauku_daudzums
            cuk = a19.cukura_daudzums

        elif vards == a20.nosaukums:
            kal = a20.kaloriju_daudzums
            tauk = a20.tauku_daudzums
            cuk = a20.cukura_daudzums

        elif vards == a21.nosaukums:
            kal = a21.kaloriju_daudzums
            tauk = a21.tauku_daudzums
            cuk = a21.cukura_daudzums

        elif vards == a22.nosaukums:
            kal = a22.kaloriju_daudzums
            tauk = a22.tauku_daudzums
            cuk = a22.cukura_daudzums
        
        elif vards != d1.nosaukums or vards != d2.nosaukums or vards != d3.nosaukums or vards != d4.nosaukums or vards != d5.nosaukums or vards != d6.nosaukums or vards != d7.nosaukums or vards != d8.nosaukums or vards != d9.nosaukums or vards != d10.nosaukums or vards != d11.nosaukums or vards != d12.nosaukums or vards != d13.nosaukums or vards != d14.nosaukums or vards != d15.nosaukums or vards != d16.nosaukums or vards != d17.nosaukums or vards != d18.nosaukums or vards != d19.nosaukums or vards != d21.nosaukums or vards != d22.nosaukums or vards != d23.nosaukums or vards != d24.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()

        elif vards != a1.nosaukums or vards != a2.nosaukums or vards != a3.nosaukums or vards != a4.nosaukums or vards != a5.nosaukums or vards != a6.nosaukums or vards != a7.nosaukums or vards != a8.nosaukums or vards != a9.nosaukums or vards != a10.nosaukums or vards != a11.nosaukums or vards != a12.nosaukums or vards != a13.nosaukums or vards != a14.nosaukums or vards != a15.nosaukums or vards != a16.nosaukums or vards != a17.nosaukums or vards != a18.nosaukums or vards != a19.nosaukums or vards != a20.nosaukums or vards != a21.nosaukums or vards != a22.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()

        elif vards != pp1.nosaukums or vards != pp2.nosaukums or vards != pp3.nosaukums or vards != pp4.nosaukums or vards != pp5.nosaukums or vards != pp6.nosaukums or vards != pp7.nosaukums or vards != pp8.nosaukums or vards != pp9.nosaukums or vards != pp10.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()

        elif vards != gap1.nosaukums or vards != gap2.nosaukums or vards != gap3.nosaukums or vards != gap4.nosaukums or vards != gap5.nosaukums or vards != gap6.nosaukums or vards != gap7.nosaukums or vards != gap8.nosaukums or vards != gap9.nosaukums or vards != gap10.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()
            
        elif vards != grp1.nosaukums or vards != grp2.nosaukums or vards != grp3.nosaukums or vards != grp4.nosaukums or vards != grp5.nosaukums or vards != grp6.nosaukums or vards != grp7.nosaukums or vards != grp8.nosaukums or vards != grp9.nosaukums or vards != grp10.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()

        vards1 = input("Ievadiet produkta nosaukumu: ")
        daudzums1 = int(input("Ievadiet produkta daudzumu gramos: "))
        print("_____________________")

        if vards1 == d1.nosaukums:
            kal1 = d1.kaloriju_daudzums
            tauk1 = d1.tauku_daudzums
            cuk1 = d1.cukura_daudzums

        elif vards1 == d2.nosaukums:
            kal1 = d2.kaloriju_daudzums
            tauk1 = d2.tauku_daudzums
            cuk1 = d2.cukura_daudzums

        elif vards1 == d3.nosaukums:
            kal1 = d3.kaloriju_daudzums
            tauk1 = d3.tauku_daudzums
            cuk1 = d3.cukura_daudzums

        elif vards1 == d4.nosaukums:
            kal1 = d4.kaloriju_daudzums
            tauk1 = d4.tauku_daudzums
            cuk1 = d4.cukura_daudzums

        elif vards1 == d5.nosaukums:
            kal1 = d5.kaloriju_daudzums
            tauk1 = d5.tauku_daudzums
            cuk1 = d5.cukura_daudzums

        elif vards1 == d6.nosaukums:
            kal1 = d6.kaloriju_daudzums
            tauk1 = d6.tauku_daudzums
            cuk1 = d6.cukura_daudzums

        elif vards1 == d7.nosaukums:
            kal1 = d7.kaloriju_daudzums
            tauk1 = d7.tauku_daudzums
            cuk1 = d7.cukura_daudzums

        elif vards1 == d8.nosaukums:
            kal1 = d8.kaloriju_daudzums
            tauk1 = d8.tauku_daudzums
            cuk1 = d8.cukura_daudzums

        elif vards1 == d9.nosaukums:
            kal1 = d9.kaloriju_daudzums
            tauk1 = d9.tauku_daudzums
            cuk1 = d9.cukura_daudzums

        elif vards1 == d10.nosaukums:
            kal1 = d10.kaloriju_daudzums
            tauk1 = d10.tauku_daudzums
            cuk1 = d10.cukura_daudzums

        elif vards1 == d11.nosaukums:
            kal1 = d11.kaloriju_daudzums
            tauk1 = d11.tauku_daudzums
            cuk1 = d11.cukura_daudzums

        elif vards1 == d12.nosaukums:
            kal1 = d12.kaloriju_daudzums
            tauk1 = d12.tauku_daudzums
            cuk1 = d12.cukura_daudzums

        elif vards1 == d13.nosaukums:
            kal1 = d13.kaloriju_daudzums
            tauk1 = d13.tauku_daudzums
            cuk1 = d13.cukura_daudzums

        elif vards1 == d14.nosaukums:
            kal1 = d14.kaloriju_daudzums
            tauk1 = d14.tauku_daudzums
            cuk1 = d14.cukura_daudzums

        elif vards1 == d15.nosaukums:
            kal1 = d15.kaloriju_daudzums
            tauk1 = d15.tauku_daudzums
            cuk1 = d15.cukura_daudzums

        elif vards1 == d16.nosaukums:
            kal1 = d16.kaloriju_daudzums
            tauk1 = d16.tauku_daudzums
            cuk1 = d16.cukura_daudzums

        elif vards1 == d17.nosaukums:
            kal1 = d17.kaloriju_daudzums
            tauk1 = d17.tauku_daudzums
            cuk1 = d17.cukura_daudzums

        elif vards1 == d18.nosaukums:
            kal1 = d18.kaloriju_daudzums
            tauk1 = d18.tauku_daudzums
            cuk1 = d18.cukura_daudzums

        elif vards1 == d19.nosaukums:
            kal1 = d19.kaloriju_daudzums
            tauk1 = d19.tauku_daudzums
            cuk1 = d19.cukura_daudzums

        elif vards1 == d21.nosaukums:
            kal1 = d21.kaloriju_daudzums
            tauk1 = d21.tauku_daudzums
            cuk1 = d21.cukura_daudzums

        elif vards1 == d22.nosaukums:
            kal1 = d22.kaloriju_daudzums
            tauk1 = d22.tauku_daudzums
            cuk1 = d22.cukura_daudzums

        elif vards1 == d23.nosaukums:
            kal1 = d23.kaloriju_daudzums
            tauk1 = d23.tauku_daudzums
            cuk1 = d23.cukura_daudzums

        elif vards1 == d24.nosaukums:
            kal1 = d24.kaloriju_daudzums
            tauk1 = d24.tauku_daudzums
            cuk1 = d24.cukura_daudzums

        elif vards1 == pp1.nosaukums:
            kal1 = pp1.kaloriju_daudzums
            tauk1 = pp1.tauku_daudzums
            cuk1 = pp1.cukura_daudzums

        elif vards1 == pp2.nosaukums:
            kal1 = pp2.kaloriju_daudzums
            tauk1 = pp2.tauku_daudzums
            cuk1 = pp2.cukura_daudzums

        elif vards1 == pp3.nosaukums:
            kal1 = pp3.kaloriju_daudzums
            tauk1 = pp3.tauku_daudzums
            cuk1 = pp3.cukura_daudzums

        elif vards1 == pp4.nosaukums:
            kal1 = pp4.kaloriju_daudzums
            tauk1 = pp4.tauku_daudzums
            cuk1 = pp4.cukura_daudzums

        elif vards1 == pp5.nosaukums:
            kal1 = pp5.kaloriju_daudzums
            tauk1 = pp5.tauku_daudzums
            cuk1 = pp5.cukura_daudzums

        elif vards1 == pp6.nosaukums:
            kal1 = pp6.kaloriju_daudzums
            tauk1 = pp6.tauku_daudzums
            cuk1 = pp6.cukura_daudzums

        elif vards1 == pp7.nosaukums:
            kal1 = pp7.kaloriju_daudzums
            tauk1 = pp7.tauku_daudzums
            cuk1 = pp7.cukura_daudzums

        elif vards1 == pp8.nosaukums:
            kal1 = pp8.kaloriju_daudzums
            tauk1 = pp8.tauku_daudzums
            cuk1 = pp8.cukura_daudzums

        elif vards1 == pp9.nosaukums:
            kal1 = pp9.kaloriju_daudzums
            tauk1 = pp9.tauku_daudzums
            cuk1 = pp9.cukura_daudzums

        elif vards1 == pp10.nosaukums:
            kal1 = pp10.kaloriju_daudzums
            tauk1 = pp10.tauku_daudzums
            cuk1 = pp10.cukura_daudzums

        elif vards1 == gap1.nosaukums:
            kal1 = gap1.kaloriju_daudzums
            tauk1 = gap1.tauku_daudzums
            cuk1 = gap1.cukura_daudzums

        elif vards1 == gap2.nosaukums:
            kal1 = gap2.kaloriju_daudzums
            tauk1 = gap2.tauku_daudzums
            cuk1 = gap2.cukura_daudzums

        elif vards1 == gap3.nosaukums:
            kal1 = gap3.kaloriju_daudzums
            tauk1 = gap3.tauku_daudzums
            cuk1 = gap3.cukura_daudzums

        elif vards1 == gap4.nosaukums:
            kal1 = gap4.kaloriju_daudzums
            tauk1 = gap4.tauku_daudzums
            cuk1 = gap4.cukura_daudzums

        elif vards1 == gap5.nosaukums:
            kal1 = gap5.kaloriju_daudzums
            tauk1 = gap5.tauku_daudzums
            cuk1 = gap5.cukura_daudzums

        elif vards1 == gap6.nosaukums:
            kal1 = gap6.kaloriju_daudzums
            tauk1 = gap6.tauku_daudzums
            cuk1 = gap6.cukura_daudzums

        elif vards1 == gap7.nosaukums:
            kal1 = gap7.kaloriju_daudzums
            tauk1 = gap7.tauku_daudzums
            cuk1 = gap7.cukura_daudzums

        elif vards1 == gap8.nosaukums:
            kal1 = gap8.kaloriju_daudzums
            tauk1 = gap8.tauku_daudzums
            cuk1 = gap8.cukura_daudzums

        elif vards1 == gap9.nosaukums:
            kal1 = gap9.kaloriju_daudzums
            tauk1 = gap9.tauku_daudzums
            cuk1 = gap9.cukura_daudzums

        elif vards1 == gap10.nosaukums:
            kal1 = gap10.kaloriju_daudzums
            tauk1 = gap10.tauku_daudzums
            cuk1 = gap10.cukura_daudzums

        elif vards1 == grp1.nosaukums:
            kal1 = grp1.kaloriju_daudzums
            tauk1 = grp1.tauku_daudzums
            cuk1 = grp1.cukura_daudzums

        elif vards1 == grp2.nosaukums:
            kal1 = grp2.kaloriju_daudzums
            tauk1 = grp2.tauku_daudzums
            cuk1 = grp2.cukura_daudzums

        elif vards1 == grp3.nosaukums:
            kal1 = grp3.kaloriju_daudzums
            tauk1 = grp3.tauku_daudzums
            cuk1 = grp3.cukura_daudzums

        elif vards1 == grp4.nosaukums:
            kal1 = grp4.kaloriju_daudzums
            tauk1 = grp4.tauku_daudzums
            cuk1 = grp4.cukura_daudzums

        elif vards1 == grp5.nosaukums:
            kal1 = grp5.kaloriju_daudzums
            tauk1 = grp5.tauku_daudzums
            cuk1 = grp5.cukura_daudzums

        elif vards1 == grp6.nosaukums:
            kal1 = grp6.kaloriju_daudzums
            tauk1 = grp6.tauku_daudzums
            cuk1 = grp6.cukura_daudzums

        elif vards1 == grp7.nosaukums:
            kal1 = grp7.kaloriju_daudzums
            tauk1 = grp7.tauku_daudzums
            cuk1 = grp7.cukura_daudzums

        elif vards1 == grp8.nosaukums:
            kal1 = grp8.kaloriju_daudzums
            tauk1 = grp8.tauku_daudzums
            cuk1 = grp8.cukura_daudzums

        elif vards1 == grp9.nosaukums:
            kal1 = grp9.kaloriju_daudzums
            tauk1 = grp9.tauku_daudzums
            cuk1 = grp9.cukura_daudzums

        elif vards1 == grp10.nosaukums:
            kal1 = grp10.kaloriju_daudzums
            tauk1 = grp10.tauku_daudzums
            cuk1 = grp10.cukura_daudzums

        elif vards1 == a1.nosaukums:
            kal1 = a1.kaloriju_daudzums
            tauk1 = a1.tauku_daudzums
            cuk1 = a1.cukura_daudzums

        elif vards1 == a2.nosaukums:
            kal1 = a2.kaloriju_daudzums
            tauk1 = a2.tauku_daudzums
            cuk1 = a2.cukura_daudzums

        elif vards1 == a3.nosaukums:
            kal1 = a3.kaloriju_daudzums
            tauk1 = a3.tauku_daudzums
            cuk1 = a3.cukura_daudzums

        elif vards1 == a4.nosaukums:
            kal1 = a4.kaloriju_daudzums
            tauk1 = a4.tauku_daudzums
            cuk1 = a4.cukura_daudzums

        elif vards1 == a5.nosaukums:
            kal1 = a5.kaloriju_daudzums
            tauk1 = a5.tauku_daudzums
            cuk1 = a5.cukura_daudzums

        elif vards1 == a6.nosaukums:
            kal1 = a6.kaloriju_daudzums
            tauk1 = a6.tauku_daudzums
            cuk1 = a6.cukura_daudzums

        elif vards1 == a7.nosaukums:
            kal1 = a7.kaloriju_daudzums
            tauk1 = a7.tauku_daudzums
            cuk1 = a7.cukura_daudzums

        elif vards1 == a8.nosaukums:
            kal1 = a8.kaloriju_daudzums
            tauk1 = a8.tauku_daudzums
            cuk1 = a8.cukura_daudzums

        elif vards1 == a9.nosaukums:
            kal1 = a9.kaloriju_daudzums
            tauk1 = a9.tauku_daudzums
            cuk1 = a9.cukura_daudzums

        elif vards1 == a10.nosaukums:
            kal1 = a10.kaloriju_daudzums
            tauk1 = a10.tauku_daudzums
            cuk1 = a10.cukura_daudzums

        elif vards1 == a11.nosaukums:
            kal1 = a11.kaloriju_daudzums
            tauk1 = a11.tauku_daudzums
            cuk1 = a11.cukura_daudzums

        elif vards1 == a12.nosaukums:
            kal1 = a12.kaloriju_daudzums
            tauk1 = a12.tauku_daudzums
            cuk1 = a12.cukura_daudzums

        elif vards1 == a13.nosaukums:
            kal1 = a13.kaloriju_daudzums
            tauk1 = a13.tauku_daudzums
            cuk1 = a13.cukura_daudzums

        elif vards1 == a14.nosaukums:
            kal1 = a14.kaloriju_daudzums
            tauk1 = a14.tauku_daudzums
            cuk1 = a14.cukura_daudzums

        elif vards1 == a15.nosaukums:
            kal1 = a15.kaloriju_daudzums
            tauk1 = a15.tauku_daudzums
            cuk1 = a15.cukura_daudzums

        elif vards1 == a16.nosaukums:
            kal1 = a16.kaloriju_daudzums
            tauk1 = a16.tauku_daudzums
            cuk1 = a16.cukura_daudzums

        elif vards1 == a17.nosaukums:
            kal1 = a17.kaloriju_daudzums
            tauk1 = a17.tauku_daudzums
            cuk1 = a17.cukura_daudzums

        elif vards1 == a18.nosaukums:
            kal1 = a18.kaloriju_daudzums
            tauk1 = a18.tauku_daudzums
            cuk1 = a18.cukura_daudzums

        elif vards1 == a19.nosaukums:
            kal1 = a19.kaloriju_daudzums
            tauk1 = a19.tauku_daudzums
            cuk1 = a19.cukura_daudzums

        elif vards1 == a20.nosaukums:
            kal1 = a20.kaloriju_daudzums
            tauk1 = a20.tauku_daudzums
            cuk1 = a20.cukura_daudzums

        elif vards1 == a21.nosaukums:
            kal1 = a21.kaloriju_daudzums
            tauk1 = a21.tauku_daudzums
            cuk1 = a21.cukura_daudzums

        elif vards1 == a22.nosaukums:
            kal1 = a22.kaloriju_daudzums
            tauk1 = a22.tauku_daudzums
            cuk1 = a22.cukura_daudzums
        
        elif vards1 != d1.nosaukums or vards1 != d2.nosaukums or vards1 != d3.nosaukums or vards1 != d4.nosaukums or vards1 != d5.nosaukums or vards1 != d6.nosaukums or vards1 != d7.nosaukums or vards1 != d8.nosaukums or vards1 != d9.nosaukums or vards1 != d10.nosaukums or vards1 != d11.nosaukums or vards1 != d12.nosaukums or vards1 != d13.nosaukums or vards1 != d14.nosaukums or vards1 != d15.nosaukums or vards1 != d16.nosaukums or vards1 != d17.nosaukums or vards1 != d18.nosaukums or vards1 != d19.nosaukums or vards1 != d21.nosaukums or vards1 != d22.nosaukums or vards1 != d23.nosaukums or vards1 != d24.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()

        elif vards1 != a1.nosaukums or vards1 != a2.nosaukums or vards1 != a3.nosaukums or vards1 != a4.nosaukums or vards1 != a5.nosaukums or vards1 != a6.nosaukums or vards1 != a7.nosaukums or vards1 != a8.nosaukums or vards1 != a9.nosaukums or vards1 != a10.nosaukums or vards1 != a11.nosaukums or vards1 != a12.nosaukums or vards1 != a13.nosaukums or vards1 != a14.nosaukums or vards1 != a15.nosaukums or vards1 != a16.nosaukums or vards1 != a17.nosaukums or vards1 != a18.nosaukums or vards1 != a19.nosaukums or vards1 != a20.nosaukums or vards1 != a21.nosaukums or vards1 != a22.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()

        elif vards1 != pp1.nosaukums or vards1 != pp2.nosaukums or vards1 != pp3.nosaukums or vards1 != pp4.nosaukums or vards1 != pp5.nosaukums or vards1 != pp6.nosaukums or vards1 != pp7.nosaukums or vards1 != pp8.nosaukums or vards1 != pp9.nosaukums or vards1 != pp10.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()

        elif vards1 != gap1.nosaukums or vards1 != gap2.nosaukums or vards1 != gap3.nosaukums or vards1 != gap4.nosaukums or vards1 != gap5.nosaukums or vards1 != gap6.nosaukums or vards1 != gap7.nosaukums or vards1 != gap8.nosaukums or vards1 != gap9.nosaukums or vards1 != gap10.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()

        elif vards1 != grp1.nosaukums or vards1 != grp2.nosaukums or vards1 != grp3.nosaukums or vards1 != grp4.nosaukums or vards1 != grp5.nosaukums or vards1 != grp6.nosaukums or vards1 != grp7.nosaukums or vards1 != grp8.nosaukums or vards1 != grp9.nosaukums or vards1 != grp10.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()

        vards2 = input("Ievadiet produkta nosaukumu: ")
        daudzums2 = int(input("Ievadiet produkta daudzumu gramos: "))
        print("_____________________")
        if vards2 == d1.nosaukums:
            kal2 = d1.kaloriju_daudzums
            tauk2 = d1.tauku_daudzums
            cuk2 = d1.cukura_daudzums

        elif vards2 == d2.nosaukums:
            kal2 = d2.kaloriju_daudzums
            tauk2 = d2.tauku_daudzums
            cuk2 = d2.cukura_daudzums

        elif vards2 == d3.nosaukums:
            kal2 = d3.kaloriju_daudzums
            tauk2 = d3.tauku_daudzums
            cuk2 = d3.cukura_daudzums

        elif vards2 == d3.nosaukums:
            kal2 = d3.kaloriju_daudzums
            tauk2 = d3.tauku_daudzums
            cuk2 = d3.cukura_daudzums

        elif vards2 == d4.nosaukums:
            kal2 = d4.kaloriju_daudzums
            tauk2 = d4.tauku_daudzums
            cuk2 = d4.cukura_daudzums

        elif vards2 == d5.nosaukums:
            kal2 = d5.kaloriju_daudzums
            tauk2 = d5.tauku_daudzums
            cuk2 = d5.cukura_daudzums

        elif vards2 == d6.nosaukums:
            kal2 = d6.kaloriju_daudzums
            tauk2 = d6.tauku_daudzums
            cuk2 = d6.cukura_daudzums

        elif vards2 == d7.nosaukums:
            kal2 = d7.kaloriju_daudzums
            tauk2 = d7.tauku_daudzums
            cuk2 = d7.cukura_daudzums

        elif vards2 == d8.nosaukums:
            kal2 = d8.kaloriju_daudzums
            tauk2 = d8.tauku_daudzums
            cuk2 = d8.cukura_daudzums

        elif vards2 == d9.nosaukums:
            kal2 = d9.kaloriju_daudzums
            tauk2 = d9.tauku_daudzums
            cuk2 = d9.cukura_daudzums

        elif vards2 == d10.nosaukums:
            kal2 = d10.kaloriju_daudzums
            tauk2 = d10.tauku_daudzums
            cuk2 = d10.cukura_daudzums

        elif vards2 == d11.nosaukums:
            kal2 = d11.kaloriju_daudzums
            tauk2 = d11.tauku_daudzums
            cuk2 = d11.cukura_daudzums

        elif vards2 == d12.nosaukums:
            kal2 = d12.kaloriju_daudzums
            tauk2 = d12.tauku_daudzums
            cuk2 = d12.cukura_daudzums

        elif vards2 == d13.nosaukums:
            kal2 = d13.kaloriju_daudzums
            tauk2 = d13.tauku_daudzums
            cuk2 = d13.cukura_daudzums

        elif vards2 == d14.nosaukums:
            kal2 = d14.kaloriju_daudzums
            tauk2 = d14.tauku_daudzums
            cuk2 = d14.cukura_daudzums

        elif vards2 == d15.nosaukums:
            kal2 = d15.kaloriju_daudzums
            tauk2 = d15.tauku_daudzums
            cuk2 = d15.cukura_daudzums

        elif vards2 == d16.nosaukums:
            kal2 = d16.kaloriju_daudzums
            tauk2 = d16.tauku_daudzums
            cuk2 = d16.cukura_daudzums

        elif vards2 == d17.nosaukums:
            kal2 = d17.kaloriju_daudzums
            tauk2 = d17.tauku_daudzums
            cuk2 = d17.cukura_daudzums

        elif vards2 == d18.nosaukums:
            kal2 = d18.kaloriju_daudzums
            tauk2 = d18.tauku_daudzums
            cuk2 = d18.cukura_daudzums

        elif vards2 == d19.nosaukums:
            kal2 = d19.kaloriju_daudzums
            tauk2 = d19.tauku_daudzums
            cuk2 = d19.cukura_daudzums

        elif vards2 == d21.nosaukums:
            kal2 = d21.kaloriju_daudzums
            tauk2 = d21.tauku_daudzums
            cuk2 = d21.cukura_daudzums

        elif vards2 == d22.nosaukums:
            kal2 = d22.kaloriju_daudzums
            tauk2 = d22.tauku_daudzums
            cuk2 = d22.cukura_daudzums

        elif vards2 == d23.nosaukums:
            kal2 = d23.kaloriju_daudzums
            tauk2 = d23.tauku_daudzums
            cuk2 = d23.cukura_daudzums

        elif vards2 == d24.nosaukums:
            kal2 = d24.kaloriju_daudzums
            tauk2 = d24.tauku_daudzums
            cuk2 = d24.cukura_daudzums

        elif vards2 == pp1.nosaukums:
            kal2 = pp1.kaloriju_daudzums
            tauk2 = pp1.tauku_daudzums
            cuk2 = pp1.cukura_daudzums

        elif vards2 == pp2.nosaukums:
            kal2 = pp2.kaloriju_daudzums
            tauk2 = pp2.tauku_daudzums
            cuk2 = pp2.cukura_daudzums

        elif vards2 == pp3.nosaukums:
            kal2 = pp3.kaloriju_daudzums
            tauk2 = pp3.tauku_daudzums
            cuk2 = pp3.cukura_daudzums

        elif vards2 == pp4.nosaukums:
            kal2 = pp4.kaloriju_daudzums
            tauk2 = pp4.tauku_daudzums
            cuk2 = pp4.cukura_daudzums

        elif vards2 == pp5.nosaukums:
            kal2 = pp5.kaloriju_daudzums
            tauk2 = pp5.tauku_daudzums
            cuk2 = pp5.cukura_daudzums

        elif vards2 == pp6.nosaukums:
            kal2 = pp6.kaloriju_daudzums
            tauk2 = pp6.tauku_daudzums
            cuk2 = pp6.cukura_daudzums

        elif vards2 == pp7.nosaukums:
            kal2 = pp7.kaloriju_daudzums
            tauk2 = pp7.tauku_daudzums
            cuk2 = pp7.cukura_daudzums

        elif vards2 == pp8.nosaukums:
            kal2 = pp8.kaloriju_daudzums
            tauk2 = pp8.tauku_daudzums
            cuk2 = pp8.cukura_daudzums

        elif vards2 == pp9.nosaukums:
            kal2 = pp9.kaloriju_daudzums
            tauk2 = pp9.tauku_daudzums
            cuk2 = pp9.cukura_daudzums

        elif vards2 == pp10.nosaukums:
            kal2 = pp10.kaloriju_daudzums
            tauk2 = pp10.tauku_daudzums
            cuk2 = pp10.cukura_daudzums

        elif vards2 == gap1.nosaukums:
            kal2 = gap1.kaloriju_daudzums
            tauk2 = gap1.tauku_daudzums
            cuk2 = gap1.cukura_daudzums

        elif vards2 == gap2.nosaukums:
            kal2 = gap2.kaloriju_daudzums
            tauk2 = gap2.tauku_daudzums
            cuk2 = gap2.cukura_daudzums

        elif vards2 == gap3.nosaukums:
            kal2 = gap3.kaloriju_daudzums
            tauk2 = gap3.tauku_daudzums
            cuk2 = gap3.cukura_daudzums

        elif vards2 == gap4.nosaukums:
            kal2 = gap4.kaloriju_daudzums
            tauk2 = gap4.tauku_daudzums
            cuk2 = gap4.cukura_daudzums

        elif vards2 == gap5.nosaukums:
            kal2 = gap5.kaloriju_daudzums
            tauk2 = gap5.tauku_daudzums
            cuk2 = gap5.cukura_daudzums

        elif vards2 == gap6.nosaukums:
            kal2 = gap6.kaloriju_daudzums
            tauk2 = gap6.tauku_daudzums
            cuk2 = gap6.cukura_daudzums

        elif vards2 == gap7.nosaukums:
            kal2 = gap7.kaloriju_daudzums
            tauk2 = gap7.tauku_daudzums
            cuk2 = gap7.cukura_daudzums

        elif vards2 == gap8.nosaukums:
            kal2 = gap8.kaloriju_daudzums
            tauk2 = gap8.tauku_daudzums
            cuk2 = gap8.cukura_daudzums

        elif vards2 == gap9.nosaukums:
            kal2 = gap9.kaloriju_daudzums
            tauk2 = gap9.tauku_daudzums
            cuk2 = gap9.cukura_daudzums

        elif vards2 == gap10.nosaukums:
            kal2 = gap10.kaloriju_daudzums
            tauk2 = gap10.tauku_daudzums
            cuk2 = gap10.cukura_daudzums

        elif vards2 == grp1.nosaukums:
            kal2 = grp1.kaloriju_daudzums
            tauk2 = grp1.tauku_daudzums
            cuk2 = grp1.cukura_daudzums

        elif vards2 == grp2.nosaukums:
            kal2 = grp2.kaloriju_daudzums
            tauk2 = grp2.tauku_daudzums
            cuk2 = grp2.cukura_daudzums

        elif vards2 == grp3.nosaukums:
            kal2 = grp3.kaloriju_daudzums
            tauk2 = grp3.tauku_daudzums
            cuk2 = grp3.cukura_daudzums

        elif vards2 == grp4.nosaukums:
            kal2 = grp4.kaloriju_daudzums
            tauk2 = grp4.tauku_daudzums
            cuk2 = grp4.cukura_daudzums

        elif vards2 == grp5.nosaukums:
            kal2 = grp5.kaloriju_daudzums
            tauk2 = grp5.tauku_daudzums
            cuk2 = grp5.cukura_daudzums

        elif vards2 == grp6.nosaukums:
            kal2 = grp6.kaloriju_daudzums
            tauk2 = grp6.tauku_daudzums
            cuk2 = grp6.cukura_daudzums

        elif vards2 == grp7.nosaukums:
            kal2 = grp7.kaloriju_daudzums
            tauk2 = grp7.tauku_daudzums
            cuk2 = grp7.cukura_daudzums

        elif vards2 == grp8.nosaukums:
            kal2 = grp8.kaloriju_daudzums
            tauk2 = grp8.tauku_daudzums
            cuk2 = grp8.cukura_daudzums

        elif vards2 == grp9.nosaukums:
            kal2 = grp9.kaloriju_daudzums
            tauk2 = grp9.tauku_daudzums
            cuk2 = grp9.cukura_daudzums

        elif vards2 == grp10.nosaukums:
            kal2 = grp10.kaloriju_daudzums
            tauk2 = grp10.tauku_daudzums
            cuk2 = grp10.cukura_daudzums

        elif vards2 == a1.nosaukums:
            kal2 = a1.kaloriju_daudzums
            tauk2 = a1.tauku_daudzums
            cuk2 = a1.cukura_daudzums

        elif vards2 == a2.nosaukums:
            kal2 = a2.kaloriju_daudzums
            tauk2 = a2.tauku_daudzums
            cuk2 = a2.cukura_daudzums

        elif vards2 == a3.nosaukums:
            kal2 = a3.kaloriju_daudzums
            tauk2 = a3.tauku_daudzums
            cuk2 = a3.cukura_daudzums

        elif vards2 == a4.nosaukums:
            kal2 = a4.kaloriju_daudzums
            tauk2 = a4.tauku_daudzums
            cuk2 = a4.cukura_daudzums

        elif vards2 == a5.nosaukums:
            kal2 = a5.kaloriju_daudzums
            tauk2 = a5.tauku_daudzums
            cuk2 = a5.cukura_daudzums

        elif vards2 == a6.nosaukums:
            kal2 = a6.kaloriju_daudzums
            tauk2 = a6.tauku_daudzums
            cuk2 = a6.cukura_daudzums

        elif vards2 == a7.nosaukums:
            kal2 = a7.kaloriju_daudzums
            tauk2 = a7.tauku_daudzums
            cuk2 = a7.cukura_daudzums

        elif vards2 == a8.nosaukums:
            kal2 = a8.kaloriju_daudzums
            tauk2 = a8.tauku_daudzums
            cuk2 = a8.cukura_daudzums

        elif vards2 == a9.nosaukums:
            kal2 = a9.kaloriju_daudzums
            tauk2 = a9.tauku_daudzums
            cuk2 = a9.cukura_daudzums

        elif vards2 == a10.nosaukums:
            kal2 = a10.kaloriju_daudzums
            tauk2 = a10.tauku_daudzums
            cuk2 = a10.cukura_daudzums

        elif vards2 == a11.nosaukums:
            kal2 = a11.kaloriju_daudzums
            tauk2 = a11.tauku_daudzums
            cuk2 = a11.cukura_daudzums

        elif vards2 == a12.nosaukums:
            kal2 = a12.kaloriju_daudzums
            tauk2 = a12.tauku_daudzums
            cuk2 = a12.cukura_daudzums

        elif vards2 == a13.nosaukums:
            kal2 = a13.kaloriju_daudzums
            tauk2 = a13.tauku_daudzums
            cuk2 = a13.cukura_daudzums

        elif vards2 == a14.nosaukums:
            kal2 = a14.kaloriju_daudzums
            tauk2 = a14.tauku_daudzums
            cuk2 = a14.cukura_daudzums

        elif vards2 == a15.nosaukums:
            kal2 = a15.kaloriju_daudzums
            tauk2 = a15.tauku_daudzums
            cuk2 = a15.cukura_daudzums

        elif vards2 == a16.nosaukums:
            kal2 = a16.kaloriju_daudzums
            tauk2 = a16.tauku_daudzums
            cuk2 = a16.cukura_daudzums

        elif vards2 == a17.nosaukums:
            kal2 = a17.kaloriju_daudzums
            tauk2 = a17.tauku_daudzums
            cuk2 = a17.cukura_daudzums

        elif vards2 == a18.nosaukums:
            kal2 = a18.kaloriju_daudzums
            tauk2 = a18.tauku_daudzums
            cuk2 = a18.cukura_daudzums

        elif vards2 == a19.nosaukums:
            kal2 = a19.kaloriju_daudzums
            tauk2 = a19.tauku_daudzums
            cuk2 = a19.cukura_daudzums

        elif vards2 == a20.nosaukums:
            kal2 = a20.kaloriju_daudzums
            tauk2 = a20.tauku_daudzums
            cuk2 = a20.cukura_daudzums

        elif vards2 == a21.nosaukums:
            kal2 = a21.kaloriju_daudzums
            tauk2 = a21.tauku_daudzums
            cuk2 = a21.cukura_daudzums

        elif vards2 == a22.nosaukums:
            kal2 = a22.kaloriju_daudzums
            tauk2 = a22.tauku_daudzums
            cuk2 = a22.cukura_daudzums

        elif vards2 != d1.nosaukums or vards2 != d2.nosaukums or vards2 != d3.nosaukums or vards2 != d4.nosaukums or vards2 != d5.nosaukums or vards2 != d6.nosaukums or vards2 != d7.nosaukums or vards2 != d8.nosaukums or vards2 != d9.nosaukums or vards2 != d10.nosaukums or vards2 != d11.nosaukums or vards2 != d12.nosaukums or vards2 != d13.nosaukums or vards2 != d14.nosaukums or vards2 != d15.nosaukums or vards2 != d16.nosaukums or vards2 != d17.nosaukums or vards2 != d18.nosaukums or vards2 != d19.nosaukums or vards2 != d21.nosaukums or vards2 != d22.nosaukums or vards2 != d23.nosaukums or vards2 != d24.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()

        elif vards2 != a1.nosaukums or vards2 != a2.nosaukums or vards2 != a3.nosaukums or vards2 != a4.nosaukums or vards2 != a5.nosaukums or vards2 != a6.nosaukums or vards2 != a7.nosaukums or vards2 != a8.nosaukums or vards2 != a9.nosaukums or vards2 != a10.nosaukums or vards2 != a11.nosaukums or vards2 != a12.nosaukums or vards2 != a13.nosaukums or vards2 != a14.nosaukums or vards2 != a15.nosaukums or vards2 != a16.nosaukums or vards2 != a17.nosaukums or vards2 != a18.nosaukums or vards2 != a19.nosaukums or vards2 != a20.nosaukums or vards2 != a21.nosaukums or vards2 != a22.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()

        elif vards2 != pp1.nosaukums or vards2 != pp2.nosaukums or vards2 != pp3.nosaukums or vards2 != pp4.nosaukums or vards2 != pp5.nosaukums or vards2 != pp6.nosaukums or vards2 != pp7.nosaukums or vards2 != pp8.nosaukums or vards2 != pp9.nosaukums or vards2 != pp10.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()

        elif vards2 != gap1.nosaukums or vards2 != gap2.nosaukums or vards2 != gap3.nosaukums or vards2 != gap4.nosaukums or vards2 != gap5.nosaukums or vards2 != gap6.nosaukums or vards2 != gap7.nosaukums or vards2 != gap8.nosaukums or vards2 != gap9.nosaukums or vards2 != gap10.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()

        elif vards2 != grp1.nosaukums or vards2 != grp2.nosaukums or vards2 != grp3.nosaukums or vards2 != grp4.nosaukums or vards2 != grp5.nosaukums or vards2 != grp6.nosaukums or vards2 != grp7.nosaukums or vards2 != grp8.nosaukums or vards2 != grp9.nosaukums or vards2 != grp10.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()

        vards3 = input("Ievadiet produkta nosaukumu: ")
        daudzums3 = int(input("Ievadiet produkta daudzumu gramos: "))
        print("_____________________")
        if vards3 == d1.nosaukums:
            kal3 = d1.kaloriju_daudzums
            tauk3 = d1.tauku_daudzums
            cuk3 = d1.cukura_daudzums

        elif vards3 == d2.nosaukums:
            kal3 = d2.kaloriju_daudzums
            tauk3 = d2.tauku_daudzums
            cuk3 = d2.cukura_daudzums

        elif vards3 == d3.nosaukums:
            kal3 = d3.kaloriju_daudzums
            tauk3 = d3.tauku_daudzums
            cuk3 = d3.cukura_daudzums

        elif vards3 == d3.nosaukums:
            kal3 = d3.kaloriju_daudzums
            tauk3 = d3.tauku_daudzums
            cuk3 = d3.cukura_daudzums

        elif vards3 == d4.nosaukums:
            kal3 = d4.kaloriju_daudzums
            tauk3 = d4.tauku_daudzums
            cuk3 = d4.cukura_daudzums

        elif vards3 == d5.nosaukums:
            kal3 = d5.kaloriju_daudzums
            tauk3 = d5.tauku_daudzums
            cuk3 = d5.cukura_daudzums

        elif vards3 == d6.nosaukums:
            kal3 = d6.kaloriju_daudzums
            tauk3 = d6.tauku_daudzums
            cuk3 = d6.cukura_daudzums

        elif vards3 == d7.nosaukums:
            kal3 = d7.kaloriju_daudzums
            tauk3 = d7.tauku_daudzums
            cuk3 = d7.cukura_daudzums

        elif vards3 == d8.nosaukums:
            kal3 = d8.kaloriju_daudzums
            tauk3 = d8.tauku_daudzums
            cuk3 = d8.cukura_daudzums

        elif vards3 == d9.nosaukums:
            kal3 = d9.kaloriju_daudzums
            tauk3 = d9.tauku_daudzums
            cuk3 = d9.cukura_daudzums

        elif vards3 == d10.nosaukums:
            kal3 = d10.kaloriju_daudzums
            tauk3 = d10.tauku_daudzums
            cuk3 = d10.cukura_daudzums

        elif vards3 == d11.nosaukums:
            kal3 = d11.kaloriju_daudzums
            tauk3 = d11.tauku_daudzums
            cuk3 = d11.cukura_daudzums

        elif vards3 == d12.nosaukums:
            kal3 = d12.kaloriju_daudzums
            tauk3 = d12.tauku_daudzums
            cuk3 = d12.cukura_daudzums

        elif vards3 == d13.nosaukums:
            kal3 = d13.kaloriju_daudzums
            tauk3 = d13.tauku_daudzums
            cuk3 = d13.cukura_daudzums

        elif vards3 == d14.nosaukums:
            kal3 = d14.kaloriju_daudzums
            tauk3 = d14.tauku_daudzums
            cuk3 = d14.cukura_daudzums

        elif vards3 == d15.nosaukums:
            kal3 = d15.kaloriju_daudzums
            tauk3 = d15.tauku_daudzums
            cuk3 = d15.cukura_daudzums

        elif vards3 == d16.nosaukums:
            kal3 = d16.kaloriju_daudzums
            tauk3 = d16.tauku_daudzums
            cuk3 = d16.cukura_daudzums

        elif vards3 == d17.nosaukums:
            kal3 = d17.kaloriju_daudzums
            tauk3 = d17.tauku_daudzums
            cuk3 = d17.cukura_daudzums

        elif vards3 == d18.nosaukums:
            kal3 = d18.kaloriju_daudzums
            tauk3 = d18.tauku_daudzums
            cuk3 = d18.cukura_daudzums

        elif vards3 == d19.nosaukums:
            kal3 = d19.kaloriju_daudzums
            tauk3 = d19.tauku_daudzums
            cuk3 = d19.cukura_daudzums

        elif vards3 == d21.nosaukums:
            kal3 = d21.kaloriju_daudzums
            tauk3 = d21.tauku_daudzums
            cuk3 = d21.cukura_daudzums

        elif vards3 == d22.nosaukums:
            kal3 = d22.kaloriju_daudzums
            tauk3 = d22.tauku_daudzums
            cuk3 = d22.cukura_daudzums

        elif vards3 == d23.nosaukums:
            kal3 = d23.kaloriju_daudzums
            tauk3 = d23.tauku_daudzums
            cuk3 = d23.cukura_daudzums

        elif vards3 == d24.nosaukums:
            kal3 = d24.kaloriju_daudzums
            tauk3 = d24.tauku_daudzums
            cuk3 = d24.cukura_daudzums

        elif vards3 == pp1.nosaukums:
            kal3 = pp1.kaloriju_daudzums
            tauk3 = pp1.tauku_daudzums
            cuk3 = pp1.cukura_daudzums

        elif vards3 == pp2.nosaukums:
            kal3 = pp2.kaloriju_daudzums
            tauk3 = pp2.tauku_daudzums
            cuk3 = pp2.cukura_daudzums

        elif vards3 == pp3.nosaukums:
            kal3 = pp3.kaloriju_daudzums
            tauk3 = pp3.tauku_daudzums
            cuk3 = pp3.cukura_daudzums

        elif vards3 == pp4.nosaukums:
            kal3 = pp4.kaloriju_daudzums
            tauk3 = pp4.tauku_daudzums
            cuk3 = pp4.cukura_daudzums

        elif vards3 == pp5.nosaukums:
            kal3 = pp5.kaloriju_daudzums
            tauk3 = pp5.tauku_daudzums
            cuk3 = pp5.cukura_daudzums

        elif vards3 == pp6.nosaukums:
            kal3 = pp6.kaloriju_daudzums
            tauk3 = pp6.tauku_daudzums
            cuk3 = pp6.cukura_daudzums

        elif vards3 == pp7.nosaukums:
            kal3 = pp7.kaloriju_daudzums
            tauk3 = pp7.tauku_daudzums
            cuk3 = pp7.cukura_daudzums

        elif vards3 == pp8.nosaukums:
            kal3 = pp8.kaloriju_daudzums
            tauk3 = pp8.tauku_daudzums
            cuk3 = pp8.cukura_daudzums

        elif vards3 == pp9.nosaukums:
            kal3 = pp9.kaloriju_daudzums
            tauk3 = pp9.tauku_daudzums
            cuk3 = pp9.cukura_daudzums

        elif vards3 == pp10.nosaukums:
            kal3 = pp10.kaloriju_daudzums
            tauk3 = pp10.tauku_daudzums
            cuk3 = pp10.cukura_daudzums

        elif vards3 == gap1.nosaukums:
            kal3 = gap1.kaloriju_daudzums
            tauk3 = gap1.tauku_daudzums
            cuk3 = gap1.cukura_daudzums

        elif vards3 == gap2.nosaukums:
            kal3 = gap2.kaloriju_daudzums
            tauk3 = gap2.tauku_daudzums
            cuk3 = gap2.cukura_daudzums

        elif vards3 == gap3.nosaukums:
            kal3 = gap3.kaloriju_daudzums
            tauk3 = gap3.tauku_daudzums
            cuk3 = gap3.cukura_daudzums

        elif vards3 == gap4.nosaukums:
            kal3 = gap4.kaloriju_daudzums
            tauk3 = gap4.tauku_daudzums
            cuk3 = gap4.cukura_daudzums

        elif vards3 == gap5.nosaukums:
            kal3 = gap5.kaloriju_daudzums
            tauk3 = gap5.tauku_daudzums
            cuk3 = gap5.cukura_daudzums

        elif vards3 == gap6.nosaukums:
            kal3 = gap6.kaloriju_daudzums
            tauk3 = gap6.tauku_daudzums
            cuk3 = gap6.cukura_daudzums

        elif vards3 == gap7.nosaukums:
            kal3 = gap7.kaloriju_daudzums
            tauk3 = gap7.tauku_daudzums
            cuk3 = gap7.cukura_daudzums

        elif vards3 == gap8.nosaukums:
            kal3 = gap8.kaloriju_daudzums
            tauk3 = gap8.tauku_daudzums
            cuk3 = gap8.cukura_daudzums

        elif vards3 == gap9.nosaukums:
            kal3 = gap9.kaloriju_daudzums
            tauk3 = gap9.tauku_daudzums
            cuk3 = gap9.cukura_daudzums

        elif vards3 == gap10.nosaukums:
            kal3 = gap10.kaloriju_daudzums
            tauk3 = gap10.tauku_daudzums
            cuk3 = gap10.cukura_daudzums

        elif vards3 == grp1.nosaukums:
            kal3 = grp1.kaloriju_daudzums
            tauk3 = grp1.tauku_daudzums
            cuk3 = grp1.cukura_daudzums

        elif vards3 == grp2.nosaukums:
            kal3 = grp2.kaloriju_daudzums
            tauk3 = grp2.tauku_daudzums
            cuk3 = grp2.cukura_daudzums

        elif vards3 == grp3.nosaukums:
            kal3 = grp3.kaloriju_daudzums
            tauk3 = grp3.tauku_daudzums
            cuk3 = grp3.cukura_daudzums

        elif vards3 == grp4.nosaukums:
            kal3 = grp4.kaloriju_daudzums
            tauk3 = grp4.tauku_daudzums
            cuk3 = grp4.cukura_daudzums

        elif vards3 == grp5.nosaukums:
            kal3 = grp5.kaloriju_daudzums
            tauk3 = grp5.tauku_daudzums
            cuk3 = grp5.cukura_daudzums

        elif vards3 == grp6.nosaukums:
            kal3 = grp6.kaloriju_daudzums
            tauk3 = grp6.tauku_daudzums
            cuk3 = grp6.cukura_daudzums

        elif vards3 == grp7.nosaukums:
            kal3 = grp7.kaloriju_daudzums
            tauk3 = grp7.tauku_daudzums
            cuk3 = grp7.cukura_daudzums

        elif vards3 == grp8.nosaukums:
            kal3 = grp8.kaloriju_daudzums
            tauk3 = grp8.tauku_daudzums
            cuk3 = grp8.cukura_daudzums

        elif vards3 == grp9.nosaukums:
            kal3 = grp9.kaloriju_daudzums
            tauk3 = grp9.tauku_daudzums
            cuk3 = grp9.cukura_daudzums

        elif vards3 == grp10.nosaukums:
            kal3 = grp10.kaloriju_daudzums
            tauk3 = grp10.tauku_daudzums
            cuk3 = grp10.cukura_daudzums

        elif vards3 == a1.nosaukums:
            kal3 = a1.kaloriju_daudzums
            tauk3 = a1.tauku_daudzums
            cuk3 = a1.cukura_daudzums

        elif vards3 == a2.nosaukums:
            kal3 = a2.kaloriju_daudzums
            tauk3 = a2.tauku_daudzums
            cuk3 = a2.cukura_daudzums

        elif vards3 == a3.nosaukums:
            kal3 = a3.kaloriju_daudzums
            tauk3 = a3.tauku_daudzums
            cuk3 = a3.cukura_daudzums

        elif vards3 == a4.nosaukums:
            kal3 = a4.kaloriju_daudzums
            tauk3 = a4.tauku_daudzums
            cuk3 = a4.cukura_daudzums

        elif vards3 == a5.nosaukums:
            kal3 = a5.kaloriju_daudzums
            tauk3 = a5.tauku_daudzums
            cuk3 = a5.cukura_daudzums

        elif vards3 == a6.nosaukums:
            kal3 = a6.kaloriju_daudzums
            tauk3 = a6.tauku_daudzums
            cuk3 = a6.cukura_daudzums

        elif vards3 == a7.nosaukums:
            kal3 = a7.kaloriju_daudzums
            tauk3 = a7.tauku_daudzums
            cuk3 = a7.cukura_daudzums

        elif vards3 == a8.nosaukums:
            kal3 = a8.kaloriju_daudzums
            tauk3 = a8.tauku_daudzums
            cuk3 = a8.cukura_daudzums

        elif vards3 == a9.nosaukums:
            kal3 = a9.kaloriju_daudzums
            tauk3 = a9.tauku_daudzums
            cuk3 = a9.cukura_daudzums

        elif vards3 == a10.nosaukums:
            kal3 = a10.kaloriju_daudzums
            tauk3 = a10.tauku_daudzums
            cuk3 = a10.cukura_daudzums

        elif vards3 == a11.nosaukums:
            kal3 = a11.kaloriju_daudzums
            tauk3 = a11.tauku_daudzums
            cuk3 = a11.cukura_daudzums

        elif vards3 == a12.nosaukums:
            kal3 = a12.kaloriju_daudzums
            tauk3 = a12.tauku_daudzums
            cuk3 = a12.cukura_daudzums

        elif vards3 == a13.nosaukums:
            kal3 = a13.kaloriju_daudzums
            tauk3 = a13.tauku_daudzums
            cuk3 = a13.cukura_daudzums

        elif vards3 == a14.nosaukums:
            kal3 = a14.kaloriju_daudzums
            tauk3 = a14.tauku_daudzums
            cuk3 = a14.cukura_daudzums

        elif vards3 == a15.nosaukums:
            kal3 = a15.kaloriju_daudzums
            tauk3 = a15.tauku_daudzums
            cuk3 = a15.cukura_daudzums

        elif vards3 == a16.nosaukums:
            kal3 = a16.kaloriju_daudzums
            tauk3 = a16.tauku_daudzums
            cuk3 = a16.cukura_daudzums

        elif vards3 == a17.nosaukums:
            kal3 = a17.kaloriju_daudzums
            tauk3 = a17.tauku_daudzums
            cuk3 = a17.cukura_daudzums

        elif vards3 == a18.nosaukums:
            kal3 = a18.kaloriju_daudzums
            tauk3 = a18.tauku_daudzums
            cuk3 = a18.cukura_daudzums

        elif vards3 == a19.nosaukums:
            kal3 = a19.kaloriju_daudzums
            tauk3 = a19.tauku_daudzums
            cuk3 = a19.cukura_daudzums

        elif vards3 == a20.nosaukums:
            kal3 = a20.kaloriju_daudzums
            tauk3 = a20.tauku_daudzums
            cuk3 = a20.cukura_daudzums

        elif vards3 == a21.nosaukums:
            kal3 = a21.kaloriju_daudzums
            tauk3 = a21.tauku_daudzums
            cuk3 = a21.cukura_daudzums

        elif vards3 == a22.nosaukums:
            kal3 = a22.kaloriju_daudzums
            tauk3 = a22.tauku_daudzums
            cuk3 = a22.cukura_daudzums
        
        elif vards3 != d1.nosaukums or vards3 != d2.nosaukums or vards3 != d3.nosaukums or vards3 != d4.nosaukums or vards3 != d5.nosaukums or vards3 != d6.nosaukums or vards3 != d7.nosaukums or vards3 != d8.nosaukums or vards3 != d9.nosaukums or vards3 != d10.nosaukums or vards3 != d11.nosaukums or vards3 != d12.nosaukums or vards3 != d13.nosaukums or vards3 != d14.nosaukums or vards3 != d15.nosaukums or vards3 != d16.nosaukums or vards3 != d17.nosaukums or vards3 != d18.nosaukums or vards3 != d19.nosaukums or vards3 != d21.nosaukums or vards3 != d22.nosaukums or vards3 != d23.nosaukums or vards3 != d24.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()

        elif vards3 != a1.nosaukums or vards3 != a2.nosaukums or vards3 != a3.nosaukums or vards3 != a4.nosaukums or vards3 != a5.nosaukums or vards3 != a6.nosaukums or vards3 != a7.nosaukums or vards3 != a8.nosaukums or vards3 != a9.nosaukums or vards3 != a10.nosaukums or vards3 != a11.nosaukums or vards3 != a12.nosaukums or vards3 != a13.nosaukums or vards3 != a14.nosaukums or vards3 != a15.nosaukums or vards3 != a16.nosaukums or vards3 != a17.nosaukums or vards3 != a18.nosaukums or vards3 != a19.nosaukums or vards3 != a20.nosaukums or vards3 != a21.nosaukums or vards3 != a22.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()

        elif vards3 != pp1.nosaukums or vards3 != pp2.nosaukums or vards3 != pp3.nosaukums or vards3 != pp4.nosaukums or vards3 != pp5.nosaukums or vards3 != pp6.nosaukums or vards3 != pp7.nosaukums or vards3 != pp8.nosaukums or vards3 != pp9.nosaukums or vards3 != pp10.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()

        elif vards3 != gap1.nosaukums or vards3 != gap2.nosaukums or vards3 != gap3.nosaukums or vards3 != gap4.nosaukums or vards3 != gap5.nosaukums or vards3 != gap6.nosaukums or vards3 != gap7.nosaukums or vards3 != gap8.nosaukums or vards3 != gap9.nosaukums or vards3 != gap10.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()

        elif vards3 != grp1.nosaukums or vards3 != grp2.nosaukums or vards3 != grp3.nosaukums or vards3 != grp4.nosaukums or vards3 != grp5.nosaukums or vards3 != grp6.nosaukums or vards3 != grp7.nosaukums or vards3 != grp8.nosaukums or vards3 != grp9.nosaukums or vards3 != grp10.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()

        vards4 = input("Ievadiet produkta nosaukumu: ")
        daudzums4 = int(input("Ievadiet produkta daudzumu gramos: "))
        print("_____________________")
        if vards4 == d1.nosaukums:
            kal4 = d1.kaloriju_daudzums
            tauk4 = d1.tauku_daudzums
            cuk4 = d1.cukura_daudzums

        elif vards4 == d2.nosaukums:
            kal4 = d2.kaloriju_daudzums
            tauk4 = d2.tauku_daudzums
            cuk4 = d2.cukura_daudzums

        elif vards4 == d3.nosaukums:
            kal4 = d3.kaloriju_daudzums
            tauk4 = d3.tauku_daudzums
            cuk4 = d3.cukura_daudzums

        elif vards4 == d3.nosaukums:
            kal4 = d3.kaloriju_daudzums
            tauk4 = d3.tauku_daudzums
            cuk4 = d3.cukura_daudzums

        elif vards4 == d4.nosaukums:
            kal4 = d4.kaloriju_daudzums
            tauk4 = d4.tauku_daudzums
            cuk4 = d4.cukura_daudzums

        elif vards4 == d5.nosaukums:
            kal4 = d5.kaloriju_daudzums
            tauk4 = d5.tauku_daudzums
            cuk4 = d5.cukura_daudzums

        elif vards4 == d6.nosaukums:
            kal4 = d6.kaloriju_daudzums
            tauk4 = d6.tauku_daudzums
            cuk4 = d6.cukura_daudzums

        elif vards4 == d7.nosaukums:
            kal4 = d7.kaloriju_daudzums
            tauk4 = d7.tauku_daudzums
            cuk4 = d7.cukura_daudzums

        elif vards4 == d8.nosaukums:
            kal4 = d8.kaloriju_daudzums
            tauk4 = d8.tauku_daudzums
            cuk4 = d8.cukura_daudzums

        elif vards4 == d9.nosaukums:
            kal4 = d9.kaloriju_daudzums
            tauk4 = d9.tauku_daudzums
            cuk4 = d9.cukura_daudzums

        elif vards4 == d10.nosaukums:
            kal4 = d10.kaloriju_daudzums
            tauk4 = d10.tauku_daudzums
            cuk4 = d10.cukura_daudzums

        elif vards4 == d11.nosaukums:
            kal4 = d11.kaloriju_daudzums
            tauk4 = d11.tauku_daudzums
            cuk4 = d11.cukura_daudzums

        elif vards4 == d12.nosaukums:
            kal4 = d12.kaloriju_daudzums
            tauk4 = d12.tauku_daudzums
            cuk4 = d12.cukura_daudzums

        elif vards4 == d13.nosaukums:
            kal4 = d13.kaloriju_daudzums
            tauk4 = d13.tauku_daudzums
            cuk4 = d13.cukura_daudzums

        elif vards4 == d14.nosaukums:
            kal4 = d14.kaloriju_daudzums
            tauk4 = d14.tauku_daudzums
            cuk4 = d14.cukura_daudzums

        elif vards4 == d15.nosaukums:
            kal4 = d15.kaloriju_daudzums
            tauk4 = d15.tauku_daudzums
            cuk4 = d15.cukura_daudzums

        elif vards4 == d16.nosaukums:
            kal4 = d16.kaloriju_daudzums
            tauk4 = d16.tauku_daudzums
            cuk4 = d16.cukura_daudzums

        elif vards4 == d17.nosaukums:
            kal4 = d17.kaloriju_daudzums
            tauk4 = d17.tauku_daudzums
            cuk4 = d17.cukura_daudzums

        elif vards4 == d18.nosaukums:
            kal4 = d18.kaloriju_daudzums
            tauk4 = d18.tauku_daudzums
            cuk4 = d18.cukura_daudzums

        elif vards4 == d19.nosaukums:
            kal4 = d19.kaloriju_daudzums
            tauk4 = d19.tauku_daudzums
            cuk4 = d19.cukura_daudzums

        elif vards4 == d21.nosaukums:
            kal4 = d21.kaloriju_daudzums
            tauk4 = d21.tauku_daudzums
            cuk4 = d21.cukura_daudzums

        elif vards4 == d22.nosaukums:
            kal4 = d22.kaloriju_daudzums
            tauk4 = d22.tauku_daudzums
            cuk4 = d22.cukura_daudzums

        elif vards4 == d23.nosaukums:
            kal4 = d23.kaloriju_daudzums
            tauk4 = d23.tauku_daudzums
            cuk4 = d23.cukura_daudzums

        elif vards4 == d24.nosaukums:
            kal4 = d24.kaloriju_daudzums
            tauk4 = d24.tauku_daudzums
            cuk4 = d24.cukura_daudzums

        elif vards4 == pp1.nosaukums:
            kal4 = pp1.kaloriju_daudzums
            tauk4 = pp1.tauku_daudzums
            cuk4 = pp1.cukura_daudzums

        elif vards4 == pp2.nosaukums:
            kal4 = pp2.kaloriju_daudzums
            tauk4 = pp2.tauku_daudzums
            cuk4 = pp2.cukura_daudzums

        elif vards4 == pp3.nosaukums:
            kal4 = pp3.kaloriju_daudzums
            tauk4 = pp3.tauku_daudzums
            cuk4 = pp3.cukura_daudzums

        elif vards4 == pp4.nosaukums:
            kal4 = pp4.kaloriju_daudzums
            tauk4 = pp4.tauku_daudzums
            cuk4 = pp4.cukura_daudzums

        elif vards4 == pp5.nosaukums:
            kal4 = pp5.kaloriju_daudzums
            tauk4 = pp5.tauku_daudzums
            cuk4 = pp5.cukura_daudzums

        elif vards4 == pp6.nosaukums:
            kal4 = pp6.kaloriju_daudzums
            tauk4 = pp6.tauku_daudzums
            cuk4 = pp6.cukura_daudzums

        elif vards4 == pp7.nosaukums:
            kal4 = pp7.kaloriju_daudzums
            tauk4 = pp7.tauku_daudzums
            cuk4 = pp7.cukura_daudzums

        elif vards4 == pp8.nosaukums:
            kal4 = pp8.kaloriju_daudzums
            tauk4 = pp8.tauku_daudzums
            cuk4 = pp8.cukura_daudzums

        elif vards4 == pp9.nosaukums:
            kal4 = pp9.kaloriju_daudzums
            tauk4 = pp9.tauku_daudzums
            cuk4 = pp9.cukura_daudzums

        elif vards4 == pp10.nosaukums:
            kal4 = pp10.kaloriju_daudzums
            tauk4 = pp10.tauku_daudzums
            cuk4 = pp10.cukura_daudzums

        elif vards4 == gap1.nosaukums:
            kal4 = gap1.kaloriju_daudzums
            tauk4 = gap1.tauku_daudzums
            cuk4 = gap1.cukura_daudzums

        elif vards4 == gap2.nosaukums:
            kal4 = gap2.kaloriju_daudzums
            tauk4 = gap2.tauku_daudzums
            cuk4 = gap2.cukura_daudzums

        elif vards4 == gap3.nosaukums:
            kal4 = gap3.kaloriju_daudzums
            tauk4 = gap3.tauku_daudzums
            cuk4 = gap3.cukura_daudzums

        elif vards4 == gap4.nosaukums:
            kal4 = gap4.kaloriju_daudzums
            tauk4 = gap4.tauku_daudzums
            cuk4 = gap4.cukura_daudzums

        elif vards4 == gap5.nosaukums:
            kal4 = gap5.kaloriju_daudzums
            tauk4 = gap5.tauku_daudzums
            cuk4 = gap5.cukura_daudzums

        elif vards4 == gap6.nosaukums:
            kal4 = gap6.kaloriju_daudzums
            tauk4 = gap6.tauku_daudzums
            cuk4 = gap6.cukura_daudzums

        elif vards4 == gap7.nosaukums:
            kal4 = gap7.kaloriju_daudzums
            tauk4 = gap7.tauku_daudzums
            cuk4 = gap7.cukura_daudzums

        elif vards4 == gap8.nosaukums:
            kal4 = gap8.kaloriju_daudzums
            tauk4 = gap8.tauku_daudzums
            cuk4 = gap8.cukura_daudzums

        elif vards4 == gap9.nosaukums:
            kal4 = gap9.kaloriju_daudzums
            tauk4 = gap9.tauku_daudzums
            cuk4 = gap9.cukura_daudzums

        elif vards4 == gap10.nosaukums:
            kal4 = gap10.kaloriju_daudzums
            tauk4 = gap10.tauku_daudzums
            cuk4 = gap10.cukura_daudzums

        elif vards4 == grp1.nosaukums:
            kal4 = grp1.kaloriju_daudzums
            tauk4 = grp1.tauku_daudzums
            cuk4 = grp1.cukura_daudzums

        elif vards4 == grp2.nosaukums:
            kal4 = grp2.kaloriju_daudzums
            tauk4 = grp2.tauku_daudzums
            cuk4 = grp2.cukura_daudzums

        elif vards4 == grp3.nosaukums:
            kal4 = grp3.kaloriju_daudzums
            tauk4 = grp3.tauku_daudzums
            cuk4 = grp3.cukura_daudzums

        elif vards4 == grp4.nosaukums:
            kal4 = grp4.kaloriju_daudzums
            tauk4 = grp4.tauku_daudzums
            cuk4 = grp4.cukura_daudzums

        elif vards4 == grp5.nosaukums:
            kal4 = grp5.kaloriju_daudzums
            tauk4 = grp5.tauku_daudzums
            cuk4 = grp5.cukura_daudzums

        elif vards4 == grp6.nosaukums:
            kal4 = grp6.kaloriju_daudzums
            tauk4 = grp6.tauku_daudzums
            cuk4 = grp6.cukura_daudzums

        elif vards4 == grp7.nosaukums:
            kal4 = grp7.kaloriju_daudzums
            tauk4 = grp7.tauku_daudzums
            cuk4 = grp7.cukura_daudzums

        elif vards4 == grp8.nosaukums:
            kal4 = grp8.kaloriju_daudzums
            tauk4 = grp8.tauku_daudzums
            cuk4 = grp8.cukura_daudzums

        elif vards4 == grp9.nosaukums:
            kal4 = grp9.kaloriju_daudzums
            tauk4 = grp9.tauku_daudzums
            cuk4 = grp9.cukura_daudzums

        elif vards4 == grp10.nosaukums:
            kal4 = grp10.kaloriju_daudzums
            tauk4 = grp10.tauku_daudzums
            cuk4 = grp10.cukura_daudzums

        elif vards4 == a1.nosaukums:
            kal4 = a1.kaloriju_daudzums
            tauk4 = a1.tauku_daudzums
            cuk4 = a1.cukura_daudzums

        elif vards4 == a2.nosaukums:
            kal4 = a2.kaloriju_daudzums
            tauk4 = a2.tauku_daudzums
            cuk4 = a2.cukura_daudzums

        elif vards4 == a3.nosaukums:
            kal4 = a3.kaloriju_daudzums
            tauk4 = a3.tauku_daudzums
            cuk4 = a3.cukura_daudzums

        elif vards4 == a4.nosaukums:
            kal4 = a4.kaloriju_daudzums
            tauk4 = a4.tauku_daudzums
            cuk4 = a4.cukura_daudzums

        elif vards4 == a5.nosaukums:
            kal4 = a5.kaloriju_daudzums
            tauk4 = a5.tauku_daudzums
            cuk4 = a5.cukura_daudzums

        elif vards4 == a6.nosaukums:
            kal4 = a6.kaloriju_daudzums
            tauk4 = a6.tauku_daudzums
            cuk4 = a6.cukura_daudzums

        elif vards4 == a7.nosaukums:
            kal4 = a7.kaloriju_daudzums
            tauk4 = a7.tauku_daudzums
            cuk4 = a7.cukura_daudzums

        elif vards4 == a8.nosaukums:
            kal4 = a8.kaloriju_daudzums
            tauk4 = a8.tauku_daudzums
            cuk4 = a8.cukura_daudzums

        elif vards4 == a9.nosaukums:
            kal4 = a9.kaloriju_daudzums
            tauk4 = a9.tauku_daudzums
            cuk4 = a9.cukura_daudzums

        elif vards4 == a10.nosaukums:
            kal4 = a10.kaloriju_daudzums
            tauk4 = a10.tauku_daudzums
            cuk4 = a10.cukura_daudzums

        elif vards4 == a11.nosaukums:
            kal4 = a11.kaloriju_daudzums
            tauk4 = a11.tauku_daudzums
            cuk4 = a11.cukura_daudzums

        elif vards4 == a12.nosaukums:
            kal4 = a12.kaloriju_daudzums
            tauk4 = a12.tauku_daudzums
            cuk4 = a12.cukura_daudzums

        elif vards4 == a13.nosaukums:
            kal4 = a13.kaloriju_daudzums
            tauk4 = a13.tauku_daudzums
            cuk4 = a13.cukura_daudzums

        elif vards4 == a14.nosaukums:
            kal4 = a14.kaloriju_daudzums
            tauk4 = a14.tauku_daudzums
            cuk4 = a14.cukura_daudzums

        elif vards4 == a15.nosaukums:
            kal4 = a15.kaloriju_daudzums
            tauk4 = a15.tauku_daudzums
            cuk4 = a15.cukura_daudzums

        elif vards4 == a16.nosaukums:
            kal4 = a16.kaloriju_daudzums
            tauk4 = a16.tauku_daudzums
            cuk4 = a16.cukura_daudzums

        elif vards4 == a17.nosaukums:
            kal4 = a17.kaloriju_daudzums
            tauk4 = a17.tauku_daudzums
            cuk4 = a17.cukura_daudzums

        elif vards4 == a18.nosaukums:
            kal4 = a18.kaloriju_daudzums
            tauk4 = a18.tauku_daudzums
            cuk4 = a18.cukura_daudzums

        elif vards4 == a19.nosaukums:
            kal4 = a19.kaloriju_daudzums
            tauk4 = a19.tauku_daudzums
            cuk4 = a19.cukura_daudzums

        elif vards4 == a20.nosaukums:
            kal4 = a20.kaloriju_daudzums
            tauk4 = a20.tauku_daudzums
            cuk4 = a20.cukura_daudzums

        elif vards4 == a21.nosaukums:
            kal4 = a21.kaloriju_daudzums
            tauk4 = a21.tauku_daudzums
            cuk4 = a21.cukura_daudzums

        elif vards4 == a22.nosaukums:
            kal4 = a22.kaloriju_daudzums
            tauk4 = a22.tauku_daudzums
            cuk4 = a22.cukura_daudzums
        
        elif vards4 != d1.nosaukums or vards4 != d2.nosaukums or vards4 != d3.nosaukums or vards4 != d4.nosaukums or vards4 != d5.nosaukums or vards4 != d6.nosaukums or vards4 != d7.nosaukums or vards4 != d8.nosaukums or vards4 != d9.nosaukums or vards4 != d10.nosaukums or vards4 != d11.nosaukums or vards4 != d12.nosaukums or vards4 != d13.nosaukums or vards4 != d14.nosaukums or vards4 != d15.nosaukums or vards4 != d16.nosaukums or vards4 != d17.nosaukums or vards4 != d18.nosaukums or vards4 != d19.nosaukums or vards4 != d21.nosaukums or vards4 != d22.nosaukums or vards4 != d23.nosaukums or vards4 != d24.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()
        elif vards4 != a1.nosaukums or vards4 != a2.nosaukums or vards4 != a3.nosaukums or vards4 != a4.nosaukums or vards4 != a5.nosaukums or vards4 != a6.nosaukums or vards4 != a7.nosaukums or vards4 != a8.nosaukums or vards4 != a9.nosaukums or vards4 != a10.nosaukums or vards4 != a11.nosaukums or vards4 != a12.nosaukums or vards4 != a13.nosaukums or vards4 != a14.nosaukums or vards4 != a15.nosaukums or vards4 != a16.nosaukums or vards4 != a17.nosaukums or vards4 != a18.nosaukums or vards4 != a19.nosaukums or vards4 != a20.nosaukums or vards4 != a21.nosaukums or vards4 != a22.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()
            
        elif vards4 != pp1.nosaukums or vards4 != pp2.nosaukums or vards4 != pp3.nosaukums or vards4 != pp4.nosaukums or vards4 != pp5.nosaukums or vards4 != pp6.nosaukums or vards4 != pp7.nosaukums or vards4 != pp8.nosaukums or vards4 != pp9.nosaukums or vards4 != pp10.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()

        elif vards4 != gap1.nosaukums or vards4 != gap2.nosaukums or vards4 != gap3.nosaukums or vards4 != gap4.nosaukums or vards4 != gap5.nosaukums or vards4 != gap6.nosaukums or vards4 != gap7.nosaukums or vards4 != gap8.nosaukums or vards4 != gap9.nosaukums or vards4 != gap10.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()

        elif vards4 != grp1.nosaukums or vards4 != grp2.nosaukums or vards4 != grp3.nosaukums or vards4 != grp4.nosaukums or vards4 != grp5.nosaukums or vards4 != grp6.nosaukums or vards4 != grp7.nosaukums or vards4 != grp8.nosaukums or vards4 != grp9.nosaukums or vards4 != grp10.nosaukums:
            print("Ievadītais produkta nosaukums ir neprecīzi ievadīt vai produkts nav pieejams. Sāciet no jauna!")
            exit()

        print(f"Kaloriju daudzums:{daudzums*kal + daudzums1*kal1 + daudzums2*kal2 + daudzums3*kal3 + daudzums4*kal4} kcal")
        print(f"Tauku daudzums:{daudzums*tauk + daudzums1*tauk1 + daudzums2*tauk2 + daudzums3*tauk3 + daudzums4*tauk4}g")
        print(f"Cukura daudzums: {daudzums*cuk + daudzums1*cuk1 + daudzums2*cuk2 + daudzums3*cuk3 + daudzums4*cuk4}g")
        exit()

    elif (darbiba == 8):
        kcal = int(input("Ievadiet produkta kaloriju daudzumu: "))
        tauki = int(input("Ievadiet produkta tauku daudzumu: "))
        cukurs = int(input("Ievadiet produkta cukura daudzumu: "))
        print("______________")

        kcal1 = int(input("Ievadiet produkta kaloriju daudzumu: "))
        tauki1 = int(input("Ievadiet produkta tauku daudzumu: "))
        cukurs1 = int(input("Ievadiet produkta cukura daudzumu: "))
        print("_______________")

        kcal2 = int(input("Ievadiet produkta kaloriju daudzumu: "))
        tauki2 = int(input("Ievadiet produkta tauku daudzumu: "))
        cukurs2 = int(input("Ievadiet produkta cukura daudzumu: "))
        print("_______________")

        kcal3 = int(input("Ievadiet produkta kaloriju daudzumu: "))
        tauki3 = int(input("Ievadiet produkta tauku daudzumu: "))
        cukurs3 = int(input("Ievadiet produkta cukura daudzumu: "))
        print("_______________")

        kcal4 = int(input("Ievadiet produkta kaloriju daudzumu: "))
        tauki4 = int(input("Ievadiet produkta tauku daudzumu: "))
        cukurs4 = int(input("Ievadiet produkta cukura daudzumu: "))
        print("_______________")

        print(f'Produktu kaloriju daudzums: {kcal + kcal1 + kcal2 + kcal3 + kcal4}kcal')
        print(f'Produktu tauku daudzums: {tauki + tauki1 + tauki2 + tauki3 + tauki4}g')
        print(f'Produktu cukura daudzums1: {cukurs + cukurs1 + cukurs2 + cukurs3 + cukurs4}g')
        exit() 