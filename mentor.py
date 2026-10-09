```python
import tiktoken

# Tokenizador local, sem usar a API
tokenizador = tiktoken.get_encoding("cl100k_base")


def contar_tokens(texto):
    return len(tokenizador.encode(texto))


def executar_teste(titulo, prompt, resposta_exemplo):
    entrada = contar_tokens(prompt)
    saida = contar_tokens(resposta_exemplo)
    total = entrada + saida

    print(f"\n{'=' * 45}")
    print(titulo)
    print("=" * 45)
    print(f"Prompt: {prompt.strip()}")
    print(f"\nTokens de entrada: {entrada}")
    print(f"Tokens de saída (resposta de exemplo): {saida}")
    print(f"Total de tokens: {total}")

    return entrada, saida, total


prompt_curto = """
Dê uma dica de carreira para um desenvolvedor Java.
"""

resposta_curta = """
Pratique Java, aprenda SQL e desenvolva projetos reais
para construir seu portfólio.
"""

prompt_detalhado = """
Atue como um mentor de carreiras especializado em tecnologia.
Analise o cenário de um desenvolvedor Java iniciante,
com foco em back-end, que deseja migrar para arquitetura
de microsserviços. Liste três habilidades essenciais,
explique sua importância, sugira um roteiro de estudos
de seis meses e mencione os frameworks mais relevantes
para o mercado atual. Organize a resposta por tópicos,
inclua exemplos práticos e indique projetos para o portfólio.
"""

resposta_detalhada = """
1. Java e Spring Boot: aprofunde a linguagem, APIs REST,
testes automatizados e boas práticas de programação.

2. Bancos de dados e SQL: pratique consultas, modelagem,
índices e transações.

3. Microsserviços: estude Docker, comunicação entre serviços,
mensageria, observabilidade e segurança.

Roteiro de seis meses:
Meses 1 e 2: Java, orientação a objetos e SQL.
Meses 3 e 4: Spring Boot, APIs REST e testes.
Mês 5: Docker e fundamentos de microsserviços.
Mês 6: desenvolva um projeto completo, documente-o
e publique o código no GitHub.

Tecnologias úteis: Spring Boot, JUnit, Docker e ferramentas
de mensageria. Consulte vagas atuais para priorizar
as tecnologias mais solicitadas.
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
print("-" * 45)
print(f"Total do teste curto: {teste1[2]}")
print(f"Total do teste detalhado: {teste2[2]}")
print(f"Diferença: {teste2[2] - teste1[2]} tokens")

if teste2[2] > teste1[2]:
    print("O teste detalhado consumiu mais tokens.")
elif teste1[2] > teste2[2]:
    print("O teste curto consumiu mais tokens.")
else:
    print("Os dois testes tiveram o mesmo total.")

print("\nObservação: a saída foi criada como exemplo.")
print("Nenhuma resposta foi gerada por uma IA nesta execução.")
```