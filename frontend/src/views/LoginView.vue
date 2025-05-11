<template>
  <main class="w-full h-full flex items-center justify-center">
    <el-card class="w-96 p-6 shadow-md m-auto flex flex-col items-center justify-between gap-2">
      <h2 class="text-center text-2xl font-semibold mb-6">Connection</h2>

      <el-form :model="form" status-icon ref="formRef">
        <el-form-item label="Email" prop="email" :rules="rules.email">
          <el-input v-model="form.email" placeholder="Email" />
        </el-form-item>

        <el-form-item label="Password" prop="password" :rules="rules.password">
          <el-input
            v-model="form.password"
            type="password"
            placeholder="Password"
          />
        </el-form-item>

        <el-form-item>
          <el-button type="primary" block @click="submitForm(formRef)">Login</el-button>
        </el-form-item>
      </el-form>

      <p class="text-center text-sm mt-4">
        Don't have an account ? <a href="/register" class="text-blue-500">Sign up</a>
      </p>
    </el-card>
  </main>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import {ElForm, ElFormItem, ElInput, ElButton} from 'element-plus'
import type { FormInstance } from 'element-plus'
import {getToken} from "@/lib/auth.js"

const formRef = ref<FormInstance>();
const form = ref({
  email: '',
  password: ''
})

const rules = {
  email: [
    { required: true, message: 'Email missing', trigger: 'blur' },
    { type: 'email' as const, message: 'Email is invalid', trigger: 'blur' }
  ],
  password: [
    { required: true, message: 'Password missing', trigger: 'blur' },
  ]
}

const router = useRouter()
const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return

  try {
    await formEl.validate();

  } catch (error) {
    console.error('error validate!', error);
    return
  }

  try {
    await formEl.validate();

    await getToken(form.value.email, form.value.password);
    await router.push('/');
    alert('Login successful!');
  } catch (error) {
    alert('Login failed!');
    console.error('error submit!', error);
  }
}
</script>
