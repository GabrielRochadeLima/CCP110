def ler_arquivo(nome_arquivo):
    """
    Lê o arquivo UTF-8 e retorna uma lista de linhas limpas.
    Retorna lista vazia se o arquivo não existir.
    """
    linhas = []
    try:
        arquivo = open(nome_arquivo, "r", encoding="utf-8")
        for linha in arquivo:
            linha_limpa = linha.strip()
            if linha_limpa:
                linhas.append(linha_limpa)
        arquivo.close()
    except FileNotFoundError:
        return []
    return linhas

def escrever_arquivo(nome_arquivo, linhas):
    try:
        arquivo = open(nome_arquivo, "w", encoding="utf-8")
        for item in linhas:
            texto = str(item)
            arquivo.write(texto + "\n")
        arquivo.close()
    except Exception as erro:
        print(f"Erro ao gravar o arquivo '{nome_arquivo}': {erro}")

def adicionar_linha(nome, linha):
    with open(nome, "a", encoding="utf-8") as f:
        f.write(linha + "\n")

# ---------- Utilidades de preço/formatos ----------

def parse_preco(txt):
    """Converte '12,50' ou '12.50' para float 12.5"""
    return float(txt.replace(",", ".").strip())

def brl(valor):
    """Formata float em padrão BR: R$xx,xx"""
    return f"R${valor:.2f}".replace(".", ",")

# ---------- Cadastro e login ----------

def cadastrar_usuario():

    # --- valida nome ---
    while True:
        nome = input("Nome: ").strip()
        if nome:
            break
        print("O nome não pode ser vazio!\n")

    # --- valida email ---
    while True:
        email = input("Email: ").strip().lower()
        if email:
            break
        print("O e-mail não pode ser vazio!\n")

    # --- valida senha ---
    while True:
        senha = input("Senha: ").strip()
        if senha:
            break
        print("A senha não pode ser vazia!\n")

    # --- verifica se email já existe ---
    usuarios = ler_arquivo("usuarios.txt")
    for u in usuarios:
        partes = u.split(";")
        if len(partes) >= 2 and email == partes[1]:
            print("Email já cadastrado!\n")
            return

    # --- grava novo usuário ---
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{nome};{email};{senha}\n")

    print("Usuário cadastrado com sucesso!\n")

def login():
    """
    Pede email e senha ao usuário e verifica se estão no arquivo usuarios.txt.
    Retorna o email normalizado se o login for bem-sucedido.
    """

    # --- valida email ---
    while True:
        email_digitado = input("Email: ").strip().lower()
        if email_digitado:
            break
        print("O e-mail não pode ser vazio!\n")

    # --- valida senha ---
    while True:
        senha_digitada = input("Senha: ").strip()
        if senha_digitada:
            break
        print("A senha não pode ser vazia!\n")

    # --- leitura dos usuários ---
    linhas_usuarios = ler_arquivo("usuarios.txt")

    for linha in linhas_usuarios:
        linha = linha.strip()
        if not linha:
            continue

        campos = linha.split(";")
        if len(campos) < 3:
            continue

        nome_arquivo = campos[0].strip()
        email_arquivo = campos[1].strip().lower()
        senha_arquivo = campos[2].strip()

        if email_arquivo == email_digitado and senha_arquivo == senha_digitada:
            print(f"Bem-vindo(a), {nome_arquivo}!\n")
            return email_digitado

    print("Email ou senha incorretos.\n")
    return



# ---------- Cardápio ----------

def mostrar_alimentos():
    alimentos = ler_arquivo("alimentos.txt")
    if not alimentos:
        print("Nenhum alimento cadastrado.\n")
        return []
    print("\n--- CARDÁPIO FEIFOOD ---")
    for i, a in enumerate(alimentos, start=1):
        try:
            nome, preco = a.split(";")
        except ValueError:
            continue
        print(f"{i}. {nome} - {brl(parse_preco(preco))}")
    print()
    return alimentos

# ---------- Pedidos com número por usuário e quantidades ----------

