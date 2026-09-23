# FATAL-02a — full-measure mixed-duration tuplet

## Eesmärk

Eraldada FATAL-02 kaks võimalikku põhjust:

1. tupletit sisaldav alatäidetud takt;
2. segakestustega 3:2 triolett.

## Finale'i test

Tee FATAL-02.musx-ist koopia nimega FATAL-02a.musx. Muuda ainult takti
2 kolmas C4 triolettnoot poolnoodist täisnoodiks.

Takti 2 sihtsisu:

- esimene C4: veerandnoot, 3:2;
- teine C4: veerandnoot, 3:2;
- kolmas C4: täisnoot, 3:2;
- sama tuplet algab esimesel ja lõpeb kolmandal noodil;
- pause ei lisata.

Eeldatava divisions=6 korral peaks XML-i kestus olema
4 + 4 + 16 = 24, mis täidab 4/4 takti täpselt.

## Tulemuse tõlgendus

- Kui Dorico säilitab kolmanda noodi, oli FATAL-02 fataalse noodikao
  peamine tingimus alatäidetud ajajoon.
- Kui Dorico kaotab kolmanda noodi ka täidetud taktis, on fataalne
  tingimus seotud segakestustega 3:2 trioletiga.

## Dorico tulemus

Dorico 6.2.30 import õnnestus:

- kõik kolm triolettnooti säilisid;
- takti 2 ajajoon on täpselt 24/24 division’it;
- taktid 3 ja 4 säilisid;
- validaator ei anna leide.

Järeldus: segakestustega 3:2 triolett ei ole iseenesest fataalne. FATAL-02
noodikadu sõltub vigasest takti ajajoonest.
