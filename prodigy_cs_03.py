import re

def assess_password_strength(password):
    strength_criteria = {
        'length': len(password) >= 8,
        'uppercase': re.search(r'[A-Z]', password) is not None,
        'lowercase': re.search(r'[a-z]', password) is not None,
        'digits': re.search(r'\d', password) is not None,
        'special_characters': re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    }

    strength_score = sum(strength_criteria.values())
    
    if strength_score == 5:
        strength = 'Very Strong'
    elif strength_score == 4:
        strength = 'Strong'
    elif strength_score == 3:
        strength = 'Moderate'
    elif strength_score == 2:
        strength = 'Weak'
    else:
        strength = 'Very Weak'
    
    feedback = []
    if not strength_criteria['length']:
        feedback.append('Password should be at least 8 characters long.')
    if not strength_criteria['uppercase']:
        feedback.append('Password should include at least one uppercase letter.')
    if not strength_criteria['lowercase']:
        feedback.append('Password should include at least one lowercase letter.')
    if not strength_criteria['digits']:
        feedback.append('Password should include at least one digit.')
    if not strength_criteria['special_characters']:
        feedback.append('Password should include at least one special character (e.g., !@#$%^&*()).')

    return strength, feedback

def main():
    password = input("Enter a password to assess: ")
    strength, feedback = assess_password_strength(password)
    
    print(f"Password Strength: {strength}")
    if feedback:
        print("\nFeedback:")
        for item in feedback:
            print(f"- {item}")

if __name__ == "__main__":
    main()
