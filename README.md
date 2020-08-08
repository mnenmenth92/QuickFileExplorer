# QuickFileExplorer

Simple command line file explorer. 

It shows and hides on shortcut command, allows filtering folder content, move across directories with arrows and use functional shortcuts.


# Layout

UI contains 3 elements:
 - current path
 - error message
 - typing input
 - folder content
 
 
 ![alt text](https://i.ibb.co/XxHGvqL/Test-Folder.png)![alt text](https://i.ibb.co/z4QshVw/Filtering.png)![alt text](https://i.ibb.co/z68pW4N/Access-denied.png)

# List of functions

 - folder content colored
   - folders - green
   - text files - yellow
   - images, videos - magenta
 - filtering displayed content while typing
 - arrows (up, down) allowing to move up and down in folder content
 - arrows (left, right) allowing to move in and out of directories
 - rising errors during exploring folders:
   - access denied - for selected folder
   - file impossible to open
 - shortcuts:
   - ctrl-D - open windows file explorer in current directory
   - Enter - run/ open file/ directory
   - ESC - hide file explorer
   
 # Get started
 

 - install windows curses:
 ```
 pip install windows-curses
 ```
 - run main app
 ```
python quick_file_explorer.py 
 ```

   
   
