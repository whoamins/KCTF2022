import random


def amazing_encryption(text: str):
    amazing_key = int()
    result = list()

    for char in text:
        amazing_key = random.randint(1, 2)
        result.append(ord(char) ^ amazing_key)

    print(result)
    return result
