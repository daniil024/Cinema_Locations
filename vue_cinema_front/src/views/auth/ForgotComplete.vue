<template>
  <base-auth-layout>
    <PasswordResetComplete/>
  </base-auth-layout>
</template>
<script>
import PasswordResetComplete from '@/components/auth/PasswordResetComplete.vue'
import BaseAuthLayout from '@/layouts/BaseAuthLayout.vue'
export default {
  name: "ForgotComplete",
  components: { PasswordResetComplete, BaseAuthLayout }
}
</script>