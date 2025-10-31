from collections import Counter, defaultdict

def map_by_frequency(s1, s2):
    freq1 = Counter(s1)
    freq2 = Counter(s2)

    group1 = defaultdict(list)
    for char, count in freq1.items():
        group1[count].append(char)

    group2 = defaultdict(list)
    for char, count in freq2.items():
        group2[count].append(char)

    if sorted(group1.keys()) != sorted(group2.keys()):
        return "Невозможно сопоставить: разные частоты"

    result = []
    for count in sorted(group1.keys()):
        chars1 = sorted(group1[count])
        chars2 = sorted(group2[count])
        if len(chars1) != len(chars2):
            return "Невозможно сопоставить: разное количество символов на одну частоту"
        for c1, c2 in zip(chars1, chars2):
            result.append(f"{c1}={c2}")
    return ' '.join(result)

s1 = "abcbaa"
s2 = "jkekjj"
print(map_by_frequency(s1, s2))