def proximo_numero_pedido(email_usuario: str) -> int:
    """
    Retorna o próximo número de pedido para o usuário informado.
    Lê 'pedidos.txt', encontra o maior número usado por esse usuário
    e retorna o próximo número disponível (ou 1, se for o primeiro pedido).
    """
    lista = ler_arquivo("pedidos.txt")
    maior_numero = 0
    prefixo_usuario = email_usuario + ";"

    for linha in lista:
        # se na linha da lista não começar com o email da pessoa logada não processa
        if not linha.startswith(prefixo_usuario):
            continue

        partes = linha.split(";", 3)
        if len(partes) < 2:
            continue

        numero_texto = partes[1].strip()
        if not numero_texto.isdigit():
            continue

        numero_inteiro = int(numero_texto)
        if numero_inteiro > maior_numero:
            maior_numero = numero_inteiro

    return maior_numero + 1


def _parse_escolhas(entrada, total_itens):
    """
    Converte '1x2,3,5x4' em [(0,2), (2,1), (4,4)] (índice zero).
    Aceita 'n' (qtd 1) ou 'nxm' (qtd m). Ignora inválidos.
    """
    pares = []
    for ped in entrada.split(","):
        ped = ped.strip()
        if not ped:
            continue
        if "x" in ped.lower():
            n_str, q_str = ped.lower().split("x", 1)
            if not (n_str.strip().isdigit() and q_str.strip().isdigit()):
                continue
            idx = int(n_str) - 1
            qtd = int(q_str)
        else:
            if not ped.isdigit():
                continue
            idx = int(ped) - 1
            qtd = 1
        if 0 <= idx < total_itens and qtd > 0:
            pares.append((idx, qtd))
    return pares

def fazer_pedido(email_usuario):
    alimentos = mostrar_alimentos()
    if not alimentos:
        return

    print("Digite os números (com quantidade opcional) separados por vírgula.")
    print("Exemplos: 1,3,5   ou   1x2,3x1,5x4")
    entrada = input("Escolha: ").strip()
    if not entrada:
        print("Pedido cancelado.\n")
        return

    escolhas = _parse_escolhas(entrada, len(alimentos))
    if not escolhas:
        print("Nenhuma escolha válida.\n")
        return

    # Monta carrinho com subtotais
    itens_pedido = []  # [(nome, preco_unit, qtd, subtotal)]
    total = 0.0
    for idx, qtd in escolhas:
        try:
            nome, preco_txt = alimentos[idx].split(";")
        except ValueError:
            continue
        preco_unit = parse_preco(preco_txt)
        subtotal = preco_unit * qtd
        itens_pedido.append((nome, preco_unit, qtd, subtotal))
        total += subtotal

    if not itens_pedido:
        print("Nenhum item válido selecionado.\n")
        return

    print("\n--- ITENS DO PEDIDO ---")
    for nome, preco_unit, qtd, subtotal in itens_pedido:
        print(f"- {nome} x{qtd}  ({brl(preco_unit)} cada)  = {brl(subtotal)}")
    print(f"Total: {brl(total)}")

    confirmar = input("Confirmar pedido? (s/n): ").strip().lower()
    if confirmar != "s":
        print("Pedido cancelado.\n")
        return

    numero_pedido = proximo_numero_pedido(email_usuario)
    # salva itens como 'Nome xQtd' separados por vírgula
    itens_texto = ",".join(f"{nome} x{qtd}" for (nome, _, qtd, _) in itens_pedido)
    adicionar_linha("pedidos.txt", f"{email_usuario};{numero_pedido};{itens_texto};{total:.2f};")
    print(f"Pedido #{numero_pedido} realizado com sucesso!\n")

# ---------- Visualizar pedidos agrupados ----------

def ver_pedidos(email_usuario):
    pedidos = ler_arquivo("pedidos.txt")
    print("\n--- SEUS PEDIDOS ---")
    encontrou = False
    for p in pedidos:
        dados = p.split(";")
        if len(dados) < 4:
            continue
        email, num, itens, total = dados[:4]
        nota = dados[4] if len(dados) > 4 and dados[4] else "Sem nota"
        if email == email_usuario:
            print(f"\nPedido #{num}")
            for item in itens.split(","):
                print(f"  - {item.strip()}")
            try:
                total_f = float(total)
            except ValueError:
                total_f = 0.0
            print(f"Total: {brl(total_f)}")
            print(f"Avaliação: {nota}")
            encontrou = True
    if not encontrou:
        print("Nenhum pedido encontrado.\n")

