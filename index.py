V=int(input())
D=int(input())
saldo=V-D
if saldo <10:
    nível="Ferro"
    print("O Herói tem saldo de",saldo,"está no nível de",nível)
elif saldo >=11 and saldo <=20:
    nível="Bronze"
    print("O Herói tem saldo de",saldo,"está no nível de",nível)
elif saldo >=21 and saldo <=50:
    nível="Prata"
    print("O Herói tem saldo de",saldo,"está no nível de",nível)
elif saldo >=51 and saldo <=80:
    nível="Ouro"
    print("O Herói tem saldo de",saldo,"está no nível de",nível)
elif saldo >=81 and saldo <=90:
    nível="Diamante"
    print("O Herói tem saldo de",saldo,"está no nível de",nível)
elif saldo >=91 and saldo <=100:
    nível="Lendário"
    print("O Herói tem saldo de",saldo,"está no nível de",nível)
elif saldo >=101:
    nível="Imortal"
    print("O Herói tem saldo de",saldo,"está no nível de",nível)