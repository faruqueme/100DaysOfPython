# 🚨 Don't change the code below 👇
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
input_num = (list(position))

x = (input_num[0])
y = (input_num[1])

if x == '1' and y == '1':
    row1[0] = "X".strip(" ")
elif x == '2' and y == '1':
    row1[1] = "X".strip(" ")
elif x == '3' and y == '1':
    row1[2] = "X".strip(" ")
elif x == '1' and y == '2':
    row2[0] = "X".strip(" ")
elif x == '2' and y == '2':
    row2[1] = "X".strip(" ")
elif x == '3' and y == '2':
    row2[2] = "X".strip(" ")
elif x == '1' and y == '3':
    row3[0] = "X".strip(" ")
elif x == '2' and y == '3':
    row3[1] = "X".strip(" ")
elif x == '3' and y == '3':
    row3[2] = "X".strip(" ")
else:
    print("You entered invalid number.")

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
