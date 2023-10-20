def if_else_lambda(boolean, true_block, false_block):
    """
    Define a function that can dynamically imitate an if-else statement
    :boolean bool: parameter boolean to determine which block to go into
    :true_block lambda:
    :false_block lambda:
    :return: void
    """
    if boolean:
        true_block()
    else:
        false_block()
    #lambda: true_block if boolean else false_block



def if_lambda(boolean, true_block):
    """
    Dynamically imitate an if statement based on the value of 'boolean'.

    :param boolean: A boolean value that determines whether to execute 'true_block'.
    :param true_block: A function representing the code to execute if 'boolean' is True.
    :return: None
    """
    if boolean:
        true_block()

# Example usage:
if_lambda(True, lambda: print("hi"))

