def global_warming_status():
    return 'The globe is heating up!'
status = global_warming_status()
print(status)

#The code running the method 'global_warming_status()', which return the string 'The globe is heating up!', and then setting it as the variable 'status'.
#'status' is then printed out into the console.

print(__name__)

#After running 'print(__name__)' if you run this file directly in the console it will return '__Main__'
#After running 'print(__name__)' if you run this file as an import from another file it will return the actual file name 'global_warming' instead of '__Main__'.
#This change occurs since when this file is run as an import from another file, it is no longer run at top main level.