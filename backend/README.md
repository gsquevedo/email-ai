# Email AI Backend

Backend responsável por processar emails, classificá-los como **Produtivo** ou **Improdutivo** utilizando IA generativa e gerar uma **resposta sugerida profissional**. O serviço expõe uma API REST consumida pelo frontend web.

---

## Objetivo do Projeto

Automatizar o tratamento inicial de emails corporativos, permitindo:

* Classificação inteligente de emails (Produtivo / Improdutivo)
* Geração automática de respostas profissionais
* Upload de emails via texto ou arquivos (.txt / .pdf)
* Integração simples via API REST

---

## Arquitetura Geral

```
Frontend (React)
        │
        ▼
FastAPI (Backend)
        │
        ▼
Groq API (LLM - LLaMA 3.1)
```

O backend atua como **orquestrador**, validando entradas, chamando a IA, normalizando respostas e devolvendo um payload padronizado ao frontend.

---

## Tecnologias Utilizadas

### Backend

* **Python 3.12**
* **FastAPI** – API REST assíncrona
* **Uvicorn** – ASGI server
* **Groq SDK** – acesso gratuito a LLMs (LLaMA 3.1)
* **NLTK** – pré-processamento opcional de texto
* **python-multipart** – upload de arquivos
* **PyPDF2** – leitura de PDFs

### IA

* **Modelo:** `llama-3.1-8b-instant`
* **Fornecedor:** Groq

---

## Estrutura do Projeto

```
email-ai-backend/
│
├── app/
│   ├── __init__.py  
│   ├── main.py          
│   ├── ai_service.py   
│   ├── nlp.py           
│   └── file_reader.py          
│
├── venv/                # Ambiente virtual
├── requirements.txt
└── README.md
```

---

## Variáveis de Ambiente

O backend depende de uma chave da Groq:

### Windows (PowerShell)

```powershell
setx GROQ_API_KEY "SUA_CHAVE_AQUI"
```

Reabra o terminal após executar.

### Linux / macOS

```bash
export GROQ_API_KEY="SUA_CHAVE_AQUI"
```

---

## Instalação

### 1. Criar ambiente virtual

```bash
python -m venv venv
```

### 2️. Ativar ambiente virtual

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3️. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## Executando o Backend

```bash
uvicorn app.main:app --reload
```

A API estará disponível em:

```
http://127.0.0.1:8000
```

---

## Endpoint Principal

### `POST /api/process-email`

Processa o email enviado via texto ou arquivo.

#### Entrada (multipart/form-data)

* `emailText` (string) **OU**
* `file` (.txt ou .pdf)

#### Saída (JSON)

```json
{
  "categoria": "Produtivo",
  "resposta_sugerida": "Obrigado pelo contato. Vou analisar sua solicitação e retorno em breve."
}
```

---

## Lógica de Classificação

A IA é instruída com prompts projetados segundo boas práticas de **Prompt Engineering**, garantindo:

* Saída restrita (apenas rótulos válidos)
* Baixa temperatura para decisões determinísticas
* Normalização defensiva da resposta

Fallback heurístico é aplicado caso a IA falhe.

---

## Exemplo de Teste via cURL

```bash
curl -X POST http://127.0.0.1:8000/api/process-email \
  -F "emailText=Podemos alinhar uma reunião amanhã às 10h?"
```

```bash
Invoke-WebRequest `
>>   -Uri http://localhost:8000/api/process-email `
>>   -Method POST `
>>   -Body @{ emailText = "Bom dia! Só passando para desejar uma ótima semana" } `
>>   -ContentType "application/x-www-form-urlencoded"
```
---

## Licença

Projeto de estudo e demonstração técnica. Livre para uso educacional.

---

## Autor

Backend desenvolvido com foco em **arquitetura limpa, robustez e integração com IA generativa**.
