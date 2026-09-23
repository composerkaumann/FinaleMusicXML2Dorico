# FATAL-03 — Voice 2 Launch lõhub trioleti impordi

## Katse eesmärk

Algne hüpotees oli, et Finale 27.4.1 ekspordib trioleti alguse ja lõpu
sama `number`-tunnusega, kuid eri `<voice>` väärtustega nootide küljes.
See hüpotees ei täitunud. Katse tulemusel tekkis teine fataalne
impordiviga, mille allpool täpselt kirjeldame.

## Finale'is ettevalmistamine

1. Tee `BASE/FMD-BASE.musx`-ist koopia `FATAL-03/FATAL-03.musx`.
2. Sisesta ainult takti 2 Voice 1-s kolm C4 veerandnooti suhtes 3:2.
3. Lisa nende järele C4 poolnoot. Nii täidab esialgne Voice 1 täpselt
   4/4 takti: triolett hõivab kaks lööki ja poolnoot kaks lööki.
4. Ava takti 2 `Edit Frame` (Speedy Entry; sulge noodisisestuse raam;
   Option-klõps taktil). Vali kolmanda triolettnoodi *entry* ning märgi
   `Voice 2` ja `V2 Launch`. Ainult `Voice 2` märkimisel korraldas Finale
   kasutaja vaatluse järgi takti kohe ümber.
5. Salvesta ja ekspordi pakkimata fail `FATAL-03/FATAL-03.musicxml`.

`Edit Frame` on Finale'i madala taseme redaktor. XML näitab, kas soovitud
juhtum tegelikult tekkis.

## Algse hüpoteesi XML-i kontroll

- `notations/tuplet type="start"` ja `type="stop"` asuvad sama partii
  sama takti eri `<voice>` väärtustega nootide küljes;
- mõlema trioletimärgendi `number` on sama;
- takti `duration`-ajajoont ja võimalikke `backup`/`forward` elemente
  võrreldakse eraldi, et vältida FATAL-02 ajajooneveaga segiajamist;
- taktid 1, 3 ja 4 võrreldakse BASE-ekspordiga pärast `divisions`
  normaliseerimist.

## Ekspordi tulemus

`FATAL-03.musicxml` on süntaktiliselt korrektne, kuid algne
sihttunnus ei tekkinud:

- trioleti algus on Voice 1 esimesel C4 veerandnoodil;
- kolmas C4 veerandnoot on Voice 2-s, ilma `time-modification`-i ja
  trioleti lõppmärgendita;
- trioleti lõpp on Voice 1 poolpausil;
- ajajoon lõpeb 16 division'il, kuigi 4/4 takt vajab 24.

Validaator tuvastab olemasoleva `FMD003` alatäitumise. See ei tõesta,
et algselt kavandatud eri häältes tuplet start/stop on Finale'i ekspordiga
tekitatav. Täiendavat reeglit praeguse XML-i põhjal ei lisatud.
Taktid 1, 3 ja 4 on baasiga rütmiliselt samad, kui `divisions` on
normaliseeritud.

## Dorico tulemus

Dorico 6.2.30 import on fataalselt vigane: trioleti kolmanda noodi
asemel on paus ning taktid 3 ja 4 puuduvad. Need taktid on MusicXML-is
olemas, nii et noodimaterjal kaob importimisel. Kasutaja kinnitas
tulemuse; ekraanipilti pole selle juhtumi jaoks salvestatud.

Tulemus kinnitab FATAL-03 faili fataalsuse, kuid ei eralda üheselt,
kas hilisemate taktide kadumise põhjustab Voice 2-sse viidud noot,
Voice 1-sse sattunud trioleti lõpp poolpausil või alatäidetud ajajoon.

## Allikafaili seis

Pärast siin analüüsitud MusicXML-i eksporti salvestati `FATAL-03.musx`
uuesti. Selle sisemine `score.dat` muutus, kuid MusicXML-i ei eksporditud
uuesti. Praeguse `.musx` ja analüüsitud `.musicxml` täpne vastavus on
seetõttu kontrollimata; Dorico tähelepanek ja validaatorileid põhinevad
olemasoleval MusicXML-il.

## Allikad

- [Finale for Mac: Edit Frame](https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/SPFRMDLG.htm)
- [MusicXML 4.0: tuplet](https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/tuplet/)
- [MusicXML 4.0: voice](https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/voice/)
