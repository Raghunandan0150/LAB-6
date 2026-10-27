


n = int(input())

winner = -1
runner_up = -1

for i in range(n):
    distance = int(input())

    if distance > winner:
        runner_up = winner
        winner = distance

    elif distance != winner and distance > runner_up:
        runner_up = distance

print(winner)
print(runner_up)