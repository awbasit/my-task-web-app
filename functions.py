FILEPATH= "list.txt"

def get_tasks(filepath=FILEPATH):
    with open(filepath, 'r') as get_file_local:
        tasks_local = get_file_local.readlines()
    return tasks_local


def write_tasks(tasks_args, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(tasks_args)