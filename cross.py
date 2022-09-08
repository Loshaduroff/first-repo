field = [['-'] * 3 for _ in range(3)]

def show_field(f):
    num = '  0 1 2'
    print(num)
    for row, i in zip(f, num.split()):
        print(f"{i} {' '.join(str(j) for j in row)}")

def input_coord(f):
    while True:
        coord = input("Введите координаты позиции: ").split()
        if len(coord) != 2:
            print ("Введите две координаты!")
            continue
        if not(coord[0].isdigit() and coord[1].isdigit()):
            print ("Введите числа")
            continue
        x, y = map(int,coord)
        if not(x>=0 and x<3 and y>=0 and y<3):
            print('Координаты от 0 до 2')
            continue
        if f[x][y]!= "-":
            print('Клетка занята')
            continue
        break
    return x,y

def winner (f, user):
    win_coord = (((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)), ((0,2), (1,1), (2,0)), ((0,0), (1,1), (2,2)), ((0,0), (1,0), (2,0)), ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2)))
    for coord in win_coord:
        simbols = []
        for c in coord:
            simbols.append(f[c[0]][c[1]])
        if simbols == [user, user, user]:
            return True
    return False

count=0
while True:
    if count == 9:
        print ("Ничья")
        break
    if count%2==0:
        user = "X"
    else:
        user = "0"
    show_field(field)
    x,y = input_coord(field)
    field[x][y]=user
    if winner(field, user):
        show_field(field)
        print(f" Выиграл игрок {user}")
        break
    count += 1




