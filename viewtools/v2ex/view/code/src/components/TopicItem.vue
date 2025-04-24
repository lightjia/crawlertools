<script setup>
import {defineProps} from 'vue'

defineProps(['topic'])
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
</script>

<template>
  <div class="h-32"><p>{{ getTime(topic.time * 1000) }}</p></div>
  <!--  <div class="grid grid-rows-12 grid-cols-12 gap-0 h-52 mb-1">-->
  <!--    <div class="row-span-full col-span-1 flex items-center justify-center">-->
  <!--      <div class="m-1 w-32 ">-->
  <!--        <span class="break-words font-bold text-3xl shadow">-->
  <!--        {{ topic.userName }}-->
  <!--      </span>-->
  <!--      </div>-->

  <!--    </div>-->
  <!--    <div class="row-end-12 col-span-11 row-span-11 flex items-center justify-between  bg-gray-300 "><p-->
  <!--        class="ml-1 text-xl">-->
  <!--      {{ topic.content }}</p>-->
  <!--      <div class="flex justify-between mr-2">-->
  <!--        <button class="badge bg-red-500 text-white px-2 py-1 font-bold shadow">-->
  <!--          {{ topic.reply_num }}-->
  <!--        </button>-->
  <!--      </div>-->
  <!--    </div>-->
  <!--    <div class="row-start-12 row-span-1 col-span-11 mb-1">-->
  <!--      <div class="flex justify-end  items-center space-x-2">-->
  <!--        <p class="font-extrabold">{{ topic.topic_id }}</p>-->
  <!--        <p>{{ getTime(topic.time * 1000) }}</p>-->
  <!--      </div>-->
  <!--    </div>-->
  <!--  </div>-->
  <!--  <div class="flex  justify-between items-end  bg-gray-300">-->
  <!--    <div class="w-16 h-16 bg-blue-500 flex items-center justify-center text-xl text-white rounded-full mr-4">-->
  <!--      <span class="text-wrap">{{ topic.userName }}</span>-->
  <!--    </div>-->
  <!--    <p class="text-3xl">{{ topic.content }}</p>-->
  <!--    <div class="flex justify-between mr-2">-->
  <!--      <p class="mr-1">{{ getTime(topic.time * 1000) }}</p>-->
  <!--      <button class="badge bg-red-500 text-white px-2 py-1 font-bold shadow">-->
  <!--        {{ topic.reply_num }}-->
  <!--      </button>-->
  <!--    </div>-->
  <!--  </div>-->
</template>

<style scoped>

</style>