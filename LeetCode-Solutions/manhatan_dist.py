def nearvalid(x: int, y: int, points: list[list[int]]) -> int:
    valid_points = [point for point in points if (point[0] == x or point[1] == y)]
    if not valid_points:
        return -1
    else:
        dest = [(abs(x-val_point[0]) + abs(y-val_point[1]),points.index(val_point)) for val_point in valid_points ]
        return sorted(dest,key=lambda x:x[0])[0][1]
        

        




print(nearvalid(x=3,y=4,points=[[1,2],[3,1],[2,4],[2,3],[4,4]]))
print(nearvalid(x = 3, y = 4, points = [[3,4]]))
print(nearvalid(x = 3, y = 4, points = [[2,3]]))




