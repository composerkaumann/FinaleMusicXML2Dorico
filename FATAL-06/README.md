# FATAL-06 — käsitsi muudetud Finale noodikestused

## Katse ülesehitus

Algse ühe noodireaga BASE-faili takti 2 sisestati neli C4 veerandnooti.
Edit Frame'i kaudu muudeti ainult teise noodi kestust:

- nullkestuse katse: Finale ei säilita Duration väärtust 0;
- 06a: Duration = 1 EDU;
- 06b: Duration = 1025 EDU.

Finale'is on veerandnoot 1024 EDU. Nullkestusest XML-eksporti ei tekkinud.
Kahe positiivse kestuse eksport on säilitatud eraldi failides
`FATAL-06a.musicxml` ja `FATAL-06b.musicxml`.

## XML-i ja Dorico tulemused

| Variant | Finale'i teise noodi kestus | XML-i divisions | XML-i teise noodi kestus | Teise noodi type | Tulemus |
| --- | --- | --- | --- | --- | --- |
| 06a | 1 EDU | 1024 | 1 ehk 1/1024 veerandist | puudub | warning |
| 06b | 1025 EDU | 2 | 2 ehk üks veerand | puudub | korras kontroll |

06a XML-is säilis väga lühike kestus. Taktis 2 on kestused
1024 + 1 + 1024 + 1024 = 3073 division'it, deklareeritud 4/4 kestus
on 4096. Teisel noodil ei ole `grace`, `type` ega `time-modification`
elementi. See kestus vastab 4096ndiknoodile.

Kasutaja sõnul näitas Dorico 06a impordil ebaharilikke vältusi ning
näis neid lähimatele võimalikele väärtustele ühtlustavat. Täpseid
imporditud vältusi ei fikseerita, sest Dorico eksporditud faili ega
ekraanipilti ei ole. Taktid 3 ja 4 olid kasutaja sõnul korras.
Klassifikatsioon on **warning**, mitte fatal.

06b XML-is on teise noodi kestus juba täpselt veerandnoot.
1025 EDU ja tavapärase 1024 EDU vahe ei säilinud MusicXML-is:
noodikestused on 2 + 2 + 2 + 2 = 8, mis täidavad 4/4 takti.
Seetõttu ei saa selle katse põhjal omistada erinevuse eemaldamist
Dorico importijale. Kasutaja nägi Doricos nelja veerandnooti ning
hilisemad taktid olid korras. Klassifikatsioon on **none**.

Mõlema faili taktid 1, 3 ja 4 vastavad BASE-failile pärast divisions'i
normaliseerimist. Mõlemas on üks partii ning kõik noodid hääles 1.
Dorico versioonina arvestatakse sama katseseansi viimati teatatud
versiooni 6.2.31; kasutaja ei korranud versiooninumbrit 06 tulemuses.

## Tuvastusreegel FMD006

`FMD006` annab warning'u tavalisele helikõrgusega noodile, millel:

- puuduvad `type` ja `time-modification`;
- puudub `grace`;
- positiivne kestus on lühem kui 1024ndiknoot.

06a annab ühe leiu P1 takti 2 teisel noodil, 06b ei anna leide.
1024ndiknoodi piiri peal olev kestus ning tupletisuhtega lühem noot
on eraldi kontrollides leiuta.

MusicXML-i `type` on valikuline; selle puudumine üksi ei ole viga.
Kõige lühem otsene graafiline noodiväärtus on `1024th`.
Reegel osutab selles korpuses täheldatud impordiriskile, mitte
MusicXML-i skeemiveale. Algset keelatud nullkestust ei õnnestunud
Finale ekspordis tekitada.

## Lähtefaili säilitamine

Kataloogis on üks ühine `FATAL-06.musx`, salvestatud pärast mõlemat
XML-eksporti. Eraldi 06a ja 06b MUSX-olekuid ei ole säilitatud.
Ühise lähtefaili täpset vastavust kummalegi ekspordile ei kinnitata;
analüüsi alus on vastava variandi MusicXML.

## Allikad

- [Finale: Edit Frame ja EDU](https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/SPFRMDLG.htm)
- [MusicXML 4.0: note, sealhulgas valikuline type](https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/note/)
- [MusicXML 4.0: note-type-value](https://www.w3.org/2021/06/musicxml40/musicxml-reference/data-types/note-type-value/)
