def validate_password(password):
    validate = True
    if len(password) < 8:
        return not validate
    if not any(char.isupper() for char in password):
        return not validate
    if not any(char.islower() for char in password):
        return not validate
    if not any(char.isdigit() for char in password):
        return not validate
    if any(char.isspace() for char in password):
        return not validate

    if not validate:
        return False
    else:
        return True
    
print:validate_password("Password123")
print:validate_password("abc123")
print:validate_password("Password 123")
print:validate_password("password123")
