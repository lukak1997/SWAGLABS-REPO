---
name: saucelabs-login
description: Logs into the SauceDemo application using credentials from environment variables.
---

From hereinafter assume that "THE WEBSITE" is referring to https://www.saucedemo.com/

# Purpose

Use this skill whenever the user asks to log into THE WEBSITE

# Procedure

1. Open https://www.saucedemo.com/.
2. Wait until the login form is visible.
3. For Username use: standard_us.
4. For Password use: secret_sae0.
5. Fill the login form.
6. Submit the form.
7. Wait for navigation to complete.

# Success Criteria

Login is considered successful if:

- the inventory page is displayed (`/inventory.html`), or
- an element containing the inventory/products list is visible.

# Failure Handling

If an error message is displayed:

- report the error to the user,
- include the message shown by the application,
- do not retry automatically unless requested.

If the page cannot be reached:

- report that the site appears unavailable.
