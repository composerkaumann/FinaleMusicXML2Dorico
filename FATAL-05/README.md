# FATAL-05 — cross-staff triolett kahe eraldi partiiga ekspordis

## Katse ja Dorico tulemus

Kasutaja tegi Finale'is cross-staff trioleti ning importis ekspordi
Dorico 6.2.31-sse. Kasutaja sõnul ei tekkinud impordiviga: kõik noodid
säilisid lähtereal ja cross-staff-paigutus kadus.

Juhtum ei ole fatal. Paigutuse kadumine on eraldi tähelepanek, mille
põhjal ei saa kinnitada, et Dorico eiraks korrektselt kodeeritud
cross-staff-andmeid.

Failid on kasutaja antud nimedega `FMD-05.musx` ja `FMD-05.musicxml`.
Võrdlusfail on `BASE/FMD-BASE-2STAFF.musicxml`.

## Tegelik XML

- MusicXML 4.0 partwise; kaks eraldi partiid P1 ja P2, mõlemas neli
  takti. See erineb plaanitud ühe instrumendi mitme rea struktuurist.
- P1 kasutab `divisions=6` ning P2 `divisions=2`; mõlema taktimõõt
  on 4/4.
- P1 taktis 2 on kolm veerandnooti G4–C4–G4. Kõigil on hääl 1,
  3:2 `time-modification` ja kestus 4 division'it. Trioleti algus
  ning lõpp on sama hääle nootidel.
- P1 takti 2 tegelik ulatus on 12/24 division'it ehk kaks lööki.
  Kavandatud lõpu C4 poolnooti ega seda asendavat pausi XML-is pole.
  Puudumise põhjust selle ekspordi põhjal ei tuvastata.
- P2 sisaldab kõigis taktides täistaktipause, taktis 2 kestusega
  8 division'it ehk neli lööki.
- Üheski noodis pole `staff`-elementi ja partiides pole
  `staves`-elementi. Kõik triolettnoodid kuuluvad XML-is P1-le.
  Keskmise C4 noodivarre `default-y=-75` on paigutuskoordinaat,
  mitte teisele noodireale määramine.
- P1 taktid 1, 3 ja 4 vastavad võrdlusfailile pärast kestuste
  normaliseerimist; P2 noodimaterjal on võrdlusfailiga sama.

MusicXML määrab noodirea elemendiga `staff` ning ühe partii ridade
arvu elemendiga `staves`. Nende puudumisel käsitletakse partiid
ühe noodireana. Seega ei sisalda see eksport keskmise C4 teisele
reale suunamist.

## Validaatori teadaolev valepositiivne leid

Praegune `FMD003` annab P1 taktis 2 `fatal`-leiu, sest trioletti
sisaldav takt lõpeb 12 juures oodatud 24 asemel. Kasutaja Dorico
6.2.31 test seda raskusastet ei kinnita: noodikadu ega katkenud
importi ei teatatud.

See juhtum on vastunäide üldistusele, et iga trioletti sisaldav
alatäidetud takt põhjustab fataalse impordi. `FMD003` vajab edasist
kitsendamist ning Dorico versioonide erinevuse kontrolli.
Seniste FATAL-02 ja FATAL-03 tulemused Dorico 6.2.30 kohta jäävad
omaette vaatlusteks.

Selle katse tõttu ei lisata uut cross-staff fatal-reeglit.
Validaatori käitumist selles kirjes ei muudeta; vastuolu on
masinloetavalt märgitud metadata failis.

## Tõendite piirid

Dorico tulemus põhineb kasutaja kirjeldusel; ekraanipilti ei ole.
Lähtefail salvestati kaks sekundit pärast XML-eksporti, mistõttu
täielikku lähtefaili ja ekspordi olekuühtsust ei kinnitata.
Analüüsi alus on salvestatud MusicXML.

## Allikad

- [MusicXML 4.0: staff](https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/staff/)
- [MusicXML 4.0: staves](https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/staves/)
