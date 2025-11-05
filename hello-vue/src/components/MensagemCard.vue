<!-- src/components/MensagemCard.vue -->
<template>
  <div class="card-mensagem">
    <header>
      <slot name="titulo"></slot>
    </header>

    <main>
      <slot name="conteudo"></slot>
    </main>

    <footer>
      <span><slot name="autor"></slot></span> |
      <span><slot name="data"></slot></span>

      <button @click="editar" class="btn-atualizar">Editar</button>
      <button @click="remover" class="btn-remover">Remover</button>
    </footer>
  </div>
</template>

<script setup>
const props = defineProps({
  id: Number
})

const emit = defineEmits(['editar', 'remover'])

function editar() {
  emit('editar', props.id)
}

function remover() {
  emit('remover', props.id)
}
</script>

<style scoped>
.card-mensagem {
  border: 1px solid #42b983; /* Fallback para a cor primária */
  padding: 12px;
  margin-bottom: 10px;
  border-radius: 6px;
  background-color: #fff;
}

header {
  font-weight: bold;
  color: #42b983; /* Fallback para a cor primária */
  margin-bottom: 5px;
}

footer {
  font-size: 0.9rem;
  color: #555;
  margin-top: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.btn-atualizar {
  padding: 6px 12px;
  border: none;
  background-color: #42b983; /* Cor amarela para o botão de edição */
  color: white;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease, opacity 0.3s ease;
}

.btn-atualizar:hover {
  background-color: #379f72; /* Cor mais escura ao passar o mouse */
  opacity: 0.9;
}

.btn-atualizar:focus {
  outline: 2px solid #42b983;
  outline-offset: 2px;
}

.btn-remover {
  padding: 6px 12px;
  border: none;
  background-color: var(--cor-primaria, #42b983); /* Fallback para a cor primária */
  color: white;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease, opacity 0.3s ease;
}

.btn-remover:hover {
  background-color: #379f72; /* Cor mais escura ao passar o mouse */
  opacity: 0.9;
}

.btn-remover:focus {
  outline: 2px solid #42b983;
  outline-offset: 2px;
}
</style>