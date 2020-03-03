import global_warming

status = global_warming.global_warming_status()
print('UN expert panel says: ' + status)

#The global_warming.py program that we just wrote is being imported and the method 'global_warming_status()' isbeing called and set as the variable 'status'.
#Since the method 'global_warming_status()' returns the string 'The globe is heating up!', 'status' now contains this value.
#status is then concatnated with the string 'UN expert panel says: ' which is then printed out into the console.
#The print output will then be 'The globe is heating up!' from the 'global_warming_status()' method call, followed by 'UN expert panel says: The globe is heating up!'.

print(__name__)

#After running 'print(__name__)' the file now also returns '__Main__'
#When 'global_warming_status()' is run, it will now print out the actual name of the file 'global_warming' instead of '__Main__', since it is not being run at top main level, but instead as an import.