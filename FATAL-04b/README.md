# FATAL-04b — Voice 1 triolett ja samaaegne Voice 2 poolnoot

## Katse eesmärk

Kontrollida, kas takti 2 teises pooles Voice 1-s olev korrektne
veerandnooditriolett koos samal ajal Voice 2-s oleva tavalise poolnoodiga
impordib Doricosse korrektselt. See on FATAL-04a kontrollkatse: ainus
plaanitud erinevus on trioleti definitsiooni noodiväärtus.

`FATAL` on testiseeria tunnus; see kontrollfail impordib korrektselt.

## Finale'is tegemine

1. Tee `FATAL-04a/FATAL-04a.musx`-ist koopia
   `FATAL-04b/FATAL-04b.musx`. Mõlemad katsed lähtuvad BASE-failist.
2. Ava Voice 1 trioleti `Tuplet Definition` ning sea mõlemad
   noodiväärtuse valikud `Quarter(s)` väärtusele: **3 veerandnooti
   2 veerandnoodi ajas**. Jäta kõik noodid, hääled ja nende asukohad
   muutmata.
3. Salvesta `FATAL-04b.musx`, ekspordi pakkimata
   `FATAL-04b.musicxml` ja impordi see Doricosse.

Ära kasuta `Edit Frame` ruute ega `Fill with Rests` käsku. Kui Finale
paigutab Voice 2 poolnoodi teise ajakohta või muudab Voice 1 noote,
kirjelda tegelikku tulemust; ära paranda seda märkamatult ümber.

## XML-is kontrollitav

- Voice 1 C4 poolnoot ja kolm G4 triolettveerandnooti katavad 4/4 takti;
- Voice 2 E4 poolnoot algab kolmandal löögil ja kestab kaks lööki;
- trioleti start/stop ja 3:2 `time-modification` on Voice 1 nootidel;
- `backup` eristab hääli ning taktid 1, 3 ja 4 vastavad BASE-failile;
- FATAL-04a XML-iga võrdlemisel peab noodimaterjal ja häälte asetus
  jääma samaks, kui Finale seda lubab.

## Dorico tulemus

Dorico 6.2.30 import õnnestus. Kasutaja sõnul lisab Dorico takti
algusse downstem voice'i pausi; see on Voice 2 hilisema alguse
ootuspärane esitus, mitte viga. 04a-s nähtud löökide lisandumist
ega peidetud taktimõõtu ei täheldatud.

## XML-i tulemus

- `divisions` on 6 ja 4/4 takti kestus 24 division'it;
- Voice 1 C4 poolnoot kestab 12 ning kolm G4 triolettveerandnooti
  kestavad 4 + 4 + 4; ajajoon lõpeb 24 juures;
- Voice 2 E4 poolnoot algab offset'il 12 ja lõpeb 24 juures;
- kõigil kolmel G4 noodil on 3:2 `time-modification`, kuid puudub
  `normal-type`; see sobib nende `quarter`-noodiväärtusega;
- XML erineb FATAL-04a-st täpselt kolme
  `<normal-type>half</normal-type>` elemendi puudumise poolest;
- taktid 1, 3 ja 4 vastavad BASE-failile pärast `divisions`-ühikute
  ühtlustamist;
- validaator ei anna leide.

Järeldus: Voice 1 korrektne veerandnooditriolett ja sellega samaaegne
Voice 2 poolnoot ei põhjusta Doricos viga. Voice 2 alguspausi ei tohi
liigitada lisatud löögiks.

## Allikad

- [Finale for Mac: Multiple voices](https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/Multiple_voices.htm)
- [Finale for Mac: Tuplet Definition](https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/TPDLG.htm)
