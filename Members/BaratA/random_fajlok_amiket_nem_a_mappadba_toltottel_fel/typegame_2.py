gemmell = 1948
legend, saga= ["druss", "drenai"] 
trusag = ""
for year in range(2020 - 1948):
    for betu in saga:
        for megegy_betu in legend:
            if betu == megegy_betu and len(trusag) <= year * 30:
                trusag += betu * year 
if len(trusag) > 4000:
    megoldas = "rák"
elif len(trusag) > 3000:
    megoldas = 1
elif len(trusag) > 2000:
    megoldas = 30/30
elif len(trusag) > 1000:
    megoldas = ["chronicles", "rigante", "waylander"]  
megoldas
print(len(trusag))