import curses

#setup the game window
curses.initscr() 
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

#game program
score = 0

while True: 
    even = win.getch()

curses.endwin()
print(f"Final score {score}") 