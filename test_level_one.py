import sys
from tkinter import E


def test_we_love_kriii():
    output = "강한친구 대한육군 \n"
    twice_ouputs = output * 2
    twice_counts = twice_ouputs.count("\n")

    print(twice_ouputs)

    assert twice_counts == 2
    assert twice_ouputs == "강한친구 대한육군 \n강한친구 대한육군 \n"


def test_dog():
    print("|\\_/|")
    print("|q p|   /}")
    print('( 0 )"""\\')
    print('|"^"`    |')
    print("||_/=\\\\__|")


def test_add_calculation():
    a, b = map(int, input().split())
    print(a + b)


def test_sub_calculation():
    a, b = map(int, input().split())
    print(a - b)


def test_multiply_calculation():
    a, b = map(int, input().split())
    print(a * b)


def test_arithmetic_operation():
    a, b = map(int, input().split())
    print(a + b)
    print(a - b)
    print(a * b)
    print(int(a / b))
    print(a % b)


def test_duplicate_name():
    intputText = input()
    suffixes = "??!"
    print(str(intputText) + suffixes)


def test_buddhist_year_convert():
    inputYear = input()
    print(int(inputYear) - 543)


def test_remainder():
    a, b, c = map(int, input().split())
    print((a + b) % c)
    print(((a % c) + (b % c)) % c)
    print((a * b) % c)
    print(((a % c) * (b % c)) % c)


def test_multiply():
    a = int(input())
    b = str(input())
    print(a * (int(b[2])))
    print(a * (int(b[1])) * 10)
    print(a * (int(b[0])))
    print((a * (int(b[2]))) + (a * (int(b[1])) * 10) + (a * (int(b[0])) * 100))


def test_compare_two_numbers():
    a, b = map(int, input().split())
    print(">" if a > b else "<" if a < b else "==")


def test_score():
    print("FFFFFFDCBAA"[0])


def leap_year():
    year = int(input())
    print("1") if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else print("0")


# 사분면 고르기
def test_pick_quadrant():
    x = int(input())
    y = int(input())

    if x > 0 and y > 0:
        print(1)
    elif x < 0 and y > 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    else:
        print(4)


def test_alarm_clock():
    H, M = map(int, input().split())
    if M >= 45:
        print(H, M - 45)
    elif H >= 1 and M <= 45:
        print(H - 1, M + 15)
    else:
        print(23, M + 15)


def test_oven_clock():
    """
    첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고
    순서대로 주어진다. 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다.
    """
    # given
    """
    23 48
    25
    """
    H, M = map(int, input().split())
    endTime = int(input())
    end_H = endTime // 60
    end_M = endTime % 60

    # when
    H_Plus = (M + end_M) // 60
    H = (end_H + H + H_Plus) % 24 if end_H + H + H_Plus >= 24 else (end_H + H + H_Plus)
    M = (M + end_M) % 60
    # then
    print(H, M)


def test_prize_calculator():
    """
    1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

    같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
    같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
    모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
    예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다.
    또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다.
    3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.

    3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.
    """
    # given
    # 2 2 2
    diceEyeList = list(map(int, input().split()))

    # when
    sameCount = len(diceEyeList) - len(set(diceEyeList))
    max_value = max(diceEyeList)
    frequency_value = diceEyeList[0]
    result = 0

    if sameCount > 0:
        for i in set(diceEyeList):
            if diceEyeList.count(i) > diceEyeList.count(frequency_value):
                frequency_value = i
        result = 100 * (10**sameCount) + (10 * (10**sameCount) * frequency_value)
    else:
        result = 100 * max_value

    print(result)

    # then
    # assert result == 12000


def test_multiplication_table():
    n = int(input())
    for i in range(1, 10):
        print(str(n) + " * " + str(i) + " = " + str(n * i))


def test_difference():
    n = int(input())
    for i in range(0, n):
        a, b = map(int, input().split())
        print(a + b)


def test_fest_difference():
    n = int(sys.stdin.readline().rstrip())
    for i in range(0, n):
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)


def test_sum():
    n = int(input())


def test_n_print():
    n = int(sys.stdin.readline().rstrip())
    for i in range(1, n + 1):
        print(i)


def test_n_print_reverse():
    n = int(sys.stdin.readline().rstrip())
    for i in range(n, 0, -1):
        print(i)


def test_fest_difference_version_6():
    n = int(sys.stdin.readline().rstrip())
    for i in range(1, n + 1):
        a, b = map(int, sys.stdin.readline().split())
        print(f"Case #{i}: {a + b}")


def test_fest_difference_version_7():
    n = int(sys.stdin.readline().rstrip())
    for i in range(1, n + 1):
        a, b = map(int, sys.stdin.readline().split())
        print(f"Case #{i}: {a} + {b} = {a + b}")


def print_star():
    n = int(sys.stdin.readline().rstrip())
    for i in range(1, n + 1):
        print(f"{i * '*' }")


def print_star_white_space():
    n = int(sys.stdin.readline().rstrip())
    for i in range(1, n + 1):
        print(f"{(n-i) * ' ' }{i*'*'}")


def test_find_number_less_than_x():
    n, x = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))
    find_numbers = [str(i) for i in numbers if i < x]
    print(" ".join(find_numbers))

    # 아래가 맞는듯
    # a, b = map(int, input().split())
    # c = list(map(int, input().split()))

    # for i in range(a):
    #     if (c[i] < b):
    #         print(c[i], end = " ")


test_find_number_less_than_x()
