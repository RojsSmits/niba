def apmekletajs_f(reitingu_skaits,reitings,zvaigznes,apmekletajs,paroles,treneris_apraksts,treneri_v,bildes,darbalaiki,telpas,aprikojums,abonetaji,abonementi,abonesanas_skaits,treneris_pieejams): #definējam funkciju
    turpinat=("nē") 
    jautajumi=("nē")       
    velme=str(input("vai gribi trenēties viens, vai ar treneri?: ")) # dod izvēli treneties vienam vai ar treneri
    if velme=="treneri" or velme=="ar treneri":
      bridinajums=str(input("(lai pieteiktos pie trenera tev jabūt abonētājam)Vai Jūs esi abonētajs?: ")) #brīdina, ka tikai abonementi var treneties ar treneri
      while bridinajums==("jā"): 
        if abonetaji==[]:
          print("nav abonētāju")
          bridinajums=("nē")
          break
        telefons=str(input("Ierakstiet savu personas kodu un telefona numuru: ")) #ieraksta informāciju, lai pierakstītos uz treniņu
        print(abonementi)
        abonements_pieteikt=(int(input("ievadiet abonementa kārtas ciparu ,skatoties no kreisāspuses (ar cipariem): "))) #rāda abonementa veidu
        for i in range(len(abonetaji)):
          if abonetaji[i]==(f"tel. num., personas kods:{telefons} abonements:{abonementi[abonements_pieteikt-1]}"): #pārbauda vai ievadītie dati ir pareizi
            print("sveiki, ievadītie dati pareizi!")
            while turpinat!=("jā"):
             darbiba=int(input("Ko jūs vēlaties darīt?\n 1.apskatīt treneru apraksus\n 2.novērtēt treneri(rakstat ar cipariem): "))#tiek dota iespēja izvēlēties funkciju
             if darbiba==(1): #ja izvēlas 1
              for i in range (len(paroles)):
               print(f"treneris/e: {treneri_v[i]} apraksts: {treneris_apraksts[i]} pieejams: {treneris_pieejams[i]} reitings:{zvaigznes[i]}") #parāda trenera aprakstus
              turpinat=(str(input("Vai gribat iziet? ")))
              if turpinat==("jā"):
                bridinajums=("nē")
                break
             elif darbiba==(2):#ja izvēlas 2
              karta=int(input(f"kuru pēckārtas skatoties no kreisās malas sarakstā {treneri_v} treneri jūs gribat novērtēt (rakstat ar skaitļiem bez punkta) "))
              reitings[karta-1]+=int(input("ievadi zvaigžņu skaitu 1-5 veselos skaitļos?: "))
              reitingu_skaits[karta-1]+=1 #tiek dota iespēja izvēlēties trenri, kuru novērtēt
              turpinat=(str(input("vai gribat iziet? ")))
              if turpinat==("jā"):
                bridinajums=("nē")
                break
          elif i==len(abonetaji)-1:  #šī funkcia iedarbojas, kad nav šāda abonementa
            print("Ievadīti nepareizi dati.")
            bridinajums=str(input("vai mēģināsiet velreiz?: "))#tiek dota iespēja mēģināt velreiz
    else:
      while jautajumi!=("jā"):
       jautajumi=int(input("Ko jūs gribat redzēt?:\n 1.Piedāvātās zāles, to darba laikus\n 2.Bildes\n 3.Aprīkojumu\n 4.Gribat pieteikties uz treniņu\n 5. Atcelt abonementu (rakstat ar cipariem|): "))#tiek dota iespēja izvēlēties funkciju
       if jautajumi==(1):#ja izvēlas 1
        for i in range(len(telpas)):
          print(f"{telpas[i]} atvērta:{darbalaiki[i]}")#tiek izprintētas telpas un to darbalaiki
       elif jautajumi==(2):#ja izvēlas 2
        for i in range (len(bildes)):
          print(f"telpa:{telpas[i]} bildes links:{bildes[i]}")#tiek izprintētas telpas un to bilžu linki
       elif jautajumi==(3):#ja izvelas 3
        for i in range (len(aprikojums)):
          print(f"telpas:{telpas[i]} aprikojums: {aprikojums[i]}")#tiek izprintētas telpas un to aprīkojums
       elif jautajumi==(4):#ja izvelas 4
        print(abonementi)
        telefons=str(input("ierakstiet savu personas kodu un telefona numuru:"))
        abonements_pieteikt=(int(input("ievadiet abonementa kārtas ciparu ,skatoties no kreisāspuses (ar cipariem): ")))#lietotājam tiek prasīts ievietot savus datus un dota iespēja izvēlēties abonementu
        abonesanas_skaits[abonements_pieteikt-1]+=1
        abonetaji.append(f"tel. num., personas kods:{telefons} abonements:{abonementi[abonements_pieteikt-1]}")#tiek pievienots jaunais abonētājs sarakstam palelināts abonētāju skaits
       while jautajumi==(5):#ja izvēlas 5
        telefons=str(input("ierakstiet savu personas kodu un telefona numuru: "))
        print(abonementi)
        abonements_pieteikt=(int(input("ievadiet abonementa kārtas ciparu ,skatoties no kreisāspuses (ar cipariem): ")))#lietotājam tiek prasīts ievietot savus datus un abonementu
        for i in range(len(abonetaji)):
          if abonetaji[i]==(f"tel. num., personas kods:{telefons} abonements:{abonementi[abonements_pieteikt-1]}"):
            abonesanas_skaits[abonements_pieteikt-1]-=1
            abonetaji.remove(f"tel. num., personas kods:{telefons} abonements:{abonementi[abonements_pieteikt-1]}")# tiek pārbaudīta sniegtā informācija un noņemts abonements
            jautajumi=("nē")
            break
          elif i==len(abonetaji)-1:
            print("Ievadīti nepareizi dati.")
            jautajums=str(input("vai mēģināsiet velreiz?: "))#šī funkcia iedarbojas, kad nav šāda abonementa, tiek dota iespēja mēģināt velreiz
            if jautajums==("jā"):
              break
            else:
              jautajumi=("nē")
       jautajumi=(str(input("Vai vēlaties beigt? ")))#lietājam tiek dota iespēja iziet       