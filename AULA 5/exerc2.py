a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))
c = int(input("Digite outro valor: "))

if( a != b) and (b != a) and (c != a):
    
    if(a > b and b > c):
        print(a,b,c)
    elif(a > c and c > b):
        print(a,c,b)
    elif(b > a and c > a):
        print(b,c,a)
    elif(b > a and a > c):
        print(b,a,c)



        


else:
    print("Valores inválidos, digite números diferentes uns dos  outros")    

