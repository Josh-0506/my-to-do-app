FilePath = r"C:\Users\joshu\OneDrive\Desktop\Web_app1\todos.txt"


# filepath is the parameter
def get_todos(FilePath):
    with open(FilePath, 'r') as file:
        todos_local = file.readlines()

    return todos_local


# this function won't return anything,no value required from this function
def write_todos(todos_arg, filepath=FilePath):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
