def unique_char_count(s: str) -> int:
    unique_chars = set(map(lambda x: x.lower(), s))
    return len(unique_chars)

print(unique_char_count("Hello"))  
print(unique_char_count("World"))  