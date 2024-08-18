
from turtle import *
BIG_SIDE = 500

def main():
    print('Welcome to andie and radu sierpinski program')

    speed(0)
    back(120)
    draw_sierpinski(BIG_SIDE, 6)


def draw_sierpinski(side_length, depth):
    if depth == 0:
        draw_triangle(side_length)
    else:
        draw_sierpinski(side_length / 2, depth - 1)
        forward(side_length / 2)
        draw_sierpinski(side_length / 2, depth - 1)
        back(side_length / 2)
        left(60)
        forward(side_length/2)
        right(60)
        draw_sierpinski(side_length / 2, depth - 1)
        right(120)
        forward(side_length/2)
        left(120)
    
def draw_triangle(side_length):
    forward(side_length)
    left(120)
    forward(side_length)
    left(120)
    forward(side_length)
    left(120)

if __name__ == '__main__':
    main()
    mainloop()
