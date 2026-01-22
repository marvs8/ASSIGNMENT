import hashlib
from Crypto.Hash import keccak  # Requires: pip install pycryptodome


def sha256_hash(data):
    """Computes SHA-256 hash (Bitcoin style often uses double-SHA256)."""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()


def keccak256_hash(data):
    """Computes Keccak-256 hash (common in Ethereum)."""
    k = keccak.new(digest_bits=256)
    k.update(data.encode('utf-8'))
    return k.hexdigest()


def get_merkle_root(hashes, hash_func):
    # Base case: only one hash remains
    if len(hashes) == 1:
        return hashes[0]

    # Handle odd number of hashes by duplicating the last one
    if len(hashes) % 2 != 0:
        hashes.append(hashes[-1])

    next_level = []
    for i in range(0, len(hashes), 2):
        # Concatenate and hash the pair
        combined = hashes[i] + hashes[i + 1]
        next_level.append(hash_func(combined))

    return get_merkle_root(next_level, hash_func)


# Example Usage
transactions = ["tx1", "tx2", "tx3", "tx4", "tx5"]
# 1. Initial Leaf Hashing
sha_leaves = [sha256_hash(tx) for tx in transactions]
keccak_leaves = [keccak256_hash(tx) for tx in transactions]

# 2. Compute Roots
sha_root = get_merkle_root(sha_leaves, sha256_hash)
keccak_root = get_merkle_root(keccak_leaves, keccak256_hash)
