# User Stories with Acceptance Criteria

Project: **ShopEase – Online Shopping System**

Format: *As a [role], I want [goal], so that [benefit].*

## US-01: User Registration

| Field | Value |
|---|---|
| Use Case | UC-01 |
| Priority | 🔴 High |
| Status | Done |

**As a** new visitor, **I want** to create an account with my name, email and password, **so that** I can shop and track my orders.

**Acceptance Criteria**

1. **Given** I am on the registration page, **When** I enter valid details and click Register, **Then** my account is created and a confirmation email is sent.
2. **Given** I enter an email that already exists, **When** I click Register, **Then** an error 'Email already registered' is shown.
3. **Given** I enter a password shorter than 8 characters, **When** I click Register, **Then** a password-strength error is shown.

---

## US-02: User Login

| Field | Value |
|---|---|
| Use Case | UC-02 |
| Priority | 🔴 High |
| Status | Done |

**As a** registered user, **I want** to log in with my email and password, **so that** I can access my account securely.

**Acceptance Criteria**

1. **Given** I have a valid account, **When** I enter correct credentials, **Then** I am redirected to my dashboard.
2. **Given** I enter a wrong password, **When** I click Login, **Then** an 'Invalid credentials' message is shown.
3. **Given** I fail login 5 times, **When** I try again, **Then** my account is locked for 15 minutes.

---

## US-03: User Logout

| Field | Value |
|---|---|
| Use Case | UC-03 |
| Priority | 🟠 Medium |
| Status | Done |

**As a** logged-in user, **I want** to log out, **so that** my account stays safe on shared devices.

**Acceptance Criteria**

1. **Given** I am logged in, **When** I click Logout, **Then** my session ends and I see the login page.
2. **Given** I have logged out, **When** I press the browser Back button, **Then** I cannot view protected pages.

---

## US-04: Reset Password

| Field | Value |
|---|---|
| Use Case | UC-04 |
| Priority | 🔴 High |
| Status | In Review |

**As a** user who forgot password, **I want** to reset my password via email, **so that** I can regain access.

**Acceptance Criteria**

1. **Given** I am on Forgot Password page, **When** I enter my registered email, **Then** a reset link valid for 30 minutes is emailed.
2. **Given** I open an expired link, **When** the page loads, **Then** an 'Link expired' message is shown.

---

## US-05: Update Profile

| Field | Value |
|---|---|
| Use Case | UC-05 |
| Priority | 🟢 Low |
| Status | To Do |

**As a** logged-in user, **I want** to edit my name, phone and photo, **so that** my details stay current.

**Acceptance Criteria**

1. **Given** I am on my profile page, **When** I change my phone number and save, **Then** the new number is stored and displayed.
2. **Given** I enter an invalid phone number, **When** I save, **Then** a validation error is shown.

---

## US-06: Browse Products

| Field | Value |
|---|---|
| Use Case | UC-06 |
| Priority | 🔴 High |
| Status | Done |

**As a** customer, **I want** to browse products by category, **so that** I can discover items.

**Acceptance Criteria**

1. **Given** I open the home page, **When** I click a category, **Then** products of that category are listed.
2. **Given** a category has no products, **When** I open it, **Then** a 'No products found' message is shown.

---

## US-07: Search Products

| Field | Value |
|---|---|
| Use Case | UC-07 |
| Priority | 🔴 High |
| Status | In Review |

**As a** customer, **I want** to search by keyword, **so that** I can quickly find what I need.

**Acceptance Criteria**

1. **Given** I am on any page, **When** I type 'phone' and press Search, **Then** matching products are displayed.
2. **Given** no product matches, **When** I search, **Then** a 'No results' message with suggestions is shown.

---

## US-08: Filter and Sort Products

| Field | Value |
|---|---|
| Use Case | UC-08 |
| Priority | 🟠 Medium |
| Status | In Progress |

**As a** customer, **I want** to filter by price/brand and sort results, **so that** I can narrow down choices.

**Acceptance Criteria**

