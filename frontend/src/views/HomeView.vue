<template>
  <el-card class="w-full">
    <template #header>
      <div class="card-header">
        <span>AdCampaign list</span>
      </div>
    </template>
    <AdCampaignTable/>
  </el-card>
</template>

<script setup lang="ts">
import AdCampaignTable from "@/components/tables/AdCampaignTable.vue";
</script>
