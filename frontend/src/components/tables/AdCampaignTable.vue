<template>
  <el-button type="primary" size="small" @click="onCreateCampaign">Create an adCampaign</el-button>
  <el-table :data="campaigns" style="width: 100%">
    <el-table-column prop="name" label="Name" fixed="left" />
    <el-table-column prop="description" label="Description" width="180" />
    <el-table-column prop="start_date" label="Start date" >
      <template #default="scope">
        {{ new Date(scope.row.start_date).toLocaleDateString() }}
      </template>
    </el-table-column>
    <el-table-column prop="end_date" label="End date" >
      <template #default="scope">
        {{ new Date(scope.row.end_date).toLocaleDateString() }}
      </template>
    </el-table-column>
    <el-table-column prop="budget" label="Budget" />
    <el-table-column prop="status" label="Status" >
      <template #default="scope">
        <el-tag :type="scope.row.status ? 'success' : 'danger'">
          {{ scope.row.status ? 'Activate' : 'Desactivate' }}
        </el-tag>
      </template>
    </el-table-column>
    <el-table-column label="Actions" fixed="right">
      <template #default="scope">
        <el-button link :type="scope.row.status ? 'danger' : 'success'" @click="onChangeCampaignStatus(scope.row.id, !scope.row.status)" size="small">
          {{scope.row.status ? 'Desactivate' : 'Activate'}}
        </el-button>
        <el-button link type="primary" size="small" @click="onEditCampaign(scope.row.id)">Edit</el-button>
        <el-button link type="danger" size="small" @click="onDeleteCampaign(scope.row.id)">Delete</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { fetchCampaigns, deleteCampaign, changeCampaignStatus } from "@/lib/adCampaign.ts";
import {useRouter} from "vue-router";

const campaigns = ref<any[]>([])

onMounted(async () => {
  const data = await fetchCampaigns()
  if (data) {
    campaigns.value = data
    console.log(campaigns);
  }
})

const onDeleteCampaign = async (id: number) => {
  try {
    await deleteCampaign(id);
    alert("Campaign deleted successfully!");
    window.location.reload();
  } catch (e) {
    alert('Error deleting campaign: ');
  }
}

const onChangeCampaignStatus = async (id: number, status: boolean) => {
  try {
    await changeCampaignStatus(id, status);
    alert("Campaign status changed successfully!");
    window.location.reload();
  } catch (e) {
    alert('Error changing campaign status: ');
  }
}

const router = useRouter()

const onCreateCampaign = async () => {
  await router.push('/adCampaigns/create');
}

const onEditCampaign = async (id: number) => {
  await router.push(`/adCampaigns/${id}`);
}

</script>
