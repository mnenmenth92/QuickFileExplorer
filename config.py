import curses

# default values
default_path = 'C:\\TestFolder'
window_name = 'Quick File Explorer'

# displayed colors

colors = {
    'default': curses.COLOR_RED,
    'folder': curses.COLOR_GREEN,
    '.txt': curses.COLOR_YELLOW,
    '.py': curses.COLOR_YELLOW,
    '.c': curses.COLOR_YELLOW,
    '.jpg': curses.COLOR_MAGENTA,
    '.png': curses.COLOR_MAGENTA,
    '.bmp': curses.COLOR_MAGENTA
}


selected_background = curses.COLOR_BLUE
default_background = curses.COLOR_BLACK

