# FATAL-03 — tuplet start/stop eri häältes

## Katse eesmärk

Kontrollida, kas Finale 27.4.1 ekspordib trioleti alguse ja lõpu sama
`number`-tunnusega, kuid erineva `<voice>` väärtusega nootide küljes.
See on testitav XML-i tunnus, mitte veel kinnitatud Finale'i ekspordiviga
ega Dorico jaoks fataalne juhtum.

## Finale'is ettevalmistamine

1. Tee `BASE/FMD-BASE.musx`-ist koopia `FATAL-03/FATAL-03.musx`.
2. Sisesta ainult takti 2 Voice 1-s kolm C4 veerandnooti suhtes 3:2.
3. Lisa nende järele C4 poolnoot. Nii täidab esialgne Voice 1 täpselt
   4/4 takti: triolett hõivab kaks lööki ja poolnoot kaks lööki.
4. Ava takti 2 `Edit Frame` (Speedy Entry; sulge noodisisestuse raam;
   Option-klõps taktil). Vali kolmanda triolettnoodi *entry* ja märgi
   ainult selle `Voice 2` ruut. Jäta trioleti ning teiste entry'de
   seaded samaks.
5. Salvesta ja ekspordi pakkimata fail `FATAL-03/FATAL-03.musicxml`.

`Edit Frame` on Finale'i madala taseme redaktor. Pärast muudatust võib
Finale noote ümber korraldada või eksportija hääled teisiti kodeerida.
XML näitab, kas soovitud juhtum tegelikult tekkis.

## XML-i kontroll

- `notations/tuplet type="start"` ja `type="stop"` asuvad sama partii
  sama takti eri `<voice>` väärtustega nootide küljes;
- mõlema trioletimärgendi `number` on sama;
- takti `duration`-ajajoont ja võimalikke `backup`/`forward` elemente
  võrreldakse eraldi, et vältida FATAL-02 ajajooneveaga segiajamist;
- taktid 1, 3 ja 4 võrreldakse BASE-ekspordiga pärast `divisions`
  normaliseerimist.

Kui start ja stop jäävad samasse häälde, ei ole FATAL-03 tunnus veel
tekitatud. Sel juhul fikseerime ekspordi tegeliku kuju enne uut katset.
Validaatorireegel ja raskusaste määratakse alles pärast XML-i ning
Dorico tulemuse nägemist.

## Dorico tulemus

Ootel.

## Allikad

- [Finale for Mac: Edit Frame](https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/SPFRMDLG.htm)
- [MusicXML 4.0: tuplet](https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/tuplet/)
- [MusicXML 4.0: voice](https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/voice/)
