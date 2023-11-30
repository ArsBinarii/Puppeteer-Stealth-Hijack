const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
    // Read the session ID from sessionID.json
    const sessionData = JSON.parse(fs.readFileSync('sessionID.json', 'utf8'));
    const sessionId = sessionData.sessionId;

    // Define the WebSocket endpoint URL
    const wsChromeEndpointurl = `ws://127.0.0.1:9222/devtools/browser/${sessionId}`;

    // Connect to the existing Chrome instance
    const browser = await puppeteer.connect({
        browserWSEndpoint: wsChromeEndpointurl,
    });

    // Create a new page
    const page = await browser.newPage();

    // Navigate to Google and perform a search
    await page.goto('https://www.google.com');
    await page.type('[name=q]', 'Puppeteer'); // Replace 'Puppeteer' with your search query
    await page.keyboard.press('Enter');

    // Wait for search results page to load
    await page.waitForNavigation();
    console.log("[END]");
    process.exit(0);
})();

