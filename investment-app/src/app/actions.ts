"use server";

import { cookies } from "next/headers";

export async function setLanguage(lang: "ge" | "en") {
  const cookieStore = await cookies();
  cookieStore.set("lang", lang, { path: "/", maxAge: 60 * 60 * 24 * 365 }); 
}
