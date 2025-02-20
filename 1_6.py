def generate(numRows):
    triangle = []
    
    for row in range(numRows):
        new_row = [1] * (row + 1)
        

        for j in range(1, row):
            new_row[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]
        
        triangle.append(new_row)
    
    return triangle


print(generate(5))  
print(generate(1))