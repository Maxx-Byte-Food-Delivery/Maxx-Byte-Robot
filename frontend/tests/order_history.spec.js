import { test, expect } from '@playwright/test';


test('user can log in and see orders', async ({ page }) => {
  await page.goto('/'); 

  // Use standard locator attribute syntax to find placeholders
  await page.locator('input[placeholder="Username"]').fill('bob_smith');
  await page.locator('input[placeholder="Password"]').fill('Bob@456');

  // Use text matcher for the button
  await page.locator('button:has-text("Login")').click();

  await expect(page).toHaveURL(/\/(student|staff)/);

  await page.goto('/orders');
  await page.locator('body:has-text("View Order History")')
  await page.locator('body:has-text("Total: $11.99")')
  await page.locator('body:has-text("Status: pending")')
});

