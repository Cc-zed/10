# -----------------------------Task 1------------------------------------

# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)

# num1 = 48
# num2 = 18
# result = gcd(num1, num2)
# print("Max dilnuk of numbers", num1, "and", num2, ":", result)

# -----------------------------Task 2------------------------------------

# from random import randint

# print('WElcome into game "Bulls and Cows"!')
# game = 'yes'

# while game == 'yes':
#    num = str(randint(1000, 9999))
#    print("Guess random generated number")
#    attempt = True

#    while attempt:
#        player_num = input("Your guess: ")

#        if len(player_num) != 4:
#            print("Number is invalid. Please enter four digits number.")
#            continue  # Return to inputting a new number

#        bulls = 0
#        cows = 0

#        for i in range(4):
#            if num[i] == player_num[i]:
#                bulls += 1

#            elif player_num[i] in num:
#                cows += 1

#        if bulls == 4:
#            print("4 Bulls! You won!")
#            game = input('Want to start new game? (yes / no): ')
#            attempt = False

#        else:
#            print(f'{bulls} Bull(-s), {cows} Cow(-s)')

# -----------------------------Task 3------------------------------------

# n = 8
# a = [[-1] * n for _ in range(n)]
# move = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

# def foo(i, j, pos):
#     if pos == n * n:
#         return True
#     for mi, mj in move:
#         i_new = i + mi
#         j_new = j + mj
#         if 0 <= i_new < n and 0 <= j_new < n and a[i_new][j_new] == -1:
#             a[i_new][j_new] = pos
#             if foo(i_new, j_new, pos + 1):
#                 return True
#             a[i_new][j_new] = -1
#     return False

# x = int(input("Enter starting row (from 0 to 7): "))
# y = int(input("Enter starting column (from 0 to 7): "))
# a[x][y] = 0

# if foo(x, y, 1):
#     for row in a:
#         print(*row)
# else:
#     print("There is no way")

# -----------------------------Task 4------------------------------------

# from tkinter import *
# from tkinter import messagebox
# from random import shuffle

# root = Tk()
# root.title('Fifteens')

# a = StringVar()
# a.set('Move')

# m = StringVar()
# m.set(' ')

# class Bbut(Button):
#     pos_x: '1'
#     pos_y: '1'
#     defvalue: '1'

# # Board
# H = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, " ")

# # Buttons
# btn = []
# for x in range (4):
#     for y in range(4):
#       foo = Bbut(width='5', height='3', relief= 'groove')
#       foo.pos_x, foo.pos_y = x, y
#       btn.append(foo)
# for i in range (16):
#     btn[i].configure(text = H[i])
#     btn[i].defvalue = H[i]

# # z - empty place
# z = btn[15]

# # Exit
# button17 = Button(bg = 'dark red', width = '5', height = '3',text = 'E')
# # Restart
# button18 = Button(bg = 'dark green', width = '5', height = '3',text = 'S')


# label2 = Label()
# label3 = Label()
# label1 = Label(width = '5', height = '3', bg = 'light green', textvariable = a)
# label4 = Label(width = '5', height = '3', bg = 'light green', textvariable = m)


# def on_enter(e):
#     if (highlights(e)):
#                 e.widget.configure(bg="khaki")

# def on_leave(e):
#     chk_color()

# def highlights(e):
#     txt = e.widget['text']
#     # If nothing
#     if txt != ' ' and txt != 'E' and txt != 'S':
#         # Coordinates of board
#         x, y = int(e.widget.pos_x), int(e.widget.pos_y)
#         zx, zy = int(z.pos_x), int(z.pos_y)
#         # If cordinates inside board
#         if (-1 < x < 4) and (-1 < y < 4) :
#             # Check coordinates for move ability
#             if (x in [zx - 1, zx + 1] and y == zy or y in [zy - 1, zy + 1] and x == zx):
#                 return True
#     return False


# # Knopki
# def callback(e):
#     txt = e.widget['text']
#     # If empty - nothing
#     if txt == ' ':
#         return
#     # Exit
#     elif txt == 'E':
#         root.destroy()
#     # Restart
#     elif txt == 'S':
#         shf()
#         chk_color()
#     # Move
#     else:
#         a.set(txt)
#         m.set((e.widget.pos_x, e.widget.pos_y))
#         if (move(e)):
#             chk_color()
#             check_win()

# # Check for win
# def check_win():
#     foo = 0
#     for i in btn:
#         if i.defvalue == i.cget('text'):
#             foo += 1
#     if foo == 16:
#         messagebox.showinfo( "Win!", "One more time?")
#         shf()
#         chk_color()
#         a.set(' ')


# # Moving Figure
# def move(e):
#     global z
#     # If place is
#     if e.widget.cget('bg') == 'khaki':
#         # Moving figure to empty place
#         z.configure(text = e.widget.cget('text'))
#         # Emptying place from what pohodit
#         e.widget.configure(text = ' ')
#         # Remembering new object of empty place
#         z = e.widget
#         return True;
#     else: return False;

# # Restart
# def shf():
#     global z
#     # Vremennyaa doska
#     s = list(H)
#     # Peremeshivaem
#     shuffle(s)
#     # Обновляем поле
#     for i in range (16):
#               btn[i].configure(text = s[i])
#     # Looking for empty place
#     for i in btn:
#         if i.cget('text') == ' ':
#             # Remembering new object of empty place
#             z = i
#             m.set((z.pos_x, z.pos_y))
#             break

# # color of board
# def chk_color():
#     for i in btn:
#         foo = i.cget('text');
#         # if figure on its place
#         if foo == i.defvalue and foo != ' ':
#             i.configure(bg = 'light green')
#         # if place is empty
#         elif foo == ' ':
#             i.configure(bg = 'light pink')
#         # if figure not on its place
#         else:
#             i.configure(bg = 'SystemButtonFace')


# def main():

#     for i in btn:
#         i.grid(row = i.pos_x, column = i.pos_y)

#     button17.grid(row = 1, column = 5)
#     button18.grid(row = 2, column = 5)

#     label2.grid(row = 1, column = 4)
#     label3.grid(row = 2, column = 4)

#     label1.grid(row = 3, column = 5)
#     label4.grid(row = 0, column = 5)

#     root.bind_class('Button','<1>', callback)
#     root.bind_class('Button','<Enter>', on_enter)
#     root.bind_class('Button','<Leave>', on_leave)
#     chk_color()
#     messagebox.showinfo( "Start?", "'S' - new game\n'E' - exit")

#     root.mainloop()
#     pass

# if __name__ == '__main__':
#     main()

# ---------------------------------END------------------------------------