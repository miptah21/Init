import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './.agents/skills',
  fullyParallel: true,
  reporter: 'line',
  use: {
    headless: true,
  },
});
