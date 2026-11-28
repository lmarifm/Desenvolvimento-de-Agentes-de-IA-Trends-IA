import os # ferramenta do sistema para ler senhas do computador
import sys # encerra o programa com segurança
from google import genai # biblioteca do gemini
from dotenv import load_dotenv # lê o .env.

# 1. config e segurança
# vai até o arquivo .env e carrega as variáveis dele para a memória
load_dotenv() 

# pega a chave
minha_chave = os.getenv("GEMINI_API_KEY") 

# validação da chave de api antes de tentar conectar 
if not minha_chave:
    print("Erro: Chave GEMINI_API_KEY não encontrada no arquivo .env.")
    sys.exit(1)  # encerra o script imediatamente e envia codigo ao sistema falando que houve erro

# cria o "mensageiro" (client) usando a senha,vai fazer a conexao com os servidores da google
client = genai.Client(api_key=minha_chave) 

# 2. entrada de dados (interação)
print(" --- BEM-VINDO AO GERADOR DE FLASHCARDS --- ")
print("(Digite 'sair' para encerrar)\n")

while True:
    # input() pausa o programa e espera digitar algo
    texto_usuario = input("Cole o texto do seu slide aqui e aperte Enter: \n> ")

    if texto_usuario.strip().lower() == "sair":
        print("Encerrando o gerador. Bons estudos!")
        break

    # valida entrada do usuario
    if not texto_usuario.strip(): #strip remove os espaços em branco, se n sobrar nada, nao envia pra ia
        print("Erro: O texto não pode estar vazio. Tente novamente.\n")
        continue

    # 3. prompt
    # a letra 'f' minúscula antes das aspas (f""") significa "Format", permite que a gente cloque a variável {texto_usuario} no meio da instrução
    prompt = f"""
Você é um assistente de estudos. O usuário vai te passar um texto de um slide de aula.
Sua tarefa é extrair os conceitos mais importantes e criar flashcards para memorização.

REGRAS OBRIGATÓRIAS:
- Crie EXATAMENTE 3 flashcards. NUNCA gere mais de 3, mesmo que o texto seja muito longo.
- Siga exatamente este formato para cada flashcard:

Pergunta: [Sua pergunta curta]
Resposta: [Sua resposta direta e simples]

Texto do slide:
{texto_usuario}
"""

    # 4. comunicação c o modelo e 5. saida de dados
    print("\nProcessando...")

    try:
        resposta = client.models.generate_content_stream(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )
        print("\n--- FLASHCARDS PRONTOS ---")
        for pedaco in resposta:
            print(pedaco.text, end="", flush=True)
        print("\n" + "-" * 30 + "\n")  # pula uma linha e separa do próximo texto
    except Exception as erro:
        print("\nErro ao se comunicar com a IA. Verifique sua conexão ou chave de API.")
        print(f"Detalhes técnicos: {erro}\n")