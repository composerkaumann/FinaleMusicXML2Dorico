# FATAL-02 — tuplet timeline mismatch

## Eesmärk

Kontrollida olukorda, kus trioleti 3:2 definitsioon ja trioleti liikmete
notatsiooniline kestus ei kirjelda sama ajavahemikku.

See test hoiab Voice 2, cross-staff-noodid ja peidetud noodid välja, et
mitte segada FATAL-03–FATAL-07 juhtumeid.

## Finale'i test

Loo FMD-BASE.musx-ist koopia ja muuda ainult takti 2:

1. loo Voice 1-s kolm C4 veerandnooti suhtes 3:2;
2. pärast trioleti loomist muuda kolmas triolettnoot poolnoodiks;
3. jäta trioleti definitsiooniks 3 veerandnooti 2 veerandnoodi ruumis;
4. ära lisa teist voice'i, cross-staff-noote ega peidetud noote.

Failid:

- FATAL-02.musx
- FATAL-02.musicxml

Kui Finale kuvab ekspordihoiatuse, jätka eksporti ja märgi hoiatus
tulemuse juurde.

## XML-is kontrollitav

- aktiivne divisions ja 4/4 takti oodatav kestus;
- takti 2 tegelik ajajoone ulatus;
- iga triolettnoodi duration;
- iga triolettnoodi type;
- time-modification/actual-notes ja normal-notes;
- notations/tuplet start/stop piirid;
- kas tuplet-liikmete kestus vastab deklareeritud 3:2 rühmale;
- kas taktid 3 ja 4 jäävad kontrollmaterjalina terveks.

MusicXML 4.0 käsitleb noodi tegelikku duration-kestust,
time-modification suhet ja visuaalse trioleti start/stop märgendeid
eraldi struktuuridena.

## Dorico tulemus

Ootel.

