### A: *k-nak és d-nek van közös lánya*

#### Megoldásod:

$\exists(k,d,x)(N(x) \land P(k,x) \land P(d,x))$

#### Visszajelzés:

- szintaxis: a végéről hiányzik egy zárójel
- tartalom: majdnem jó, de a $k$-t és $d$-t nem kell megkötni kvantorral, mert ők konkrét személyek

#### Példa helyes megoldásra:

$\exists x(N(x) \land P(k,x) \land P(d,x))$

------------------------------------------------

### B: *csak a férfiak között vannak gyermektelenek*

#### Megoldásod:

$\exists(y)(F(y) \land \forall a(\neg P(y,a)) \land \nexists x(N(x) \land \forall b(\neg P(x,b)$

#### Visszajelzés:

- szintaxis: megint hiányzik pár zárójel
- tartalom: egyébként tökéletes megoldás

#### Példa helyes megoldásra:

$\forall x(\nexists y(P(x,y)) \Rightarrow F(x)) \land \exists x(\nexists y(P(x,y)))$

vagy ahogy te csináltad: $\exists y(F(y) \land \forall a(\neg P(y,a))) \land \nexists x(N(x) \land \forall b(\neg P(x,b)))$

------------------------------------------------

### C: *vannak egynemű testvérek*

#### Megoldásod:

$\exists(x,y,a,b)(F(a) \land F(b) \land P(x,a) \land P(x,b) \land P(y,a) \land P(y,b)$

#### Visszajelzés:

- szintaxis: helyes
- tartalom: majdnem jó, de ezzel azt fejezed ki, hogy **léteznek fiútestvérek**, pedig az eredeti állítás **csak az egyneműséget követeli meg**

#### Példa helyes megoldásra:
*Én kikötöm, hogy az egyik szülő nő, a másik férfi, mert biológiai testvérekként értelmezem az állításban szereplőket, de ezt el lehet hagyni.*

$\exists (x,y,m,f)((N(x) \Leftrightarrow N(y)) \land N(m) \land P(m,x) \land P(m,y) \land F(f) \land P(f,x) \land P(f,y))$

vagy, ahogy te kezdtél neki: $\exists(x,y,a,b)(((F(a) \land F(b)) \lor (N(a) \land N(b))) \land P(x,a) \land P(x,b) \land P(y,a) \land P(y,b)$