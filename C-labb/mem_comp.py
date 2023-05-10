import timeit
import tracemalloc
import numpy as np
import matplotlib.pyplot as plt
import re


def sequence_DNA(n):
    k = (n - 3) // 4 # Compute the number of repetitions needed for the sequence
    sequence = 'ATCG' * k + 'AAA' + 'ATCG' * k # Construct the sequence
    remaining_chars = n - len(sequence) # Compute the number of remaining characters needed
    if remaining_chars > 0:
        sequence += 'ATCG'[:remaining_chars] # Add additional characters if needed
    # sequence = "A"*n #Worst case scenario for regex
    return sequence

def kmp_search(pat, txt):
    """Knuth-Morris-Pratt string search algorithm."""
    m, n = len(pat), len(txt)
    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pat[j] != pat[i]:
            j = lps[j-1]
        if pat[j] == pat[i]:
            j += 1
        lps[i] = j
    j = 0
    matches = []
    for i in range(n):
        while j > 0 and pat[j] != txt[i]:
            j = lps[j-1]
        if pat[j] == txt[i]:
            j += 1
        if j == m:
            matches.append(i - m + 1)
            j = lps[j-1]
    return matches


def regex(pat, txt):
    """Regex pattern matching."""
    # pattern = re.compile(pat)
    # match = pattern.findall(txt)
    match = re.findall(pat, txt) #Worst case for regex
    return match


def main():
    i = 10**5
    sequence_n = []
    while i < 10**6 + 1:
        sequence_n.append(i)
        i += 10**5
    
    kmptimes = []
    regextimes = []
    
    # reg_pattern = r'A{1000}B' # Use a regex that matches a large number of repeating characters
    # pattern = "A"*1000+"B" # Worst case for regex
    pattern = "AAA" # Normal case

    for n in sequence_n:
        # Construct the DNA sequence of length n
        sequence = sequence_DNA(n)
        
        # Run KMP search and measure memory usage
        tracemalloc.start()
        kmp_matches = kmp_search(pattern, sequence)
        kmp_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        kmptimes.append((n, kmp_memory))
        
        # Run Regex search and measure memory usage
        tracemalloc.start()
        regex_matches = regex(pattern, sequence)
        regex_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        regextimes.append((n, regex_memory))
        

    # Print the results
    print("KMP memory usage:")
    for n, mem in kmptimes:
        print(f"n = {n}: {mem} bytes")
        
    print("\nRegex memory usage:")
    for n, mem in regextimes:
        print(f"n = {n}: {mem} bytes")
main()