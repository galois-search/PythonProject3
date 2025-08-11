def legendre_symbol(a, p):
    """Compute the Legendre symbol (a/p)."""
    a = a % p
    if a == 0:
        return 0
    ls = pow(a, (p - 1) // 2, p)
    if ls == 1:
        return 1
    elif ls == p - 1:
        return -1
    else:
        return 0  # Shouldn't occur for primes

def legendre_binary_sequence(p):
    """
    Generate Legendre binary sequence of length p (p must be an odd prime).
    Returns a list of 0s and 1s.
    """
    seq = []
    for i in range(p):
        symbol = legendre_symbol(i, p)
        if symbol == 1:
            seq.append(1)
        else:
            seq.append(0)  # 0 for non-residue and zero
    return seq

if __name__ == "__main__":
    seq_1489 = legendre_binary_sequence(727)
    seq_11 = legendre_binary_sequence(773)
    print("Legendre binary sequence of 1489 bits:\n", seq_1489)
    print("\nLegendre binary sequence of 11 bits:\n", seq_11)
