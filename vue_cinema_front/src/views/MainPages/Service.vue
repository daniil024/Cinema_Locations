<template>
  <Mainlayouts>
    <ServiceForm />
  </Mainlayouts>
</template>
<script>
import ServiceForm from '@/components/SearchAndMain/ServiceForm.vue'
import Mainlayouts from '@/layouts/MainLayouts.vue'
export default {
  name: "Service",
  components: { ServiceForm, Mainlayouts }
}
</script>