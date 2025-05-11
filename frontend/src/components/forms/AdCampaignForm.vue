<template>
  <el-form :model="form" status-icon label-width="auto" style="max-width: 600px" ref="formRef">
    <el-form-item label="Campaign name" prop="name" :rules="rules.name">
      <el-input v-model="form.name"/>
    </el-form-item>
    <el-form-item label="Campaign description" prop="description" :rules="rules.description">
      <el-input v-model="form.description" type="textarea"/>
    </el-form-item>
    <el-form-item label="Campaign start date" prop="start_date" :rules="rules.start_date">
      <el-date-picker
        v-model="form.start_date"
        type="date"
        placeholder="Pick a date"
        style="width: 100%"
      />
    </el-form-item>
    <el-form-item label="Campaign end date" prop="end_date" :rules="rules.end_date">
      <el-date-picker
        v-model="form.end_date"
        type="date"
        placeholder="Pick a date"
        style="width: 100%"
      />
    </el-form-item>
    <el-form-item label="Campaign budget" prop="budget" :rules="rules.budget">
      <el-input type="number" v-model="form.budget"/>
    </el-form-item>
    <el-form-item label="Campaign status" prop="status">
      <el-switch v-model="form.status"/>
    </el-form-item>
    <el-form-item>
      <el-button block type="primary" @click="submitForm(formRef)">{{isEdit ? 'Update' : 'Create'}}</el-button>
      <el-button @click="onCancel">Cancel</el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import {ref, watch, computed} from 'vue'
import {useRouter} from "vue-router";
import type {FormInstance} from "element-plus";
import {type AdCampaign, createCampaign, updateCampaign} from "@/lib/adCampaign.ts";

const router = useRouter()

const formRef = ref<FormInstance>();
const form = ref({
  name: '',
  description: '',
  start_date: '',
  end_date: '',
  budget: 0,
  status: true,
})

const props = defineProps<{
  campaign?: AdCampaign
}>()

watch(
  () => props.campaign,
  (newVal) => {
    if (newVal) {
      const { name, description, start_date, end_date, budget, status } = newVal
      form.value = {
        name,
        description,
        start_date,
        end_date,
        budget,
        status,
      }
    }
  },
  { immediate: true }
)

const isEdit = computed(() => !!props.campaign?.id)

const rules = {
  name: [
    { required: true, message: 'Campaign name is required', trigger: 'blur' },
  ],
  description: [
    { required: true, message: 'Campaign description is required', trigger: 'blur' },
  ],
  start_date: [
    { required: true, message: 'Campaign start date is required', trigger: 'change' },
  ],
  end_date: [
    { required: true, message: 'Campaign end date is required', trigger: 'change' },
    // Need to use any otherwise the build will fail (even with the correct type)
    { validator: (rule: any, value: string, callback: (error?: string | Error) => void) => {
        if (new Date(value) < new Date(form.value.start_date)) {
          callback(new Error('End date must be after start date'))
        } else {
          callback()
        }
      }, trigger: 'change'
    }
  ],
  budget: [
    { required: true, message: 'Campaign budget is required', trigger: 'blur' },
    // Need to use any otherwise the build will fail (even with the correct type)
    { validator: (rule: any, value: string, callback: (error?: string | Error) => void) => {
        if (Number(value) < 0) {
          callback(new Error('Budget must be greater than or equal to 0'))
        } else {
          callback()
        }
      }, trigger: 'blur'
    }
  ],
}

const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return

  try {
    await formEl.validate();

  } catch (error) {
    console.error('error validate!', error);
    return
  }

  try {
    if (isEdit.value && props.campaign?.id) {
      await updateCampaign(props.campaign.id, form.value)
      alert('Campaign updated successfully!')
    } else if (!isEdit.value) {
      await createCampaign(form.value)
      alert('Campaign created successfully!')
    }
    await router.push('/')
  } catch (error) {
    alert(`Error ${isEdit.value ? 'edit' : 'create'} campaign`)
    console.error('error submit!', error);
  }
}

const onCancel = () => {
  router.push('/')
}

</script>
