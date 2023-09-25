"""
Spectral Convolution Problem: Compute the convolution of a spectrum.

    Input: A collection of integers Spectrum in increasing order..
    Output: The list of elements in the convolution of Spectrum.
    If an element has multiplicity k, it should appear exactly k times; you may return the elements in any order.

Code Challenge: Solve the Spectral Convolution Problem.  (Note: the convolution should not contain any zeroes.)

Sample Input:
0 137 186 323

Sample Output:
137 137 186 186 323 49
"""

def read_spectrum(file_name):
    with open(file_name, 'r') as file:
        spectrum = [int(mass) for mass in file.read().split()]
    return spectrum

def spectral_convolution(spectrum):
    conv = []
    sorted_spectrum = sorted(spectrum)
    for i in range(len(sorted_spectrum)):
        for j in range(i + 1, len(sorted_spectrum)):
            diff = sorted_spectrum[j] - sorted_spectrum[i]
            if diff != 0:
                conv.append(diff)
    return conv

# Read input from file
spectrum = read_spectrum('dataset_104_4.txt')

# Calculate the spectral convolution
convolution = spectral_convolution(spectrum)

# Sort the convolution
sorted_convolution = sorted(convolution)

# Print the result
for element in sorted_convolution:
    print(element, end=" ")