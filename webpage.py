
import streamlit as st
import functions as ys

todos = ys.get()


def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    ys.write_todos(todos)


st.title("My to-do App")
st.subheader("This Is My Todo App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        ys.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a Todo", placeholder="Add a todo..", on_change=add_todo, key='new_todo')
