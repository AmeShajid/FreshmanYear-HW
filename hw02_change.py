#Ame Shajid
#January 22, 2023
#this program  takes input the number of Quadrans a person has in their account. Then it print out the minimal number of coins that can be used to represent this amount.

#right here it asks for the quadrans value
quadrans = int(input("Enter Number of Quadrans: "))

#right here is the calculations for the differnt coins
#first Aureus divide it by 1600 for main value then by modulus to add on the calculations to the next coin
Aureus = quadrans // 1600
Aureus1 = quadrans % 1600
#next coin we do 800 this time and then same thing divide by modulus for next value
GoldQuinarius = Aureus1 // 800
GoldQuinarius1 = Aureus1 % 800
#next coin divide by 128 this time then devide by modulus to add on for next coin.
Antoninianus = GoldQuinarius1 // 128 
Antoninianus1 = GoldQuinarius1 % 128
#next coin divide by 64 this time then devide by modulus to add on for next coin.
Denarius =  Antoninianus1 // 64
Denarius1 = Antoninianus1 % 64
#next coing divide by 32 this time then devide by modulus to add on for next coin.
Quinarius = Denarius1 // 32
Quinarius1 = Denarius1 % 32
#next coing divide by 16 this time then devide by modulus to add on for next coin.
Sestertius = Quinarius1 // 16
Sestertius1 =Quinarius1 % 16
#next coin  divide by 8 this time then devide by modulus to add on for next coin.
Dupondius = Sestertius1 // 8
Dupondius1 = Sestertius1 % 8 
#next coin  divide by 4 this time then devide by modulus to add on for next coin.
As = Dupondius1 // 4
As1 = Dupondius1 % 4
#next coin divide by 2 this time then devide by modulus to add on for next coin.
Semis = int(As1// 2)
Semis1 = As1 % 2
# now its just the quadrans so divide by the modulus semis1 and then thats it
Quadrans = int(Semis1 // 2)


#over here it prints the values out after getting the values
print(f'Aureus: {Aureus}')
print(f'Gold Quinarius: {GoldQuinarius}')
print(f'Antoninianus: {Antoninianus}')
print(f'Denarius: {Denarius}')
print(f'Quinarius: {Quinarius}')
print(f'Sestertius: {Sestertius}')
print(f'Dupondius: {Dupondius}')
print(f'As: {As}')
print(f'Semis: {Semis}')
print(f'Quadrans: {Quadrans}')