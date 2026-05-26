import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './skills',
  fullyParallel: true,
  reporter: 'line',
  use: {
    headless: true,
  },
});
