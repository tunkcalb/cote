import sys

input = sys.stdin.readline


def counting_stars(n):
    if n == 1:
        return "*"

    stars = counting_stars(n // 3)
    answer = []
    for star in stars:
        answer.append(star * 3)
    for star in stars:
        answer.append(star + " " * (n // 3) + star)
    for star in stars:
        answer.append(star * 3)

    return answer


n = int(input().rstrip())
print("\n".join(counting_stars(n)))
