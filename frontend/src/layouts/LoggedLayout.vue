<template>
  <div class="h-[60px] w-full flex items-center justify-between" style="background: white; padding: 1rem; top: 0; left: 0">
    <el-button text @click="goHome" style="font-weight: bold">AdCampaign</el-button>

    <div class="flex items-center gap-4" style="gap: 1rem">
      <el-text style="color: black">{{ username }}</el-text>
      <el-button type="danger" @click="logout">Logout</el-button>
    </div>
  </div>

  <main class="w-full h-full p-4" style="padding: 1rem">
    <RouterView/>
  </main>
</template>

<script setup lang="ts">
import {RouterView, useRouter} from 'vue-router'
import {logout} from "@/lib/auth.js"
import { ref, onMounted } from 'vue';

const username = ref('');

onMounted(() => {
  username.value = sessionStorage.getItem('username') || '';
});

const router = useRouter()

function goHome() {
  router.push('/')
}

</script>

<style scoped>
</style>
