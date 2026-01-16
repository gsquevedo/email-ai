# Email AI — Classificação Inteligente de Emails com IA

Sistema **fullstack** que utiliza **Inteligência Artificial Generativa** para analisar emails corporativos, classificá-los como **Produtivos** ou **Improdutivos** e gerar automaticamente uma **resposta sugerida profissional**.

O projeto foi desenvolvido com foco em **arquitetura limpa**, **boas práticas de backend**, **integração com LLMs** e **experiência do usuário**.

---

## Objetivo do Projeto

Automatizar o tratamento inicial de emails, ajudando equipes e profissionais a:

- Identificar rapidamente emails que exigem ação
- Reduzir tempo gasto com respostas repetitivas
- Padronizar respostas profissionais
- Demonstrar uso prático de IA generativa em sistemas reais

---

## Visão Geral da Arquitetura

```bash
Frontend (React + Vite)
│
▼
Backend (FastAPI)
│
▼
Groq API (LLM — LLaMA 3.1)

```

- **Frontend**: Interface web para entrada de emails (texto ou arquivo)
- **Backend**: API REST responsável por processar, classificar e gerar respostas
- **IA**: Modelo LLaMA 3.1 acessado via Groq (free tier)

---

## Estrutura do Repositório (Monorepo)

```bash
email-ai/
│
├── backend/
│ ├── app/
│ │ ├── main.py
│ │ ├── ai_service.py
│ │ └── nlp.py 
│ ├── requirements.txt
│ └── README.md
│
├── frontend/ # Interface Web
│ ├── src/
│ ├── public/
│ ├── package.json
│ ├── vite.config.ts
│ └── README.md
│
├── .gitignore
└── README.md # Documentação geral do sistema
```

---

## Tecnologias Utilizadas

### Backend
- **Python 3.12**
- **FastAPI** — API REST assíncrona
- **Uvicorn** — ASGI Server
- **Groq SDK** — acesso a LLMs gratuitos
- **NLTK** — pré-processamento de texto
- **PyPDF2** — leitura de arquivos PDF
- **python-multipart** — upload de arquivos

### Frontend
- **React**
- **Vite**
- **JavaScript (ES6+)**
- **Fetch API**
- **CSS moderno (UX/UI focado em clareza)**

### Inteligência Artificial
- **Modelo:** `llama-3.1-8b-instant`
- **Fornecedor:** Groq
- **Abordagem:** Prompt Engineering + validação defensiva de saída

---

## Variáveis de Ambiente

### Backend
É necessário configurar a chave da Groq.

#### Windows (PowerShell)

```powershell
setx GROQ_API_KEY "SUA_CHAVE_AQUI"
Reabra o terminal após executar.
```

### Frontend
Arquivo .env na pasta frontend/:

```bash
VITE_API_URL=http://localhost:8000
```

## Como Executar Localmente
### Backend

```bash
cd backend
python -m venv venv
```

Ativar ambiente virtual:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar API:

```bash
uvicorn app.main:app --reload
```

A API ficará disponível em:

```bash
http://127.0.0.1:8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

A interface estará disponível em:

```bash
http://localhost:5173
```

## 🔌 Endpoint Principal
POST /api/process-email
Processa um email enviado como texto ou arquivo.

#### Entrada
emailText (string) OU

file (.txt ou .pdf)

#### Saída
```json
{
  "categoria": "Produtivo",
  "resposta_sugerida": "Obrigado pelo contato. Vou analisar sua solicitação e retorno em breve."
}
```

## Lógica de Classificação
A classificação é feita via IA generativa, orientada por prompts cuidadosamente projetados para:
- Retornar apenas categorias válidas
- Minimizar ambiguidade
- Gerar respostas profissionais e educadas
- Garantir previsibilidade da saída
- Caso a IA falhe ou retorne algo inesperado, o backend aplica normalização defensiva para evitar erros.


## Licença
Projeto educacional e de portfólio. Livre para uso e estudo.

## Autoria
Projeto desenvolvido com foco em fullstack moderno, integração com IA generativa e boas práticas de engenharia de software.