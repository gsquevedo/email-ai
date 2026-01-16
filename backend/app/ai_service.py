import os
from groq import Groq

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError("GROQ_API_KEY não foi encontrada nas variáveis de ambiente.")

client = Groq(api_key=api_key)

MODEL_NAME = "llama-3.1-8b-instant"

def extract_text(response) -> str:
    """
    Extrai o conteúdo textual da resposta da API Groq.
    Assume o padrão compatível com OpenAI.
    """
    try:
        content = response.choices[0].message.content
        if not content:
            raise ValueError("Conteúdo vazio retornado pela IA.")
        return content.strip()
    except (AttributeError, IndexError) as exc:
        raise RuntimeError(f"Erro ao extrair texto da resposta da IA: {exc}")

def classify_email(text: str) -> str:
    """
    Classifica um email como 'Produtivo' ou 'Improdutivo'
    de forma determinística.
    """

    if not text or not text.strip():
        return "Improdutivo"

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "Você é um classificador determinístico de emails corporativos.\n\n"
                    "Definições operacionais:\n"
                    "- Produtivo: emails que solicitam ação, informação, suporte, análise, "
                    "execução de tarefas, envio de documentos ou tratam de processos de negócio.\n"
                    "- Improdutivo: emails sociais, cumprimentos, agradecimentos, felicitações "
                    "ou mensagens que não exigem nenhuma ação.\n\n"
                    "Regras obrigatórias:\n"
                    "- Responda APENAS com uma única palavra\n"
                    "- A palavra deve ser exatamente uma das opções abaixo:\n"
                    "Produtivo\n"
                    "Improdutivo"
                )
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=0.0,
        max_tokens=5
    )

    return extract_text(response)

def generate_reply(original_text: str, category: str) -> str:
    """
    Gera uma resposta profissional baseada na categoria do email.
    """

    if not original_text or not original_text.strip():
        return ""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "Você é um assistente corporativo de uma empresa do setor financeiro.\n\n"
                    "Diretrizes obrigatórias de comunicação:\n"
                    "- Tom profissional, educado e objetivo\n"
                    "- Linguagem formal de negócios\n"
                    "- Respostas entre 2 e 3 frases\n"
                    "- Não utilize emojis ou linguagem informal\n\n"
                    "Comportamento por categoria:\n"
                    "- Se o email for Produtivo: responda atendendo à solicitação ou "
                    "informando claramente o próximo passo.\n"
                    "- Se o email for Improdutivo: responda de forma cordial e breve, "
                    "sem iniciar processos ou ações."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Categoria do email: {category}\n\n"
                    f"Email:\n{original_text}"
                )
            }
        ],
        temperature=0.3,
        max_tokens=150
    )

    return extract_text(response)
