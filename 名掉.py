Polls_Cand_W_Vrate = 50
Polls_Cand_L_Vrate = 50
Polls_Cand_W_name = "Cand1"
Polls_Cand_L_name = "Cand2"
Polls_Cand_W_Vrate = 50
Polls_Cand_L_Vrate = 50
Polls_ratio = int(input("輸入此民調抽樣比(輸入百分比，不用加%號)"))
for k in range(50):
    Polls_Cand_W_Vrate += 1
    Polls_Cand_L_Vrate -= 1
    print(Polls_Cand_W_Vrate, Polls_Cand_L_Vrate)

    Pos_number = 0

    Polls_ratio_left = 100 - Polls_ratio
    x = Polls_ratio_left
    y = 0

    for k in range(Polls_ratio_left):
        x_compare = Polls_Cand_W_Vrate * Polls_ratio / 100 + x
        y_compare = Polls_Cand_L_Vrate * Polls_ratio / 100 + y
        x -= 1
        y += 1
        if x_compare > y_compare:
            Pos_number += 1
            Pos_name = Polls_Cand_W_name
            Pos_BL = "T"

        elif x_compare < y_compare:
            Pos_name = Polls_Cand_L_name
            Pos_BL = "F"

        else:
            Pos_name = Polls_Cand_L_name + Polls_Cand_L_name
            Pos_BL = "F"

    print(
        "準確率是",
        Pos_number,
        "/ ",
        Polls_ratio_left,
        Pos_number / Polls_ratio_left * 100,
        "%",
    )
