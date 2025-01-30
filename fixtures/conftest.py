# fixtures/conftest.py

import pytest
from fixtures.random_email_generator import random_email  # Correct import path

@pytest.fixture
def generate_random_email():
    """Fixture to generate a unique random email for each test"""
    return random_email()

