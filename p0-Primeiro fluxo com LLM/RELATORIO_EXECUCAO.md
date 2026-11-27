```markdown
# Relatório de Execução — P0 (Gerador de Flashcards)

## 1. Evolução por Nível
- **Básico:** Construção do fluxo completo de chamada ao LLM via terminal, isolamento de ambiente (`venv`), proteção de credenciais (`.env` e `.gitignore`), validação de entrada vazia e tratamento de exceções na comunicação com a API.
- **Intermediário:** *Em desenvolvimento.*
- **Avançado:** *Em desenvolvimento.*

## 2. Decisões Principais

| Decisão Tomada | Alternativa Considerada | Justificativa |
| :--- | :--- | :--- |
| Uso do SDK `google-genai` com modelo `gemini-3.8-flash` | Biblioteca antiga `google-generativeai` | A biblioteca antiga apresentou aviso de descontinuação (*deprecated*); o novo SDK garante compatibilidade atual. |
| Validação de entrada com `.strip()` antes da chamada à API | Enviar qualquer texto direto para o LLM | Evita consumo desnecessário de tokens e requisições inúteis quando o usuário envia texto vazio ou apenas espaços. |
| Tratamento de erros com `try/except` e `sys.exit(1)` | Deixar o *traceback* padrão do Python | Garante mensagens amigáveis ao usuário em caso de queda de internet ou chave inválida, sem quebrar abruptamente. |

## 3. Testes e Resultados

| Teste | Entrada ou Situação | Resultado Esperado | Resultado Obtido |
| :--- | :--- | :--- | :--- |
| Geração com sucesso | Parágrafo de slide sobre conteúdo técnico | Retorno de até 3 flashcards no formato Pergunta/Resposta | Passou (flashcards gerados corretamente) |
| Entrada vazia | Pressionar `Enter` sem digitar texto | Exibir erro de texto vazio e encerrar sem chamar a API | Passou |
| Falha de credencial | Arquivo `.env` sem `GEMINI_API_KEY` | Exibir aviso de chave não encontrada e encerrar | Passou |
| Falha de conexão | Execução com Wi-Fi desligado | Capturar exceção no `try/except` e exibir mensagem amigável | Passou |

## 4. Falhas e Limitações
- **O que aconteceu:** Latência acima de 30 segundos para retorno da resposta da API do Gemini, mesmo para textos curtos.
- **Como foi identificado:** Durante a execução dos testes manuais no terminal no ambiente Linux.
- **Como foi tratado:** Foi adicionada uma mensagem de feedback (`Processando seus flashcards...`) para indicar que o programa não travou.
- **Por que permanece:** A investigação de rede (IPv6/retentativas) e a implementação de *streaming* foram priorizadas para os próximos níveis para garantir o cumprimento do prazo do Nível Básico.

## 5. Uso de IA no Desenvolvimento
- **Ferramenta utilizada:** Gemini.
- **Tarefa delegada:** Apoio na depuração de erro de biblioteca descontinuada, estruturação do tratamento de exceções (`try/except`) e organização da documentação (`README.md` e relatório).
- **Resultado aproveitado:** Migração para `google-genai`, adição de validações de entrada/chave e estrutura dos arquivos Markdown.
- **Correções ou alterações realizadas:** Adaptação dos comandos e caminhos de diretórios para o ambiente local (Linux/VS Code) e ajuste da estrutura de README raiz vs. pasta do P0.
- **Forma de verificação:** Execução manual no terminal testando cenários de sucesso e falha e conferência do `git status` antes do envio.

## 6. Reflexão Final
- **Principal aprendizado:** Como integrar um LLM de forma segura em Python, separando credenciais, isolando dependências e tratando falhas externas.
- **Competência mais desenvolvida:** Depuração de ambiente Linux/Python (uso de `venv`, caminhos de diretório e leitura de mensagens de erro no terminal).
- **Aspecto a aprimorar:** Otimização de latência (uso de *streaming*) e maior autonomia na escrita inicial de validações e testes automatizados.