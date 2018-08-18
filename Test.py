# this is the global socpe of the variable
spam = 'global'
eggs = 'global'

# this is the local scope of the variable
def in_function():
    """any variables here will exist 
    only at the function level"""	

    global eggs

    spam = 'local'
    eggs = 'local'

    return spam + ' ' + eggs

print(in_function()) # Out[1]: local local

# the local scope does not change the global scope
print(spam, eggs) # Out[1]: global local