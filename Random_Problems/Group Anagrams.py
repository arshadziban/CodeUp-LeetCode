from collections import defaultdict

def group_anagrams(strs):
    anagram_dict = defaultdict(list)
    
    for s in strs:
        
        key = tuple(sorted(s))
        anagram_dict[key].append(s)
    
    return list(anagram_dict.values())


input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(input_strs))