import random
import string

def generate_password(length=12):
    # Define the character pool
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example usage
password = generate_password(16)  # Generates a 16-character password
print("Generated Password:", password)
