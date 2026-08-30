def longest_common_prefix(strings):
    if not strings:
        return ""
        
    prefix = strings[0]
    
    for string in strings[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

words = ["flower", "flow", "flight"]
print(longest_common_prefix(words))  
