
def sum_values(my_dict):
    total = 0
    for value in my_dict.values():
        total = total + value
    return total

score_board = {"round1": 10, "round2": 20, "round3": 15}
print("Total Score:", sum_values(score_board))  

