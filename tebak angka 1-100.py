import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Hai guys! Aku punya sebuah angka antara 1 dan 100. Bisakah kamu menebaknya?")

    while True:
        guess = int(input("Tebak angka: "))
        attempts += 1

        if guess < secret_number:
            print("Angka terlalu kecil, coba lagi .")
        elif guess > secret_number:
            print("Angka terlalu besar, coba lagi .")
        else:
            print(f"Selamat! Kamu menebak angka dengan benar ({secret_number}) dalam {attempts} percobaan. Kamu memang suhu")
            break

if __name__ == "__main__":
    guess_number()