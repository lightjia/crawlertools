<script setup>
import {defineProps, ref} from 'vue'
import {StarFilled} from "@element-plus/icons-vue";
import {NAvatar, NBadge, NButton, NDrawer, NDrawerContent, NIcon, NTime} from "naive-ui";
import axios from "axios";
import TopicReplys from "@/components/TopicReplys.vue";

const props = defineProps(['topic'])
const loadImage = ref(true)
const isStar = ref(props.topic.is_star >= 0)
const isView = ref(false)
const replys = ref([])
const stickyPosition = ref('static')
const handleStar = () => {
  console.log(`is_star ${isStar.value}`)
  isStar.value = !isStar.value
}
const handleView = async () => {
  isView.value = !isView.value
  if (isView.value) {
    stickyPosition.value = 'sticky'
    const response = await axios.post('http://localhost:8080/api/op_code', {
      code: 'detail',
      topic_id: props.topic.topic_id
    }, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
    replys.value = response.data
  }
}
const handleOrigin = () => {
  window.open(`https://global.v2ex.co/t/${props.topic.topic_id}`, '_blank');
}
</script>

<template>
  <div class="min-h-28 max-h-96 mt-2 mb-2 w-full border-dashed border-2 flex justify-start">
    <div class="self-center w-20 flex items-center justify-center">
      <img class="w-full h-full" v-if="loadImage" :src="topic.userImg" @error="()=>loadImage = false"/>
      <n-avatar v-else round :size="78">
        {{ topic.userName }}
      </n-avatar>
    </div>
    <div class="flex-grow flex flex-col-reverse">
      <div class="pt-1 pb-1 h-4 flex flex-row-reverse justify-start items-center bg-gray-300">
        <n-time :time="topic.time" format="yyyy-MM-dd hh:mm:ss" unix/>
        <p class="text-sm font-bold mr-5">{{ topic.topic_id }}</p>
        <n-icon size="20" :color="isStar?'red':'gray'" class="mr-5" @click="handleStar">
          <StarFilled/>
        </n-icon>
      </div>
      <div
          :class="['flex-grow', {'bg-blue-100':!isView}, {'bg-lime-500':isView},'flex', 'flex-row-reverse', 'w-full', 'items-center']"
          @click="handleView">
        <n-badge :value="topic.reply_num" :max="1500" show-zero/>
        <p class="ml-1 text-left text-xl flex-grow">
          {{ topic.content }}
        </p>
      </div>
    </div>
  </div>
  <n-drawer v-model:show="isView" style="width: 75vw;" on-after-leave="handleView">
    <n-drawer-content closable>
      <template #header>
        <div class="flex flex-row-reverse justify-start mr-2">
          <n-button type="primary" @click="handleOrigin">
            查看原文
          </n-button>
          <p class="flex-grow text-pink-900 font-bold text-xl"> {{ topic.content }}</p>
        </div>
      </template>
      <TopicReplys v-for="(item, index) in replys" :key="index" :reply="item"></TopicReplys>
    </n-drawer-content>
  </n-drawer>
</template>

<style scoped>

</style>