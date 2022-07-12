import os
from tkinter import Tk, filedialog
from cryptography.fernet import Fernet
import atexit

root = Tk()
root.withdraw()
root.attributes('-topmost', True)
key = bytes(open("key.txt", 'r').read(), 'utf-8')
f = Fernet(key)

main_form = """
    Select an action:
        [1] Crypt path
        [2] Decrypt path

        [3] Quit
""";

while True:
    print(main_form)

    r = input("""\n    :>> """)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(key)

    if r == '1':
        open_file = filedialog.askdirectory()
        files = os.listdir(open_file)

        for file in files:
            with open(open_file + '\\' + file, 'rb') as original_file:
                original = original_file.read()

            encrypted = f.encrypt(original)

            with open (open_file + '\\' + file, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)

    elif r == '2':
        open_file = filedialog.askdirectory()
        files = os.listdir(open_file)

        for file in files:
            with open(open_file + '\\' + file, 'rb') as original_file:
                original = original_file.read()

            encrypted = f.decrypt(original)

            with open (open_file + '\\' + file, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)