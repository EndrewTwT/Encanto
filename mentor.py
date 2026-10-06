from openai import OpenAI

client = OpenAI()


def executar_mentor(prompt):
    resposta = client.responses.create(
        model="gpt-5.6",
        instructions=(
            "Você é um mentor de carreira especializado em tecnologia. "
            "Responda de maneira clara, objetiva e útil."
        ),
        input=prompt
    )

    print("\nResposta do mentor:")
    print(resposta.output_text)

    print("\nConsumo de tokens:")
    print(f"Tokens de entrada: {resposta.usage.input_tokens}")
    print(f"Tokens de saída: {resposta.usage.output_tokens}")
    print(f"Total de tokens: {resposta.usage.total_tokens}")
    print("-" * 40)

    return resposta


# TESTE 1 - PROMPT CURTO

prompt_curto = "Dê uma dica de carreira para um desenvolvedor Java."

print("TESTE 1 - PROMPT CURTO")
executar_mentor(prompt_curto)


# TESTE 2 - PROMPT DETALHADO

prompt_detalhado = """
Atue como um mentor de carreiras especializado em tecnologia.

Analise o cenário de um desenvolvedor Java iniciante,
com foco em desenvolvimento back-end, que deseja migrar
para uma carreira trabalhando com arquitetura de microsserviços.

Liste 3 habilidades essenciais que ele deve desenvolver,
explique por que cada uma delas é importante, sugira um
roteiro de estudos para os próximos 6 meses e mencione
os principais frameworks e tecnologias que ele deveria
conhecer para se preparar para o mercado de trabalho.

Organize a resposta por tópicos e seja detalhado nas
explicações.
"""

print("\nTESTE 2 - PROMPT DETALHADO")
executar_mentor(prompt_detalhado)