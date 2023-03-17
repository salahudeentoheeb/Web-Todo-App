import streamlit as st
import functions as f

todos = f.read_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    f.write_todos(todos)


st.title("My To-do App")
st.subheader("A very easy to use To-do App")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        f.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="", placeholder="Enter a new to-do here... ",
              on_change=add_todo, key="new_todo")


#st.session_state #This helps us to see the actions of state behind the scene on the webpage
