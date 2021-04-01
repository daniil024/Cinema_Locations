<template>
  <b-col cols="6" class="mx-auto border p-3 rounded">
      <!-- При вызове этой формы вместо slot будет вставляться другая любая форма -->
    <slot></slot> 
  </b-col>
</template>
<script>
export default {
  name: 'BaseAuthLayout'
}
</script>