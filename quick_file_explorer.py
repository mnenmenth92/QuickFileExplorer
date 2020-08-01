import curses
from user_handler import UserHandler
from folder_handler import FolderHandler
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

        # Temporary
        # self.user_handler.curses.init_pair(1, self.user_handler.curses.COLOR_YELLOW,self.user_handler.curses.COLOR_BLACK)
        # self.user_handler.window.attron(self.user_handler.curses.color_pair(1))

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
