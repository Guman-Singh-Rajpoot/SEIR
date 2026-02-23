import sys
import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
def rolling_hash(word, p=53, m=2**64):
    h = 0
    power = 1
    for ch in word:
        h = (h + ord(ch) * power) % m
        power = (power * p) % m
    return h
def simhash(freq):
    bits = [0] * 64
    for word, count in freq.items():
        h = rolling_hash(word)
        for i in range(64):
            if (h >> i) & 1:
                bits[i] += count
            else:
                bits[i] -= count
    final_hash = 0
    for i in range(64):
        if bits[i] > 0:
            final_hash |= (1 << i)

    return final_hash
def get_words(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    text = soup.get_text().lower()
    words = re.findall(r'\w+', text)

    return Counter(words)
if len(sys.argv) < 3:
    print("Usage: python Project2.py <URL1> <URL2>")
    exit()

url1 = sys.argv[1]
url2 = sys.argv[2]

print("Fetching pages...")

freq1 = get_words(url1)
freq2 = get_words(url2)

hash1 = simhash(freq1)
hash2 = simhash(freq2)
diff_bits = bin(hash1 ^ hash2).count("1")
common_bits = 64 - diff_bits

print("\nSimHash URL1 =", hash1)
print("SimHash URL2 =", hash2)
print("Common bits =", common_bits, "/ 64")