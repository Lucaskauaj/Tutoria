<template>
  <div style="max-width:700px;margin:30px auto;font-family:Arial,Helvetica,sans-serif">
    <h1>Mensagens (CRUD)</h1>

    <form @submit.prevent="create" style="display:flex;gap:8px;margin-bottom:12px">
      <input v-model="newAuthor" placeholder="Autor" required style="flex:1;padding:8px"/>
      <input v-model="newText" placeholder="Mensagem" required style="flex:2;padding:8px"/>
      <button type="submit">Criar</button>
    </form>

    <div v-if="loading">Carregando...</div>
    <div v-else>
      <div v-if="messages.length === 0">Nenhuma mensagem.</div>

      <ul style="padding:0;list-style:none">
        <li v-for="m in messages" :key="m.id" style="border:1px solid #ddd;padding:10px;border-radius:6px;margin-bottom:8px;">
          <div style="display:flex;justify-content:space-between;align-items:center">
            <div>
              <strong>{{ m.author }}</strong>
            </div>
            <div>
              <button @click="startEdit(m)" style="margin-right:6px">Editar</button>
              <button @click="remove(m.id)">Deletar</button>
            </div>
          </div>

          <div style="margin-top:8px">
            <div v-if="editingId !== m.id">{{ m.text }}</div>

            <div v-else style="display:flex;gap:8px">
              <input v-model="editText" style="flex:1;padding:6px"/>
              <button @click="saveEdit(m.id)">Salvar</button>
              <button @click="cancelEdit">Cancelar</button>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
const API = 'http://localhost:3000/messages'

export default {
  data() {
    return {
      messages: [],
      loading: false,
      newAuthor: '',
      newText: '',
      editingId: null,
      editText: ''
    }
  },
  created() {
    this.load()
  },
  methods: {
    async load() {
      this.loading = true
      try {
        const res = await fetch(API)
        this.messages = await res.json()
      } catch (e) {
        alert('Erro ao carregar')
        console.error(e)
      } finally {
        this.loading = false
      }
    },
    async create() {
      const payload = {
        author: this.newAuthor.trim(),
        text: this.newText.trim()
      }
      if (!payload.author || !payload.text) return
      try {
        const res = await fetch(API, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        })
        const created = await res.json()
        this.messages.push(created)
        this.newAuthor = ''
        this.newText = ''
      } catch (e) {
        alert('Erro ao criar')
        console.error(e)
      }
    },
    startEdit(msg) {
      this.editingId = msg.id
      this.editText = msg.text
    },
    cancelEdit() {
      this.editingId = null
      this.editText = ''
    },
    async saveEdit(id) {
      if (!this.editText.trim()) return
      try {
        const res = await fetch(`${API}/${id}`, {
          method: 'PATCH',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ text: this.editText.trim() })
        })
        const updated = await res.json()
        const i = this.messages.findIndex(x => x.id === id)
        if (i !== -1) this.messages.splice(i, 1, updated)
        this.cancelEdit()
      } catch (e) {
        alert('Erro ao salvar')
        console.error(e)
      }
    },
    async remove(id) {
      if (!confirm('Confirma exclusão?')) return
      try {
        await fetch(`${API}/${id}`, { method: 'DELETE' })
        this.messages = this.messages.filter(m => m.id !== id)
      } catch (e) {
        alert('Erro ao deletar')
        console.error(e)
      }
    }
  }
}
</script>
