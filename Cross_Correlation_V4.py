import ast
import numpy as np
from itertools import combinations
from multiprocessing import Pool, cpu_count


def compute_cross_correlation(seq1, seq2):
    seq1 = np.array(seq1)
    seq2 = np.array(seq2)
    N = len(seq1)
    results = []
    for k in range(N):
        shifted_seq2 = np.roll(seq2, k)
        agreements = np.sum(seq1 == shifted_seq2)
        disagreements = N - agreements
        result = agreements - disagreements
        results.append(int(result))
    return results


# Worker for one pair
def process_pair(args):
    seq1, seq2 = args
    seq1_str = ''.join(str(x) for x in seq1)
    seq2_str = ''.join(str(x) for x in seq2)
    cc = compute_cross_correlation(seq1, seq2)
    ccr_max = max(abs(val) for val in cc)
    return (seq1_str, seq2_str), ccr_max


def compute_ccr(list_of_binary_sequence):
    # Build all unique pairs
    pairs = list(combinations(list_of_binary_sequence, 2))

    # Run in parallel
    with Pool(processes=30) as pool:
        results = pool.map(process_pair, pairs)

    # Convert results to dictionary
    ccr_results = dict(results)

    # Find max pair
    max_pair = max(ccr_results, key=ccr_results.get)
    return max_pair, ccr_results[max_pair], ccr_results


if __name__ == "__main__":
    sequences = []

    # Read sequences from file
    with open("output_data_1500.txt", "r") as f:
        for line in f:
            entry = ast.literal_eval(line.strip())
            sequences.append(entry['sequence'])

    max_pair, max_val, ccr_dict = compute_ccr(sequences)

    print("Max CCR value:", max_val)
    for pair, val in ccr_dict.items():
        print(pair, val)
