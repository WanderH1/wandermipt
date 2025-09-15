def main():
    s = input().strip()
    mirror_map = {
        'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', '1': '1', '8': '8', 'E': '3', '3': 'E', 'J': 'L', 'L': 'J', 'S': '2', '2': 'S', 'Z': '5', '5': 'Z'
    }

    is_palindrome = s == s[::-1]

    is_mirrored = True
    n = len(s)
    for i in range((n + 1) // 2):
        if s[i] not in mirror_map:
            is_mirrored = False
            break
        if mirror_map[s[i]] != s[n - 1 - i]:
            is_mirrored = False
            break

    if is_palindrome and is_mirrored:
        print(f"{s} is a mirrored palindrome.")
    elif is_palindrome:
        print(f"{s} is a regular palindrome.")
    elif is_mirrored:
        print(f"{s} is a mirrored string.")
    else:
        print(f"{s} is not a palindrome.")


if __name__ == "__main__":
    main()