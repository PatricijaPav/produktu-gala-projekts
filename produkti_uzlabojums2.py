class Darzeni:

    def __init__(self, nosaukums, kaloriju_daudzums, tauku_daudzums, cukura_daudzums ):
        self.nosaukums = nosaukums
        self.kaloriju_daudzums = kaloriju_daudzums
        self.tauku_daudzums = tauku_daudzums
        self.cukura_daudzums = cukura_daudzums

visi_darzeni = [
"Avokado- kcal: 1,9814 tauki: 0,194g cukurs: 0,0066g",
"Baklažāns-  kcal: 0.2223, tauki: 0.002g, cukurs: 0.029g",
"Baravikas- kcal: 0.3011, tauki: 0.0023g, cukurs: 0.0161g",
"Bietes- kcal: 0.3824, tauki: 0.002g, cukurs: 0.068g",
"Brokoļi- kcal: 0.3489, tauki: 0.003g, cukurs: 0.0195g",
"Burkāni- kcal: 0,413, tauki: 0,002g cukurs: 0,047g",
"Cukini- kcal: 0.24, tauki: 0.003g, cukurs: 0.025g",
"Gailenes- kcal: 0.2677, tauki: 0.0069g, cukurs: 0.0144g",
"Gurķis- kcal: 0,15, tauki: 0,001g cukurs: 0,017g",
"Kabacis- kcal: 0.17, tauki: 0.004g, cukurs: 0.003g",
"Kartupeļi- kcal: 0.76, tauki: 0.002, cukurs: 0.006",
"Kāposts- kcal: 0.2772, tauki: 0.002g, cukurs: 0.0406g",
"Kukurūza- kcal: 1.2763, tauki: 0.0129g, cukurs: 0.0342g",
"Ķiploks- kcal: 1.0827, tauki: 0.006g, cukurs: 0.016g",
"Ķirbis- kcal: 0.1577, tauki: 0.001, cukuri: 0.017g",
"Paprika- kcal: 0.2103, tauki: 0.003g, cukuri: 0.024g",
"Redīsi- kcal: 0.2462, tauki: 0.0003g, cukurs: 0.0307g",
"Saldais kartupelis- kcal: 0.8795, tauki: 0.0005g, cukuri: 0.0454g",
"Sīpols- kcal: 0.3011, tauki: 0.002g, cukurs: 0.048g",
"Spārģeļi- kcal:  0.2, tauki: 0.001g, cukurs: 0.019g",
"Tomāti- kcal: 0.2271, tauki: 0.003g, cukurs: 0.0335g",
"Zirņi- kcal: 0.7505, tauki: 0.0079g, cukurs: 0.0531g"]


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
d16= Darzeni("zirņi", 0.7505, 0.0079, 0.0531)
d17= Darzeni("baklažāns", 0.2223, 0.002, 0.029)
d18= Darzeni("baravikas", 0.3011, 0.0023, 0.0161)
d19= Darzeni("gailenes", 0.2677, 0.0069, 0.0144)
d20= Darzeni("lācenes", 0.5497, 0.0106, 0.0581)
d21= Darzeni("spārģeļi", 0.2, 0.001, 0.019)
d22 = Darzeni("tomāti", 0.2271, 0.003, 0.0335)
d23= Darzeni("bietes", 0.3824, 0.002, 0.068)

class PienaProdukti:

    def __init__(self, nosaukums, kaloriju_daudzums, tauku_daudzums, cukura_daudzums):
        self.nosaukums = nosaukums
        self.kaloriju_daudzums = kaloriju_daudzums
        self.tauku_daudzums = tauku_daudzums
        self.cukura_daudzums = cukura_daudzums

visi_PienaProdukti = [
"biezpiens- kcal: 0.8963, tauki: 0.0151, cukurs: 0.0236"
"jogurts- kcal: 0.7098, tauki: 0.0011, cukurs: 0.142"
"krējums- kcal: 1.7615, tauki: 0.17, cukurs: 0.031"
"saldais krējums- kcal: 3.3007, tauki: 0.35, cukurs: 0.03"
"siers- kcal: 2.7701, tauki: 0.1995, cukurs: 0.0022"
]


