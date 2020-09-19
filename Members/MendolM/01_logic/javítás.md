### A: *k-nak és d-nek van közös lánya*

#### Megoldásod:

$\exists k F(k) \land \exists d N(d) \land \exists n N(n) \land P(k,n) \land P(d,n)$

#### Visszajelzés:

- szintaxis: a kvantorral bevezetett paraméterek után kéne zárójel
- tartalom: $k$-t és $d$-t nem kell kvantorral megkötni, mert ezek konrét személyek

#### Példa helyes megoldásra:

$\exists x(N(x) \land P(k,x) \land P(d,x))$

------------------------------------------------

### B: *csak a férfiak között vannak gyermektelenek*

#### Megoldásod:

$\nexists x(F(x) \land \exists z \land P(x,z)) \land \nexists y(N(y) \land \nexists z \land P(y,z)$

#### Visszajelzés:

- szintaxis:
    - az $\exists z \land P(x,z)$ értelmetlen, helyette $\exists z (P(x,z))$-t kell használni
    - a végéről lemaradt egy zárójel
- tartalom: azt állítod, hogy nincs olyan férfi, akinek van gyereke, pedig az eredeti állítás csak annyit mond, hogy vannak gyermektelen férfiak (a nőkre vonatkozó rész helyes)

#### Példa helyes megoldásra:

$\forall x(\nexists y(P(x,y)) \Rightarrow F(x)) \land \exists x(\nexists y(P(x,y)))$

vagy: $\exists f(F(f) \land \nexists x(P(f,x))) \land \nexists n(N(n) \land \nexists y(P(n,y)))$

------------------------------------------------

### C: *vannak egynemű testvérek*

#### Megoldásod:

$\exists x F(x) \land \exists y \land P(y,x) \land \exists z F(z) \land P(y,z) \lor \exists a N(a) \land P(y,a) \land \exists c N(c) \land P(y,c)$

#### Visszajelzés:

- szintaxis:
    - ahogy az előzőnél, a $\exists y \land P(y,x)$ helyett $\exists y(P(y,x))$-et kell írni
    - a sorrend és a zárójelek hiánya összezavaró, ha egy kifejezés tartalmaz egy korábban kvantorral megkötött paramétert, akkor annak a kifejezésnek a kvantorhoz tartozó zárójelen belül kell lennie. a te megoldásodban a teljes kifejezés vonatkozik $y$-ra, míg $x$-re csak a fele, ezért így írnám: $\exists y(\exists x(F(x) \land P(y,x) \land \exists z(F(z) \land P(y,z))) \lor \exists a(N(a) \land P(y,a) \land \exists c(N(c) \land P(y,c))))$
- tartalom: így is csak azt állítod, hogy vannak féltestvérek (a testvérhez két közös szülő kell)

#### Példa helyes megoldásra:
*Én kikötöm, hogy az egyik szülő nő, a másik férfi, mert biológiai testvérekként értelmezem az állításban szereplőket, de ezt el lehet hagyni.*

$\exists (x,y,m,f)((N(x) \Leftrightarrow N(y)) \land N(m) \land P(m,x) \land P(m,y) \land F(f) \land P(f,x) \land P(f,y))$

vagy: $\exists (x,y,m,f)(((F(x) \land F(y)) \lor (N(x) \land N(y))) \land N(m) \land P(m,x) \land P(m,y) \land F(f) \land P(f,x) \land P(f,y))$