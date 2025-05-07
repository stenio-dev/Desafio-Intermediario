import random # Importa a função para sortear

def sortear_aluno(arquivo_lista="lista_alunos.txt"):
    """Lê a lista de alunos de um arquivo e sorteia um nome."""
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
        return None

    # Sorteia um nome da lista
    aluno_sorteado = random.choice(alunos)
    return aluno_sorteado

# Bloco principal que executa quando o script é rodado
if __name__ == "__main__":
    print("--- Sorteador de Alunos ---")
    nome_sorteado = sortear_aluno()
    if nome_sorteado:
        print(f"O aluno sorteado é: {nome_sorteado}")
    else:
        print("Não foi possível realizar o sorteio.")
    print("---------------------------")