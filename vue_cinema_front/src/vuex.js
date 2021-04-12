import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex);

const state = {
    user: null,
    token: null,    
};

const store = new Vuex.Store({
state,
getters:{
    user: (state)=>{
        return state.user;
    },
    token: (state)=>{
        return state.token;
    }
},
actions:{
    user(context, user){
        context.commit('user', user);
    },
    token(context, token){
        context.commit('token', token);
    }
},
mutations:{
    user(state, user){
        state.user = user;
    },
    token(state, token){
        state.token = token;
    }
},

plugins: [createPersistedState()]
});

export default store;