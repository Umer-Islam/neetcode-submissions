class Solution:
    def groupAnagrams(self, strs):
        words = {} 
        for word in strs:
            key = "".join(sorted(word))
            if key not in words:
                words[key] = []
            words[key].append(word)
        # print(list(words.values()))
        return list(words.values())