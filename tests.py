from rules import *
from main import do_external_sandhi

def unittest(actual, expected, msg):
  assert actual == expected, f'{msg}\nExpected: {expected}.\nGot: {actual}.'

'''
The first hundred tests are the first hundred lines from a Sanskrit text, the Bhagavad Gita
An online version with IAST can be found at http://www.sanskritweb.net/sansdocs/gita-big.pdf
Bear in mind the following equivalences:
ā becomes A'
ḍ becomes D
ḥ becomes H
ī becomes I
ṃ becomes M
ṇ becomes N
ñ becomes J
ṅ becomes G
ṛ becomes R
ṝ becomes RR
ṣ becomes S
ś becomes z
ṭ becomes T
ū becomes U
ḍh becomes Dh
ṭh becomes Th
'''

unittest(do_external_sandhi('dharmakSetre kurukSetre samavetAH yuyutsavaH'), 'dharmakSetre kurukSetre samavetA yuyutsavaH', 'Line 1,1 failed')
unittest(do_external_sandhi('mAmakAH pANDavAH ca eva kim akurvata saMjaya'), 'mAmakAH pANDavAz caiva kim akurvata saMjaya', 'Line 1,2 failed')
unittest(do_external_sandhi('dRSTvA tu pANDavAnIkam vyUDham duryodhanaH tadA'), 'dRSTvA tu pANDavAnIkaM vyUDhaM duryodhanas tadA', 'Line 2,1 failed')
unittest(do_external_sandhi('AcAryam upasaMgamya rAjA vacanam abravIt'), 'AcAryam upasaMgamya rAjA vacanam abravIt', 'Line 2,2 failed')
unittest(do_external_sandhi('pazya etAn pANDuputrANAm AcArya mahatIm camUm'), 'pazyaitAn pANDuputrANAm AcArya mahatIM camUm', 'Line 3,1 failed')
unittest(do_external_sandhi('vyUDhAm drupadaputreNa tava ziSyeNa dhImatA'), 'vyUDhAM drupadaputreNa tava ziSyeNa dhImatA', 'Line 3,2 failed')
unittest(do_external_sandhi('atra zUrAH maheSvAsAH bhImArjunasamAH yudhi'), 'atra zUrA maheSvAsA bhImArjunasamA yudhi', 'Line 4,1 failed')
unittest(do_external_sandhi('yuyudhAnaH virATaH ca drupadaH ca mahArathaH'), 'yuyudhAno virATaz ca drupadaz ca mahArathaH', 'Line 4,2 failed')
unittest(do_external_sandhi('dhRSTaketuH ca IkitAnaH kAzirAjaH ca vIryavAn'), 'dhRSTaketuz cekitAnaH kAzirAjaz ca vIryavAn', 'Line 5,1 failed')
unittest(do_external_sandhi('purujit kuntibhojaH ca zaibyaH ca narapuMgavaH'), 'purujit kuntibhojaz ca zaibyaz ca narapuMgavaH', 'Line 5,2 failed')
unittest(do_external_sandhi('yudhAmanyuH ca vikrAntaH uttamaujaH ca vIryavAn'), 'yudhAmanyuz ca vikrAnta uttamaujaz ca vIryavAn', 'Line 6,1 failed')
unittest(do_external_sandhi('saubhadraH draupadeyAH ca sarve eva mahArathAH'), 'saubhadro draupadeyAz ca sarva eva mahArathAH', 'Line 6,2 failed')
unittest(do_external_sandhi('asmAkam tu viziSTAH ye tAn nibodha dvijottama'), 'asmAkaM tu viziSTA ye tAn nibodha dvijottama', 'Line 7,1 failed')
unittest(do_external_sandhi('nAyakAH mama sainyasya saMjJArtham tAn bravImi te'), 'nAyakA mama sainyasya saMjJArthaM tAn bravImi te', 'Line 7,2 failed')
unittest(do_external_sandhi('bhavAn bhISmaH ca karNaH ca kRpaH ca samitiMjayaH'), 'bhavAn bhISmaz ca karNaz ca kRpaz ca samitiMjayaH', 'Line 8,1 failed')
unittest(do_external_sandhi('azvatthAmA vikarnaH ca saumyadattiH tathA eva ca'), 'azvatthAmA vikarnaz ca saumyadattis tathaiva ca', 'Line 8,2 failed')
unittest(do_external_sandhi('anye ca bahavaH zUrAH madarthe tyaktajIvitAH'), 'anye ca bahavaH zUrA madarthe tyaktajIvitAH', 'Line 9,1 failed')
unittest(do_external_sandhi('nAnAzastrapraharaNAH sarve yuddhavizAradAH'), 'nAnAzastrapraharaNAH sarve yuddhavizAradAH', 'Line 9,2 failed')
unittest(do_external_sandhi('aparyAptam tat asmAkam balam bhISmAbhirakSitam'), 'aparyAptaM tad asmAkaM balaM bhISmAbhirakSitam', 'Line 10, 1 failed')
unittest(do_external_sandhi('paryAptam tu idam eteSAm balam bhImAbhirakSitam'), 'paryAptaM tv idam eteSAM balaM bhImAbhirakSitam', 'Line 10, 2 failed')
unittest(do_external_sandhi('ayaneSu ca sarveSu yathAbhAgam avasthitAH'), 'ayaneSu ca sarveSu yathAbhAgam avasthitAH', 'Line 11, 1 failed')
unittest(do_external_sandhi('bhISmam eva abhirakSantu bhavantaH sarve eva hi'), 'bhISmam evAbhirakSantu bhavantaH sarva eva hi', 'Line 11, 2 failed')
unittest(do_external_sandhi('tasya saMjanayan harSam kuruvRddhaH pitAmahaH'), 'tasya saMjanayan harSaM kuruvRddhaH pitAmahaH', 'Line 12, 1 failed')
unittest(do_external_sandhi('siMhanAdam vinadya ucchaiH zaGkham dadhmau pratApavAn'), 'siMhanAdaM vinadyocchaiH zaGkhaM dadhmau pratApavAn', 'Line 12, 2 failed')
unittest(do_external_sandhi('tataH zaGkhAH ca bheryAH ca paNavAnakagomukhAH'), 'tataH zaGkhAz ca bheryAz ca paNavAnakagomukhAH', 'Line 13, 1 failed')
unittest(do_external_sandhi('sahasA eva abhyahanyanta sa zabdaH tumulaH abhavat'), 'sahasaivAbhyahanyanta sa zabdas tumulo \'bhavat', 'Line 13, 2 failed')
unittest(do_external_sandhi('tataH zvetaiH hayaiH yukte mahati syandane sthitau'), 'tataH zvetair hayair yukte mahati syandane sthitau', 'Line 14, 1 failed')
unittest(do_external_sandhi('mAdhavaH pANDavaH ca eva divyau zaGkhau pradadhmatuH'), 'mAdhavaH pANDavaz caiva divyau zaGkhau pradadhmatuH', 'Line 14, 2 failed')
unittest(do_external_sandhi('pAJcajanyam hRSIkezaH devadattam dhanaMjayah'), 'pAJcajanyaM hRSIkezo devadattaM dhanaMjayah', 'Line 15, 1 failed')
unittest(do_external_sandhi('pauNDram dadhmau mahAzaGkham bhImakarmA vRkodaraH'), 'pauNDraM dadhmau mahAzaGkhaM bhImakarmA vRkodaraH', 'Line 15, 2 failed')
unittest(do_external_sandhi('anantavijayam rAjA kuntiputraH yudhiSThiraH'), 'anantavijayaM rAjA kuntiputro yudhiSThiraH', 'Line 16, 1 failed')
unittest(do_external_sandhi('nakulaH sahadevaH ca sughoSamaNipuSpakau'), 'nakulaH sahadevaz ca sughoSamaNipuSpakau', 'Line 16,2 failed')
unittest(do_external_sandhi('kAzyaH ca parameSvAsaH zikhaNDI ca mahArathaH'), 'kAzyaz ca parameSvAsaH zikhaNDI ca mahArathaH', 'Line 17,1 failed')
unittest(do_external_sandhi('dhRSTadyumnaH virATaH ca sAtyakiH ca aparAjitaH'), 'dhRSTadyumno virATaz ca sAtyakiz cAparAjitaH', 'Line 17,2 failed')
unittest(do_external_sandhi('drupadaH draupadeyAH ca sarvazaH pRthivIpate'), 'drupado draupadeyAz ca sarvazaH pRthivIpate', 'Line 18,1 failed')
unittest(do_external_sandhi('saubhadraH ca mahAbAhuH zaGkhAn dadhmuH pRthak pRthak'), 'saubhadraz ca mahAbAhuH zaGkhAn dadhmuH pRthak pRthak', 'Line 18,2 failed')
unittest(do_external_sandhi('sa ghoSaH dhArtarASTrANAm hRdayani vyadArayat'), 'sa ghoSo dhArtarASTrANAM hRdayani vyadArayat', 'Line 19,1 failed')
unittest(do_external_sandhi('nabhaH ca pRthivim ca eva tumulaH vyanunAdayan'), 'nabhaz ca pRthiviM caiva tumulo vyanunAdayan', 'Line 19,2 failed')
unittest(do_external_sandhi('atha vyavasthitAn dRSTvA dhArtarASTrAn kapidhvajaH'), 'atha vyavasthitAn dRSTvA dhArtarASTrAn kapidhvajaH', 'Line 20,1 failed')
unittest(do_external_sandhi('pravRtte zastrasaMpAte dhanuH udyamya pANDavaH'), 'pravRtte zastrasaMpAte dhanur udyamya pANDavaH', 'Line 20,2 failed')
unittest(do_external_sandhi('hRSIkezam tadA vAkyam idam Aha mahIpate'), 'hRSIkezaM tadA vAkyam idam Aha mahIpate', 'Line 21,1 failed')
unittest(do_external_sandhi('senayoH ubhayoH madhye ratham sthApaya me acyuta'), 'senayor ubhayor madhye rathaM sthApaya me \'cyuta', 'Line 21,2 failed')
unittest(do_external_sandhi('yAvat etAn nirIkSe aham yoddhukAmAn avasthitAn'), 'yAvad etAn nirIkSe \'haM yoddhukAmAn avasthitAn', 'Line 22,1 failed')
unittest(do_external_sandhi('kaiH mayA saha yoddhavyam asmin raNasamudyame'), 'kair mayA saha yoddhavyam asmin raNasamudyame', 'Line 22,2 failed')
unittest(do_external_sandhi('yotsyamAnAn avekSe aham ye ete atra samAgatAH'), 'yotsyamAnAn avekSe \'haM ya ete \'tra samAgatAH', 'Line 23,1 failed')
unittest(do_external_sandhi('dhArtarASTrasya durbuddheH yuddhe priyacikIrSavaH'), 'dhArtarASTrasya durbuddher yuddhe priyacikIrSavaH', 'Line 23,2 failed')
unittest(do_external_sandhi('evam uktaH hRSIkezaH guDAkezena bhArata'), 'evam ukto hRSIkezo guDAkezena bhArata', 'Line 24,1 failed')
unittest(do_external_sandhi('senayoH ubhayoH madhye sthApayitvA rathottamam'), 'senayor ubhayor madhye sthApayitvA rathottamam', 'Line 24,2 failed')
unittest(do_external_sandhi('bhISmadroNapramukhataH sarveSAm ca mahIkSitAm'), 'bhISmadroNapramukhataH sarveSAM ca mahIkSitAm', 'Line 25,1 failed')
unittest(do_external_sandhi('uvAca pArtha pazya etAn samavetAn kurUn iti'), 'uvAca pArtha pazyaitAn samavetAn kurUn iti', 'Line 25,2 failed')
unittest(do_external_sandhi('tatra apazyat sthitAn pArthaH pitRRn atha pitAmahAH'), 'tatrApazyat sthitAn pArthaH pitRRn atha pitAmahAH', 'Line 26,1 failed')
unittest(do_external_sandhi('AcAryAn mAtulAn bhrAtRRn putrAn pautrAn sakhIn tathA'), 'AcAryAn mAtulAn bhrAtRRn putrAn pautrAn sakhIMs tathA', 'Line 26,2 failed')
unittest(do_external_sandhi('zvazurAn suhRdaH ca eva senayoH ubhayoH api'), 'zvazurAn suhRdaz caiva senayor ubhayor api', 'Line 27,1 failed')
unittest(do_external_sandhi('tAn samIkSya sa kaunteyaH sarvAn bandhUn avasthitAn'), 'tAn samIkSya sa kaunteyaH sarvAn bandhUn avasthitAn', 'Line 27,2 failed')
unittest(do_external_sandhi('kRpayA parayA AviSTaH viSIdan idam abravIt'), 'kRpayA parayAviSTo viSIdann idam abravIt', 'Line 28,1 failed')
unittest(do_external_sandhi('dRSTvA imAn svajanAn kRSNa yuyutsUn samavasthitAn'), 'dRSTvemAn svajanAn kRSNa yuyutsUn samavasthitAn', 'Line 28,2 failed')
unittest(do_external_sandhi('sIdanti mama gAtrANi mukham ca parizuSyati'), 'sIdanti mama gAtrANi mukhaM ca parizuSyati', 'Line 29,1 failed')
unittest(do_external_sandhi('vepathuH ca zarIre me romaharSaH ca jAyate'), 'vepathuz ca zarIre me romaharSaz ca jAyate', 'Line 29,2 failed')
unittest(do_external_sandhi('gANDIvam sraMsate hastAt tvak ca eva paridahyate'), 'gANDIvaM sraMsate hastAt tvak caiva paridahyate', 'Line 30,1 failed')
unittest(do_external_sandhi('na ca zaknomi avasthAtum bhramati iva ca me manas'), 'na ca zaknomy avasthAtuM bhramatIva ca me manaH', 'Line 30,2 failed')
unittest(do_external_sandhi('nimittAni ca pazyAmi viparItAni kezava'), 'nimittAni ca pazyAmi viparItAni kezava', 'Line 31,1 failed')
unittest(do_external_sandhi('na ca zreyaH anupazyAmi hatvA svajanam Ahave'), 'na ca zreyo \'nupazyAmi hatvA svajanam Ahave', 'Line 31,2 failed')
unittest(do_external_sandhi('na kAGkSe vijayam kRSNa na ca rAjyam sukhAni ca'), 'na kAGkSe vijayaM kRSNa na ca rAjyaM sukhAni ca', 'Line 32,1 failed')
unittest(do_external_sandhi('kim naH rAjyena govinda kim bhogaiH jIvitena vA'), 'kiM no rAjyena govinda kiM bhogair jIvitena vA', 'Line 32,2 failed')
unittest(do_external_sandhi('yeSAm arthe kAGkSitam naH rAjyam bhogAH sukhAni ca'), 'yeSAm arthe kAGkSitaM no rAjyaM bhogAH sukhAni ca', 'Line 33,1 failed')
unittest(do_external_sandhi('te ime avasthitAH yuddhe prANAn tyaktvA dhanAni ca'), 'ta ime \'vasthitA yuddhe prANAMs tyaktvA dhanAni ca', 'Line 33,2 failed')
unittest(do_external_sandhi('AcAryAn pitaraH putrAH tathA eva ca pitAmahAH'), 'AcAryAn pitaraH putrAs tathaiva ca pitAmahAH', 'Line 34,1 failed')
unittest(do_external_sandhi('mAtulAH zvazurAH pautrAH syAlAH saMbandhinaH tathA'), 'mAtulAH zvazurAH pautrAH syAlAH saMbandhinas tathA', 'Line 34,2 failed')
unittest(do_external_sandhi('etAn na hantum icchAmi ghnataH api madhusUdana'), 'etAn na hantum icchAmi ghnato \'pi madhusUdana', 'Line 35,1 failed')
unittest(do_external_sandhi('api trailokyarAjyasya hetoH kim nu mahIkRte'), 'api trailokyarAjyasya hetoH kiM nu mahIkRte', 'Line 35,2 failed')
unittest(do_external_sandhi('nihatya dhArtarASTrAn naH kA prItiH syAt janArdana'), 'nihatya dhArtarASTrAn naH kA prItiH syAj janArdana', 'Line 36,1 failed')
unittest(do_external_sandhi('pApam eva azrayet asmAn hatvA etAn AtatAyinaH'), 'pApam evAzrayed asmAn hatvaitAn AtatAyinaH', 'Line 36,2 failed')
unittest(do_external_sandhi('tasmAt na arhAH vayam hantum dhArtarASTrAn sabandhavAn'), 'tasmAn nArhA vayaM hantuM dhArtarASTrAn sabandhavAn', 'Line 37,1 failed')
unittest(do_external_sandhi('svajanam hi katham hatvA sukhinaH syAma mAdhava'), 'svajanaM hi kathaM hatvA sukhinaH syAma mAdhava', 'Line 37,2 failed')
unittest(do_external_sandhi('yadi api ete na pazyanti lobhopahatacetasaH'), 'yady apy ete na pazyanti lobhopahatacetasaH', 'Line 38,1 failed')
unittest(do_external_sandhi('kulakSayakRtam doSam mitradrohe ca pAtakam'), 'kulakSayakRtaM doSaM mitradrohe ca pAtakam', 'Line 38,2 failed')
unittest(do_external_sandhi('katham na jJeyam asmAbhiH pApAt asmAn nivartitum'), 'kathaM na jJeyam asmAbhiH pApAd asmAn nivartitum', 'Line 39,1 failed')
unittest(do_external_sandhi('kulakSayakRtam doSam prapazyadbhiH janArdana'), 'kulakSayakRtaM doSaM prapazyadbhir janArdana', 'Line 39,2 failed')
unittest(do_external_sandhi('kulakSaye praNazyanti kuladharmAH sanAtanAH'), 'kulakSaye praNazyanti kuladharmAH sanAtanAH', 'Line 40,1 failed')
unittest(do_external_sandhi('dharme naSTe kulam kRtsnam adharmaH abhibhavati uta'), 'dharme naSTe kulaM kRtsnam adharmo \'bhibhavaty uta', 'Line 40,2 failed')
unittest(do_external_sandhi('adharmAbhibhavAt kRSNa praduSyanti kulastriyaH'), 'adharmAbhibhavAt kRSNa praduSyanti kulastriyaH', 'Line 41,1 failed')
unittest(do_external_sandhi('strISu duSTAsu vARSNeya jAyate varNasaMkaraH'), 'strISu duSTAsu vARSNeya jAyate varNasaMkaraH', 'Line 41,2 failed')
unittest(do_external_sandhi('saMkaraH narakAya eva kulaghnAnAm kulasya ca'), 'saMkaro narakAyaiva kulaghnAnAM kulasya ca', 'Line 42,1 failed')
unittest(do_external_sandhi('patanti pitaraH hi eSAm luptapiNDodakakriyAH'), 'patanti pitaro hy eSAM luptapiNDodakakriyAH', 'Line 42,2 failed')
unittest(do_external_sandhi('doSaiH etaiH kulaghAnAm varNasaMkarakArakaiH'), 'doSair etaiH kulaghAnAM varNasaMkarakArakaiH', 'Line 43,1 failed')
unittest(do_external_sandhi('utsAdyante jAtidharmAH kuladharmAH ca zAzvatAH'), 'utsAdyante jAtidharmAH kuladharmAz ca zAzvatAH', 'Line 43,2 failed')
unittest(do_external_sandhi('utsannakuladharmAnAm manuSyANAm janArdana'), 'utsannakuladharmAnAM manuSyANAM janArdana', 'Line 44,1 failed')
unittest(do_external_sandhi('narake niyatam vasaH bhavati iti anuzuzruma'), 'narake niyataM vaso bhavatIty anuzuzruma', 'Line 44,2 failed')
unittest(do_external_sandhi('aho bata mahat pApam kartum vyavasitAH vayam'), 'aho bata mahat pApaM kartuM vyavasitA vayam', 'Line 45,1 failed')
unittest(do_external_sandhi('yat rAjyasukhalobhena hantum svajanam udyatAH'), 'yad rAjyasukhalobhena hantuM svajanam udyatAH', 'Line 45,2 failed')
unittest(do_external_sandhi('yadi mAm apratikAram azastram zastrapANayaH'), 'yadi mAm apratikAram azastraM zastrapANayaH', 'Line 46,1 failed')
unittest(do_external_sandhi('dhArtarASTrAH raNe hanyuH tat me kSemataram bhavet'), 'dhArtarASTrA raNe hanyus tan me kSemataraM bhavet', 'Line 46,2 failed')
unittest(do_external_sandhi('evam uktvA arjunaH saMkhye rathopasthe upAvizat'), 'evam uktvArjunaH saMkhye rathopastha upAvizat', 'Line 47,1 failed')
unittest(do_external_sandhi('visRjya sazaram cApam zokasaMvignamAnasaH'), 'visRjya sazaraM cApaM zokasaMvignamAnasaH', 'Line 47,2 failed')
unittest(do_external_sandhi('tam tathA kRpayA AviSTam azrupUrNAkulekSaNam'), 'taM tathA kRpayAviSTam azrupUrNAkulekSaNam', 'Line 48,1 failed')
unittest(do_external_sandhi('viSIdantam idam vAkyam uvAca madhusUdanaH'), 'viSIdantam idaM vAkyam uvAca madhusUdanaH', 'Line 48,2 failed')
unittest(do_external_sandhi('kutaH tvA kazmalam idam viSame samupasthitam'), 'kutas tvA kazmalam idaM viSame samupasthitam', 'Line 49,1 failed')
unittest(do_external_sandhi('anAryajuSTam asvargyam akIrtikaram arjuna'), 'anAryajuSTam asvargyam akIrtikaram arjuna', 'Line 49,2 failed')
unittest(do_external_sandhi('klaibyam mA sma gamaH pArtha na etat tvayi upapadyate'), 'klaibyaM mA sma gamaH pArtha naitat tvayy upapadyate', 'Line 50,1 failed')
unittest(do_external_sandhi('kSudram hRdayadaurbalyam tyaktvA uttiSTha paraMtapa'), 'kSudraM hRdayadaurbalyaM tyaktvottiSTha paraMtapa', 'Line 50,2 failed')

