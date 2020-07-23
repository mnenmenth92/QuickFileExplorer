# default values
default_path = 'C:\\TestFolder'
window_name = 'Quick File Explorer'

# displayed colors
# colorama: https://pypi.org/project/colorama/

colors = {
    'default': '\033[31m',  # red
    'folder': '\033[32m',  # green
    '.txt': '\033[33m',  # yellow
    '.py': '\033[34m',  # blue
    '.c': '\033[34m',  # blue
    '.jpg': '\033[35m',  # magenta
    '.png': '\033[35m',  # magenta
    '.bmp': '\033[35m'  # magenta
}

selected_background = '\033[47m'
reset_background = '\033[49m'
link_format =  '\033[2m'
reset_format =  '\033[0m'