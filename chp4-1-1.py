n = int(input())
command = input().split()
type = ["L","R","U","D"]
dx = [-1,1,0,0]
dy = [0, 0, 1, -1]
x = 1
y = 1

for i in range(len(command)):
    
    if type[i] == command[i]:
        x += dx[i]
        y += dy[i]



print(x,y)