# ---------- Buscar alimentos ----------

def listar_info_alimentos(alimentos_lista):
    if not alimentos_lista:
        print("Nenhum alimento encontrado.\n")
        return
    print("\n--- RESULTADOS DA BUSCA ---")
    for i, (nome, preco_str) in enumerate(alimentos_lista, start=1):
        try:
            preco_fmt = brl(parse_preco(preco_str))
        except Exception:
            preco_fmt = f"R${preco_str}"
        print(f"{i}. {nome} - {preco_fmt}")
    print()

def buscar_por_alimento():
    termo = input("Digite parte do nome do alimento para buscar: ").strip().lower()
    if not termo:
        print("Busca cancelada.\n")
        return

    linhas = ler_arquivo("alimentos.txt")
    resultados = []
    for linha in linhas:
        try:
            nome, preco = linha.split(";")
        except ValueError:
            continue
        if termo in nome.lower():
            resultados.append((nome, preco))

    listar_info_alimentos(resultados)

# ---------- Avaliar um pedido inteiro (com proteção para reavaliação) ----------

def avaliar_pedido(email_usuario):
    pedidos = ler_arquivo("pedidos.txt")
    meus_pedidos = [p for p in pedidos if p.startswith(email_usuario + ";")]

    if not meus_pedidos:
        print("Você ainda não possui pedidos.\n")
        return

    print("\n--- PEDIDOS PARA AVALIAR ---")
    for p in meus_pedidos:
        dados = p.split(";")
        if len(dados) < 4:
            continue
        _, num, itens, total, *resto = dados
        nota_atual = (resto[0] if resto else "").strip()
        print(f"\nPedido #{num}")
        for item in itens.split(","):
            print(f"  - {item.strip()}")
        try:
            total_f = float(total)
        except ValueError:
            total_f = 0.0
        print(f"Total: {brl(total_f)}")
        print(f"Avaliação atual: {nota_atual if nota_atual else 'Sem nota'}")

    escolha = input("\nDigite o número do pedido que deseja avaliar: ").strip()
    if not escolha.isdigit():
        print("Número inválido.\n")
        return

    novos_pedidos = []
    alterado = False
    for p in pedidos:
        dados = p.split(";")
        if len(dados) < 4:
            novos_pedidos.append(p)
            continue
        email, num, itens, total = dados[:4]
        nota_existente = dados[4].strip() if len(dados) > 4 else ""

        if email == email_usuario and num == escolha:
            if nota_existente:
                resp = input(f"Este pedido já possui nota {nota_existente}. Deseja atualizar? (s/n): ").strip().lower()
                if resp != "s":
                    print("Avaliação mantida.\n")
                    return
            # valida nota 0..5
            nota_in = input("Digite sua nota de 0 a 5: ").strip().replace(",", ".")
            try:
                nota_val = float(nota_in)
                if not (0.0 <= nota_val <= 5.0):
                    raise ValueError
            except ValueError:
                print("Nota inválida. Use um número entre 0 e 5.\n")
                return
            nota_fmt = f"{nota_val:.1f}"
            novos_pedidos.append(f"{email};{num};{itens};{total};{nota_fmt}")
            alterado = True
        else:
            novos_pedidos.append(p)

    if alterado:
        escrever_arquivo("pedidos.txt", novos_pedidos)
        print("Avaliação registrada!\n")
    else:
        print("Pedido não encontrado.\n")

