# from sklearn.linear_model import LinearRegression
# import numpy as np
# from bs4 import BeautifulSoup as bs
# import requests
# from numpy import logical_not
# import pandas as pd
# acc = pd.Series([1, 2, 3, 4, 5])
# acc += 10
# print(acc)


# url = 'https://www.dip.or.kr'
# response = requests.get(url)
# html = bs(response.text, 'html.parser')
# logo = html.find('img')
# print(logo)


# # 2023년의 삼성전자 주식 상장률과 가격 데이터 (예시 데이터)
# # X: 상장률, Y: 가격
# X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # 2023년 상장률
# Y = np.array([100, 110, 120, 130, 140])  # 2023년 가격

# # 선형 회귀 모델 생성
# model = LinearRegression()
# model.fit(X, Y)

# # 2024년의 상장률을 입력하여 주식 가격 예측
# predicted_price = model.predict(
#     np.array([6]).reshape(-1, 1))  # 2024년 상장률에 대한 가격 예측
# print("2024년 삼성전자 주식 예상 가격:", predicted_price[0])


# 사용자로부터 줄 수 입력 받기
num_lines = int(input("몇 줄을 출력하시겠습니까? "))

# 역방향으로 별찍기
for i in range(num_lines, 0, -1):
    # 공백 출력
    spaces = ' ' * (num_lines - i)
    # 별 출력
    stars = '*' * i
    # 공백과 별 결합하여 출력
    print(spaces + stars)
