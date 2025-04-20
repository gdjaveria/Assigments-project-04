import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40

# create the grid of blue cells on the canvas........
def create_grid(canvas):
    grid = []
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        row_cells = []
        for col in range(0, CANVAS_WIDTH,CELL_SIZE):
            rect = canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE,
                                        outline='black', fill='blue')
            row_cells.append(rect)
        grid.append(row_cells)
    return grid

# Handle mouse click events to erase cells........
def on_click(event, canvas, grid):
    col = event.x // CELL_SIZE
    row = event.y // CELL_SIZE

    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        canvas.itemconfig(grid[row][col], fill= 'white')

def main():
    root = tk.Tk()
    root.title('Grid Erasing Game')

    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT , bg= 'white')
    canvas.pack()

    grid = create_grid(canvas)
    canvas.bind('<Button-1>', lambda event: on_click(event,canvas, grid))
    root.mainloop()

if __name__ == '__main__':
    main()

