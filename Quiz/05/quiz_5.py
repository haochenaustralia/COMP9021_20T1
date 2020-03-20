# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# In both functions below, grid is supposed to be a sequence of strings
# all of the same length, consisting of nothing but spaces and *s,
# and represent one or more "full polygons" that do not "touch" each other.

def display(*grid):
    for items in grid:
        print(" ".join(items))
    # REPLACE pass ABOVE WITH YOUR CODE


# check boundary
# 只要不被4个星号围住，就是boundary
def check_boundary(grid, y, x):
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    count = 0
    y_length = len(grid)
    x_length = len(grid[0])
    for direction_y, direction_x in directions:
        current_y = y + direction_y
        current_x = x + direction_x
        # check 边界
        if 0 <= current_y < y_length and 0 <= current_x < x_length \
                and grid[current_y][current_x] != ' ':
            count = count + 1

    if count < 4:
        return True
    else:
        return False


def get_leftmost_topmost_point(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '*':
                return y, x


def loop_boundary(grid, y, x):

    directions = [(1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
    grid[y][x] = '1'
    y_length = len(grid)
    x_length = len(grid[0])
    for direction_y, direction_x in directions:
        current_y = y + direction_y
        current_x = x + direction_x
        # check 边界
        if 0 <= current_y < y_length and 0 <= current_x < x_length \
                and grid[current_y][current_x] == '*' \
                and check_boundary(grid, current_y, current_x):
            loop_boundary(grid, current_y, current_x)

def display_leftmost_topmost_boundary(*grid):
    # 获取最左边和最顶部的点
    leftmost_y, leftmost_x = get_leftmost_topmost_point(grid)
    new_grid = [list(item) for item in grid]
    loop_boundary(new_grid, leftmost_y, leftmost_x)
    for items in new_grid:
        print(" ".join("".join(items).replace("*",' ').replace("1",'*')))

# POSSIBLY DEFINE OTHER FUNCTIONS

# POSSIBLY DEFINE OTHER FUNCTIONS
if __name__ == "__main__":
    grid_2 = (' *        ',
              '***   **  ',
              ' *** ***  ',
              ' ***  *   ',
              '****      ',
              ' **       '
              )
    display(*grid_2)
    display_leftmost_topmost_boundary(*grid_2)
