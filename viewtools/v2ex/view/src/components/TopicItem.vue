<script setup>
import {defineProps, ref} from 'vue'
import {StarFilled} from "@element-plus/icons-vue";
import {NAvatar, NBadge, NIcon} from "naive-ui";

const props = defineProps(['topic'])
const loadImage = ref(true)
const isStar = ref(props.topic.is_star >= 0)
const getTime = (timestamp) => {
  const date = new Date(timestamp);
  const year = date.getFullYear();
  const month = ('0' + (date.getMonth() + 1)).slice(-2); // 月份从 0 开始，需要加 1
  const day = ('0' + date.getDate()).slice(-2);
  const hour = ('0' + date.getHours()).slice(-2);
  const minute = ('0' + date.getMinutes()).slice(-2);
  const second = ('0' + date.getSeconds()).slice(-2);
  return `${year}-${month}-${day} ${hour}:${minute}:${second}`;
}

const handleStar = () => {
  console.log(`is_star ${isStar.value}`)
  isStar.value = !isStar.value
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
        <p class="text-sm ">{{ getTime(topic.time * 1000) }}</p>
        <p class="text-sm font-bold mr-5">{{ topic.topic_id }}</p>
        <n-icon size="20" :color="isStar?'red':'gray'" class="mr-5" @click="handleStar">
          <StarFilled/>
        </n-icon>
      </div>
      <div class="flex-grow bg-blue-100 flex flex-row-reverse w-full items-center">
        <n-badge :value="topic.reply_num" :max="1500" show-zero/>
        <p class="ml-1 text-left text-xl flex-grow">
          {{ topic.content }}
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>