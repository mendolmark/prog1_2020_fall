### A: *k-nak és d-nek van közös lánya*

#### Megoldásod:

$ \exists x(N(x) \land P(x) \land P(d,x) $

#### Visszajelzés:

- szintaxis: a $P$ predikátumnak két paramétere van, $P(x,y)$ azt jelenti, hogy $y$ $x$-nek a gyereke, egy paraméterrel értelmetlen a kifejezés
- tartalom: emiatt hiányzik, hogy $x$ $k$ lánya is ($P(k, x)$)

#### Példa helyes megoldásra:

$\exists x(N(x) \land P(k,x) \land P(d,x))$

------------------------------------------------

### B: *csak a férfiak között vannak gyermektelenek*

#### Megoldásod:

$\exists x(F(x) \land \forall a \neg P(x)) \land \nexists x(N(x) \land b(\neg P(x))$

#### Visszajelzés:

- szintaxis:
	- ahogy az előbb, a $P$ predikátumnak két paramétert kell megadni, $P(x)$-nek nincs értelme
	- a $\forall a$ után zárójelet kell nyitni, és abba írni a vonatkozó kifejezést
	- a $b$ előtt hiányzik a $\forall$ kvantor (minden $b$-re igaz, hogy...)
	- a legvégéről hiányzik egy zárójel
- a fenti hibák javításával a tartalom egyébként jó lenne: $\exists x(F(x) \land \forall a (\neg P(x,a))) \land \nexists x(N(x) \land \forall b(\neg P(x,b)))$

#### Példa helyes megoldásra:

$\forall x(\nexists y(P(x,y)) \Rightarrow F(x)) \land \exists x(\nexists y(P(x,y)))$

vagy: $\exists f(F(f) \land \nexists x(P(f,x))) \land \nexists n(N(n) \land \nexists y(P(n,y)))$

------------------------------------------------

### C: *vannak egynemű testvérek*

#### Megoldásod:

$\exists x(F(a) \land F(b)) \land (P(x) \land P(y) \land P(y) \land P(b))$

#### Visszajelzés:

- szintaxis:
	- a teljes kifejezést az $x$ utáni zárójelbe kell írni, ha $x$-re vonatkozik
	- megint csak egy paramétert adtál meg a $P$ predikátumnak
- tartalom:
	- a második rész nehezen értelmezhető a $P$ predikátum helytelen használata miatt
	- $a, b$ és $y$ nincsenek kvantorhoz rendelve, így olyan, mintha konkrét személyek lennének, pedig általános állítást kell tenni
	- csak azt az esetet veszed figyelembe, mikor fiútestvérekről van szó, pedig az állítás csak az egyneműséget követeli meg

#### Példa helyes megoldásra:
*Én kikötöm, hogy az egyik szülő nő, a másik férfi, mert biológiai testvérekként értelmezem az állításban szereplőket, de ezt el lehet hagyni.*

$\exists (x,y,m,f)((N(x) \Leftrightarrow N(y)) \land N(m) \land P(m,x) \land P(m,y) \land F(f) \land P(f,x) \land P(f,y))$

vagy: $\exists (x,y,m,f)(((F(x) \land F(y)) \lor (N(x) \land N(y))) \land N(m) \land P(m,x) \land P(m,y) \land F(f) \land P(f,x) \land P(f,y))$
