class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

        result = []
        for i in range(len(s) - total_len + 1):
            seen_words = {}
            j = 0
            while j < len(words):
                word = s[i + j * word_len : i + (j + 1) * word_len]
                if word in word_counts:
                    seen_words[word] = seen_words.get(word, 0) + 1
                    if seen_words[word] > word_counts[word]:
                        break
                else:
                    break
                j += 1
            if j == len(words):
                result.append(i)
        return result

sol = Solution()
#s = "wordgoodgoodgoodbestword"
#words = ["word","good","best","word"]
s = "barfoothefoobarman"
words = ["foo", "bar"]
print(sol.findSubstring(s, words))