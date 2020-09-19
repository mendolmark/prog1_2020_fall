### A: *k-nak és d-nek van közös lánya*

#### Megoldásod:

$\exists x(N(x) \land P(k,x) \land P(d,x))$

#### Visszajelzés:

- szintaxis: ha a nyilak azt mutatják, hogy felcserélted a paramétereket, akkor helyes
- tartalom: helyes megoldás

#### Példa helyes megoldásra:

$\exists x(N(x) \land P(k,x) \land P(d,x))$

------------------------------------------------

### B: *csak a férfiak között vannak gyermektelenek*

#### Megoldásod:

$\exists f(F(f) \land \neg P(f,x) \land \nexists u(N(u) \land \neg P(u,y)$

#### Visszajelzés:

- szintaxis: lemaradt pár zárójel, a $\neg P(f,x)$ után és a legvégéről (továbbá kissé olvashatatlan az egész)
- tartalom: $x$ és $y$ nem konkrét személyek, ezért kvantorral meg kell őket kötni (nem létezik egy $x/y$ sem, aki $f/u$-nak a gyereke)

#### Példa helyes megoldásra:

$\forall x(\nexists y(P(x,y)) \Rightarrow F(x)) \land \exists x(\nexists y(P(x,y)))$

vagy: $\exists f(F(f) \land \nexists x(P(f,x))) \land \nexists n(N(n) \land \nexists y(P(n,y)))$

------------------------------------------------

### C: *vannak egynemű testvérek*

#### Megoldásod:

$\exists f(F(f)) \land \exists u(N(u) \land \exists y(P(f,y) \land P(u,y)) \land \exists z(P(f,z) \land P(u,z)$

#### Visszajelzés:

- szintaxis: a zárójelezés kicsit zavaros, úgy lenne helyes, hogy $\exists f(F(f) \land \exists u(N(u) \land \exists y(P(f,y) \land P(u,y)) \land \exists z(P(f,z) \land P(u,z))))$
- tartalom: $y$-ról és $z$-ről csak azt állítod, hogy testvérek, azt kihagytad, hogy egyneműek

#### Példa helyes megoldásra:

$\exists (x,y,m,f)((N(x) \Leftrightarrow N(y)) \land N(m) \land P(m,x) \land P(m,y) \land F(f) \land P(f,x) \land P(f,y))$

vagy: $\exists (x,y,m,f)(((F(x) \land F(y)) \lor (N(x) \land N(y))) \land N(m) \land P(m,x) \land P(m,y) \land F(f) \land P(f,x) \land P(f,y))$