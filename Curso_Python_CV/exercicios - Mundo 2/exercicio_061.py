primeirotermo= int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
quantidade = 10
contador = 0 

while contador < quantidade:
    print(primeirotermo, end=" → ")  
    primeirotermo = primeirotermo + razao  
    contador += 1  

print("FIM")  