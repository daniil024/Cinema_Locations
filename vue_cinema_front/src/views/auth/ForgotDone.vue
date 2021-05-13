<template>
  <base-auth-layout>
    <PasswordResetDone/>
  </base-auth-layout>
</template>
<script>
import PasswordResetDone from '@/components/auth/PasswordResetDone.vue'
import BaseAuthLayout from '@/layouts/BaseAuthLayout.vue'
export default {
  name: "ForgotDone",
  components: { PasswordResetDone, BaseAuthLayout }
}
</script>