pp1 = PienaProdukti("siers", 2.7701, 0.1995, 0.0022)
pp2 = PienaProdukti("biezpiens", 0.8963, 0.0151, 0.0236)
pp3 = PienaProdukti("jogurts", 0.7098, 0.0011, 0.142)
pp4 = PienaProdukti("krējums", 1.7615, 0.17, 0.031)
pp5 = PienaProdukti("saldais krējums", 3.3007, 0.35, 0.03)

while True:
    darbiba = int(input("""Kādu darbību vēlaties veikt?
    1- Izprintēt visu pieejamo produktu sarakstu
    2- Izprintēt dārzeņu pieejamo sarakstu
    3- Izprintēt piena produktu pieejamo sarakstu
    4- Izvēlēties produktus no pieejamajiem un veikt aprēķinu
    5- Manuāli ievadīt produktus un saskaitīt vai uzzināt to kaloriju daudzumu, tauku daudzumu un cukura daudzumu \n"""))

    if(darbiba == 1):
        print("____ Dārzeņi ____")
        for vdarzeni in visi_darzeni:
            print (vdarzeni)

        print("____ Piena produkti ____")
        for vPienaProdukti in visi_PienaProdukti:
            print(vPienaProdukti)

    elif(darbiba == 2):
        print("Darzeņu saraksts")
        for darzenu_saraksts in visi_darzeni:
            print(darzenu_saraksts)

    elif (darbiba == 3):
        print("Piena produktu saraksts:")
        for Piena_produktu_saraksts in visi_PienaProdukti:
            print(Piena_produktu_saraksts)

    elif(darbiba == 4):
        #print("Kad vēlaties beigt ivadīt produktus rakstiet: BEIGT ")
        vards = input("Ievadiet produkta nosaukumu: ")
        daudzums = int(input("Ievadiet produkta daudzumu: "))
        print("_____________________")
        if vards == "BEIGT":
            exit()

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


        vards1 = input("Ievadiet produkta nosaukumu: ")
        daudzums1 = int(input("Ievadiet produkta daudzumu: "))
        print("_____________________")
        if vards1 == "BEIGT":
            exit()
        
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

        vards2 = input("Ievadiet produkta nosaukumu: ")
        daudzums2 = int(input("Ievadiet produkta daudzumu: "))
        print("_____________________")
        if vards2 == "BEIGT":
            exit()
        
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

        vards3 = input("Ievadiet produkta nosaukumu: ")
        daudzums3 = int(input("Ievadiet produkta daudzumu: "))
        print("_____________________")
        if vards3 == "BEIGT":
            exit()
        
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

        vards4 = input("Ievadiet produkta nosaukumu: ")
        daudzums4 = int(input("Ievadiet produkta daudzumu: "))
        print("_____________________")
        if vards4 == "BEIGT":
            exit()
        
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

        print(daudzums*kal + daudzums1*kal1 + daudzums2*kal2 + daudzums3*kal3 + daudzums4*kal4)
        print(daudzums*tauk + daudzums1*tauk1 + daudzums2*tauk2 + daudzums3*tauk3 + daudzums4*tauk4)
        print(daudzums*cuk + daudzums1*cuk1 + daudzums2*cuk2 + daudzums3*cuk3 + daudzums4*cuk4)
        exit()
    
    elif (darbiba == 5):
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

        print(f'Produktu kaloriju daudzums ir: {kcal + kcal1 + kcal2 + kcal3 + kcal4}kcal')
        print(f'Produktu tauku daudzums ir: {tauki + tauki1 + tauki2 + tauki3 + tauki4}g')
        print(f'Produktu cukura daudzums ir: {cukurs + cukurs1 + cukurs2 + cukurs3 + cukurs4}g')
        exit()