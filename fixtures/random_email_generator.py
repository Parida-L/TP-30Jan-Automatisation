import random  # Importing the random module to generate random choices
import string  # Importing string module to use lowercase letters and digits

def random_email():
    """
    Generate a random email address with a random domain.
    
    Criteria:
    - The username consists of 10 random lowercase letters and digits.
    - The domain is randomly selected from a predefined list of domains.
    - The email format is: username@domain
    """

    # List of possible domains
    domains = ["test.com", "qa.com", "example.org", "automation.io"]

    # Generate a random username (10 characters long) using lowercase letters and digits
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

    # Select a random domain from the list
    domain = random.choice(domains)

    # Construct the final email address
    return f"{username}@{domain}"

# Generate and print a random email
print(random_email())  # Example output: s9dhd2k4l3@automation.io
