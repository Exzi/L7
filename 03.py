from collections import Counter

def can_be_poly(s: str) -> bool:
    char_counts = Counter(s)
    odd_count = sum(1 for count in char_counts.values() if count % 2 != 0)
    return odd_count <= 1

print(can_be_poly("abcba"))  
print(can_be_poly("abbbc"))  