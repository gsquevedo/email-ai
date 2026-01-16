import { useState } from 'react'
import './App.css'

const API_URL = import.meta.env.VITE_API_URL || ''

function App() {
  const [emailText, setEmailText] = useState('')
  const [file, setFile] = useState(null)
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)

  const handleSubmit = async () => {
    setLoading(true)
    setError(null)
    setResult(null)

    const form = new FormData()

    if (file) {
      form.append('file', file)
    } else {
      form.append('emailText', emailText)
    }

    try {
      const response = await fetch(`${API_URL}/api/process-email`, {
        method: 'POST',
        body: form,
      })

      console.log('Response:', response)

      if (!response.ok) {
        throw new Error(
          'Não foi possível processar o email no momento. Tente novamente.'
        )
      }

      const data = await response.json()
      setResult(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  const handleRemoveFile = () => {
    setFile(null)
  }

  return (
    <div className="app-container">
      <div className="card">
        <h1>Classificação Inteligente de Emails</h1>

        <p className="text-muted">
          Cole o conteúdo do email ou envie um arquivo (.txt ou .pdf) para
          classificar automaticamente e gerar uma resposta sugerida.
        </p>

        {/* Entrada de texto */}
        <textarea
          placeholder="Cole o texto do email aqui..."
          value={emailText}
          onChange={(e) => setEmailText(e.target.value)}
          disabled={!!file || loading}
        />

        {/* Upload + ação */}
        <div
          style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            marginTop: '1rem',
            gap: '1rem',
          }}
        >
          <div>
            <input
              type="file"
              accept=".txt,.pdf"
              onChange={(e) => setFile(e.target.files[0])}
              disabled={loading}
            />

            {file && (
              <div className="text-muted" style={{ marginTop: '0.25rem' }}>
                Arquivo selecionado: <strong>{file.name}</strong>{' '}
                <button
                  style={{
                    background: 'none',
                    border: 'none',
                    color: '#2563eb',
                    cursor: 'pointer',
                    padding: 0,
                    marginLeft: '0.25rem',
                  }}
                  onClick={handleRemoveFile}
                >
                  Remover
                </button>
              </div>
            )}
          </div>

          <button
            onClick={handleSubmit}
            disabled={loading || (!emailText && !file)}
          >
            {loading ? 'Processando email...' : 'Processar Email'}
          </button>
        </div>

        {/* Erro */}
        {error && <div className="error">{error}</div>}

        {/* Resultado */}
        {result && (
          <div className="result">
            <div style={{ marginBottom: '0.75rem' }}>
              <span className="text-muted">Categoria</span>
              <div>
                <span
                  className={`badge ${
                    result.categoria === 'Produtivo'
                      ? 'produtivo'
                      : 'improdutivo'
                  }`}
                >
                  {result.categoria}
                </span>
              </div>
            </div>

            <div>
              <span className="text-muted">Resposta sugerida</span>
              <div className="response-box">
                {result.resposta_sugerida}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default App
