# SauceDemo Login Test Plan

## Application Overview

Validate the SauceDemo login page and observed authentication outcomes using independent tests that start from the fresh login page at https://www.saucedemo.com/. Assertions are limited to the supplied live observations; this plan does not assert that any test has been executed.

## Test Scenarios

### 1. Login Page and Form

**Seed:** `seed.spec.ts`

#### 1.1. Display login controls and accepted credentials

**File:** `specs/login-test-plan.spec.ts`

**Steps:**
  1. Open https://www.saucedemo.com/ from a fresh browser state.
    - expect: The page title is Swag Labs.
    - expect: The page exposes a Username textbox, a Password textbox, and a Login button.
    - expect: The page displays the accepted usernames standard_user, locked_out_user, problem_user, performance_glitch_user, error_user, and visual_user.
    - expect: The page displays the common password secret_sauce.

#### 1.2. Require a username when submitting an empty form

**File:** `specs/login-test-plan.spec.ts`

**Steps:**
  1. Open https://www.saucedemo.com/ from a fresh browser state and leave both textboxes empty.
    - expect: The Username and Password textboxes and Login button are visible.
  2. Click Login.
    - expect: The page displays the error message 'Epic sadface: Username is required'.

### 2. Login Outcomes

**Seed:** `seed.spec.ts`

#### 2.1. Reject standard_user with an incorrect password

**File:** `specs/login-test-plan.spec.ts`

**Steps:**
  1. Open https://www.saucedemo.com/ from a fresh browser state.
    - expect: The login form is available.
  2. Enter standard_user in the Username textbox and wrong_password in the Password textbox, then click Login.
    - expect: The page displays the error message 'Epic sadface: Username and password do not match any user in this service'.

#### 2.2. Show locked-out message for locked_out_user

**File:** `specs/login-test-plan.spec.ts`

**Steps:**
  1. Open https://www.saucedemo.com/ from a fresh browser state.
    - expect: The login form is available.
  2. Enter locked_out_user in the Username textbox and secret_sauce in the Password textbox, then click Login.
    - expect: The page displays the error message 'Epic sadface: Sorry, this user has been locked out.'.

#### 2.3. Log in successfully as standard_user

**File:** `specs/login-test-plan.spec.ts`

**Steps:**
  1. Open https://www.saucedemo.com/ from a fresh browser state.
    - expect: The login form is available.
  2. Enter standard_user in the Username textbox and secret_sauce in the Password textbox, then click Login.
    - expect: The browser navigates to /inventory.html.
