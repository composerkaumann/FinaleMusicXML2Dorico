# FATAL-01a — conflicting measure durations between parts

## Eesmärk

Kontrollida, kuidas Dorico käsitleb sama takti erinevat kestust kahes
instrumendis.

## Finale'i test

Loo FMD-BASE-ist kahe instrumendiga koopia. Muuda ainult takti 2:

- instrument 1: täpselt 4 lööki;
- instrument 2: kolm C4 veerandnooti ja üks C4 poolnoot, kokku 5 lööki.

Taktid 1, 3 ja 4 peavad mõlemas instrumendis olema korrektsed. Ekspordi
pakkimata MusicXML failina ka juhul, kui Finale kuvab hoiatuse.

Failid:

- \`FATAL-01a.musx\`
- \`FATAL-01a.musicxml\`

## Kontrollitav hüpotees

Partii P1 takti 2 ajajoon lõpeb kestusel 8 ja partii P2 sama takt kestusel
10. Kontrollime, kas Dorico:

1. impordib mõlemad partiid ja lisab ainult P2-le peidetud lokaalse
   taktimõõdumuutuse;
2. muudab mõlema partii taktimõõtu või joondust;
3. kaotab või nihutab materjali järgmistes taktides;
4. katkestab impordi.

## Dorico tulemus

Ootel.

