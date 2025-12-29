const {expect, test} = require("@playwright/test")

// Runs before each tests
test.beforeEach(async ({page}) => {
    await page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
})

// Runs after each tests
test.afterEach(async ({page}) => {
    await page.waitForTimeout(3000)
})

// Validating title
test("1. Validate Title", async ({page}) => {
    const til = await page.title()
    console.log(`Title: ${til}.`)
    // TDD[Test Driven Development] style - to check actual with respect to expected
    await expect(til).toBe("OrangeHRM")
})

// Validating URL
test("2. Validate URL", async ({page}) => {
    const ul = await page.url()
    console.log(`URL: ${ul}.`)
    // TDD style
    await expect(ul).toBe("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
})

test("3. Validate Heading", async ({page}) => {
    const txt = await page.locator('//h5').innerText()
    console.log('Heading Text:', txt);
    await expect(page.locator('//h5')).toHaveText('Login');
})