1. **Given** a product list is shown, **When** I set a price range, **Then** only products in that range are displayed.
2. **Given** a product list is shown, **When** I choose 'Price: Low to High', **Then** products are sorted ascending.

---

## US-09: View Product Details

| Field | Value |
|---|---|
| Use Case | UC-09 |
| Priority | 🔴 High |
| Status | Done |

**As a** customer, **I want** to see images, price, description and stock, **so that** I can decide to buy.

**Acceptance Criteria**

1. **Given** I click a product, **When** the page loads, **Then** I see images, price, description and stock status.
2. **Given** the product is out of stock, **When** I view it, **Then** the Add to Cart button is disabled.

---

## US-10: Add to Cart

| Field | Value |
|---|---|
| Use Case | UC-10 |
| Priority | 🔴 High |
| Status | In Progress |

**As a** customer, **I want** to add products to my cart, **so that** I can buy several items together.

**Acceptance Criteria**

1. **Given** I am viewing an in-stock product, **When** I click Add to Cart, **Then** the item is added and cart count increases.
2. **Given** the item is already in cart, **When** I click Add to Cart, **Then** its quantity increases by one.

---

## US-11: Update Cart Quantity

| Field | Value |
|---|---|
| Use Case | UC-11 |
| Priority | 🟠 Medium |
| Status | To Do |

**As a** customer, **I want** to change item quantity in cart, **so that** I can buy the right amount.

**Acceptance Criteria**

1. **Given** my cart has items, **When** I change quantity to 3, **Then** the subtotal updates immediately.
2. **Given** I enter a quantity above stock, **When** I update, **Then** an 'Only N available' message is shown.

---

## US-12: Remove from Cart

| Field | Value |
|---|---|
| Use Case | UC-12 |
| Priority | 🟠 Medium |
| Status | To Do |

**As a** customer, **I want** to remove an item from my cart, **so that** I only buy what I want.

**Acceptance Criteria**

1. **Given** my cart has an item, **When** I click Remove, **Then** the item disappears and the total updates.

---

## US-13: Wishlist

| Field | Value |
|---|---|
| Use Case | UC-13 |
| Priority | 🟢 Low |
| Status | Backlog |

**As a** logged-in user, **I want** to save products to a wishlist, **so that** I can buy them later.

**Acceptance Criteria**

1. **Given** I am viewing a product, **When** I click the heart icon, **Then** it is saved to my wishlist.
2. **Given** an item is in my wishlist, **When** I click Move to Cart, **Then** it is moved to the cart.

---

## US-14: Apply Coupon

| Field | Value |
|---|---|
| Use Case | UC-14 |
| Priority | 🟠 Medium |
| Status | Backlog |

**As a** customer, **I want** to apply a coupon code at checkout, **so that** I get a discount.

**Acceptance Criteria**

1. **Given** I have items in cart, **When** I enter a valid coupon, **Then** the discount is applied to the total.
2. **Given** I enter an expired coupon, **When** I apply, **Then** an 'Invalid or expired coupon' message is shown.

---

## US-15: Checkout

| Field | Value |
|---|---|
| Use Case | UC-15 |
| Priority | 🔴 High |
| Status | To Do |

**As a** customer, **I want** to review my order and confirm delivery address, **so that** I can place my order.

**Acceptance Criteria**

1. **Given** my cart is not empty, **When** I click Checkout, **Then** I see order summary, address and payment options.
2. **Given** I am not logged in, **When** I click Checkout, **Then** I am asked to log in first.

---

## US-16: Make Payment

| Field | Value |
|---|---|
| Use Case | UC-16 |
| Priority | 🔴 High |
| Status | To Do |

**As a** customer, **I want** to pay by UPI, card or cash on delivery, **so that** my order is confirmed.

**Acceptance Criteria**

1. **Given** I am on the payment page, **When** I pay successfully, **Then** an order confirmation page and email are shown.
2. **Given** the payment fails, **When** the gateway returns an error, **Then** the order is not placed and I can retry.

