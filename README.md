Here is the complete project documentation in English, structured and formatted for a GitHub `README.md` or technical guide:

---

# Password Strength Checker - Project Documentation

## 📌 Project Overview

This interactive Python script evaluates the strength and security of a user-provided password based on standard cybersecurity practices. It tests the password against **5 core security parameters**.

Unlike basic password checkers that only highlight missing requirements, this tool provides complete feedback showing the status (**✅ / ❌**) of **all rules** at once. This gives users full clarity on what conditions were met and what needs improvement.

---

## ⚙️ How It Works

The script evaluates the password using Python's built-in **Regular Expressions (Regex)** and conditional statements.

### 1. Security Criteria & Scoring System

The password is awarded a score out of **5 points** based on the following rules:

| Criterion (Rule) | Condition | Python Logic / Regex | Points |
| --- | --- | --- | --- |
| **1. Length Check** | Minimum 8 characters long | `len(password) >= 8` | +1 |
| **2. Uppercase Letter** | At least one capital letter (A-Z) | `re.search(r"[A-Z]", password)` | +1 |
| **3. Lowercase Letter** | At least one small letter (a-z) | `re.search(r"[a-z]", password)` | +1 |
| **4. Digit / Number** | At least one number (0-9) | `re.search(r"\d", password)` | +1 |
| **5. Special Character** | At least one symbol (`@`, `$`, `!`, `%`, `*`, `?`, `&`, `#`, `^`, `_`, `-`) | `re.search(r"[@$!%*?&#^_-]", password)` | +1 |

### 2. Password Strength Ratings

The total score determines the final strength rating:

* **5 Points:** Very Strong 🟢 *(All security criteria met)*
* **4 Points:** Strong 🔵 *(Good security, missing 1 requirement)*
* **3 Points:** Medium 🟡 *(Average security, missing 2 requirements)*
* **0 to 2 Points:** Weak 🔴 *(Insecure, vulnerable to attacks)*

---

## 🔍 Code Breakdown

```python
import re  # 're' is Python's built-in Regular Expression library for pattern matching.

def check_password_strength(password):
    score = 0
    all_rules_feedback = []

    # 1. Length Check
    # Checks if the character count is 8 or more.
    if len(password) >= 8:
        score += 1
        all_rules_feedback.append("✅ Must be at least 8 characters long.")
    else:
        all_rules_feedback.append("❌ Must be at least 8 characters long.")

    # 2. Uppercase Letter Check
    # Searches for at least one capital letter from A to Z.
    if re.search(r"[A-Z]", password):
        score += 1
        all_rules_feedback.append("✅ Must contain at least one uppercase letter (A-Z).")
    else:
        all_rules_feedback.append("❌ Must contain at least one uppercase letter (A-Z).")

    # 3. Lowercase Letter Check
    # Searches for at least one small letter from a to z.
    if re.search(r"[a-z]", password):
        score += 1
        all_rules_feedback.append("✅ Must contain at least one lowercase letter (a-z).")
    else:
        all_rules_feedback.append("❌ Must contain at least one lowercase letter (a-z).")

    # 4. Number Check (\d)
    # '\d' matches any digit from 0 to 9.
    if re.search(r"\d", password):
        score += 1
        all_rules_feedback.append("✅ Must contain at least one number (0-9).")
    else:
        all_rules_feedback.append("❌ Must contain at least one number (0-9).")

    # 5. Special Character Check
    # Checks for defined special symbols within the brackets.
    if re.search(r"[@$!%*?&#^_-]", password):
        score += 1
        all_rules_feedback.append("✅ Must contain at least one special character (e.g., @, $, !, %, *, ?).")
    else:
        all_rules_feedback.append("❌ Must contain at least one special character (e.g., @, $, !, %, *, ?).")

    # Final Strength Calculation
    if score == 5:
        strength = "Very Strong 🟢"
    elif score == 4:
        strength = "Strong 🔵"
    elif score == 3:
        strength = "Medium 🟡"
    else:
        strength = "Weak 🔴"

    return strength, score, all_rules_feedback

```

---

## 💻 Example Output

**User Input:** `Rajkumar123`

**Evaluation:**

1. **Length:** 11 characters `>= 8` 👉 **Passed ✅**
2. **Uppercase:** 'R' present 👉 **Passed ✅**
3. **Lowercase:** 'ajkumar' present 👉 **Passed ✅**
4. **Digit:** '123' present 👉 **Passed ✅**
5. **Special Character:** Missing 👉 **Failed ❌**

**Terminal Output:**

```text
--- Password Strength Checker ---
Enter your password: Rajkumar123

Password Strength: Strong 🔵

Keep these points in mind to make your password strong:
✅ Must be at least 8 characters long.
✅ Must contain at least one uppercase letter (A-Z).
✅ Must contain at least one lowercase letter (a-z).
✅ Must contain at least one number (0-9).
❌ Must contain at least one special character (e.g., @, $, !, %, *, ?).

```

---

🛠️ Installation & Usage Guide
Prerequisites
Make sure you have Python 3.x installed on your system. You can verify this by running:

```Bash
python --version
```
1. Download or Clone the Repository
Using Git:

```Bash
git clone [https://github.com/HackerRank7/password-checker.git](https://github.com/HackerRank7/password-checker.git)
cd password-checker
```

2. Run the Script
Navigate to the project directory in your terminal or command prompt and execute:

```Bash
python password_checker.py
```
(On macOS/Linux, use python3 password_checker.py if needed)

🚀 Key Advantages
User-Centric Feedback: Shows what rules you satisfied alongside what needs fixing.

Lightweight & Fast: Executes instantly with zero external package dependencies.

Clean & Modular Code: Easy to read, maintain, or integrate into web apps (Flask/Django).

## 👤 Author
Gaurav Bharty


## 📜 License
This project is open-source and available under the MIT License.
