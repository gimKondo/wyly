<template>
  <div class="container">
    <div>
      <h1 class="title">
        Login Page
      </h1>
      <div>
        <button class="button--grey" @click="authGoogle">
          Googleでログイン
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

import { Auth, PROVIDERS } from "@/services/auth";
export default Vue.extend({
  async asyncData() {},
  data() {
    return {};
  },
  methods: {
    async authGoogle() {
      const auth = new Auth(this.$accessor, this.$config.firebase);
      await auth.login(PROVIDERS.Google);
      this.$router.push("/");
    }
  }
});
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>
