# FATAL-01 — measure duration mismatch

## Test

Taktis 2 on kolm C4 veerandnooti ja üks C4 poolnoot. Materjali
kogukestus on viis neljandiklööki 4/4 taktis.

Finale näitas MusicXML-i ekspordil hoiatust; eksporti jätkati.

## XML-i tulemus

- \`divisions = 2\`
- 4/4 takti lubatud kestus: \`8\`
- nootide kestused: \`2 + 2 + 2 + 4\`
- tegelik ajajoone ulatus: \`10\`
- ületäituvus: \`2\` ehk üks veerandnoot
- XML on well-formed
- taktid 1, 3 ja 4 on BASE-ekspordiga identsed

## Klassifikatsioon

- reegel: \`FMD001\`
- raskusaste: \`warning\`
- kategooria: \`rhythmic-timeline\`
- Dorico 6.2.30 jaoks fataalne: ei

Reegel rakendub, kui partii takti ajajoone kõige kaugem positsioon on
suurem kui aktiivse taktimõõdu põhjal arvutatud takti kestus.

## Dorico tulemus

Dorico 6.2.30 import õnnestus. Taktis 2 tekkis peidetud lokaalne
taktimõõdumuutus. Taktid 3 ja 4 jäid korrektseks.

Järeldus: ühe partii isoleeritud ületäituv takt ei katkesta selles testis
importi. Dorico säilitab viis lööki lokaalse taktimõõduparandusega.

