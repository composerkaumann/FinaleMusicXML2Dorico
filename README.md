# Finale 27.4.1 → MusicXML → Dorico Validator

Testkorpus MusicXML-i vigade ja Dorico imporditõrgete uurimiseks.

[GitHubi repositoorium](https://github.com/composerkaumann/FinaleMusicXML2Dorico)

## Töövoog

Ühe noodirea testid lähtuvad `BASE/FMD-BASE.musx` failist; kahe rea
FATAL-05 lähtub `BASE/FMD-BASE-2STAFF.musx` failist. Testitav muudatus
tehakse ainult taktis 2; taktid 1, 3 ja 4 jäävad muutmata kontrollmaterjaliks.
Kontrollpaari variandid võivad olla eelneva testfaili duplikaadid.

Kasutaja teeb Finale'is ja Doricos ainult järgmised sammud:

1. teeb baasfailist testfaili koopia;
2. tekitab Finale'is taktis 2 uuritava olukorra;
3. salvestab `.musx`-faili ja ekspordib pakkimata `.musicxml`-faili;
4. impordib MusicXML-i Doricosse;
5. kirjeldab lühidalt Dorico tulemust.

XML-i analüüs, klassifikatsioon, metadata ja tuvastusreegel lisatakse
pärast testfailide valmimist.

## Referentsfail

- Finale: 27.4 for Mac
- MusicXML: 4.0 partwise
- partii: 1
- taktimõõt: 4/4
- `divisions`: 2
- oodatav takti kestus: 8 division'it
- takt 1: neli C4 veerandnooti
- takt 2: täistaktipaus, kestus 8
- takt 3: G4–F4–E4–D4 veerandnoodid
- takt 4: C4–E4–G4–C5 kaheksandikud ja G4 poolnoot

Baasi detailne masinloetav kirjeldus ja kontrollsummad asuvad failis
`BASE/metadata.json`.

Kahe rea võrdlusfail on `BASE/FMD-BASE-2STAFF.musx` koos vastava
MusicXML-iga. Eksport esitab selle kahe eraldi ühe noodireaga partiina;
P1 kontrollmaterjal vastab algsele baasile ja P2 sisaldab täistaktipause.
Selle variandi kirjeldus on `BASE/metadata-2staff.json`.

## Validaatori käivitamine

```sh
python3 tools/fmd_validator.py BASE/FMD-BASE.musicxml
python3 tools/fmd_validator.py FATAL-01/FATAL-01.musicxml
```

Masinloetava tulemuse saamiseks lisa `--json`. Validaator tagastab
leidude korral väljumiskoodi 1 ja sisendvea korral väljumiskoodi 2.

Praegu rakendatud reeglid:

- `FMD001` — takti rütmiline ajajoon ületab aktiivse taktimõõdu kestust
  (`warning`; Dorico 6.2.30 taastus ühe partii FATAL-01 testist).
- `FMD002` — sama takti tegelik rütmiline ulatus erineb partiide vahel
  hoolimata samast deklareeritud taktikestusest (`warning`).
- `FMD003` — tupletit sisaldava tavapärase takti ajajoon lõpeb enne
  deklareeritud taktikestust (`fatal`; FATAL-02 põhjustas Doricos
  eksporditud noodi kadumise).
- `FMD004` — tupletit ja pause sisaldava takti ajajoon ületab
  deklareeritud taktikestuse (`fatal`; FATAL-02b põhjustas Doricos
  eksporditud noodi kadumise).
- `FMD005` — ühe takti sees lõppeva, selgesõnalise
  `normal-type`-iga trioleti noodid katavad määratletust lühema
  ajavahemiku (`warning`; FATAL-04a põhjustas Doricos lisalööke).

## Teadaolev piirang

FATAL-05 annab praeguse `FMD003` järgi fatal-leiu, kuigi kasutaja Dorico
6.2.31 testis noodikadu ega katkenud importi ei esinenud. Seega ei saa
iga trioletti sisaldavat alatäidetud takti automaatselt fatal-iks lugeda.
Reegel vajab kitsendamist ja Dorico versioonide mõju kontrolli;
[FATAL-05 analüüs](FATAL-05/README.md) kirjeldab vastunäidet.

## Testide järjekord

1. `FATAL-01` — measure duration mismatch / overfilled measure; Dorico
   6.2.30 taastus peidetud lokaalse taktimõõdumuutusega
2. `FATAL-01a` — conflicting measure durations between two parts;
   Dorico 6.2.30 täitis lühema partii veerandpausiga
3. `FATAL-02` — tuplet timeline mismatch; kinnitatud `fatal`, sest
   Dorico 6.2.30 kaotas XML-is oleva C4 poolnoodi ja lisas pausid
4. `FATAL-02a` — sama segakestustega 3:2 triolett täpselt täidetud
   4/4 taktis; Dorico importis selle korrektselt
5. `FATAL-02b` — Finale Fill with Rests lisab tegelikust vabast
   ruumist pikema poolpausi; kinnitatud `fatal`
6. `FATAL-03` — Voice 2 Launch trioletis; Dorico 6.2.30 kaotas
   kolmanda triolettnoodi ja taktid 3–4. Algne eri häälte start/stop
   hüpotees XML-is ei täitunud; olemasolev `FMD003` leiab ajajoonevea
7. `FATAL-04` — täielik 3:2 triolett Finale Voice 2-s koos nelja
   löögini täidetud Voice 1 ja Voice 2-ga; Dorico import korras,
   validaatoril leide pole
8. `FATAL-04a` — Voice 1 teises taktiosas triolettveerandnoodid ja
   samaaegne Voice 2 poolnoot; trioleti vale poolnoodidefinitsioon,
   kinnitatud `warning`: Dorico lisas takti lööke ja peidetud
   taktimõõdu, kuid import ei katkenud
9. `FATAL-04b` — sama kahe hääle materjal, kuid korrektne
   veerandnooditrioleti definitsioon; Dorico import korras, Voice 2
   alguspaus on ootuspärane
10. `FATAL-05` — cross-staff katse; Dorico 6.2.31 säilitas noodid
    lähtereal. Eksport ei kodeeri teise rea määramist; juhtum ei ole
    fatal, praegune `FMD003` annab teadaoleva valepositiivse leiu
11. `FATAL-06` — illegal MusicXML duration
12. `FATAL-07` — Human Playback hidden-note rhythmic residue

Teste tehakse rangelt selles järjekorras.
