'''##include <stdio.h>
#int main ()
{
    float n1, n2, n3, media;
    print("MEDIA DA PROVA\n");
    print{"Digite a primeira nota:"};
    scanf("%f",&n1);
    print{"Digite a segunda nota:"};
    scanf("%f",&n2);
    print("Digite a terceira nota:");
    scanf("%f",&n3);
    media = n1 + n2 + n3;
    if(media >= 7){
        printf("Ta voando, cachorro, passou de ano!");
    }
    elif(media >=5 ){
        print("Ta na corda bamba, bulldog...Recuperacao ");
    }
    else{
        print("Fe em Deus que ele eh justo, reprovado!")
    }
    return 0;

}##'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
print(f"MÉDIA DA PROVA FOI {media:.2f}")

if media >= 7:
    print("Ta voando, cachorro, passou de ano!")
elif media >= 5:
    print("Ta na corda bamba, bulldog... Recuperação!")
else:
    print("Fé em Deus que ele é justo, reprovado!")