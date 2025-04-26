<template>
  <n-infinite-scroll style="height: calc(100% - 64px);" :distance="10" @load="handleLoad">
    <TopicItem v-for="(item, index) in topics" :key="index" :topic="item"></TopicItem>
  </n-infinite-scroll>
</template>

<script setup>
import TopicItem from './TopicItem.vue'
import {onMounted, ref} from "vue"
import axios from "axios";
import _ from "lodash";
import {NInfiniteScroll} from "naive-ui";

const topics = ref([])
onMounted(async () => {
  await handleLoad()
})

const handleLoad = async () => {
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