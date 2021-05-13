<template>
  <base-auth-layout>
    <PasswordResetConfirm/>
  </base-auth-layout>
</template>
<script>
import PasswordResetConfirm from '@/components/auth/PasswordResetConfirm.vue'
import BaseAuthLayout from '@/layouts/BaseAuthLayout.vue'
export default {
  name: "ForgotConfirm",
  components: { PasswordResetConfirm, BaseAuthLayout }
}
</script>