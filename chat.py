import os  # Importa o módulo 'os' para permitir a limpeza da tela

mensagens = []  # Inicializa uma lista vazia para armazenar as mensagens

nome = input("Insira seu nome: ")  # Solicita ao usuário que insira seu nome

while True:  # Inicia um loop infinito
    os.system('cls')  # Limpa a tela (no Windows, use 'clear' se estiver no Linux ou Mac)

    # Verifica se há mensagens na lista e as exibe
    if len(mensagens) > 0:  # Usa a função len() para checar o número de mensagens
        for m in mensagens:  # Itera sobre cada mensagem armazenada
            print(m['nome'], "-", m['texto'])  # Exibe o nome do usuário e a mensagem

    print("_________________________")  # Exibe uma linha para separar mensagens de entrada

    texto = input("Mensagem: ")  # Solicita ao usuário que insira uma mensagem
    if texto == "fim":  # Verifica se a mensagem digitada é "fim"
        break  # Encerra o loop se "fim" for digitado

    # Adiciona a nova mensagem à lista
    mensagens.append({
        "nome": nome,  # Armazena o nome do usuário
        "texto": texto  # Armazena a mensagem enviada
    })