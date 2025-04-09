# # Implement an 'eraser' on a canvas.

# # The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

# from graphics import GraphWin, Rectangle, Point, color_rgb
# import time

# canvas_width:int = 500
# canvas_height:int = 500

# cell_size:int = 10
# eraser_size:int = 50

# def erase_objects(cells, eraser_rect):
#     """Erase the cells that are within the bounds of the eraser rectangle."""
#     for cell in cells:
#         if (cell.getP1().getX() < eraser_rect.getP2().getX() and
#             cell.getP2().getX() > eraser_rect.getP1().getX() and
#             cell.getP1().getY() < eraser_rect.getP2().getY() and
#             cell.getP2().getY() > eraser_rect.getP1().getY()):
#             cell.setFill("white")

# def main():
#     """Main function to create a canvas and an eraser."""
#     global win
#     win = GraphWin("Eraser", canvas_width, canvas_height)
#     win.setBackground("blue")

#     # Create a grid of rectangles (cells)
#     cells = []
#     for x in range(0, canvas_width, cell_size):
#         for y in range(0, canvas_height, cell_size):
#             cell = Rectangle(Point(x, y), Point(x + cell_size, y + cell_size))
#             cell.setFill("blue")
#             cell.draw(win)
#             cells.append(cell)

#     # Create the eraser rectangle
#     eraser_rect = Rectangle(Point(0, 0), Point(eraser_size, eraser_size))
#     eraser_rect.setFill("red")
#     eraser_rect.draw(win)

#     while not win.isClosed():
#         mouse_pos = win.getMouse()
#         if mouse_pos:
#             eraser_rect.move(mouse_pos.getX() - (eraser_rect.getP1().getX() + eraser_size / 2),
#                              mouse_pos.getY() - (eraser_rect.getP1().getY() + eraser_size / 2))
#             erase_objects(cells, eraser_rect)
#         time.sleep(0.1)
        
#     win.close()

# if __name__ == "__main__":
#     main()

from graphics import GraphWin, Rectangle, Point, color_rgb
import time

canvas_width: int = 500
canvas_height: int = 500

cell_size: int = 10
eraser_size: int = 50

def erase_objects(cells, eraser_rect):
    """Erase the cells that are within the bounds of the eraser rectangle."""
    for cell in cells:
        if (cell.getP1().getX() < eraser_rect.getP2().getX() and
            cell.getP2().getX() > eraser_rect.getP1().getX() and
            cell.getP1().getY() < eraser_rect.getP2().getY() and
            cell.getP2().getY() > eraser_rect.getP1().getY()):
            cell.setFill("white")

def main():
    win = GraphWin("Eraser", canvas_width, canvas_height)
    win.setBackground("blue")

    # Create a grid of rectangles (cells)
    cells = []
    for x in range(0, canvas_width, cell_size):
        for y in range(0, canvas_height, cell_size):
            cell = Rectangle(Point(x, y), Point(x + cell_size, y + cell_size))
            cell.setFill("blue")
            cell.draw(win)
            cells.append(cell)

    # Create the eraser rectangle
    eraser_rect = Rectangle(Point(0, 0), Point(eraser_size, eraser_size))
    eraser_rect.setFill("red")
    eraser_rect.draw(win)

    while True:
        if win.isClosed():
            break

        mouse_pos = win.checkMouse()
        if mouse_pos:
            eraser_center_x = mouse_pos.getX()
            eraser_center_y = mouse_pos.getY()

            # Calculate current top-left corner of eraser
            current_center_x = (eraser_rect.getP1().getX() + eraser_rect.getP2().getX()) / 2
            current_center_y = (eraser_rect.getP1().getY() + eraser_rect.getP2().getY()) / 2

            dx = eraser_center_x - current_center_x
            dy = eraser_center_y - current_center_y

            eraser_rect.move(dx, dy)
            erase_objects(cells, eraser_rect)

        time.sleep(0.01)

    win.close()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)

