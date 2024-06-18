FilePath=r"C:\Users\joshu\OneDrive\Desktop\To Do Python\todos.txt"
# filepath is the parameter
def get_todos(filepath=FilePath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()

    return todos_local


# this function wont return anything,no value required from this function
def write(todos_arg, filepath=FilePath):
    with open(filepath, 'w') as file:
      file.writelines(todos_arg)