#Below are unit tests for pairs of words for each rule.

#Prazlista:

RULE = Prazlista()
assert RULE.applies_to('ta at'), 'Prazlista applies_to ta at failed'
unittest(do_external_sandhi('ta at'), 'tAt', 'Prazlista apply ta at failed')
assert RULE.applies_to('tA at'), 'Prazlista applies_to tA at failed'
unittest(do_external_sandhi('tA at'), 'tAt', 'Prazlista apply tA at failed')
assert RULE.applies_to('ta At'), 'Prazlista applies_to ta At failed'
unittest(do_external_sandhi('ta At'), 'tAt', 'Prazlista apply ta At failed')
assert RULE.applies_to('tA At'), 'Prazlista applies_to tA At failed'
unittest(do_external_sandhi('tA At'), 'tAt', 'Prazlista apply tA At failed')
assert RULE.applies_to('ti it'), 'Prazlista applies_to ti it failed'
unittest(do_external_sandhi('ti it'), 'tIt', 'Prazlista apply ti it failed')
assert RULE.applies_to('tI it'), 'Prazlista applies_to tI it failed'
unittest(do_external_sandhi('tI it'), 'tIt', 'Prazlista apply tI it failed')
assert RULE.applies_to('ti It'), 'Prazlista applies_to ti It failed'
unittest(do_external_sandhi('ti It'), 'tIt', 'Prazlista apply ti it failed')
assert RULE.applies_to('tI It'), 'Prazlista applies_to tI It failed'
unittest(do_external_sandhi('tI It'), 'tIt', 'Prazlista apply tI It failed')
assert RULE.applies_to('tu ut'), 'Prazlista applies_to tu ut failed'
unittest(do_external_sandhi('tu ut'), 'tUt', 'Prazlista apply tu ut failed')
assert RULE.applies_to('tU ut'), 'Prazlista applies_to tU ut failed'
unittest(do_external_sandhi('tU ut'), 'tUt', 'Prazlista apply tU ut failed')
assert RULE.applies_to('tu Ut'), 'Prazlista applies_to tu Ut failed'
unittest(do_external_sandhi('tu Ut'), 'tUt', 'Prazlista apply tu Ut failed')
assert RULE.applies_to('tU Ut'), 'Prazlista applies_to tU Ut failed'
unittest(do_external_sandhi('tU Ut'), 'tUt', 'Prazlista apply tU Ut failed')
assert not RULE.applies_to('ta it'), 'Prazlista applies_to ta it failed'
assert not RULE.applies_to('ta ut'), 'Prazlista applies_to ta ut failed'
assert not RULE.applies_to('tu it'), 'Prazlista applies_to tu it failed'
assert not RULE.applies_to('tu at'), 'Prazlista applies_to tu at failed'
assert not RULE.applies_to('ti at'), 'Prazlista applies_to ti at failed'
assert not RULE.applies_to('ti ut'), 'Prazlista applies_to ti ut failed'
assert not RULE.applies_to('t at'), 'Prazlista applies_to t it failed'
assert not RULE.applies_to('ta t'), 'Prazlista applies_to ta t failed'

