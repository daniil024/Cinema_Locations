<template>
  <Mainlayouts>
    <EditServiceForm />
  </Mainlayouts>
</template>
<script>
import EditServiceForm from '@/components/Profile/EditServiceForm.vue'
import Mainlayouts from '@/layouts/MainLayouts.vue'
export default {
  name: "EditService",
  components: { EditServiceForm, Mainlayouts }
}
</script>