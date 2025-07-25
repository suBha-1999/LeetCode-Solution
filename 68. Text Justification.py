
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        while i < len(words):
            current_line = []
            current_length = 0
            j = i

            # Greedy line packing
            while j < len(words) and (current_length + len(words[j]) + len(current_line)) <= maxWidth:
                current_line.append(words[j])
                current_length += len(words[j])
                j += 1

            # Calculate spaces needed
            spaces_needed = maxWidth - current_length
            num_gaps = len(current_line) - 1

            # Handle last line or single word line
            if j == len(words) or num_gaps == 0:
                justified_line = " ".join(current_line)
                justified_line += " " * (maxWidth - len(justified_line))
                result.append(justified_line)
            else:
                # Distribute spaces for full lines
                base_spaces_per_gap = spaces_needed // num_gaps
                extra_spaces = spaces_needed % num_gaps

                justified_line = ""
                for k in range(len(current_line)):
                    justified_line += current_line[k]
                    if k < num_gaps:  # Add spaces if not the last word in the line
                        justified_line += " " * (base_spaces_per_gap + (1 if k < extra_spaces else 0))
                result.append(justified_line)

            i = j
        return result
    
sol = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(sol.fullJustify(words, maxWidth))