import { test, expect } from '@playwright/test';


test('user can log in successfully', async ({ page }) => {
  // Navigate using the configured baseURL
  await page.goto('/login');

  // Locate elements using accessible user-facing attributes
  await page.getByLabel('User Name').fill('user@example.com');
  await page.getByLabel('Password').fill('SecurePassword123');
  
  // Trigger submission
  await page.getByRole('button', { name: 'Sign In' }).click();

  await page.goto('/dashboard'); // Change to your actual route

  // Finds a button specifically containing the exact text "Settings"
  const settingsButton = page.getByRole('button', { name: 'Settings', exact: true });
  
  // Asserts the element is rendered and visible in the viewport
  await expect(settingsButton).toBeVisible();

  await expect(page )
});
