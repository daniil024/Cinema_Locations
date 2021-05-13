<template>
 <div class="container p-5">
	    <h2 class="font-weight-bold mt-3">Password Reset Confirm</h2>
		<hr>
        <p>Please enter your new password.</p>
        <form method="POST">
            {% csrf_token %}
            {{ form|crispy }}                    
            <button class="btn btn-primary" type="submit">Reset password</button>
        </form>
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