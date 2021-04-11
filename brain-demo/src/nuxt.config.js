export default {
  generate: {
    dir: "../public"
  },
  buildModules: [
    "@nuxt/typescript-build",
    "nuxt-typed-vuex"
  ],
  typescript: {
    typeCheck: {
      eslint: {
        files: "./**/*.{ts,js,vue}"
      }
    }
  }
};
