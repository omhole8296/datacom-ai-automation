# 🐞 Debug Log – AI Assisted Development

## Step 1: Understanding Code

Prompt:
Explain the structure and functionality of this script.

Observation:
The script processes customer and transaction data, generates reports, and exports results.

---

## Step 2: Bug Diagnosis

Prompt:
Given the error log, identify the issue.

Finding:
Error: 'dict' object has no attribute 'keys'

Cause:
Improper handling of dictionary keys while exporting CSV data.

---

## Step 3: Writing Test Case

Created unit tests to validate export functionality.

Result:
Initial tests helped identify failure in CSV export.

---

## Step 4: Fix & Refactor

- Improved export_customer_data() for safer handling
- Simplified dictionary operations
- Optimized find_matches() function

---

## Step 5: Verification

- All test cases passed
- Script executed successfully

---

## Final Learning

- Importance of testing before fixing
- How to use AI for debugging
- Writing cleaner and efficient Python code