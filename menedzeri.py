def menedzeris_f(reitingu_skaits,reitings,zvaigznes,apmekletajs,paroles,treneris_apraksts,treneri_v,bildes,darbalaiki,telpas,aprikojums,abonetaji,abonementi,abonesanas_skaits,treneris_pieejams): #definējam funkciju
  jautajumi=("nē")
  while jautajumi!=("jā"):
     jautajumi=int(input("ko grbat darīt?\n 1.redzēt treneru aprakstus\n 2.redzdēt treneru reitingus\n 3.pārmainīt bilžu linkus\n 4.mainīt aprīkojuma sarakstu\n 5.mainīt darbalaikus\n 6.pievienot jaunu treneri\n 7.redzēt abonētāju skiatu\n 8.redzēt abonējošos cilvēkus (ar cipariem): ")) #jautājam lietotājam ko vēlas darīt
     if jautajumi==(1): #ja izvēlas 1
      for i in range (len(treneri_v)):
        print(f"vārds:{treneri_v[i]} apraksts:{treneris_apraksts[i]}") #rāda trenera aprakstus
     elif jautajumi==(2):#ja izvēlas 2
      for i in range (len(treneri_v)):
        print(f"vārds:{treneri_v[i]} reitings:{zvaigznes[i]}") #rāda trenera reitingus
     elif jautajumi==(3):#ja izvēlas 3
      for i in range (len(bildes)):
        bildes[i]=str(input(f"iekopējiet bildes linu {telpas[i]} telpai: ")) #rāda telpa bildes
     elif jautajumi==(4):#ja izvēlas 4
      for i in range (len(aprikojums)):
        aprikojums[i]=str(input(f"ierakstat pilnu aprīkojuma uzskaitījumu {telpas[i]} telpai: ")) #rāda sporta aprīkojumu
     elif jautajumi==(5):#ja izvēlas 5
      for i in range (len(darbalaiki)):
        darbalaiki[i]=str(input(f"ievadiet {telpas[i]} laikus: ")) #rāda darbalaikus
     elif jautajumi==(6):#ja izvēlas 6
      treneri_v.append(str(input("ievadiet trenera vārdu uzvārdu: "))) #dod iespēju peivienot treneri
      paroles.append(str(input("ievadi trenera paroli: "))) #ievadīt trenera paroli
      treneris_apraksts.append("_") #ievada aprakstu
      treneris_pieejams.append("_") #ievada, kad šis treneris ir pieejams
      zvaigznes.append("") #ja ir novērtējums, pievieno to
      reitingu_skaits.append(0)
      reitings.append(0)
     elif jautajumi==(7):#ja izvēlas 7
      for i in range (len(abonementi)):
        print(f"{abonementi[i]} cilvēki pieteikušies: {abonesanas_skaits[i]}") #rāda cik cilvēki ir pieteikušies
     elif jautajumi==(8):#ja izvēlas 8
      print(abonetaji) #rāda abonējušo skaitu
     jautajumi=(str(input("Vai vēlaties beigt? ")))