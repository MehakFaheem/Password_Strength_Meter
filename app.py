# password_strength_meter.py

import streamlit as st
import re
import random
import string

# Constants
COMMON_PASSWORDS = ["password", "123456", "12345678", "qwerty", "abc123", "password1"]

# Functions
def is_common_password(password):
    return password.lower() in COMMON_PASSWORDS

def generate_strong_password():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*"
    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    all_chars = lowercase + uppercase + digits + special_chars
    password += random.choices(all_chars, k=4)  # Adjust length as needed
    
    random.shuffle(password)
    return ''.join(password)

def check_password_strength(password):
    if is_common_password(password):
        return "❌ This password is too common and weak. Please choose a different one."
    
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 2
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    if score >= 4:
        feedback.append("✅ Strong Password!")
    elif score == 3:
        feedback.append("⚠️ Moderate Password - Consider adding more security features.")
    else:
        feedback.append("❌ Weak Password - Improve it using the suggestions above.")
    
    return "\n".join(feedback)

# Streamlit App
def main():
    st.title("Password Strength Meter 🔐")
    
    choice = st.radio("Choose an option:", ("Check Password Strength", "Generate Strong Password"))
    
    if choice == "Check Password Strength":
        password = st.text_input("Enter your password:", type="password")
        if password:
            result = check_password_strength(password)
            st.write(result)
    else:
        if st.button("Generate Strong Password"):
            strong_password = generate_strong_password()
            st.write(f"Here's a strong password suggestion: **{strong_password}**")

# Run the app
if __name__ == "__main__":
    main()