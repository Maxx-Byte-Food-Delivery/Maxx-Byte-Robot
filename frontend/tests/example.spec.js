import { test, expect } from '@playwright/test';

test('user can log in successfully', async ({ page }) => {
  // 1. Navigate to the frontend login page
  await page.goto('/'); 

  // 2. Fill in the login form fields using placeholder text matching your JSX
  await page.getByPlaceholderText('Username').fill('user@example.com');
  await page.getByPlaceholderText('Password').fill('SecurePassword123');

  // 3. Click the login button matching your JSX text
  await page.getByRole('button', { name: 'Login', exact: true }).click();

  // 4. Assert transition to one of your component's redirect paths (e.g., /student or /staff)
  await expect(page).toHaveURL(/\/(student|staff)/);
});

