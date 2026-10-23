# Detailed Use Cases: Registration and Login

## UC-01: User Registration

| Field | Description |
|---|---|
| Use Case ID | UC-01 |
| Name | User Registration |
| Actor | New Visitor |
| Description | A visitor creates an account in the system |
| Preconditions | User is not logged in and has internet access |
| Postconditions | Account is created; confirmation email is sent |
| Trigger | Visitor clicks "Sign Up" |

**Main Flow**
1. Visitor opens the registration page.
2. Visitor enters name, email, phone and password.
3. System validates the input.
4. System checks that the email is not already registered.
5. System creates the account and stores the password hashed.
6. System sends a confirmation email.
7. System displays "Registration successful" and redirects to Login.

**Alternate Flows**
- 3a. Invalid input: system highlights the fields and shows errors.
- 4a. Email exists: system shows "Email already registered".

**Exceptions**
- Server or database down: system shows "Try again later".

## UC-02: User Login

| Field | Description |
|---|---|
| Use Case ID | UC-02 |
| Name | User Login |
| Actor | Registered User |
| Description | User authenticates to access their account |
| Preconditions | User has a registered account |
| Postconditions | User session is created |
| Trigger | User clicks "Login" |

**Main Flow**
1. User opens the login page.
2. User enters email and password.
3. System verifies the credentials.
4. System creates a session.
5. System redirects the user to the dashboard.

**Alternate Flows**
- 3a. Wrong credentials: system shows "Invalid credentials".
- 3b. 5 failed attempts: account locked for 15 minutes.
- 2a. User clicks "Forgot Password": goes to UC-04.

**Exceptions**
- Server down: system shows an error message.

> The full list of 25 use cases is in [04a-use-case-list.md](04a-use-case-list.md).
