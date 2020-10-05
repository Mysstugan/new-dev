
summa = 0 
print("Mata in 0 för att avsluta programmet")
alla_nummer = []

while True:

    num = int(input("Mata in ett tal: "))
    
    if num == 0:
        break

    print(f"Du matade in {num}")
    
    summa = summa + num
    
    print(f"Summan är {summa}")
    
    alla_nummer.insert(0,num)
    talatträkna = len(alla_nummer)
    if talatträkna > 3:
        talatträkna = 3
    
    medelvärde = 0

    

    