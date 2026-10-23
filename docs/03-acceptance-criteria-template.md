# Acceptance Criteria Template

## Format 1: Given / When / Then (Gherkin style)

```
Scenario: <name>
  Given <precondition>
  And   <another precondition>
  When  <user action>
  Then  <expected result>
  And   <another expected result>
```

## Format 2: Checklist

```
- [ ] The system must ...
- [ ] The user can ...
- [ ] Error message is shown when ...
```

## Table Template

| AC ID | Given | When | Then | Pass/Fail |
|-------|-------|------|------|-----------|
| AC-01 |       |      |      |           |
| AC-02 |       |      |      |           |

## Example (Login)

| AC ID | Given | When | Then | Pass/Fail |
|-------|-------|------|------|-----------|
| AC-01 | I have a valid account | I enter correct email and password | I am redirected to the dashboard | ✔ |
| AC-02 | I have a valid account | I enter a wrong password | "Invalid credentials" is shown | ✔ |
| AC-03 | I failed login 5 times | I try again | Account is locked for 15 minutes | ✔ |
