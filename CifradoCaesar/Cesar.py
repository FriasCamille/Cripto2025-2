
A=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

diccionario = {A[i]: i for i in range(len(A))}
frase=input("Ingrese la frase a cifrar:_")
frase=frase.upper()
k=int(input("Ingrese la llave:_"))
codigo=[]
cifrado=[]
for i in frase:
    codigo.append(diccionario[i])
j=0
for i in codigo:
    codigo[j]=(i+k)%len(A)
    j+=1 

for i in codigo:
    cifrado.append(A[i])

print(f"El cifrado es: {cifrado}")