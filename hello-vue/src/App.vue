<template>
  <div class="container">
    <h1 class="titulo">📬 Mensagens da API</h1>

    <MensagemForm @adicionar="adicionarMensagem" />

    <div v-if="carregando" class="estado carregando">
      <p>⏳ Carregando mensagens...</p>
    </div>

    <div v-else-if="erro" class="estado erro">
      <p>⚠️ {{ erro }}</p>
      <button @click="carregarMensagens">Tentar novamente</button>
    </div>

    <div v-else-if="mensagens.length === 0" class="estado vazio">
      <p>🗒️ Nenhuma mensagem encontrada.</p>
      <small>Dica: adicione uma nova mensagem usando o formulário!</small>
    </div>

    <div v-else class="lista">
      <MensagemCard v-for="(msg, i) in mensagens" :key="msg.id" @editar="editarMensagem(msg, i)"
        @remover="excluirMensagem(msg, i)">
        <template #titulo>{{ msg.titulo }}</template>
        <template #conteudo>{{ msg.conteudo }}</template>
        <template #autor>{{ msg.autor }}</template>
        <template #data>{{ formatarData(msg.data_criacao) }}</template>
      </MensagemCard>
    </div>
  </div>
</template>

<!-- script atualizado do App.vue -->
<script setup>
import { ref, onMounted } from 'vue'
import { getMensagens, criarMensagem, atualizarMensagem, removerMensagem } from '@/services/mensagensService.js'
import MensagemCard from '@/components/MensagemCard.vue'
import MensagemForm from '@/components/MensagemForm.vue'

const mensagens = ref([])
const carregando = ref(true)
const erro = ref(null)

function formatarData(iso) {
  return new Date(iso).toLocaleString('pt-BR', {
    dateStyle: 'short',
    timeStyle: 'short'
  })
}

async function carregarMensagens() {
  carregando.value = true
  erro.value = null
  try {
    mensagens.value = await getMensagens()
  } catch (e) {
    erro.value = e?.message || 'Erro ao carregar mensagens.'
  } finally {
    carregando.value = false
  }
}

onMounted(carregarMensagens)

async function adicionarMensagem(dados) {
  try {
    const novaMensagem = await criarMensagem(dados)
    mensagens.value.push(novaMensagem)
  } catch (e) {
    alert(e?.message || 'Falha ao enviar mensagem.')
  }
}

// Atualiza o conteúdo de uma mensagem
async function editarMensagem(msg, index) {
  const novoTitulo = prompt('Novo título:', msg.titulo)
  const novoConteudo = prompt('Novo conteúdo:', msg.conteudo)

  if (!novoTitulo || !novoConteudo) return

  try {
    const dadosAtualizados = await atualizarMensagem(msg.id, {
      titulo: novoTitulo,
      conteudo: novoConteudo,
      autor: msg.autor
    })
    mensagens.value[index] = dadosAtualizados
  } catch (e) {
    alert(e?.message || 'Erro ao atualizar mensagem.')
  }
}

// Remove uma mensagem
async function excluirMensagem(msg, index) {
  if (!confirm(`Deseja realmente excluir "${msg.titulo}"?`)) return

  try {
    await removerMensagem(msg.id)
    mensagens.value.splice(index, 1)
  } catch (e) {
    alert(e?.message || 'Erro ao remover mensagem.')
  }
}
</script>