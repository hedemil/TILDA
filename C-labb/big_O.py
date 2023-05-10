import matplotlib.pyplot as plt
import numpy as np

# Define the functions for the different Big O's
def linear(n):
    return n

def quadratic(n):
    return n**2

def logarithmic(n):
    return np.log(n)

def nlogn(n):
    return n * np.log(n)

# Define the range of input values
n_values = np.arange(1, 100)
print(n_values)

# Plot the graphs
plt.plot(n_values, linear(n_values), label='O(n)')
plt.plot(n_values, quadratic(n_values), label='O(n^2)')
plt.plot(n_values, logarithmic(n_values), label='O(log n)')
plt.plot(n_values, nlogn(n_values), label='O(n log n)')

# Add axis labels and legend
plt.xlabel('Input size (n)')
plt.ylabel('Time complexity')
plt.legend()

# Show the plot
plt.show()

'''In the regular expression r'A{1000}B', the {1000} quantifier means that the letter 'A' must appear exactly 1000 times before the letter 'B' appears in the string.

If you search for this regex in a string consisting only of 'A's, such as 'A' * 1001, the regular expression engine will start by matching the first 1000 'A's with the {1000} quantifier. However, when it reaches the end of the string and does not find the 'B', it realizes that the match has failed.

Since the engine has already matched the first 1000 'A's and advanced its position in the string, it needs to backtrack to try a different match. In this case, it needs to backtrack by undoing the match for the last 'A' and try to match it with the 'B'. If that fails, it needs to backtrack again and undo the match for the second to last 'A', and so on, until it either finds a match or has backtracked all the way to the beginning of the string.

Backtracking can be a very expensive operation, especially when dealing with long strings and complex regular expressions, because the engine needs to keep track of all possible matches it has tried so far and undo them as necessary. In this case, the regex engine will need to backtrack 1000 times, each time undoing a match for a previous 'A', until it reaches the beginning of the string and concludes that there is no match for the regex.'''
