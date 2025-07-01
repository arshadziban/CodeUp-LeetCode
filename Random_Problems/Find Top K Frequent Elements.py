from collections import Counter

def top_k_frequent(nums, k):
   
    count = Counter(nums)
    
   
    most_common = count.most_common(k)
    
    
    return [num for num, freq in most_common]


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_frequent(nums, k)) 
