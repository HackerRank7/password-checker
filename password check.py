import re

def check_password_strength(password):
    score = 0
    all_rules_feedback = []

    # 1. Length check
    if len(password) >= 8:
        score += 1
        all_rules_feedback.append("✅ Must be at least 8 characters long.")
    else:
        all_rules_feedback.append("❌ Must be at least 8 characters long.")

    # 2. Uppercase letter check
    if re.search(r"[A-Z]", password):
        score += 1
        all_rules_feedback.append("✅ Must contain at least one uppercase letter (A-Z).")
    else:
        all_rules_feedback.append("❌ Must contain at least one uppercase letter (A-Z).")

    # 3. Lowercase letter check
    if re.search(r"[a-z]", password):
        score += 1
        all_rules_feedback.append("✅ Must contain at least one lowercase letter (a-z).")
    else:
        all_rules_feedback.append("❌ Must contain at least one lowercase letter (a-z).")

    # 4. Number check
    if re.search(r"\d", password):
        score += 1
        all_rules_feedback.append("✅ Must contain at least one number (0-9).")
    else:
        all_rules_feedback.append("❌ Must contain at least one number (0-9).")

    # 5. Special character check
    if re.search(r"[@$!%*?&#^_-]", password):
        score += 1
        all_rules_feedback.append("✅ Must contain at least one special character (e.g., @, $, !, %, *, ?).")
    else:
        all_rules_feedback.append("❌ Must contain at least one special character (e.g., @, $, !, %, *, ?).")

    # Strength decide karna
    if score == 5:
        strength = "Very Strong 🟢"
    elif score == 4:
        strength = "Strong 🔵"
    elif score == 3:
        strength = "Medium 🟡"
    else:
        strength = "Weak 🔴"

    return strength, score, all_rules_feedback

if __name__ == "__main__":
    print("--- Password Strength Checker ---")
    user_password = input("Enter your password: ")
    
    strength, score, feedback_list = check_password_strength(user_password)
    
    print(f"\nPassword Strength: {strength}")
    
    if score < 5:
        print("\nKeep these points in mind to make your password strong:")
        for rule in feedback_list:
            print(rule)
    else:
        print("\n✅ Excellent! Your password is very secure.")