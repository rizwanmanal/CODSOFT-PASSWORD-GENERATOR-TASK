length=int(input("ENTER THE LENGTH OF YOUR PASSWORD YOU WANT TO ENTER: "))
import string
import random

# Define The Characters That Can Be Used In The Password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate Random Password
random_password = ''.join(random.choice(characters) for i in range(length))

# Display  The Random Password
print("Random Password by using given length is :", random_password)