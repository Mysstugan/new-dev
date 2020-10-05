#2 Skriv namn och filstorlek på
#ut alla textfiler som finns i ett speciellt bibliotek

import os
import sys



for filename in os.listdir('c:\\Users\\tobia\\Desktop'): 
     s = os.path.getsize('c:\\Users\\tobia\\Desktop' + filename)
     print(f"{filename} is {s} bytes")

