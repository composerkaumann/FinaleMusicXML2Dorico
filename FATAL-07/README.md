# FATAL-07 — Human Playbacki peidetud trillinootide kontrollpaar

## Tulemus

Kasutaja sõnul avanevad nii 07a kui ka 07b Dorico 6.2.31-s.
Dorico jätab 07b peidetud noodid tähelepanuta. Mõlemad juhtumid
on mittefataalsed ja validaator ei anna leide.

XML-i võrdlus kinnitab Human Playbacki peidetud noodijada olemasolu
07b-s. Selle katse ajajoon on korrektne; peidetud nootide olemasolu
ise ei anna alust fatal-reeglile.

## Kontrollfail 07a

`FATAL-07a.musx` lähtub ühe noodireaga BASE-failist.
Taktis 2 on C4 poolnoot trillimärgiga ja G4 poolnoot.
Human Playbacki rakendamata kontrolli eksport:

- `divisions=2`;
- kestused 4 + 4 = 8 division'it ehk neli lööki;
- kaks nähtavat nooti hääles 1;
- üks `trill-mark`;
- peidetud noote ega `cue`-noote ei ole.

## Human Playbackiga fail 07b

`FATAL-07b.musx` on 07a koopia, mille taktile 2 rakendati
Apply Human Playback. Ekspordis:

- `divisions=1024` ja 4/4 takti kestus 4096 division'it;
- nähtava C4 poolnoodi kestus on 2048, sellele lisandus `cue` ning
  `type size="full"`. Cue-noodi täpset esitust Doricos eraldi ei
  kontrollitud;
- `backup` väärtusega 2048 viib ajakursori takti algusse;
- hääles 2 on 14 peidetud nooti, vaheldumisi C4–D4;
- kõigil 14 noodil on `print-object="no"` ja `print-spacing="no"`
  ning puudub `type`;
- 13 nooti kestavad igaüks 146 division'it, viimane 150:
  13 × 146 + 150 = 2048 ehk täpselt kaks lööki;
- nähtav G4 poolnoot hääles 1 kestab seejärel 2048 division'it;
- kogu takti ajajoon lõpeb 4096 juures: ei ole üle- ega alatäitumist;
- trillimärk on säilinud.

Taktid 1, 3 ja 4 vastavad mõlemas XML-is BASE-failile pärast
kestuste normaliseerimist. Lisaks divisions'i muutusele on 07b
esimese takti tempo 120 eraldi `sound`-elemendis; tempo väärtus
ei muutu.

## Validaatori järeldus

Uut hoiatus- ega fatal-reeglit ei lisata. Mõlemad failid on
regressioonikontrollid: õigesti ajastatud Human Playbacki
peidetud noodijada peab jääma leiuta.

Peidetud noodid osalevad XML-i ajajoone arvestuses koos backup'iga.
Neid ei eemaldata validaatoris üldise erandina, sest mõnes teises
failis võivad nende kestused siiski ajajoont rikkuda.

Selles kontrollpaaris peidetud noodijada importi häirivat rütmijääki
ei tekkinud. Tähelepanek ei kinnita kõigi Human Playbacki
võimalike väljundite ohutust.

## Tõendite piirid

Dorico tulemus põhineb kasutaja kirjeldusel, ekraanipilte ega
Dorico eksporditud võrdlusfaile ei ole. Hilisemate taktide
täpne Dorico-tulemus ei olnud kasutaja selles teates eraldi
kirjeldatud; kontrollmaterjali võrdsus on kinnitatud XML-is.

Mõlemal variandil on eraldi MUSX- ja MusicXML-fail. Lähtefailid
salvestati pärast vastavat eksporti: 07a kaks ja 07b neli sekundit
hiljem. Täielikku lähteoleku ja ekspordi vastavust ei kinnitata
ainult ajatemplite põhjal; analüüsi alus on MusicXML.
