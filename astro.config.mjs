// @ts-check
import { defineConfig } from 'astro/config';

import preact from "@astrojs/preact";

import sitemap from "@astrojs/sitemap";

// https://astro.build/config
export default defineConfig({
  site: "https://profound-snickerdoodle-c52602.netlify.app",
  integrations: [preact(), sitemap({
    filter: (page) => page !== 'https://profound-snickerdoodle-c52602.netlify.app/internal',
    xslURL: '/sitemap.xsl'
  })]
});