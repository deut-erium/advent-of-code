with open('input.txt','r') as f:
    grid = f.read().strip().split('\n')
    width, height = len(grid[0]), len(grid)

def get_tree_count(RIGHT,DOWN):
    tree_count = sum(grid[DOWN*i][(RIGHT*i)%width]=='#' for i in range(height//DOWN))
    return tree_count

print(get_tree_count(3,1))

slopes = [
        (1,1),
        (3,1),
        (5,1),
        (7,1),
        (1,2)
        ]

product_slope = 1
for right,down in slopes:
    product_slope *= get_tree_count(right,down)
print(product_slope)


