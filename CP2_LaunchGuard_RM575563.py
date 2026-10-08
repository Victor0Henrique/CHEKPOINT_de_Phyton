# variaveis para registrar que aquele processo ja foi feito
oferta_salva = False

# variaveis globais com as necessidades da ONG (meta e quanto ja foi concluido)
# os valores sao ficticios por enquanto
kits_meta = 300
kits_concluidos = 100

transporte_meta = 4
transporte_concluidos = 1

divulgacao_meta = 3
divulgacao_concluidos = 0

financeiro_meta = 5000
financeiro_concluidos = 0

# variaveis globais para guardar a oferta do apoiador
apoiador_nome = ""
apoiador_contato = ""
tipo_apoio = ""
necessidade_atendida = ""
descricao_apoio = ""
quantidade_apoio = 0
prazo_dias = 0
autoriza_divulgacao = False

# status da oferta: "prometido", "confirmado" ou "concluido"
status_oferta = ""
publicado = False
proximo_contato = ""


# separamos as funcionalidades em funcoes para organizacao do codigo

# funcao que mostra o resumo da oferta
def mostrar_resumo_oferta():
    print("RESUMO DA OFERTA")
    print(f"Apoiador: {apoiador_nome}")
    print(f"Contato: {apoiador_contato}")
    print(f"Tipo de apoio: {tipo_apoio}")
    print(f"Necessidade atendida: {necessidade_atendida}")
    print(f"Descrição: {descricao_apoio}")
    print(f"Quantidade: {quantidade_apoio}")
    print(f"Status: {status_oferta.upper()}")

# funcionalidade 1 - necessidades da ONG e impacto

def mostrar_necessidades_e_impacto():
    print("\nNECESSIDADES DA ONG")
    print(f"- Kits de higiene bucal: {kits_concluidos} de {kits_meta} kits")
    print(f"- Transporte de materiais: {transporte_concluidos} de {transporte_meta} entregas")
    print(f"- Divulgação nas redes sociais: {divulgacao_concluidos} de {divulgacao_meta} ações")
    print(f"- Apoio financeiro: R$ {financeiro_concluidos} de R$ {financeiro_meta}")

    print("\nIMPACTO: UMA AULA QUE CONTINUOU EM CASA")
    print("Uma atividade de higiene bucal em uma escola só foi possível com a ajuda de:")
    print("- Horizonte Dental (Empresa): 60 kits de higiene bucal")
    print("- Marina Costa (Apoiadora): 40 kits de higiene bucal")
    print("- Rota Solidária (Empresa): transporte dos materiais")

    # se o apoiador autorizou e a equipe aprovou, ele aparece como colaborador
    if publicado == True:
        print(f"- {apoiador_nome}: {quantidade_apoio} ({tipo_apoio})")

# funcionalidade 2 - oferecer apoio

def realizar_oferta():
    global oferta_salva, apoiador_nome, apoiador_contato, tipo_apoio, necessidade_atendida
    global descricao_apoio, quantidade_apoio, prazo_dias, autoriza_divulgacao
    global status_oferta, publicado, proximo_contato

    print("\nOFERECER APOIO")

    print("Tipos de apoio:")
    print("1 - Material")
    print("2 - Serviço")
    print("3 - Divulgação")
    print("4 - Financeiro")

    # loop para forcar o usuario a escolher uma opcao valida
    opcao = 0
    while opcao < 1 or opcao > 4:
        opcao = int(input("Digite o número do tipo de apoio (1-4): "))
        if opcao < 1 or opcao > 4:
            print("Opção inválida.")

    # de acordo com o tipo, ja ligamos o apoio a uma necessidade da ONG
    if opcao == 1:
        tipo_apoio = "material"
        necessidade_atendida = "Kits de higiene bucal"
    elif opcao == 2:
        tipo_apoio = "serviço"
        necessidade_atendida = "Transporte de materiais"
    elif opcao == 3:
        tipo_apoio = "divulgação"
        necessidade_atendida = "Divulgação nas redes sociais"
    else:
        tipo_apoio = "financeiro"
        necessidade_atendida = "Apoio financeiro"

    apoiador_nome = input("Digite seu nome (pessoa ou empresa): ")
    apoiador_contato = input("Digite seu e-mail ou telefone: ")
    descricao_apoio = input("Descreva o que você vai oferecer: ")

    # a quantidade precisa ser maior que zero
    quantidade_apoio = 0
    while quantidade_apoio <= 0:
        quantidade_apoio = int(input("Digite a quantidade (itens, ações ou valor em R$): "))
        if quantidade_apoio <= 0:
            print("A quantidade precisa ser maior que zero.")

    prazo_dias = int(input("Em quantos dias consegue entregar? (0 se não souber): "))

    # loop para garantir que o usuario responda sim ou nao
    resposta = ""
    while resposta != "s" and resposta != "n":
        resposta = input("Autoriza divulgar seu nome como colaborador? (s/n): ").lower()

    if resposta == "s":
        autoriza_divulgacao = True
    else:
        autoriza_divulgacao = False

    # toda oferta nova comeca como apoio prometido
    status_oferta = "prometido"
    publicado = False
    proximo_contato = "Equipe analisar a oferta e responder ao apoiador"
    oferta_salva = True

    print("\nOferta registrada com sucesso!\n")
    mostrar_resumo_oferta()

