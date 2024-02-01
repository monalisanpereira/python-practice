import requests
import sys

def read_word_list(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

def fuzz(word_list, target_URL):
    for word in word_list:
        res = requests.get(url=target_URL.replace("FUZZ", word))
        if res.status_code != 404:
            print(f"{word} {res.status_code}")

def main():
    if len(sys.argv) != 3 or "FUZZ" not in sys.argv[2]:
        print("Usage: python3 apifuzzer.py <wordlist_file> <target_URL/FUZZ>")
        sys.exit(1)

    file_path = sys.argv[1]
    target_URL = sys.argv[2]

    print(f"Running fuzzer on {target_URL.replace('FUZZ', '')}")

    word_list = read_word_list(file_path)

    fuzz(word_list, target_URL)

if __name__ == "__main__":
    main()