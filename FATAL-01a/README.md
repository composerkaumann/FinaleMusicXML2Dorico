# FATAL-01a — conflicting measure durations between parts

## Eesmärk

Kontrollida, kuidas Dorico käsitleb sama takti erinevat kestust kahes
instrumendis.

## Finale'i test

FMD-BASE-ist loodi kahe instrumendiga koopia. Taktis 2:

- P1: kolm C4 veerandnooti ja üks C4 poolnoot, kokku 5 lööki;
- P2: neli C4 veerandnooti, kokku 4 lööki.

Taktid 1, 3 ja 4 on mõlemas instrumendis rütmiliselt korrektsed.

Failid:

- \`FATAL-01a.musx\`
- \`FATAL-01a.musicxml\`

## XML-i tulemus

- mõlemad partiid deklareerivad 4/4 takti kestuseks 8 division’it;
- P1 takti 2 tegelik ulatus on 10;
- P2 takti 2 tegelik ulatus on 8;
- partiiülene erinevus on 2 division’it ehk üks veerandnoot;
- XML on well-formed.

Validaator annab P1 ületäituvuse kohta \`FMD001\` ja partiide omavahelise
erinevuse kohta \`FMD002\`. Mõlema raskusaste on \`warning\`.

## Dorico tulemus

Dorico 6.2.30 import õnnestus. Teisele reale lisandus veerandpaus.

Tulemus on kooskõlas sellega, et Dorico võttis takti ulatuseks pikema P1
ajajoone (10) ja täitis P2 puuduva kestuse 2 division’i pikkuse pausiga.
See seletus on XML-i ja nähtava tulemuse põhjal tehtud järeldus.
