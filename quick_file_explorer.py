import curses
from user_handler import UserHandler


class QuickFileExplorer:
    """
    combain all app modules
    """

    # init
    def __init__(self,stdscr):
        # initialize user handler
        self.user_handler = UserHandler(stdscr)

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
