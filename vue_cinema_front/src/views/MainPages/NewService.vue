<template>
  <Mainlayouts>
    <NewServiceForm />
  </Mainlayouts>
</template>
<script>
import NewServiceForm from '@/components/SearchAndMain/NewServiceForm.vue'
import Mainlayouts from '@/layouts/MainLayouts.vue'
export default {
  name: "NewService",
  components: { NewServiceForm, Mainlayouts }
}
</script>