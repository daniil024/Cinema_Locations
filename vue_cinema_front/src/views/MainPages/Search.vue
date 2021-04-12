<template>
  <Mainlayouts>
    <SearchForm />
  </Mainlayouts>
</template>
<script>
import SearchForm from '@/components/SearchAndMain/SearchForm.vue'
import Mainlayouts from '@/layouts/MainLayouts.vue'
export default {
  name: "Search",
  components: { SearchForm, Mainlayouts }
}
</script>