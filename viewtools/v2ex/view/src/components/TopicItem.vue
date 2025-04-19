<script setup>
import {defineProps} from 'vue'

defineProps(['topic'])
const getTime = (timestamp) => {
  const date = new Date(timestamp);
  const options = {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    hour12: false
  };
  return new Intl.DateTimeFormat('en-GB', options).format(date);

}
</script>

<template>
  <div class="grid grid-rows-12 grid-cols-12 gap-0 h-52">
    <div class="row-span-full col-span-1 flex items-center justify-center">
      <span class="font-bold  text-2xl">
        {{ topic.userName }}
      </span>
    </div>
    <div class="row-end-12 col-span-11 row-span-11 flex items-center justify-between  bg-gray-300 "><p
        class="ml-1 text-3xl">
      {{ topic.content }}</p>
      <div class="flex justify-between mr-2">
        <button class="badge bg-red-500 text-white px-2 py-1 font-bold shadow">
          {{ topic.reply_num }}
        </button>
      </div>
    </div>
    <div class="row-start-12 row-span-1 col-span-11 mb-1"><p class="mr-1">{{ getTime(topic.time * 1000) }}</p>
    </div>
  </div>
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