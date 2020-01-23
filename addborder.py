def addBorder(picture):
    wall = len(picture[0]) + 2
    border = '*'  *  wall 

    picture.append(border)
    picture.insert(0, border)
    print(picture)


print(addBorder(['efa', 'ff', 'fwr']))
