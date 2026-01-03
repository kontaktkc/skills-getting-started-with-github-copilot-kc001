"""
Test cases for prime number functionality
"""
import sys
from pathlib import Path

# Add src to path to import app
sys.path.insert(0, str(Path(__file__).parent / "src"))

from app import is_prime, get_first_n_primes


def test_is_prime():
    """Test the is_prime function"""
    # Test known primes
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert is_prime(11)
    assert is_prime(13)
    
    # Test non-primes
    assert not is_prime(0)
    assert not is_prime(1)
    assert not is_prime(4)
    assert not is_prime(6)
    assert not is_prime(8)
    assert not is_prime(9)
    assert not is_prime(10)


def test_get_first_n_primes():
    """Test getting first n prime numbers"""
    # First 5 primes
    assert get_first_n_primes(5) == [2, 3, 5, 7, 11]
    
    # First 10 primes
    assert get_first_n_primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    
    # First prime
    assert get_first_n_primes(1) == [2]


def test_sum_of_first_100_primes():
    """Test the sum of the first 100 prime numbers"""
    primes = get_first_n_primes(100)
    
    # Verify we have 100 primes
    assert len(primes) == 100
    
    # Verify first few primes
    assert primes[0] == 2
    assert primes[1] == 3
    assert primes[2] == 5
    
    # Verify the 100th prime is 541
    assert primes[99] == 541
    
    # Calculate and verify the sum
    total = sum(primes)
    
    # The sum of first 100 primes is 24133
    assert total == 24133
    
    print(f"Sum of first 100 prime numbers: {total}")


if __name__ == "__main__":
    test_is_prime()
    test_get_first_n_primes()
    test_sum_of_first_100_primes()
    print("All tests passed!")
