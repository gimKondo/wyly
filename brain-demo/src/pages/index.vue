<template>
  <div>{{ helloWorld }}</div>
</template>
<script lang="ts">
import { Component, Vue } from "nuxt-property-decorator";

@Component({
  middleware: "auth-filter"
})
export default class Index extends Vue {
  get helloWorld(): string {
    return "Hello world!";
  }
}
</script>
