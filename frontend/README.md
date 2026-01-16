# Email AI Frontend

Frontend web responsável por permitir que o usuário envie emails para análise por IA, visualize a **classificação (Produtivo / Improdutivo)** e receba uma **resposta sugerida profissional**, consumindo a API do Email AI Backend.

---

## Objetivo do Projeto

Fornecer uma interface simples, intuitiva e rápida para:

* Inserir o conteúdo de um email manualmente
* Enviar o email para processamento por IA
* Visualizar a categoria atribuída ao email
* Visualizar a resposta sugerida automaticamente

O frontend atua apenas como **camada de apresentação**, delegando toda a inteligência e regras de negócio ao backend.

---

## Arquitetura Geral

```
Usuário (Browser)
        │
        ▼
Frontend (React)
        │ HTTP (REST)
        ▼
Email AI Backend (FastAPI)
        │
        ▼
LLM (Groq / LLaMA 3.1)
```

---

## Tecnologias Utilizadas

### Frontend

* **React**
* **JavaScript (ES6+)**
* **HTML5**
* **CSS3**
* **Fetch API** – comunicação com backend

### Integração

* Consumo de API REST (`POST /api/process-email`)
* Envio de dados via `application/x-www-form-urlencoded`

---

## Estrutura do Projeto

```
email-ai-frontend/
│
├── public/
│
├── src/
|   ├── assets/
│   ├── App.jsx
│   ├── App.css
│   ├── main.jsx
│   └── index.css
│
├── package.json
└── README.md
```

---

## Instalação

### 1️. Pré-requisitos

* **Node.js 18+**
* **npm** ou **yarn**

Verifique:

```bash
node -v
npm -v
```

---

### 2. Instalar dependências

```bash
npm install
```

ou

```bash
yarn install
```

---

## Executando o Frontend

```bash
npm run dev
```

ou

```bash
yarn dev
```

A aplicação estará disponível em:

```
http://localhost:5173
```

---

## Comunicação com o Backend

O frontend envia requisições para:

```
POST http://localhost:8000/api/process-email
```

### Resposta Esperada

```json
{
  "categoria": "Improdutivo",
  "resposta_sugerida": "Agradecemos a mensagem e desejamos uma ótima semana."
}
```

## Experiência do Usuário (UX)

* Campo de texto único para colar o email
* Botão de envio
* Exibição clara da categoria do email
* Área dedicada para a resposta sugerida
* Feedback visual durante o processamento

---

## Licença

Projeto de estudo e demonstração técnica. Livre para uso educacional.

---

## Autor

Frontend desenvolvido com foco em **simplicidade, clareza e integração fluida com IA**.
