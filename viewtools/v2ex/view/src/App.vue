<template>
<TopicView></TopicView>
</template>

<script>
import TopicView from './components/TopicView.vue'

export default {
  name: 'App',
  components: {
    TopicView: TopicView
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 20px;
}
</style>
