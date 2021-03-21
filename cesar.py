from __future__ import print_function
from time import sleep


letter_min = list({chr(i+96):i for i in range(1,27)}.keys())
letter_maj = list({chr(i+64):i for i in range(1,27)}.keys())


def crypter(text):
     for i in range(len(text)):
          try:
               text_crypter = str(letter_min[letter_min.index(text[i])+3])
               print(text_crypter, end="")
          except ValueError:
               print("Ecrire toutes les lettres en minuscules")
               break


def decrypter(text):
     for i in range(len(text)):
          try:
               text_decrypter = str(letter_min[letter_min.index(text[i])-3])
               print(text_decrypter, end="")
          except ValueError:
               print("Ecrire toutes les lettres en minuscules")
               break


if __name__ == "__main__":
     try:
          choice = int(input(("Choisir [1] pour crypter et [2] pour décrypter >>> ")))
          try:
               if choice == 1:
                    text = str(input("Message à crypter >>> "))
                    crypter(text)
               elif choice == 2:
                    text = str(input("Message à décrypter >>> "))
                    decrypter(text)
               else:
                    print("Veuillez choisir entre [1] et [2]")
          except KeyboardInterrupt:
               print("\nExiting...")
               sleep(1.5)
     except KeyboardInterrupt:
               print("\nExiting...")
               sleep(1.5)