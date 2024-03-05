# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e.,
# grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can
# only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take
# to reach the bottom-right corner.
# The test cases are generated so that the answer will be less than or equal to 2 * 109.

m=0
n=0
while m<1 and type(m)==int:
    
    try:
        m=int(input("Enter number of rows greater than 1: "))
    except Exception:
        pass
while (n<=0 or n>=100) and type(m)==int:
    try:
        n=int(input("Enter number of columns greater than 0 and <=100: "))
    except Exception:
        pass
    
x='Finish'
grid=[[0]*n]*m
print(grid)
grid[m-1][n-1]=x
start=grid[0][0]
end=grid[m-1][n-1]
counti=0
countj=1

while True:
    for i in range(m):
        start=grid[i][0]
        counti+=1
        if i == m-1:
            for j in range(n):
                start=grid[i][j]
                countj+=1
                if j==n-1:
                    print("Robot has reached: ", start)
    break
count=counti+countj
print("Total counts:",count,'\n')
# print("Right counts:",countj,'\n')
