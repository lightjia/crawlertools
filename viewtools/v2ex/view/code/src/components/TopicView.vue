<template>
  <div class="overflow-hidden w-full h-full">
    <!--    <div class="fixed bg-red-500 h-16 w-full mt-0"></div>-->
    <div class="divide-y divide-dashed overflow-y-auto" @wheel.stop="handleWheel" @scroll.stop="handleScroll"
         ref="scrollDiv">
      <TopicItem v-for="(item, index) in topics" :key="index" :topic="item"></TopicItem>
    </div>
  </div>
  <!--  <div class="flex items-center justify-center">-->
  <!--    <span class="block font-bold  text-2xl">这是一个非常长的文本，它应该会自动换行。</span>-->
  <!--  </div>-->
</template>

<script setup>
import TopicItem from './TopicItem.vue'
import {onMounted, ref} from "vue"
import axios from "axios";
import _ from "lodash";

const scrollDiv = ref(null)
const topics = ref([])
onMounted(async () => {
  await getTopics()
})
const handleWheel = async (event) => {
  // 判断滚轮方向
  if (event.deltaY > 0) {
    await reqMore(event.target)
  }
}
const handleScroll = async (event) => {
  await reqMore(event.target)
}
const reqMore = async (element) => {
  if (element !== scrollDiv.value) return
  console.log(`req1 scrollHeight: ${element.scrollHeight} scrollTop: ${element.scrollTop} clientHeight: ${element.clientHeight}`)
  if (element.scrollHeight - element.scrollTop === element.clientHeight) {
    console.log('req 2')
    await getTopics()
  }
}
const getTopics = async () => {
  const respone = await axios.post('http://localhost:8080/api/op_code', {code: 'more'}, {
    headers: {
      'Content-Type': 'application/json'
    }
  })
  // console.log(`data is ${JSON.stringify(respone.data)}`)
  _.forEach(respone.data, (value, key) => {
    const topicData = _.merge({topic_id: key}, value)
    const findData = _.find(topics.value, {topic_id: key})
    if (!_.isNil(findData)) _.assign(findData, topicData)
    else topics.value.push(topicData)
  })
  console.log(`topic_len ${topics.value.length}`)
}
</script>

<style scoped>
</style>