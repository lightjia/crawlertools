<template>
  <div class="divide-y divide-dashed">
    <TopicItem v-for="(value, key) in topics" :key="key" :topic="value"></TopicItem>
  </div>
</template>

<script setup>
import TopicItem from './TopicItem.vue'
import {onMounted, ref} from "vue"
import axios from "axios";

const topics = ref({})
onMounted(async () => {
  const respone = await axios.post('http://localhost:8080/api/op_code', {code: 'more'}, {
    headers: {
      'Content-Type': 'application/json'
    }
  })
  console.log(`data is ${JSON.stringify(respone.data)}`)
  topics.value = respone.data
})
</script>

<style scoped>
</style>