# funcionalidade 3 - acompanhar minha oferta

def acompanhar_oferta():
    print("\nACOMPANHAR MINHA OFERTA")

    # so da pra acompanhar se ja existe uma oferta
    if oferta_salva == False:
        print("\nVocê ainda não fez nenhuma oferta. Use a opção 2 do menu.\n")
    else:
        mostrar_resumo_oferta()

        if status_oferta == "prometido":
            print("Seu apoio foi prometido e está aguardando análise da equipe.")
        elif status_oferta == "confirmado":
            print("Seu apoio foi confirmado! A equipe vai combinar os detalhes.")
        else:
            print("Seu apoio foi concluído. Muito obrigado!")

        if publicado == True:
            print("Seu resultado já foi publicado na área de impacto.")

# funcionalidade 4 - painel interno da ONG (equipe)

def painel_equipe():
    global status_oferta, publicado, proximo_contato
    global kits_concluidos, transporte_concluidos, divulgacao_concluidos, financeiro_concluidos

    print("\nPAINEL DA EQUIPE")

    # a equipe tem 3 tentativas para acertar a senha
    tentativas = 0
    acesso = False
    while tentativas < 3 and acesso == False:
        senha = input("Digite a senha da equipe: ")
        if senha == "equipe123":
            acesso = True
        else:
            tentativas = tentativas + 1
            print(f"Senha incorreta. Tentativas restantes: {3 - tentativas}")

    if acesso == False:
        print("\nAcesso negado. Retornando ao menu...\n")
    elif oferta_salva == False:
        print("\nNenhuma oferta recebida ainda.\n")
    else:
        mostrar_resumo_oferta()
        print(f"Próximo contato: {proximo_contato}")
        print(f"Autoriza divulgação: {autoriza_divulgacao}")

        print("\nO que deseja fazer?")
        print("1 - Avançar status (prometido > confirmado > concluído)")
        print("2 - Aprovar publicação do resultado")
        print("3 - Registrar próximo contato")
        print("0 - Voltar ao menu")
        acao = int(input("Digite sua escolha: "))

        if acao == 1:
            if status_oferta == "prometido":
                status_oferta = "confirmado"
                print("\nStatus atualizado para CONFIRMADO.\n")
            elif status_oferta == "confirmado":
                status_oferta = "concluido"
                print("\nStatus atualizado para CONCLUÍDO.\n")

                # quando conclui, o apoio entra no total de cada necessidade
                if tipo_apoio == "material":
                    kits_concluidos = kits_concluidos + quantidade_apoio
                elif tipo_apoio == "serviço":
                    transporte_concluidos = transporte_concluidos + quantidade_apoio
                elif tipo_apoio == "divulgação":
                    divulgacao_concluidos = divulgacao_concluidos + quantidade_apoio
                else:
                    financeiro_concluidos = financeiro_concluidos + quantidade_apoio
            else:
                print("\nEssa oferta já está concluída.\n")

        elif acao == 2:
            # so publica se estiver concluido e se o apoiador autorizou
            if status_oferta != "concluido":
                print("\nSó é possível publicar apoios concluídos.\n")
            elif autoriza_divulgacao == False:
                print("\nO apoiador não autorizou a divulgação.\n")
            else:
                publicado = True
                print("\nResultado publicado na área de impacto.\n")

        elif acao == 3:
            proximo_contato = input("Descreva o próximo contato a fazer: ")
            print("\nPróximo contato registrado.\n")

        else:
            print("\nRetornando ao menu...\n")

# aqui é o loop principal onde vai ter a logica do programa e o menu

print("Bem-vindo à Plataforma de Apoio da Turma do Bem!")
print("Dentista do Bem e Apolônias do Bem: juntos, levamos sorrisos a quem mais precisa.")

while True:
    print("MENU:")
    print("1 - NECESSIDADES E IMPACTO")
    print("2 - OFERECER APOIO")
    print("3 - ACOMPANHAR MINHA OFERTA")
    print("4 - PAINEL DA EQUIPE")
    print("5 - ENCERRAR")

    escolha = int(input("\nDigite sua escolha: "))

    # depois de cada funcionalidade o loop recomeca e o menu aparece de novo
    if escolha == 1:
        mostrar_necessidades_e_impacto()

    elif escolha == 2:
        # se ja existe uma oferta, pergunta se quer sobrescrever
        if oferta_salva == True:
            sobrescrever = ""
            while sobrescrever != "s" and sobrescrever != "n":
                sobrescrever = input("Você já tem uma oferta salva, deseja sobrescrever? (s/n): ").lower()

                if sobrescrever == "s":
                    realizar_oferta()
                elif sobrescrever == "n":
                    break
                else:
                    print("Opção inválida. Por favor, digite 's' para sim e 'n' para não")
        else:
            realizar_oferta()

    elif escolha == 3:
        acompanhar_oferta()

    elif escolha == 4:
        painel_equipe()

    elif escolha == 5:
        print("\nEncerrando a Plataforma de Apoio da Turma do Bem. Obrigado!")
        break

    else:
        print("\nOpção inválida. Por favor, escolha um número de 1 a 5.\n")
