### A: *k-nak és d-nek van közös lánya*

#### Megoldásod:

$\exists (k,d,y)(N(y) \land P(d,y) \land P(k,y))$

#### Visszajelzés:

- szintaxis: jó
- tartalom: $k$-t és $d$-t nem kell kvantorral megkötni, mert konkrét személyek

#### Példa helyes megoldásra:

$\exists x(N(x) \land P(k,x) \land P(d,x))$

------------------------------------------------

### B: *csak a férfiak között vannak gyermektelenek*

#### Megoldásod:

$\nexists y(N(y) \land \exists x(P(n,x))) \land \exists z(F(z) \land \exists n(\neg P(z,n))$

#### Visszajelzés:

- szintaxis: a végéről hiányzik egy zárójel (de lehet, hogy csak nem fért ki)
- tartalom: ezzel a megoldással azt állítod, hogy **nincs olyan nő, akinek van gyereke, és van olyan férfi, akinek nem mindenki a gyereke**

#### Példa helyes megoldásra:

$\forall x(\nexists y(P(x,y)) \Rightarrow F(x)) \land \exists x(\nexists y(P(x,y)))$

vagy: $\exists f(F(f) \land \nexists x(P(f,x))) \land \nexists n(N(n) \land \nexists y(P(n,y)))$

------------------------------------------------

### C: *vannak egynemű testvérek*

#### Megoldásod:

$\exists (w,d,x,y)(F(n) \land N(d) \land F(y) \land F(x) \land P(n,x) \land P(d,y) \land P(n,y) \land P(d,x)) \lor \exists (w,d,z,zs)(F(n) \land N(d) \land F(z) \land F(zs) \land P(n,z) \land P(n,zs) \land P(d,z) \land P(d,zs)$

#### Visszajelzés:

- szintaxis: a végéről megint lemaradt egy zárójel
- tartalom: jó megoldás

#### Példa helyes megoldásra:

$\exists (x,y,m,f)((N(x) \Leftrightarrow N(y)) \land N(m) \land P(m,x) \land P(m,y) \land F(f) \land P(f,x) \land P(f,y))$

vagy: $\exists (x,y,m,f)(((F(x) \land F(y)) \lor (N(x) \land N(y))) \land N(m) \land P(m,x) \land P(m,y) \land F(f) \land P(f,x) \land P(f,y))$