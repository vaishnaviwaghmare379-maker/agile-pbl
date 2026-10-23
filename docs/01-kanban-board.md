# Kanban Board

## Columns

| Column | Meaning | WIP Limit |
|---|---|---|
| ⚪ Backlog | All stories not yet planned | – |
| 🔵 To Do | Planned for the current sprint | – |
| 🟡 In Progress | Being developed | 3 |
| 🟣 In Review | Under testing / code review | 2 |
| 🟢 Done | Meets Definition of Done | – |

## Color Coding

**Priority**

| Color | Priority |
|---|---|
| 🔴 | High |
| 🟠 | Medium |
| 🟢 | Low |

**Card Type**

| Color | Type |
|---|---|
| 🟦 | Feature (user story) |
| 🟪 | Bug |
| 🟨 | Task / Chore |

**Definition of Done:** code complete, acceptance criteria passed, reviewed, merged to `main`.

## Board View

| ⚪ Backlog | 🔵 To Do | 🟡 In Progress | 🟣 In Review | 🟢 Done |
|---|---|---|---|---|
| 🟢 🟦 **US-13** Wishlist | 🟢 🟦 **US-05** Update Profile | 🟠 🟦 **US-08** Filter and Sort Products | 🔴 🟦 **US-04** Reset Password | 🔴 🟦 **US-01** User Registration |
| 🟠 🟦 **US-14** Apply Coupon | 🟠 🟦 **US-11** Update Cart Quantity | 🔴 🟦 **US-10** Add to Cart | 🔴 🟦 **US-07** Search Products | 🔴 🟦 **US-02** User Login |
| 🟠 🟦 **US-17** Manage Addresses | 🟠 🟦 **US-12** Remove from Cart |   |   | 🟠 🟦 **US-03** User Logout |
| 🟠 🟦 **US-18** Track Order | 🔴 🟦 **US-15** Checkout |   |   | 🔴 🟦 **US-06** Browse Products |
| 🟠 🟦 **US-19** Cancel Order | 🔴 🟦 **US-16** Make Payment |   |   | 🔴 🟦 **US-09** View Product Details |
| 🟢 🟦 **US-20** Return and Refund | 🔴 🟦 **US-23** Admin: Manage Products |   |   |   |
| 🟢 🟦 **US-21** Rate and Review |   |   |   |   |
| 🟠 🟦 **US-22** View Order History |   |   |   |   |
| 🔴 🟦 **US-24** Admin: Manage Orders |   |   |   |   |
| 🟢 🟦 **US-25** Admin: Manage Users |   |   |   |   |

## Card Template

```
[Priority color][Type color] US-XX  Title
Assignee: <name>
Story Points: <1,2,3,5,8>
Linked Use Case: UC-XX
Acceptance Criteria: ✔ / ✘
```
