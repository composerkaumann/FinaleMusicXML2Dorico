# FATAL-04 — terve triolett Finale Voice 2-s

## Katse eesmärk

Kontrollida, kas Finale 27.4.1-st eksporditud täielik Voice 2 triolett
impordib Dorico 6.2.30-sse korrektselt. FATAL-03-s viidi Voice 2-sse
üksnes trioleti viimane noot ning eksport kaotas trioleti seose selle
noodiga. Siin luuakse kogu triolett algusest peale Voice 2-s.

`FATAL-04` on testiseeria tunnus. Juhtumi raskusaste selgub alles XML-i
ja Dorico tulemuse põhjal.

## Finale'is tegemine

1. Tee `BASE/FMD-BASE.musx`-ist koopia `FATAL-04/FATAL-04.musx`.
2. Sisesta ainult takti 2 Voice 1-sse neli C4 veerandnooti.
3. Vali Speedy Entry ja liigu esimese Voice 1 C4 noodi juurde.
   Vajuta apostroofi (`'`), et alustada selle noodi juurest Voice 2.
   Kontrolli, et Speedy Entry näitab `V2`.
4. Sea sisestuskursor G4 kõrgusele. Vajuta `Option+3` ja sisesta Voice 2-sse
   kolm G4 veerandnooti 3:2 trioletina. Lisa samas Voice 2-s nende järele
   üks G4 poolnoot. Nii on ka Voice 2 kogupikkus neli lööki.
5. Salvesta ning ekspordi `FATAL-04/FATAL-04.musicxml` pakkimata kujul.
   Seejärel impordi fail Doricosse ja kirjelda, kas taktid 2–4 ja mõlemad
   hääled on alles.

Ära kasuta `Edit Frame` ruute, kihte ega `Fill with Rests` käsku. Katse
sisaldab ainult takti 2 tavapäraselt sisestatud kahte häält.

## XML-is kontrollitav

- taktis 2 on kaks eri `<voice>` väärtust;
- Voice 1 sisaldab nelja C4 veerandnooti;
- Voice 2 sisaldab kolme G4 3:2 triolettveerandnooti ja G4 poolnooti;
- trioleti start ja stop kuuluvad mõlemad Voice 2 nootidele;
- kummagi hääle ajajoon täidab 4/4 takti eraldi;
- taktid 1, 3 ja 4 vastavad BASE-failile pärast `divisions` normaliseerimist.

Kui Finale eksport erineb sellest, kirjeldame tegelikku XML-i enne
juhtumi klassifitseerimist.

## Dorico tulemus

Ootel.

## Allikad

- [Finale for Mac: Multiple voices](https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/Multiple_voices.htm)
- [Finale for Mac: Tuplets](https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/Tuplets.htm)
