I1 = float(input('Enter price of the first item: ')) 
I2 = float(input('Enter price of the second item: ')) 
Y = True 
y = True 
N = False 
n = False 
CC = str(input('Does customer have a club card? (Y/N): ')) 
Tr = float(input('Enter tax rate, e.g. 5.5 for 5.5% tax: '))

BP = I1 + I2

if (I1 >= I2): PD1 = (I2/2) + I1

else: PD1 = (I1/2) + I2

if CC == Y or y: PD2 = PD1 * 0.9

elif CC == N or n: PD2 == PD1

T = (Tr/100)*PD2 
F = T+PD2

print('Base price =', "{:.2f}".format(BP)) 
print('Price after discounts =', "{:.2f}".format(PD2)) 
print('Total price =', "{:.2f}".format(F))