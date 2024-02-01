import base64
import argparse

def encrypt(string_to_encrypt):
    return base64.b64encode(string_to_encrypt.encode()).decode('utf-8')

def decrypt(string_to_decrypt):
    return base64.b64decode(string_to_decrypt.encode()).decode('utf-8')

def main():
    parser = argparse.ArgumentParser(description='Encrypts or decrypts a given string.')
    parser.add_argument('-d', '--decrypt', type=str, help='Decrypt the string provided')
    parser.add_argument('-e', '--encrypt', type=str, help='Encrypt the string provided')
    args = parser.parse_args()

    if (args.decrypt and args.encrypt) or not (args.decrypt or args.encrypt):
        parser.error("Please provide either --decrypt or --encrypt option.")

    if args.decrypt:
        print(f"Your decrypted string is {decrypt(args.decrypt)}")
    else:
        print(f"Your encrypted string is {encrypt(args.encrypt)}")

if __name__ == "__main__":
    main()