# FATAL-04a — Voice 1 triolett ja Voice 2 poolnoot, vale definitsioon

## Katse eesmärk

Kontrollida, mida Finale 27.4.1 ekspordib, kui takti 2 teises pooles
on Voice 1-s kolm veerandnooti 3:2 triolettina ja nendega samal ajal
Voice 2-s tavaline poolnoot, kuid trioleti definitsioonis on määratud
**3 poolnooti 2 poolnoodi ajas**.

Suhe on mõlemal juhul 3:2, ent definitsiooni noodiväärtus erineb
tegelikult sisestatud nootidest. Paariskatse FATAL-04b kasutab sama
noodimaterjali ja Voice 2 poolnooti, aga õiget trioleti definitsiooni.
Nii saab eristada valest definitsioonist tuleneva mõju kahe hääle
koosesinemisest. Nimetuses `FATAL` on seerianumber; raskusaste on ootel.

## Finale'is tegemine

1. Tee `BASE/FMD-BASE.musx`-ist koopia `FATAL-04a/FATAL-04a.musx`.
2. Sisesta ainult takti 2 Voice 1-sse C4 poolnoot takti algusse ning
   teise poolde kolm G4 veerandnooti tavalise 3:2 trioletina.
3. Käivita Voice 2 trioleti esimese G4 noodi juurest (kolmas löök)
   ja sisesta sinna tavaline E4 poolnoot. Ära tee Voice 2-s trioletti.
4. Ava Voice 1 trioleti `Tuplet Definition` ning muuda mõlemad
   noodiväärtuse valikud `Quarter(s)` väärtuselt `Half(s)` väärtusele.
   Numbrid jäävad **3** ja **2**. Ära muuda sisestatud kolme G4 noodi
   väärtust, Voice 2 E4 poolnooti ega lisa pause.
5. Salvesta `FATAL-04a.musx`, ekspordi pakkimata
   `FATAL-04a.musicxml` ja impordi see Doricosse.

Finale'is saab juba loodud trioleti definitsiooni avada Tuplet Tooliga:
klõpsa trioleti esimest nooti ning ava selle pide topeltklõpsuga
definitsioon. Kui Finale pärast muudatust taktisisu ümber korraldab,
jäta tulemus muutmata ja kirjelda seda koos ekspordiga.
Ära kasuta `Edit Frame` ruute ega `Fill with Rests` käsku.

## XML-is kontrollitav

- Voice 1 C4 poolnoodi ja kolme G4 noodi ning Voice 2 E4 poolnoodi
  tegelikud `duration`-kestused ja algushetked;
- aktiivne `divisions` ning mõlema hääle ajajoone ulatus 4/4 suhtes;
- G4 nootide `<type>`, `time-modification` ja võimalik `normal-type`;
- trioleti start/stop ja võimalikud `tuplet-actual` / `tuplet-normal`
  noodiväärtused;
- häälte vaheline `backup` ning võrdlus FATAL-04b XML-iga;
- taktid 1, 3 ja 4 võrreldes BASE-failiga.

Kui XML normaliseerib selle tavaliseks korrektseks veerandnooditrioletiks,
ei ole failis tuvastatavat definitsiooniviga. Kui tegelik ajajoon muutub,
liigitame tulemuse ekspordi ja Dorico testi põhjal.

## Dorico tulemus

Ootel.

## Allikad

- [Finale for Mac: Tuplet Definition](https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/TPDLG.htm)
- [Finale for Mac: Multiple voices](https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/Multiple_voices.htm)
- [MusicXML 4.0: time-modification](https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/time-modification/)
- [MusicXML 4.0: tuplet](https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/tuplet/)
