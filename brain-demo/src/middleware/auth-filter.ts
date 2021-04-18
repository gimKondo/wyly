import { Context } from "@nuxt/types";

export default ({ redirect, app: { $accessor } }: Context) => {
  if (!$accessor.user.token) {
    return redirect("/login");
  }
};
