def get_input(tests):
    coins_list = []
    if tests == 0:
        coins_list.append([0])
        return coins_list
    
    for i in range(tests):
        mons = int(input())
        if mons == 0:
            coins_list.append([0])
            return coins_list

        if (mons >=0 and mons <= 10**4):
            k = [int(e.strip()) for e in input().split()]
            if (min(k)>= 0 and max(k) <= 10**9):
                coins_list.append(k[: mons])
            else:
                coins_list.append([0])
        else:
            coins_list.append([0])
    return coins_list

if __name__ == "__main__":
    mons_coins = []
    tests = int(input ())
    mons_coins = get_input(tests)
    for i in range(len(mons_coins)):
        evenSum = sum([mons_coins[i][j] for j in range(len(mons_coins[i])) if j % 2 == 0])
        evenOdd = sum([mons_coins[i][j] for j in range(len(mons_coins[i])) if j % 2 == 1])
        print(f"Case {i+1}: {max(evenSum,evenOdd)}" )
