# Last updated: 13.08.2025, 17:01:04
from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_length = word_len * len(words)
        word_count = Counter(words)
        result = []

        # Slide the window in each possible alignment starting from 0 to word_len - 1
        for i in range(word_len):
            left = i
            current_count = Counter()
            
            # Move the right pointer in steps of word_len
            for right in range(i, len(s) - word_len + 1, word_len):
                # Get the current word
                word = s[right:right + word_len]
                
                if word in word_count:
                    current_count[word] += 1
                    
                    # If there's an excess of this word, slide the left pointer to adjust
                    while current_count[word] > word_count[word]:
                        current_count[s[left:left + word_len]] -= 1
                        left += word_len
                    
                    # Check if the window is valid
                    if (right - left + word_len) == total_length:
                        result.append(left)
                else:
                    # Reset counters if word not in words
                    current_count.clear()
                    left = right + word_len

        return result
