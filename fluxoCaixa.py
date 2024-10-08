# Lista para armazenar as transações de fluxo de caixa
fluxo_caixa = []

print("\nSelecione uma opção:")
print("1 - Adicionar Receita")
print("2 - Adicionar Despesa")
print("Digite outro número para encerrar")

def adicionar_transacao(tipo):
    """Função para adicionar uma transação (receita ou despesa) ao fluxo de caixa."""
    nome = input("Digite o nome: ")  # Solicita o nome da transação
    valor = float(input("Digite o valor: R$ "))  # Solicita o valor da transação
    
    # Adiciona a transação na lista com o valor positivo para receitas e negativo para despesas
    fluxo_caixa.append({
        "nome": nome,
        "valor": valor if tipo == "receita" else -valor
    })

while True:
    opcao = input("Digite a opção: ")  # Solicita a opção ao usuário

    if opcao == "1":
        adicionar_transacao("receita")  # Adiciona uma receita

    elif opcao == "2":
        adicionar_transacao("despesa")  # Adiciona uma despesa

    else:
        break  # Encerra o loop se a opção não for 1 ou 2

# Nota fiscal
total = 0

print("\nNota Fiscal:")
for fc in fluxo_caixa:  # Itera sobre todas as transações
    print("Nome:", fc['nome'], "- Valor: R$", fc['valor'])  # Exibe nome e valor da transação
    total += fc['valor']  # Soma os valores para calcular o total

print("Saldo atual: R$", total)  # Exibe o saldo final