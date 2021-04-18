export default {
  generate: {
    dir: "../public"
  },
  buildModules: [
    "@nuxt/typescript-build",
    "nuxt-typed-vuex"
  ],
  publicRuntimeConfig: {
    firebase: {
      apiKey: process.env.FIREBASE_AUTH_API_KEY,
      authDomain: process.env.FIREBASE_AUTH_DOMAIN
    }
  },
  typescript: {
    typeCheck: {
      eslint: {
        files: "./**/*.{ts,js,vue}"
      }
    }
  }
};
