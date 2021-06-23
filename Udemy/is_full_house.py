from typing import Dict


def is_full_house(a: list) -> bool:
    house = {}
    for _ in a:
        if _ in house:
            house[_] += 1
        else:
            house[_] = 1
    if len(house) == 2 and sum(house.values()) == 5:
        return True
    # else:
    #     if sum(house.values()) == 5:
    #         return True
    return False


print(is_full_house(["A", "A", "A", "K", "K"]))
print(is_full_house(["3", "j", "j", "j", "3"]))
print(is_full_house(["10", "A", "10", "K", "K"]))
print(is_full_house(["7", "J", "3", "4", "3"]))
print(is_full_house(["7", "J", "3", "4", "3", "3"]))
