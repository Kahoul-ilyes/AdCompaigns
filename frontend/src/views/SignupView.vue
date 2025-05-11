<template>
  <main class="w-full h-full flex items-center justify-center">
    <el-card class="w-96 p-6 shadow-md m-auto flex flex-col items-center justify-between gap-2">
      <h2 class="text-center text-2xl font-semibold mb-6">Register</h2>

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

        <el-form-item label="Password confirmation" prop="passwordConfirmation" :rules="rules.passwordConfirmation">
          <el-input
            v-model="form.passwordConfirmation"
            type="password"
            placeholder="Password confirmation"
          />
        </el-form-item>

        <el-form-item>
          <el-button type="primary" block @click="submitForm(formRef)">Signup</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </main>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import {ElForm, ElFormItem, ElInput, ElButton} from 'element-plus'
import type { FormInstance } from "element-plus";
import { register } from "@/lib/auth.ts";

const formRef = ref<FormInstance>();
const form = ref({
  email: '',
  password: '',
  passwordConfirmation: ''
})

const rules = {
  email: [
    { required: true, message: 'Email missing', trigger: 'blur' },
    { type: 'email' as const, message: 'Email is invalid', trigger: 'blur' }
  ],
  password: [
    { required: true, message: 'Password missing', trigger: 'blur' },
  ],
  passwordConfirmation: [
    { required: true, message: 'Password confirmation missing', trigger: 'blur' },
    // Need to use any otherwise the build will fail (even with the correct type)
    { validator: (rule: any, value: string, callback: (error?: string | Error) => void) => {
        if (value !== form.value.password) {
          callback(new Error('Passwords do not match'))
        } else {
          callback()
        }
      },
      trigger: 'blur'
    }
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

    await register(form.value.email, form.value.password);

    await router.push('/login');
    alert('Registration successful!');
  } catch (error) {
    alert('Registration failed!');
    console.error('error submit!', error);
  }
}
</script>
