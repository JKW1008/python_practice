# 사용자로부터 숫자 입력 받기
user_input = float(input("숫자를 입력하세요: "))

# 입력값이 양수, 음수, 또는 0인지 판별
if user_input > 0:
    print("입력한 숫자는 양수입니다.")
elif user_input < 0:
    print("입력한 숫자는 음수입니다.")
else:
    print("입력한 숫자는 0입니다.")


# 사용자로부터 높이 입력 받기
height = int(input("별의 높이를 입력하세요: "))

# 삼각형 모양으로 별 찍기
for i in range(1, height + 1):
    print(" " * (height - i) + "*" * (2 * i - 1))
