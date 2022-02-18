import treneris #ievietojam mūsu veidotu funkciju
import apmekletaji #ievietojam mūsu veidotu funkciju
import menedzeri #ievietojam mūsu veidotu funkciju
atbilde=("jā")
jaut=("jā")
treneri_v=["Juris Ozols","x", "Tomas Liepa", "Edvards Kalniņš", "Linus Bruņinieks", "Santa Balode"] #mūsu dotie treneri
paroles=["5629","l","0492","1452","0372","7436"] #treneru paroles, lai viņi varētu piekļūt savam profilam
treneris_apraksts=["jautrs tel. num.:11112222","spējīgs treneris tel. num.:31112222","labs čoms tel. num.:11692222","mīl runāt par traktoriem tel. num.:00112222","augstākā izglītība sportā tel. num.:11114522","Apdāvināts treneris tel. num.:1234567"] 
treneris_pieejams=["pirmdienas-piekdienas(10:00-19:00)","pirmdienas-ceturdienas(10:00-20:00)","pirmdienas-sesdiendas(9:00-19:00)","otradienas-piekdienas(10:00-18:00)","pirmdienas-piekdienas(10:00-19:00)","pirmdienas-piekdienas(18:00-22:00)"] 
telpas=["Valmiera, Kaktusa iela, 34","Cēsis, Poda iela, 12","Valmiera, desu iela, 1"]
darbalaiki=["8:30-20:00","9:00-21:00","8:00-22:00"]
bildes=["https://www.baseins.eu/wp-content/uploads/2013/04/6X4B8217.jpg","https://www.baseins.eu/wp-content/uploads/2013/04/6X4B8217.jpg","https://www.baseins.eu/wp-content/uploads/2013/04/6X4B8217.jpg"]
aprikojums=["divas 10 kg hanteles","25 kg svaru bumba","12 matrači, 2 skriešanas trenežieri"]
abonementi=["1 treniņš nedēļā: 5 eiro","2 treniņi nedēļā: 10 eiro","4 treniņi nedēļā: 20 eiro","7 treniņi nedēļā: 30 eiro"] #kādi abonementi ir pieejami un cik tie maksā
abonetaji=["tel. num., personas kods:5720 abonements:2 treniņi nedēļā: 10 eiro"] #mūsu dotais abonements
reitingu_skaits=[2,2,2,2,2,2] #cik reizes katrs treneris ir novērtēts
reitings=[9,10,8,6,9,2] #kopējais reitings no vērtētājiem
abonesanas_skaits=[3,4,5,2] # skaits cik daudz ir katram abonementa veidam
zvaigznes=[" "," "," "," "," ",""] #aprēķinātais reitings
run=True
while run==True:
  for i in range(len(reitings)): #darbojas kamēr ir reitingi
   if reitings[i]==0: #ja reitings ir 0
    zvaigznes[i]=0 #tad zvaigznes ir 0 un nereiķina reitingu
    break
   zvaigznes[i]=reitings[i]/reitingu_skaits[i] #aprēķina reitingu trenerim
  apmekletajs=str(input("Vai esi apmeklētājs, vai treneris?: ")) #jautā vai ir apmeklētājs vai treneris
  if apmekletajs==("treneris"): #ja treneris
    treneris.treneris_f(treneri_v,paroles,treneris_apraksts,zvaigznes,treneris_pieejams) # tad izsauc trenera funkciju
  elif apmekletajs==("apmeklētājs"): #ja apmeklētājs     
    apmekletaji.apmekletajs_f(reitingu_skaits,reitings,zvaigznes,apmekletajs,paroles,treneris_apraksts,treneri_v,bildes,darbalaiki,telpas,aprikojums,abonetaji,abonementi,abonesanas_skaits,treneris_pieejams) #izsauc apmeklētāja funkciju
  elif apmekletajs==("dunkey32"): #ja ievada menedžera lietotājvārdu
    menedzeri.menedzeris_f(reitingu_skaits,reitings,zvaigznes,apmekletajs,paroles,treneris_apraksts,treneri_v,bildes,darbalaiki,telpas,aprikojums,abonetaji,abonementi,abonesanas_skaits,treneris_pieejams) #izsauc menedžera funkciju