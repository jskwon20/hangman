import random

def play_hangman():
    words = [
        {"word": "apple", "hint": "fruits"},
        {"word": "house", "hint": "building"},
        {"word": "water", "hint": "liquid"},
        {"word": "music", "hint": "sound"},
        {"word": "happy", "hint": "emotion"}
    ]

    selected = random.choice(words)
    ok = selected["word"]
    hint = selected["hint"]
    attempts = 6  # 시도 횟수
    display = ["_"] * len(ok)
    hint_shown = False  # 힌트가 보여졌는지 여부
    correct_letters = 0  # 맞춘 글자 수

    print("행맨 게임을 시작합니다!")
    print(" ".join(display))

    while attempts > 0 and "_" in display:
        letter = input("글자를 입력하세요: ").lower()

        if len(letter) == 1 and letter.isalpha():
            found = False
            for i in range(len(ok)):
                if letter == ok[i]:
                    if display[i] == "_":
                        correct_letters += 1
                    display[i] = letter
                    found = True

            if not found:
                attempts -= 1
                print(f"틀렸습니다! 남은 시도 횟수: {attempts}")

            if correct_letters >= 2 and not hint_shown:
                print(f"힌트: {hint}")
                hint_shown = True

            print(" ".join(display))
        else:
            print("한 글자의 알파벳만 입력해주세요!")

    if "_" not in display:
        print(f"축하합니다! 정답은 '{ok}'입니다!")
    else:
        print(f"아쉽네요! 정답은 '{ok}'였습니다.")

if __name__ == "__main__":
    play_hangman() 