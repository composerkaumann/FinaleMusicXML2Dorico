# FATAL-02b — overfilling rest after an incomplete tuplet

## Finale'i test

Takt 2 sisaldab sama materjali nagu FATAL-02:

- C4 veerandnoot, 3:2;
- C4 veerandnoot, 3:2;
- C4 poolnoot, 3:2;
- tuplet algab esimesel ja lõpeb kolmandal noodil.

Seejärel käivitati Finale'is Fill with Rests. Finale lisas poolpausi,
kuigi tegelik vaba ruum ei vastanud enam poolnoodile.

## XML-i tulemus

- divisions: 6
- 4/4 takti oodatav kestus: 24
- tupletnootide kestus: 4 + 4 + 8 = 16
- lisatud poolpausi kestus: 12
- takti tegelik ulatus: 28
- ületäituvus: 4 division’it

Tegelik vaba ruum enne pausi oli 8 division’it, kuid Finale eksportis
pausi kestusega 12.

## Dorico tulemus

Dorico 6.2.30 import lõpeb, kuid tulemus on fataalselt vigane. Kolmas
XML-is olev C4 poolnoot kaob ning Dorico näitab selle asemel pause.
Tulemus on failis Fatal02bDorico.png.

## Klassifikatsioon

- reegel: FMD004
- raskusaste: fatal
- kategooria: tuplet-rest-fill-timeline

Reegel tuvastab tupletit ja pause sisaldava takti, mille ajajoon ulatub
aktiivse taktimõõdu kestusest kaugemale.

