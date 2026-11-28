```markdown
# Relatório de Execução — P0 (Gerador de Flashcards)

## 2. Decisões Principais

| Decisão Tomada | Alternativa Considerada | Justificativa |
|:---|:---|:---|
| **SDK `google-genai` + `gemini-3.5-flash-lite` com *streaming*** | `gemini-3.8-flash` sem *streaming* ou `google-generativeai` | A biblioteca antiga está descontinuada e o `3.8-flash` apresentou alta latência e erro `503`. A versão `-lite` com *streaming* tornou as respostas quase instantâneas. |
| **Validação de entrada com `.strip()`** | Enviar qualquer texto diretamente para a API | Evita o consumo desnecessário de tokens e requisições inúteis quando o usuário envia um texto vazio ou contendo apenas espaços. |
| **Tratamento de erros com `try/except`** | Deixar o *traceback* padrão do Python | Exibe mensagens amigáveis em caso de falha na conexão, chave inválida ou erro da API, sem interromper inesperadamente o programa. |
| **Loop contínuo com `while True` e comando `'sair'`** | Encerrar o script após cada geração | Melhora a usabilidade no terminal, deixando o gerador pronto para receber novos textos em sequência sem precisar executar `python3 gerador.py` novamente. |

## 3. Testes e Resultados

| Teste | Entrada / Situação | Resultado Esperado | Status |
|:---|:---|:---|:---:|
| **Entrada vazia** | Pressionar `Enter` sem texto | Exibir erro de texto vazio e solicitar uma nova entrada, sem chamar a API. | ✅ Passou |
| **Falha de credencial** | `.env` sem `GEMINI_API_KEY` | Exibir aviso de chave não encontrada e encerrar com segurança. | ✅ Passou |
| **Falha de conexão** | Execução com Wi-Fi desligado | Capturar a exceção no `try/except` e exibir uma mensagem amigável. | ✅ Passou |
| **Instabilidade da API** | Pico de demanda (`503 UNAVAILABLE`) | Capturar a exceção da API e orientar o usuário sem travar o loop. | ✅ Passou |
| **Texto longo (limite do prompt)** | Envio de texto extenso de slide | Respeitar a regra rígida do prompt (sem gerar 4 flashcards ou mais) | ✅ Passou |
| **Execução contínua** | Enviar um texto, receber os flashcards, enviar outro e digitar `sair` | Manter o programa pronto para novas entradas e encerrar apenas ao digitar `sair` | ✅ Passou |

## 4. Falhas e Limitações

- **O que aconteceu:**
  1. Durante os testes com o modelo `gemini-3.8-flash`, a API apresentou latência acima de 30 segundos e retornou erro `503 UNAVAILABLE` por pico de demanda.
  2. Ao enviar textos longos, o modelo ignorava o limite inicial ("até 3 flashcards") e chegava a gerar mais de 6 perguntas.
  3. Na primeira versão, o programa encerrava após uma única resposta, exigindo rodar `python3 gerador.py` novamente para cada novo texto.
- **Como foi identificado:** Durante testes práticos no terminal com textos reais e extensos de slides.
- **Como foi tratado:**
  1. Migrei para o modelo `gemini-3.5-flash-lite` com retorno em *streaming* (`generate_content_stream`).
  2. Reforcei o prompt com uma regra explícita e restritiva (*"Crie EXATAMENTE 3 flashcards. NUNCA gere mais de 3, mesmo que o texto seja muito longo"*).
  3. Implementei um laço `while True` com saída controlada pelo comando `'sair'`, deixando o gerador pronto para receber novas entradas continuamente.
- **Por que permanece:** A dependência de conexão com a internet e eventuais instabilidades externas da API permanecem por ser uma solução em nuvem, mas agora são tratadas com `try/except` sem interromper o loop.

## 5. Uso de IA no Desenvolvimento
- **Ferramenta utilizada:** Gemini.
- **Tarefa delegada:** Apoio na depuração de erro de biblioteca descontinuada, estruturação do tratamento de exceções (`try/except`) e organização da documentação (`README.md` e relatório).
- **Resultado aproveitado:** Migração para `google-genai`, adição de validações de entrada/chave e estrutura dos arquivos Markdown.
- **Correções ou alterações realizadas:** Adaptação dos comandos e caminhos de diretórios para o ambiente local (Linux/VS Code) e ajuste da estrutura de README raiz vs. pasta do P0.
- **Forma de verificação:** Execução manual no terminal testando cenários de sucesso e falha e conferência do `git status` antes do envio.

## 6. Reflexão Final
- **Principal aprendizado:** Como integrar um LLM de forma segura em Python, separando credenciais, isolando dependências e tratando falhas externas.
- **Competência mais desenvolvida:** Depuração de ambiente Linux/Python (uso de `venv`, caminhos de diretório e leitura de mensagens de erro no terminal).
- **Aspecto a aprimorar:** Maior autonomia na escrita inicial de validações e testes automatizados.