import hashlib
import itertools
import string
import time
import sys
from multiprocessing import Pool, cpu_count, Manager

salt     = "10961c2d1d573b87"
target   = "11a5246bc2d9ff293735cf9962ada5bd"  
suffix   = "password"
p__refix = "itis"

TOTAL_LEN  = 13
PREFIX_LEN = TOTAL_LEN - len(suffix)
ALPHABET   = string.ascii_lowercase  

PRINT_EVERY = 1_000_000

def init_globals(s, t, suf, plen):
    global salt, target, suffix, prefix_len
    salt, target, suffix, prefix_len = s, t, suf, plen

def worker(first_letter):
    start = time.time()
    attempts = 0
    for combo in itertools.product(ALPHABET, repeat=prefix_len-1):
        attempts += 1
        prefix = first_letter + "".join(combo)
        candidate = p__refix + prefix + suffix
        h = hashlib.md5((salt + candidate).encode()).hexdigest()
        if h == target:
            return candidate, attempts, time.time() - start

        if attempts % PRINT_EVERY == 0:
            rate = attempts / (time.time() - start)
            print(f"[{first_letter}] Tried {attempts:,} @ {rate:,.0f} H/s", file=sys.stderr)
    return None, attempts, time.time() - start

def main():
    if PREFIX_LEN <= 0:
        print("Error: suffix too long.", file=sys.stderr)
        sys.exit(1)

    total_prefixes = 26 ** PREFIX_LEN
    with Pool(initializer=init_globals,
              initargs=(salt, target, suffix, PREFIX_LEN)) as pool: 
        for result in pool.imap_unordered(worker, ALPHABET):
            candidate, attempts, elapsed = result
            if candidate:
                print(f"\n[+] FOUND: {candidate}")
                print(f"    Attempts: {attempts:,} in {elapsed:.1f}s")
                pool.terminate()
                return
    print("\n[-] Exhausted all candidates without a match.")

if __name__ == "__main__":
    main()