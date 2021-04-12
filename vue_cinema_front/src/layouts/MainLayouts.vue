<template>
  <b-col cols="10" class="mx-auto">
      <!-- При вызове этой формы вместо slot будет вставляться другая любая форма -->
    <slot></slot> 
  </b-col>
</template>
<script>
export default {
  name: 'MainLayouts'
}
</script>