import random

def guess_the_number(difficulty="easy"):
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "medium":
        attempts = 5
    else:
        attempts = 3

    secret_number = random.randint(1, 100)
    used_numbers = set()

    while attempts > 0:
        guess = int(input("Вгадайте число від 1 до 100: "))
        if guess in used_numbers:
            print("Ви вже вводили це число.")
        elif guess < secret_number:
            print("Спробуйте більше число.")
        elif guess > secret_number:
            print("Спробуйте менше число.")
        else:
            print(f"Вітаємо! Ви вгадали число {secret_number}.")
            break

        used_numbers.add(guess)
        attempts -= 1
        print(f"У вас залишилося {attempts} спроб.")
        print(f"Використані числа: {', '.join(map(str, used_numbers))}")

    if attempts == 0:
        print(f"Ви програли. Правильне число було {secret_number}.")

if __name__ == "__main__":
    guess_the_number()
 