---

## US-17: Manage Addresses

| Field | Value |
|---|---|
| Use Case | UC-17 |
| Priority | 🟠 Medium |
| Status | Backlog |

**As a** logged-in user, **I want** to add, edit and delete delivery addresses, **so that** I can ship to different places.

**Acceptance Criteria**

1. **Given** I am on Address Book, **When** I add a new address, **Then** it appears in my saved addresses.
2. **Given** I delete an address, **When** I confirm, **Then** it is removed from the list.

---

## US-18: Track Order

| Field | Value |
|---|---|
| Use Case | UC-18 |
| Priority | 🟠 Medium |
| Status | Backlog |

**As a** customer, **I want** to see the live status of my order, **so that** I know when it will arrive.

**Acceptance Criteria**

1. **Given** I have a placed order, **When** I open Track Order, **Then** I see its current status (Packed/Shipped/Delivered).

---

## US-19: Cancel Order

| Field | Value |
|---|---|
| Use Case | UC-19 |
| Priority | 🟠 Medium |
| Status | Backlog |

**As a** customer, **I want** to cancel an order before it ships, **so that** I am not charged for unwanted items.

**Acceptance Criteria**

1. **Given** an order is not yet shipped, **When** I click Cancel, **Then** its status becomes Cancelled and refund is initiated.
2. **Given** an order is already shipped, **When** I view it, **Then** the Cancel option is not available.

---

## US-20: Return and Refund

| Field | Value |
|---|---|
| Use Case | UC-20 |
| Priority | 🟢 Low |
| Status | Backlog |

**As a** customer, **I want** to return a delivered item, **so that** I get my money back for faulty goods.

**Acceptance Criteria**

1. **Given** an order was delivered within 7 days, **When** I request a return, **Then** a return request is created.
2. **Given** 7 days have passed, **When** I request a return, **Then** the request is rejected with a reason.

---

## US-21: Rate and Review

| Field | Value |
|---|---|
| Use Case | UC-21 |
| Priority | 🟢 Low |
| Status | Backlog |

**As a** customer, **I want** to rate and review purchased products, **so that** others can make informed choices.

**Acceptance Criteria**

1. **Given** I bought a product, **When** I submit 4 stars and a comment, **Then** my review appears on the product page.
2. **Given** I never bought the product, **When** I open the page, **Then** the review form is hidden.

---

## US-22: View Order History

| Field | Value |
|---|---|
| Use Case | UC-22 |
| Priority | 🟠 Medium |
| Status | Backlog |

**As a** logged-in user, **I want** to see my past orders, **so that** I can re-order or check details.

**Acceptance Criteria**

1. **Given** I have past orders, **When** I open Order History, **Then** orders are listed newest first with status and total.

---

## US-23: Admin: Manage Products

| Field | Value |
|---|---|
| Use Case | UC-23 |
| Priority | 🔴 High |
| Status | To Do |

**As a** admin, **I want** to add, edit and delete products, **so that** the catalogue stays up to date.

**Acceptance Criteria**

1. **Given** I am logged in as admin, **When** I add a product with valid data, **Then** it appears in the store.
2. **Given** I am a normal user, **When** I open the admin URL, **Then** access is denied.

---

## US-24: Admin: Manage Orders

| Field | Value |
|---|---|
| Use Case | UC-24 |
| Priority | 🔴 High |
| Status | Backlog |

**As a** admin, **I want** to view orders and update their status, **so that** customers get accurate updates.

**Acceptance Criteria**

1. **Given** an order exists, **When** I change status to Shipped, **Then** the customer sees the updated status and gets an email.

---

## US-25: Admin: Manage Users

| Field | Value |
|---|---|
| Use Case | UC-25 |
| Priority | 🟢 Low |
| Status | Backlog |

**As a** admin, **I want** to view, block or unblock users, **so that** I can prevent misuse.

**Acceptance Criteria**

1. **Given** a user is listed, **When** I click Block, **Then** that user can no longer log in.

---

