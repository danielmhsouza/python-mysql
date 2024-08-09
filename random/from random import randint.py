from random import randint
secret = randint(1,100)
n = 0
print("olá")
while n != secret:
    n = int(input("adivinhe o número:"))
    if n > secret:
        print("mais baixo")
    elif n < secret:
        print("mais alto")
    else:
        print("Acertou mizeravel")
 
