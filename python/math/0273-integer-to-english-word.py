
# Convert a non-negative integer num to its English words representation.


def numberToWords(num: int) -> str:
    if num == 0:
        return "Zero"

    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]

    def chunk_to_words(chunk):
        parts = []
        if chunk >= 100:
            parts.append(ones[chunk // 100] + " Hundred")
            chunk %= 100
        if chunk >= 20:
            parts.append(tens[chunk // 10])
            chunk %= 10
        if chunk > 0:
            parts.append(ones[chunk])
        return " ".join(parts)

    result = []
    group_ind = 0
    while num > 0:
        chunk = num % 1000
        if chunk:
            result.insert(0, chunk_to_words(chunk) + (f" {thousands[group_ind]}" if thousands[group_ind] else ""))
        num //= 1000
        group_ind += 1

    return " ".join(result).strip()


print(numberToWords(123))
print(numberToWords(12345))
print(numberToWords(1234567))