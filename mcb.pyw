#! python3
# mcb.pyw - Saves, loads and deletes pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.
# py.exe mcb.pyw delete - Deletes all keywords
# py.exe mcb.pyw delete <keyword> - Deletes a specific keyword
import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')
# Save clipboard content by keyword.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
# Deletes content by keyword.
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    # Deletes all.
    elif sys.argv[1].lower() == 'delete':
        for k in list(mcbShelf.keys()):
                      del mcbShelf[k]
    # Loads content by keyword.
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()

#note: will create mcb.bak, mcb.dat, mcb.dir in same directory as mcb.pyw to store.