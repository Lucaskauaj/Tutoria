import api from './api';
/**
 * Lista todas as mensagens.
 * GET /mensagens
 */
export async function getMensagens() {
  try {
    const resposta = await api.get('/mensagens')
    return resposta.data
  } catch (erro) {
    throw erro.response?.data || {
      erro: 'NetworkError',
      message: 'Falha ao carregar mensagens.',
      status: 500
    }
  }
}

export async function atualizarMensagem(id, dados) {
  try {
    const resposta = await api.put(`/mensagens/${id}`, dados)
    return resposta.data
  } catch (erro) {
    throw erro.response?.data || {
      erro: 'NetworkError',
      message: 'Falha ao atualizar mensagem.',
      status: 500
    }
  }
}

/**
 * Remove uma mensagem.
 * DELETE /mensagens/:id
 */
export async function removerMensagem(id) {
  try {
    const resposta = await api.delete(`/mensagens/${id}`)
    return resposta.data
  } catch (erro) {
    throw erro.response?.data || {
      erro: 'NetworkError',
      message: 'Falha ao remover mensagem.',
      status: 500
    }
  }
}
// src/services/mensagensService.js
export async function criarMensagem(dados) {
  try {
    const resposta = await api.post('/mensagens', dados)
    return resposta.data
  } catch (erro) {
    throw erro.response?.data || {
      erro: 'NetworkError',
      message: 'Falha ao criar mensagem.',
      status: 500
    }
  }
}