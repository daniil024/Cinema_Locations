<template>
  <div class="container p-4">
	    <h2 class="font-weight-bold mt-3">Password reset complete</h2>
		<hr>
        <p>Your password has been set. You may go ahead and log in now.</p>                 
        <a href="http://127.0.0.1:8080/auth/signin/" class="btn btn-primary">Log in</a>
    </div>
</template>
<script>
import { mapGetters } from "vuex";
export default {
  name: "ForgotForm",
  data() {
    return {
      form: {
        email: "",
      },
    };
  },
  methods:{
    async handleSubmit(){
      
    }
  },
  
};
</script>