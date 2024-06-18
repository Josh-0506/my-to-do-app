FilePath = r"C:\Users\joshu\OneDrive\Desktop\Web_app1\todos.txt"


# filepath is the parameter
def get_todos(filepath: object = FilePath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()

    return todos_local


# this function won't return anything,no value required from this function
def write_todos(todos_arg, filepath=FilePath):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
