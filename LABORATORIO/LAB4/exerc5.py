# A duração de um mês varia de 28 a 31 dias. Neste exercício, você criará um programa que lê o nome de um mês do usuário como uma string. Em seguida, seu programa deve exibir o número de dias naquele mês. Exiba “28 ou 29 dias” para fevereiro para que os anos bissextos sejam considerados.
mes = input("")

if(mes == "janeiro"):
    print("31 dias")
elif(mes == "fevereiro"):
    print("28 ou 29 dias")
elif(mes == "março"):
    print("31 dias")
elif(mes == "abril"):
    print("30 dias")
elif(mes == "maio"):
    print("31 dias")
elif(mes == "junho"):
    print("30 dias")
elif(mes == "julho"):
    print("31 dias")
elif(mes == "agosto"):
    print("31 dias")
elif(mes == "setembro"):
    print("30 dias")
elif(mes == "outubro"):
    print("31 dias")
elif(mes == "novembro"):
    print("30 dias")
elif(mes == "dezembro"):
    print("31 dias")