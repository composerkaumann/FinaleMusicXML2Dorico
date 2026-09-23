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
koosesinemisest. Nimetuses `FATAL` on seerianumber; tegelik raskusaste
on **warning**, mitte fatal.

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

## XML-i tulemus

- XML on süntaktiliselt korrektne; `divisions` on 6 ja 4/4 takti
  deklareeritud kestus 24 division'it.
- Voice 1: C4 poolnoot kestusega 12, siis kolm G4 veerandnooti
  kestustega 4 + 4 + 4. Seega lõpeb XML-i ajajoon täpselt 24 juures.
- Voice 2: E4 poolnoot algab kolmandal löögil (offset 12) ja lõpeb
  samuti 24 juures. Häälte vahel on `backup`-elemendid.
- Kõigil kolmel G4 noodil on `time-modification` 3:2 ja
  `normal-type` = `half`; `type` jääb `quarter`-iks. Nende tegelikud
  kestused katavad kaks lööki, kuid poolnooditrioleti definitsioon
  kirjeldab neljalöögilist vahemikku. See on tupletigrupi sisuline
  vastuolu, mitte üle- või alatäidetud MusicXML-i ajajoon.
- XML-is puudub taktis 2 taktimõõdumuutus. Taktid 1, 3 ja 4 vastavad
  BASE-failile pärast `divisions`-ühikute ühtlustamist.
- Validaatori `FMD005` annab ühe `warning`-leiu: tupletigrupi
  määratletud ulatus on 24 division'it, gruppi kuuluvad noodid
  katavad 12 division'it.

FATAL-04b kontrollfail erineb XML-is ainult kolme `normal-type`
`half`-elemendi puudumise poolest. Sellega on eraldatud vale
trioletidefinitsiooni mõju Voice 2 poolnoodi olemasolust.

## Dorico tulemus

Dorico 6.2.30 import õnnestus, kuid kasutaja sõnul lisandus takti 2
lööke koos peidetud taktimõõduga. Ekraanipildil on näha lisatud pause
ja taktimõõdu signpost; taktid 3 ja 4 on olemas.

Järeldus: **warning** — import ei katke, kuid takt 2 muutub. Dorico
täpset lisatud löökide arvu ekraanipildi põhjal ei fikseerita.

Tõendus: `FATAL-04aDorico.png`. Lähte-`musx` salvestati pärast
`musicxml`-eksporti; seetõttu ei kinnita failide ajatemplid nende
täielikku olekuühtsust. Analüüsi alus on eksporditud XML.

## Allikad

- [Finale for Mac: Tuplet Definition](https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/TPDLG.htm)
- [Finale for Mac: Multiple voices](https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/Multiple_voices.htm)
- [MusicXML 4.0: time-modification](https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/time-modification/)
- [MusicXML 4.0: tuplet](https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/tuplet/)
