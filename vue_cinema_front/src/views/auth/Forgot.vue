<template>
  <base-auth-layout>
    <forgot-form />
  </base-auth-layout>
</template>
<script>
import ForgotForm from '@/components/auth/ForgotForm.vue'
import BaseAuthLayout from '@/layouts/BaseAuthLayout.vue'
export default {
  name: "Forgot",
  components: { ForgotForm, BaseAuthLayout }
}
</script>