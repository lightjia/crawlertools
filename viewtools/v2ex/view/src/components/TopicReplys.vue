<script setup>
import {defineProps} from "vue";
import {NDivider, NGi, NGrid, NTime} from "naive-ui";

defineProps(['reply'])
</script>

<template>
  <n-divider dashed/>
  <n-grid>
    <n-gi span="2">
      <p class="font-bold text-lime-600 text-left break-words">
        {{ reply.userName }}
      </p>
    </n-gi>
    <n-gi span="22">
      <div class="flex-grow flex flex-col-reverse pl-1">
        <n-time class="self-end text-sm" :time="reply.time" format="yyyy-MM-dd hh:mm:ss" unix/>
        <p class="flex-grow text-left text-xl text-wrap">
          {{ reply.content }}
        </p>
      </div>

    </n-gi>
  </n-grid>
</template>

<style scoped>

</style>