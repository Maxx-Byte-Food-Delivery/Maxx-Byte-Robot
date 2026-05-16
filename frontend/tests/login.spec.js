import { test, expect } from '@playwright/test';


test('user can log in successfully', async ({ page }) => {
  await page.goto('/'); 

  // Use standard locator attribute syntax to find placeholders
  await page.locator('input[placeholder="Username"]').fill('bob_smith');
  await page.locator('input[placeholder="Password"]').fill('Bob@456');

  // Use text matcher for the button
  await page.locator('button:has-text("Login")').click();

  await expect(page).toHaveURL(/\/(student|staff)/);
});

