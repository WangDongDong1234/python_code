n=int(input())
attack_str=input().strip()
attack=[int(item) for item in attack_str.split(' ')]
money_str=input().strip()
money=[int(item) for item in money_str.split(' ')]
total_attack=0
total_money=0
for i in range(len(attack)):
    if total_attack<attack[i]:
        total_attack+=attack[i]
        total_money+=money[i]
    else:
        continue
print(total_money)