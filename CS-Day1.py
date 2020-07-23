# Decimal to Binary 

#input 
n = 1743

binary = "" 

while n >= 1:
  remainder = str(n % 2) 
  binary = remainder + binary 
  n = n // 2

#output
print(binary)
