<template>
  <el-card class="w-full">
    <template #header>
      <div class="card-header">
        <span>Edit an AdCampaign</span>
      </div>
    </template>
    <AdCampaignForm v-if="campaign" :campaign="campaign" />
    <div v-else>Loading...</div>
  </el-card>
</template>

<script setup lang="ts">
import AdCampaignForm from "@/components/forms/AdCampaignForm.vue";
import {ref, onMounted} from 'vue'
import {useRoute} from 'vue-router'
import {type AdCampaign, getCampaign} from '@/lib/adCampaign.ts'

const route = useRoute()
const campaign = ref<AdCampaign | null>(null)

onMounted(async () => {
  const id = Number(route.params.id)
  try {
    campaign.value = await getCampaign(id)
  } catch (e) {
    console.error('Error loading campaign:', e)
  }
})

</script>
