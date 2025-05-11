<template>
  <el-card class="w-full">
    <template #header>
      <div class="card-header">
        <span>Create an AdCampaign</span>
      </div>
    </template>
    <AdCampaignForm/>
  </el-card>
</template>

<script setup lang="ts">
import AdCampaignForm from "@/components/forms/AdCampaignForm.vue";
</script>
