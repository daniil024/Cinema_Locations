<template>
  <Mainlayouts>
    <LK-form />
  </Mainlayouts>
</template>
<script>
import LKForm from '@/components/Profile/LKForm.vue'
import Mainlayouts from '@/layouts/MainLayouts.vue'
export default {
  name: "LK",
  components: { LKForm, Mainlayouts }
}
</script>