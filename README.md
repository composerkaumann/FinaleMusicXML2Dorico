# Finale 27.4.1 → MusicXML → Dorico Validator

Testkorpus MusicXML-i vigade ja Dorico imporditõrgete uurimiseks.

## Töövoog

Iga test luuakse \`BASE/FMD-BASE.musx\` duplikaadina. Testitav muudatus
tehakse ainult taktis 2; taktid 1, 3 ja 4 jäävad muutmata kontrollmaterjaliks.

Kasutaja teeb Finale'is ja Doricos ainult järgmised sammud:

1. teeb baasfailist testfaili koopia;
2. tekitab Finale'is taktis 2 uuritava olukorra;
3. salvestab \`.musx\`-faili ja ekspordib pakkimata \`.musicxml\`-faili;
4. impordib MusicXML-i Doricosse;
5. kirjeldab lühidalt Dorico tulemust.

XML-i analüüs, klassifikatsioon, metadata ja tuvastusreegel lisatakse
pärast testfailide valmimist.

## Referentsfail

- Finale: 27.4 for Mac
- MusicXML: 4.0 partwise
- partii: 1
- taktimõõt: 4/4
- \`divisions\`: 2
- oodatav takti kestus: 8 division'it
- takt 1: neli C4 veerandnooti
- takt 2: täistaktipaus, kestus 8
- takt 3: G4–F4–E4–D4 veerandnoodid
- takt 4: C4–E4–G4–C5 kaheksandikud ja G4 poolnoot

Baasi detailne masinloetav kirjeldus ja kontrollsummad asuvad failis
\`BASE/metadata.json\`.

## Validaatori käivitamine

\`\`\`sh
python3 tools/fmd_validator.py BASE/FMD-BASE.musicxml
python3 tools/fmd_validator.py FATAL-01/FATAL-01.musicxml
\`\`\`

Masinloetava tulemuse saamiseks lisa \`--json\`. Validaator tagastab
leidude korral väljumiskoodi 1 ja sisendvea korral väljumiskoodi 2.

Praegu rakendatud reegel:

- \`FMD001\` — takti rütmiline ajajoon ületab aktiivse taktimõõdu kestust
  (\`warning\`; Dorico 6.2.30 taastus ühe partii FATAL-01 testist).

## Testide järjekord

1. \`FATAL-01\` — measure duration mismatch / overfilled measure; Dorico
   6.2.30 taastus peidetud lokaalse taktimõõdumuutusega
2. \`FATAL-01a\` — conflicting measure durations between two parts
3. \`FATAL-02\` — tuplet timeline mismatch
4. \`FATAL-03\` — tuplet start/stop voice mismatch
5. \`FATAL-04\` — Finale Voice 2 + tuplet
6. \`FATAL-05\` — cross-staff tuplet / missing or ambiguous voice
7. \`FATAL-06\` — illegal MusicXML duration
8. \`FATAL-07\` — Human Playback hidden-note rhythmic residue

Teste tehakse rangelt selles järjekorras.
