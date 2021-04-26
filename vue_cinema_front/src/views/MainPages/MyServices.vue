<template>
  <Mainlayouts>
    <MyServicesForm />
  </Mainlayouts>
</template>
<script>
import MyServicesForm from '@/components/Profile/MyLocationsForm.vue'
import Mainlayouts from '@/layouts/MainLayouts.vue'
export default {
  name: "MyServices",
  components: { MyServicesForm, Mainlayouts }
}
</script>