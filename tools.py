todo_list = []

def add_todo(item: str):
    todo_list.append(item)
    return f'Added "{item}" to your to-do list.'

# Accept arbitrary args even if unused
def list_todos(*args):
    if not todo_list:
        return "Your to-do list is empty."
    return "\n".join(f"{i+1}. {item}" for i, item in enumerate(todo_list))

def remove_todo(item: str):
    if item in todo_list:
        todo_list.remove(item)
        return f'Removed "{item}" from your to-do list.'
    return f'"{item}" not found in your to-do list.'
