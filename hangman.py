import random

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
ok1 = ok[0]
ok2 = ok[1]
ok3 = ok[2]
ok4 = ok[3]
ok5 = ok[4]
attempts = 6  # 시도 횟수
display = ["_", "_", "_", "_", "_"]
hint_shown = False  # 힌트가 보여졌는지 여부
correct_letters = 0  # 맞춘 글자 수

while attempts > 0 and "_" in display:  # 시도 횟수가 남아있고 아직 맞추지 못한 글자가 있을 때
    letter_ok1 = input("글자를 입력하세요: ")  # .lower() 제거

    if len(letter_ok1) == 1 and letter_ok1.isalpha():
        found = False  # 글자를 찾았는지 여부
        for i in range(5):
            if letter_ok1 == ok[i]:  # 대소문자 구분됨
                if display[i] == "_":  # 이전에 맞추지 않은 글자인 경우에만
                    correct_letters += 1
                display[i] = letter_ok1
                found = True

        if not found:  # 글자를 찾지 못했다면
            attempts -= 1  # 시도 횟수 감소
            print(f"틀렸습니다! 남은 시도 횟수: {attempts}")

        # 힌트 표시 조건: 2개 이상의 글자를 맞추고 힌트가 아직 보여지지 않았을 때
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