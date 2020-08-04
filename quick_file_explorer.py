import curses
from user_handler import UserHandler
from folder_handler import FolderHandler
from display_handler import DisplayHandler
from config import default_path

class QuickFileExplorer:
    """
    combain all app modules
    """

    # init
    def __init__(self,stdscr):
        # initialize user handler
        self.user_handler = UserHandler(stdscr)
        self.folder_handler = FolderHandler(default_path)
        self.display_handler = DisplayHandler(self.folder_handler, stdscr)

        self.display_handler.print_path_line()
        self.display_handler.print_folder_content(0)
        self.user_handler.set_cursor()
        self.user_handler.window.refresh()


    def one_loop_cycle(self):
        self.user_handler.select_action()
        self.user_handler.window.refresh()



# run app
def main(stdscr):

    # create QuickFileExplorer object
    explorer = QuickFileExplorer(stdscr)

    # run endless loop
    while explorer.user_handler.continue_loop:
        explorer.one_loop_cycle()

curses.wrapper(main)