RULE = Gliding()
assert RULE.applies_to('ti at'), 'Gliding applies_to ti at failed'
unittest(do_external_sandhi('ti at'), 'ty at', 'Gliding apply ti at failed')
assert RULE.applies_to('tI at'), 'Gliding applies_to tI at failed'
unittest(do_external_sandhi('tI at'), 'ty at', 'Gliding apply tI at failed')
assert RULE.applies_to('tu at'), 'Gliding applies_to tu at failed'
unittest(do_external_sandhi('tu at'), 'tv at', 'Gliding apply tu at failed')
assert RULE.applies_to('tU at'), 'Gliding applies_to ti at failed'
unittest(do_external_sandhi('tU at'), 'tv at', 'Gliding apply tU at failed')
assert RULE.applies_to('tR at'), 'Gliding applies_to tR at failed'
unittest(do_external_sandhi('tR at'), 'tr at', 'Gliding apply tR at failed')
assert not RULE.applies_to('ta at'), 'Gliding applies_to ta at failed'
assert not RULE.applies_to('ti it'), 'Gliding applies_to ta at failed'
assert not RULE.applies_to('tI It'), 'Gliding applies_to ta at failed'

RULE = NucleusTensing()
assert RULE.applies_to('t@ at'), 'NucleusTensing applies_to tai at failed'
unittest(do_external_sandhi('t@ at'), 'tA at', 'NucleusTensing apply tai at failed')
assert not RULE.applies_to('t at'), 'NucleusTensing applies_to t at failed'
assert not RULE.applies_to('t@ t'), 'NucleusTensing applies_to tai t failed'

RULE = LongMidMonophthongs()
assert RULE.applies_to('te at'), 'LongMidMonophthongs applies_to te at failed'
unittest(do_external_sandhi('te at'), 'te \'t', 'LongMidMonophthongs apply te at failed')
assert RULE.applies_to('to at'), 'LongMidMonophthongs applies_to to at failed'
unittest(do_external_sandhi('to at'), 'to \'t', 'LongMidMonophthongs apply to at failed')
assert RULE.applies_to('te At'), 'LongMidMonophthongs applies_to te At failed'
unittest(do_external_sandhi('te At'), 'ta At', 'LongMidMonophthongs apply te At failed')
assert RULE.applies_to('to At'), 'LongMidMonophthongs applies_to to At failed'
unittest(do_external_sandhi('to At'), 'ta At', 'LongMidMonophthongs apply te at failed')
assert not RULE.applies_to('t@ at'), 'LongMidMonophthongs applies_to tai at failed'
assert not RULE.applies_to('t$ at'), 'LongMidMonophthongs applies_to tau at failed'
assert not RULE.applies_to('t at'), 'LongMidMonophthongs applies_to t at failed'
assert not RULE.applies_to('te t'), 'LongMidMonophthongs applies_to tai at failed'

#...

