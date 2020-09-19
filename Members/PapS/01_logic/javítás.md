### A: *k-nak és d-nek van közös lánya*

#### Megoldásod:

$\exists k,d(\exists z(P(k,z) \land P(d,z) \land N(z))$

#### Visszajelzés:

- szintaxis: jó, de van tartalmi hiba
- tartalom: $k$-t és $d$-t nem kell kvantorral megkötni, mert konkrét személyek

#### Példa helyes megoldásra:

$\exists x(N(x) \land P(k,x) \land P(d,x))$

------------------------------------------------

### B: *csak a férfiak között vannak gyermektelenek*

#### Megoldásod:

$\nexists x(F(x) \land \exists z(P(x,z)) \land \nexists y(N(y) \land \nexists z(P(y,z)))$

#### Visszajelzés:

- szintaxis: jó, de van tartalmi hiba
- tartalom: azt állítod, hogy **nincs olyan férfi, akinek van gyereke**, az eredeti állítás pedig csak annyit köt ki, hogy **vannak gyermektelen férfiak** (a nőkre vonatkozó rész jó)

#### Példa helyes megoldásra:

$\forall x(\nexists y(P(x,y)) \Rightarrow F(x)) \land \exists x(\nexists y(P(x,y)))$

vagy: $\exists f(F(f) \land \nexists x(P(f,x))) \land \nexists n(N(n) \land \nexists y(P(n,y)))$

------------------------------------------------

### C: *vannak egynemű testvérek*

#### Megoldásod:

$\exists x,y,z((P(z,x) \land P(z,y) \land N(x) \land N(y)) \lor (P(z,x) \land P(z,y) \land F(x) \land F(y)))$

vagy rövidebben: $\exists x,y,z(P(z,x) \land P(z,y) \land ((N(x) \land N(y)) \lor (F(x) \land F(y))))$

#### Visszajelzés:

- szintaxis: jó
- tartalom: kisebb hiba, hogy a te kifejezésed szerint $x$ és $y$ féltestvérek is lehetnek, mert csak egy közös szülőt kötsz ki

#### Példa helyes megoldásra:
*Én kikötöm, hogy az egyik szülő nő, a másik férfi, mert biológiai testvérekként értelmezem az állításban szereplőket, de ezt el lehet hagyni.*

$\exists (x,y,m,f)((N(x) \Leftrightarrow N(y)) \land N(m) \land P(m,x) \land P(m,y) \land F(f) \land P(f,x) \land P(f,y))$

vagy: $\exists (x,y,m,f)(((F(x) \land F(y)) \lor (N(x) \land N(y))) \land N(m) \land P(m,x) \land P(m,y) \land F(f) \land P(f,x) \land P(f,y))$
