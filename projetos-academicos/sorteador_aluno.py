import random # Importa a função para sortear

def sortear_alunos(arquivo_lista="lista_alunos.txt", num_alunos=1):
    """
    Lê a lista de alunos de um arquivo e sorteia um número especificado de nomes sem repetir.
    Retorna uma lista com os nomes sorteados ou None em caso de erro.
    """
    alunos = []
    try:
        # Abre o arquivo para leitura
        with open(arquivo_lista, 'r', encoding='utf-8') as f:
            # Lê cada linha do arquivo, remove espaços extras e linhas vazias
            alunos = [linha.strip() for linha in f if linha.strip()]

    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_lista}' não encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return None

    if not alunos:
        print("A lista de alunos está vazia.")
        return [] # Retorna lista vazia se não houver alunos

    total_alunos = len(alunos)

    # Verifica se o número de alunos a sortear é válido
    if num_alunos <= 0:
        print("O número de alunos a sortear deve ser positivo.")
        return []
    elif num_alunos > total_alunos:
        print(f"Aviso: Você pediu para sortear {num_alunos} alunos, mas a lista só tem {total_alunos}.")
        print("Sorteando todos os alunos disponíveis.")
        num_alunos_sortear = total_alunos
    else:
        num_alunos_sortear = num_alunos

    # Sorteia 'num_alunos_sortear' nomes da lista sem repetição
    alunos_sorteados = random.sample(alunos, num_alunos_sortear)

    return alunos_sorteados

# Bloco principal que executa quando o script é rodado
if __name__ == "__main__":
    print("--- Sorteador de Alunos ---")

    while True:
        try:
            # Pergunta ao usuário quantos alunos sortear
            num_pedidos_str = input("Quantos alunos você quer sortear? (Digite um número positivo): ")
            num_pedidos = int(num_pedidos_str)
            if num_pedidos < 1:
                 print("Por favor, digite um número maior que zero.")
                 continue
            break # Sai do loop se um número válido for digitado
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    # Chama a função de sorteio com o número especificado pelo usuário
    lista_sorteada = sortear_alunos(num_alunos=num_pedidos)

    if lista_sorteada is not None: # Verifica se a função retornou uma lista (não None por erro)
        if lista_sorteada: # Verifica se a lista sorteada não está vazia
            print("\nAlunos sorteados:")
            for aluno in lista_sorteada:
                print(f"- {aluno}")
        else:
             print("Nenhum aluno foi sorteado.") # Isso aconteceria se a lista original estivesse vazia ou num_pedidos <= 0

    print("---------------------------")