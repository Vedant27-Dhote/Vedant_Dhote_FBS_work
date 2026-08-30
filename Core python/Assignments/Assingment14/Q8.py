def group_anagrams(strings):
    anagram_map = {}
    
    for string in strings:
        
        sorted_str = "".join(sorted(string))
        
        if sorted_str not in anagram_map:
            anagram_map[sorted_str] = []
        anagram_map[sorted_str].append(string)
        
    return list(anagram_map.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))  
