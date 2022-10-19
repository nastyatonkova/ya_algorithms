"""
The "Speed Print Simulator" game is a 4x4 key field. 
In it, a configuration of numbers and dots appears on each round. 
On the key is written either a dot or a number from 1 to 9.
At time t, the player must simultaneously press all the keys 
on which the number t is written. Gosha and Timofey can press k keys each at a moment of time. 
If at time t all necessary keys are pressed, the players get 1 point.
Find the number of points that Gosha and Timofey can earn, if they press the keys together.

The following algorithm is used:

Method get_count_buttons converts list of buttons
to the dictionary (button name:number of occurance), dots are ignored.

Method sleight_of_hand counts max points by iterating through all buttons 
in the dictionary and check the condition that each player can press only
k buttons max: 2*k >= number of buttons occurance (value in dict).


Example:
4
1111
9999
1111
9911

field_buttons=(1:10,9:6)
press_buttons=8
max_points=1

"""


from typing import Dict, Tuple, List


def get_count_buttons(buttons: str) -> Dict[int, int]:
    field_buttons = dict()
    for r in buttons:
        if r.isdigit():
            num = r
            if field_buttons.get(num):
                field_buttons[num] += 1
            else:
                field_buttons[num] = 1
    return field_buttons


def sleight_of_hand(k: int, buttons: str) -> int:
    max_points = 0
    press_buttons = k * 2
    field_buttons = get_count_buttons(buttons)
    for button in field_buttons:
        count_button = field_buttons.get(button)
        if count_button <= press_buttons:
            max_points += 1
    return max_points


def read_input() -> Tuple[int, str]: 
    k = int(input())
    buttons = ""
    for _ in range(4):
        buttons = buttons + input().strip()
    return k, buttons


if __name__ == '__main__':
    result = sleight_of_hand(*read_input())
    print(result)
