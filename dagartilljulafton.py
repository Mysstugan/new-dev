import datetime
from datetime import datetime

idag = datetime.now()
julafton = datetime(idag.year, 12, 24)
skillnad = julafton - idag
resultat = skillnad.days

if resultat > 0:
    print(resultat, "dagar till julafton")
elif resultat == 0:
    print("God jul!")
elif final < 0:
    print("Julafton har redan varit")


