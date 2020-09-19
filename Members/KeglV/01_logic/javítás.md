**Általánosan: végig a *metszet* halmazművelet jelét ($\cap) használtad az *és* logikai művelet jele ($\land$) helyett. Bár van fogalmi kapcsolat a kettő között, ezeket jobb nem keverni.**

### A: *k-nak és d-nek van közös lánya*

#### Megoldásod:

$\exists y(P(y,k) \land P(y,d))$

#### Visszajelzés:

- szintaxis: a $P$ predikátum paramétereit felcserélted, így azt állítod, hogy $k$ és $d$ $y$ gyerekei
- tartalom: hiányzik, hogy $y$ nő

#### Példa helyes megoldásra:

$\exists x(N(x) \land P(k,x) \land P(d,x))$

------------------------------------------------

### B: *csak a férfiak között vannak gyermektelenek*

#### Megoldásod:

$\exists x(F(x) \land \nexists y(P(x,y))) \land \nexists z(N(z) \land \nexists z(P(z,y)))$

#### Visszajelzés:

- szintaxis: szerintem a végén elírtad a paramétereket, annak lenne értelme, hogy $...\land \nexists y(P(z,y)))$
- tartalom: ha a fenti hiba tényleg csak elírás, akkor különben jó a megoldás

#### Példa helyes megoldásra:

$\forall x(\nexists y(P(x,y)) \Rightarrow F(x)) \land \exists x(\nexists y(P(x,y)))$

vagy ahogy te csináltad, a javítással együtt

------------------------------------------------

### C: *vannak egynemű testvérek*

#### Megoldásod:

$\exists a(F(a) \land P(a,x) \land P(a,y)) \land \exists b(F(b) \land P(b,x) \land P(a,x))$

#### Visszajelzés:

- szintaxis: a paramétereket a vége felé eléggé összekeverted, ha $a$ és $b$ az egynemű testvérek, és $x,y$ a szüleik, akkor úgy lenne értelme, hogy $\exists a(F(a) \land P(x,a) \land P(y,a)) \land \exists b(F(b) \land P(x,b) \land P(y,b))$
- tartalom:
    - de így még mindig nem vagyunk meg, mert $x$ és $y$ nem konkrét személyek, tehát egy kvantorral meg kell kötni őket (létezik olyan $x,y$, akik $a,b$ szülei)
    - a másik, hogy te azt állítod, **vannak fiútestvérek**, pedig az eredeti állítás **csak az egyneműséget követeli meg**

#### Példa helyes megoldásra:
*Én kikötöm, hogy az egyik szülő nő, a másik férfi, mert biológiai testvérekként értelmezem az állításban szereplőket, de ezt el lehet hagyni.*

$\exists (x,y,m,f)((N(x) \Leftrightarrow N(y)) \land N(m) \land P(m,x) \land P(m,y) \land F(f) \land P(f,x) \land P(f,y))$

vagy: $\exists (x,y,m,f)(((F(x) \land F(y)) \lor (N(x) \land N(y))) \land N(m) \land P(m,x) \land P(m,y) \land F(f) \land P(f,x) \land P(f,y))$