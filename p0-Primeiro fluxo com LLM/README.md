# Gerador de Flashcards com LLM (P0)

## Problema Escolhido
Estudantes gastam muito tempo resumindo slides extensos manualmente para criar material de revisão ativa.

## Usuário / Público-alvo
Estudantes universitários e vestibulandos que utilizam revisão espaçada (flashcards) para memorizar conteúdos de aulas.

## Justificativa para Utilizar um LLM
A extração de conceitos-chave e a formulação de perguntas e respostas objetivas a partir de texto livre exige compreensão semântica e capacidade de síntese, tarefas que algoritmos baseados em regras fixas não conseguem executar com precisão.

## Funcionamento da Solução
A aplicação em Python recebe um texto de aula via terminal, valida se a entrada não está vazia e envia o conteúdo estruturado em um prompt para a API do Gemini. O modelo retorna até 3 flashcards no formato `Pergunta / Resposta`.

### Evolução por Nível
- [x] **Básico:** Fluxo via terminal, validação de entrada, tratamento de exceções (`try/except`), `.env` e `requirements.txt`.
- [ ] **Intermediário:** *A implementar*
- [ ] **Avançado:** *A implementar*

## Limites do Projeto
- Processa apenas texto colado diretamente no terminal (ainda não lê arquivos `.pdf` ou `.pptx`).
- Gera no máximo 3 flashcards por execução.
- Não possui persistência em banco de dados ou exportação direta para o Anki nesta versão.

## Instalação

1. Clone o repositório e acesse a pasta do projeto:
   ```bash
   git clone <https://github.com/lmarifm/Desenvolvimento-de-Agentes-de-IA-Trends-IA.git>
   cd "p0-Primeiro fluxo com LLM"
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   python3 -m venv venv
   # No Linux/macOS:
   source venv/bin/activate
   # No Windows:
   venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Configuração do LLM e Testes
- **Provedor:** Google AI Studio
- **Modelo:** `gemini-3.8-flash` (via SDK oficial `google-genai`)
- Copie o arquivo `.env.example` para `.env` na raiz da pasta do projeto e insira sua chave de API:
  ```env
  GEMINI_API_KEY=sua_chave_aqui
  ```
- **Tipo de testes:** Os testes de sucesso e de latência foram realizados com chamadas **reais** à API. Os testes de falha foram realizados simulando entrada vazia, ausência de chave no `.env` e indisponibilidade de rede.

## Execução
Com o ambiente virtual ativado, execute:
```bash
python gerador.py
```

## Exemplos de Entrada e Saída

**Entrada:**
> A memória RAM é uma memória volátil usada para armazenar dados temporários de programas em execução. Quando o computador é desligado, seu conteúdo é perdido.

**Saída:**
```text
Pergunta: O que significa dizer que a memória RAM é volátil?
Resposta: Significa que ela perde todos os dados armazenados quando o computador é desligado.

Pergunta: Qual é a principal função da memória RAM?
Resposta: Armazenar temporariamente os dados dos programas que estão em execução.
```

## Execução dos Testes
Para reproduzir os cenários de teste manualmente:
1. **Sucesso:** Execute `python gerador.py` e insira um parágrafo de texto válido.
2. **Falha (entrada vazia):** Execute o script e pressione `Enter` sem digitar texto.
3. **Falha (chave/rede):** Remova temporariamente a chave do `.env` ou desconecte a internet e execute o script.

## Limitações Conhecidas
- **Latência elevada:** Em alguns testes locais, a resposta da API ultrapassou 30 segundos, sem exibição progressiva (*streaming*) no terminal.
- **Dependência de conexão:** O sistema não funciona offline.

## Vídeo de Entrega
[Assista ao vídeo de demonstração aqui](link_a_ser_anexado_futuramente)