def editar_pedido(email_usuario):
    """
    Permite EDITAR um pedido do usuário (apenas pedidos sem avaliação).
    """
    pedidos = ler_arquivo("pedidos.txt")
    meus = [p for p in pedidos if p.startswith(email_usuario + ";")]

    if not meus:
        print("Você ainda não possui pedidos.\n")
        return

    print("\n--- SEUS PEDIDOS (para editar) ---")
    for p in meus:
        dados = p.split(";")
        if len(dados) < 4:
            continue
        _, num, itens, total, *resto = dados
        nota_atual = (resto[0] if resto else "").strip()
        status = "avaliado" if nota_atual else "em aberto"
        print(f"\nPedido #{num}  [{status}]")
        for item in itens.split(","):
            print(f"  - {item.strip()}")
        try:
            total_f = float(total)
        except ValueError:
            total_f = 0.0
        print(f"Total atual: {brl(total_f)}")
        if nota_atual:
            print(f"Nota: {nota_atual}")

    alvo = input("\nDigite o número do pedido que deseja editar: ").strip()
    if not alvo.isdigit():
        print("Número inválido.\n")
        return

    # Localiza o pedido selecionado e verifica se pode editar (sem nota)
    indice_no_arquivo = None
    email, num, itens_antigos, total_antigo, nota_existente = None, None, None, None, ""

    for i, p in enumerate(pedidos):
        dados = p.split(";")
        if len(dados) < 4:
            continue
        e, n, itens, total = dados[:4]
        nota = dados[4].strip() if len(dados) > 4 else ""
        if e == email_usuario and n == alvo:
            indice_no_arquivo = i
            email, num, itens_antigos, total_antigo, nota_existente = e, n, itens, total, nota
            break

    if indice_no_arquivo is None:
        print("Pedido não encontrado.\n")
        return

    if nota_existente:
        print("Este pedido já foi avaliado e não pode ser editado.\n")
        return

    # Mostra cardápio e pede NOVA seleção
    alimentos = mostrar_alimentos()
    if not alimentos:
        return

    print("Digite a NOVA seleção (com quantidades opcionais).")
    print("Exemplos: 1,3,5   ou   1x2,3x1,5x4")
    entrada = input("Nova escolha: ").strip()
    if not entrada:
        print("Edição cancelada.\n")
        return

    escolhas = _parse_escolhas(entrada, len(alimentos))
    if not escolhas:
        print("Nenhuma escolha válida.\n")
        return

    # Monta novo carrinho
    itens_pedido = []  # [(nome, preco_unit, qtd, subtotal)]
    total = 0.0
    for idx, qtd in escolhas:
        try:
            nome, preco_txt = alimentos[idx].split(";")
        except ValueError:
            continue
        preco_unit = parse_preco(preco_txt)
        subtotal = preco_unit * qtd
        itens_pedido.append((nome, preco_unit, qtd, subtotal))
        total += subtotal

    if not itens_pedido:
        print("Nenhum item válido selecionado.\n")
        return

    print("\n--- NOVO RESUMO DO PEDIDO ---")
    for nome, preco_unit, qtd, subtotal in itens_pedido:
        print(f"- {nome} x{qtd}  ({brl(preco_unit)} cada)  = {brl(subtotal)}")
    print(f"Total novo: {brl(total)}")

    confirmar = input("Salvar alterações? (s/n): ").strip().lower()
    if confirmar != "s":
        print("Edição cancelada. Nada foi alterado.\n")
        return

    # Gera nova linha e substitui no arquivo (nota continua vazia)
    itens_texto = ",".join(f"{nome} x{qtd}" for (nome, _, qtd, _) in itens_pedido)
    nova_linha = f"{email};{num};{itens_texto};{total:.2f};"

    pedidos[indice_no_arquivo] = nova_linha
    escrever_arquivo("pedidos.txt", pedidos)
    print(f"Pedido #{num} atualizado com sucesso!\n")

# ---------- Menus ----------

def menu_usuario(email):
    while True:
        print("1 - Ver cardápio")
        print("2 - Fazer pedido")
        print("3 - Ver meus pedidos")
        print("4 - Avaliar pedido")
        print("5 - Editar pedido")
        print("6 - Buscar alimento")
        print("7 - Sair da conta")
        op = input("Escolha: ").strip()

        if op == "1":
            mostrar_alimentos()
        elif op == "2":
            fazer_pedido(email)
        elif op == "3":
            ver_pedidos(email)
        elif op == "4":
            avaliar_pedido(email)
        elif op == "5":
            editar_pedido(email)
        elif op == "6":
            buscar_por_alimento()
        elif op == "7":
            print("Saindo...\n")
            break
        else:
            print("Opção inválida!\n")

def main():
    while True:
        print("=== FEIFOOD ===")
        print("1 - Cadastrar usuário")
        print("2 - Fazer login")
        print("3 - Sair")
        op = input("Escolha: ").strip()
        if op == "1":
            cadastrar_usuario()
        elif op == "2":
            email = login()
            if email:
                menu_usuario(email)
        elif op == "3":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!\n")

# ---------- Execução ----------
if __name__ == "__main__":
    main()
