<!-- src/components/Mensagem.vue -->
<template>
  <div class="mensagem">
    <p>{{ texto }}</p>
    <button @click="remover">Remover</button>
  </div>
</template>

<script setup>
const props = defineProps({
  id: Number,
  texto: String
})

const emit = defineEmits(['remover'])

function remover() {
  // Envia um "sinal" para o pai informando qual mensagem deve ser removida
  emit('remover', props.id)
}
</script>

<style scoped>
.mensagem {
  border: 1px solid var(--cor-primaria, #42b983); /* Define um fallback caso a variável não exista */
  padding: 10px;
  margin-bottom: 8px;
  border-radius: 5px;
  background-color: #fff;
  color: #333;
}

button {
  margin-top: 5px;
  padding: 6px 12px; /* Ajuste no espaçamento interno */
  border: none;
  background-color: var(--cor-primaria, #42b983); /* Define um fallback */
  color: white;
  border-radius: 5px; /* Bordas mais arredondadas */
  cursor: pointer;
  transition: background-color 0.3s ease, opacity 0.3s ease; /* Adiciona transições suaves */
}

button:hover {
  background-color: #379f72; /* Cor mais escura ao passar o mouse */
  opacity: 0.9;
}

button:focus {
  outline: 2px solid #42b983; /* Adiciona um contorno ao focar */
  outline-offset: 2px;
}
</style>