
import tiktoken

tokenizador = tiktoken.get_encoding("cl100k_base")


def contar_tokens(texto):
    return len(tokenizador.encode(texto))


def executar_teste(titulo, prompt, resposta):
    entrada = contar_tokens(prompt)
    saida = contar_tokens(resposta)
    total = entrada + saida

    print(f"\n{titulo}")
    print("-" * 35)
    print(f"Tokens de entrada: {entrada}")
    print(f"Tokens de saída (exemplo): {saida}")
    print(f"Total de tokens: {total}")

    return entrada, saida, total


prompt_curto = "Dê uma dica de carreira para um desenvolvedor Java."

resposta_curta = (
    "Pratique Java, aprenda SQL e desenvolva projetos "
    "reais para construir seu portfólio."
)

prompt_detalhado = """
Atue como um mentor de carreira especializado em tecnologia.
Analise um desenvolvedor Java iniciante, com foco em back-end,
que deseja trabalhar com arquitetura de microsserviços.
Liste três habilidades essenciais, explique sua importância,
sugira um roteiro de estudos de seis meses e mencione os
frameworks relevantes para o mercado. Organize a resposta
por tópicos, inclua exemplos e sugira projetos para o portfólio.
"""

resposta_detalhada = """
1. Java e Spring Boot: estude a linguagem, APIs REST e testes.
2. SQL: pratique consultas, modelagem e transações.
3. Microsserviços: aprenda Docker, mensageria e observabilidade.

Roteiro de seis meses:
Meses 1 e 2: Java, orientação a objetos e SQL.
Meses 3 e 4: Spring Boot, APIs REST e testes.
Mês 5: Docker e fundamentos de microsserviços.
Mês 6: desenvolva e publique um projeto no GitHub.

Tecnologias úteis incluem Spring Boot, JUnit e Docker.
Consulte vagas atuais para identificar as competências
mais solicitadas pelas empresas.
"""

teste1 = executar_teste(
    "TESTE 1 - PROMPT CURTO",
    prompt_curto,
    resposta_curta
)

teste2 = executar_teste(
    "TESTE 2 - PROMPT DETALHADO",
    prompt_detalhado,
    resposta_detalhada
)

print("\nCOMPARAÇÃO FINAL")
print(f"Total do teste curto: {teste1[2]}")
print(f"Total do teste detalhado: {teste2[2]}")
print(f"Diferença: {teste2[2] - teste1[2]} tokens")

if teste2[2] > teste1[2]:
    print("O teste detalhado consumiu mais tokens.")
else:
    print("O teste curto consumiu mais ou a contagem foi igual.")

print("\nAtenção: as respostas são exemplos, não foram geradas por IA.")
print("O tokenizador utilizado é cl100k_base.")
