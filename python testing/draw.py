#graphics
import graphics

def main():
    win = graphics.GraphWin('Shapes')


    center = graphics.Point(100,100)

    circ = graphics.Circle(center, 50)
    circ.setFill('red')
    circ.draw(win)
    
    label = graphics.Text(center, "Red Circle")
    label.draw(win)

    win.getMouse()





main()