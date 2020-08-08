import curses

# default values
default_path = 'C:\\'
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
path_color = curses.COLOR_WHITE
type_line_color = curses.COLOR_WHITE
user_info_color_fg = curses.COLOR_RED
user_info_color_bg = curses.COLOR_YELLOW

# UI elements position

path_line_num = 0
type_line_num = 3
folder_content_line_num = 5
user_info_line = 1
last_selected_element = 2

