#!/usr/bin/env python
# sliding_window.py
# Initialize variables
dna_string = 'atgcaaaatttttggggccccatgcatgcgcgta'
start = 0
window_size = 20

# Get the length of dna_string
end = len(dna_string) - window_size + 1

# Slide along dna string from beginning to end
for position in range(start,end):
    # Get the substring from the start position to the end of the window
    print dna_string[position:position+window_size]
