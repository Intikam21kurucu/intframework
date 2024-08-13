import itertools
import string
import hashlib

def hash_password(password, hash_algorithm='sha256'):
    """Verilen şifreyi belirtilen hash algoritması ile hash'ler."""
    hash_obj = hashlib.new(hash_algorithm)
    hash_obj.update(password.encode('utf-8'))
    return hash_obj.hexdigest()

def brute_force_attack(target_hash, hash_algorithm='sha256', max_length=4):
    """Hash'lenen şifreyi kırmak için brute force saldırısı yapar."""
    chars = string.ascii_letters + string.digits + string.punctuation
    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            guess_str = ''.join(guess)
            if hash_password(guess_str, hash_algorithm) == target_hash:
                return guess_str
    return None