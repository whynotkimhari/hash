import sys
def main():
    data = sys.argv[1]
    m = int(input("Input the size of data: "))
    m_a = m + 1000000007
    while is_prime(m_a) == False:
        m_a += 1
    hashes_list = []
    hashes_set = set()
    with open(data) as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            else:
                value = hash(line, m_a)
                hashes_list.append(value)
                hashes_set.add(value)
    dup = len(hashes_list) - len(hashes_set)
    print(f"There are {dup} duplicates after hashing process")
def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True
def hash(s, mod):
    base = 2
    hash_ = 0
    for i in range(len(s)):
        hash_ = hash_ * base + ord(s[i])
    return hash_%mod
if __name__ == "__main__":
   main()

   