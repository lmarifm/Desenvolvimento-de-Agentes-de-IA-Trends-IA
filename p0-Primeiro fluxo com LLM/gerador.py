import os # ferramenta do sistema para ler senhas do computador
from google import genai # biblioteca do gemini
from dotenv import load_dotenv # lê o .env.

# 1. config e segurança
# vai até o arquivo .env e carrega as variáveis dele para a memória
load_dotenv() 

# pega a chave
minha_chave = os.getenv("GEMINI_API_KEY") 

# cria o "mensageiro" (client) usando a senha,vai fazer a conexao com os servidores da google
client = genai.Client(api_key=minha_chave) 

# 2. entrada de dados (interação)
print(" --- BEM-VINDO AO GERADOR DE FLASHCARDS --- ")

# input() pausa o programa e espera digitar algo
texto_usuario = input("Cole o texto do seu slide aqui e aperte Enter: \n> ")

# 3. prompt
# a letra 'f' minúscula antes das aspas (f""") significa "Format", permite que a gente cloque a variável {texto_usuario} no meio da instrução
prompt = f"""
Você é um assistente de estudos. O usuário vai te passar um texto de um slide de aula.
Sua tarefa é extrair os conceitos mais importantes e criar até 3 flashcards para memorização.
Siga exatamente este formato para cada flashcard:

Pergunta: [Sua pergunta curta]
Resposta: [Sua resposta direta e simples]

Texto do slide:
{texto_usuario}
"""

# 4. comunicação c o modelo
print("\nProcessando...")

# o cliente vai ao modelo e entrega o prompt pra trazer a resposta
resposta = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=prompt
)

# 5. saida de dados 
print("\n--- FLASHCARDS PRONTOS ---")

# o .text no final serve para extrair apenas o texto limpo que a IA gerou, ignorando os códigos técnicos e metadados que ela manda junto.
print(resposta.text)