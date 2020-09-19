### A: *k-nak és d-nek van közös lánya*

#### Megoldásod:

$\exists x(N(x) \land P(k,x) \land P(d,x))$

#### Visszajelzés:

- szintaxis: tökéletes
- tartalom: tökéletes

#### Példa helyes megoldásra:

amit te is írtál

------------------------------------------------

### B: *csak a férfiak között vannak gyermektelenek*

#### Megoldásod:

$\nexists x(N(x) \land \neg P(x,z)) \land \exists y(F(y) \land \neg P(y,q))$

#### Visszajelzés:

- szintaxis: jó, de a tartalmi hibák vannak
- tartalom: ezzel azt mondod, hogy **nincs olyan nő, akinek $z$ nem a gyereke (tehát $z$ minden nőnek a gyereke), és van olyan férfi, akinek $q$ nem a gyereke**. $z$-t és $q$-t kvantorral kell megkötni ahhoz, hogy azt jelentse a kifejezés, mint az eredeti állítás (nincs olyan nő, akinek **egy $z$ sem a gyereke**, és van olyan férfi, akinek **egy $q$ sem a gyereke**)

#### Példa helyes megoldásra:

$\forall x(\nexists y(P(x,y)) \Rightarrow F(x)) \land \exists x(\nexists y(P(x,y)))$

vagy: $\exists f(F(f) \land \nexists x(P(f,x))) \land \nexists n(N(n) \land \nexists y(P(n,y)))$

------------------------------------------------

### C: *vannak egynemű testvérek*

#### Megoldásod:

$\exists x \land y(F(x) \land F(y) \land P(z,x) \land P(q,x) \land P(z,y) \land P(q,y))$

#### Visszajelzés:

- szintaxis: olyan nincs, hogy $\exists x \land y$, itt az *és* szót vesszővel kell jelölni ($\exists x,y$)
- tartalom:
    - egyrészt azt állítod csak, hogy **fiútestvérek vannak**, pedig az eredeti állítás **csak az egyneműséget követeli meg**
    - másrészt $z$-t és $q$-t is kvantorral kell megkötni, mert nem konkrét személyek

#### Példa helyes megoldásra:
*Én kikötöm, hogy az egyik szülő nő, a másik férfi, mert biológiai testvérekként értelmezem az állításban szereplőket, de ezt el lehet hagyni.*

$\exists (x,y,m,f)((N(x) \Leftrightarrow N(y)) \land N(m) \land P(m,x) \land P(m,y) \land F(f) \land P(f,x) \land P(f,y))$

vagy: $\exists (x,y,m,f)(((F(x) \land F(y)) \lor (N(x) \land N(y))) \land N(m) \land P(m,x) \land P(m,y) \land F(f) \land P(f,x) \land P(f,y))$