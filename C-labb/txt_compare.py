import timeit
import matplotlib.pyplot as plt
import re


def sequence_DNA(n):
    # Normala fallet
    k = (n - 3) // 4 # Compute the number of repetitions needed for the sequence
    sequence = 'AADAM' * k + 'AAA' + 'ATCG' * k # Construct the sequence
    remaining_chars = n - len(sequence) # Compute the number of remaining characters needed
    if remaining_chars > 0:
        sequence += 'ATCG'[:remaining_chars] # Add additional characters if needed
    # sequence = "A"*n # Värsta fallet
    return sequence

def kmp_search(pat, txt):
    """Knuth-Morris-Pratt string search algorithm."""
    m, n = len(pat), len(txt)
    lps = [0] * m # next vektor
    j = 0
    for i in range(1, m): # O(m) iterates over pattern
        while j > 0 and pat[j] != pat[i]:
            j = lps[j-1]
        if pat[j] == pat[i]:
            j += 1
        lps[i] = j
    j = 0
    
    for i in range(n): # O(n) iterates over text
        while j > 0 and pat[j] != txt[i]:
            j = lps[j-1] # sets j to next vector for that index 
        if pat[j] == txt[i]:
            j += 1 
        if j == m:
            return i - m + 1  # Return the first occurrence of the pattern
    return -1  # Pattern not found

def regex(pat, txt):
    """Regex pattern matching."""
    pattern = re.compile(pat)
    match = pattern.search(txt) #finds first occurence.
    if match:
        return match.group() #returns the string
    else:
        return -1  # Pattern not found

def main():
    # Normala fallet
    i = 10**5
    sequence_n = []
    while i < 10**6 + 1:
        sequence_n.append(i)
        i += 2*10**5

    # Värsta fallet
    # i = 10
    # sequence_n = []
    # while i < 21:
    #     sequence_n.append(i)
    #     i += 2

    kmptimes = []
    regextimes = []
    
    #reg_pattern = r'(A|A)*B' # Värsta fallet
    pattern = "AAA" # Normal fallet
    reg_pattern = "AAA" # Normala fallet

    for i in sequence_n:
        dna_seq = sequence_DNA(i)
        kmp_time = timeit.timeit(stmt=lambda: kmp_search(pattern, dna_seq), number=10)
        regex_time = timeit.timeit(stmt=lambda: regex(reg_pattern, dna_seq), number=10)
        kmptimes.append(kmp_time/10)
        regextimes.append(regex_time/10)
    

    plt.plot(sequence_n, kmptimes, label='KMP')
    plt.scatter(sequence_n, kmptimes, marker='o', color='blue', label='KMP')
    plt.plot(sequence_n, regextimes, color='red', label='REGEX')
    plt.scatter(sequence_n, regextimes, marker='o', color='red', label='REGEX')
    

    plt.xlabel('Text Length (n)')
    plt.ylabel('Time (s)')
    plt.title('Algorithm Comparison')

    plt.legend()
    plt.show()

    print("KMP tid: ")  
    print(kmptimes)
    print("REGEX tid: ")
    print(regextimes) 
    print("SEQUENCE: ")
    print(sequence_n)

main()