import shelve, pyperclip, sys
shelfobj = shelve.open('multiclipboard')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    shelfobj[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'del':
    try:
      del shelfobj[sys.argv[2]]
    except KeyError:
      pass  
elif  len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
      pyperclip.copy(str(list(shelfobj.keys())))
    elif sys.argv[1].lower() == 'del':
      shelfobj.clear()  
    else:
      pyperclip.copy(shelfobj[sys.argv[1]])     
shelfobj.close()      
    
