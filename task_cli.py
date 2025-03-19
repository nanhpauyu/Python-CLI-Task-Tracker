import sys
import json
import os

TASK_FILE = 'tasks.json'


def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as task_file:
            return json.load(task_file)
    return []


def save_tasks(tasks):
    with open(TASK_FILE, 'w') as task_file:
        json.dump(tasks, task_file, indent=4)


def add_task(task_desc):
    tasks = load_tasks()
    task_id = 1 if len(tasks) == 0 else tasks[-1]['id'] + 1
    new_task = {
        'id': task_id,
        'description': task_desc,
        'status': 'todo',
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f'Task added successfully (ID: {task_id})')


def update_task(task_id, task_desc):
    tasks = load_tasks()
    task = get_task_by_id(tasks=tasks, task_id=task_id)
    if task:
        old_desc = task['description']
        task['description'] = task_desc
        save_tasks(tasks)
        print(
            f'Task id = {task_id} has updated description from {old_desc} to {task['description']}')
    else:
        print(f'No task of ID {task_id} and fail to update task')


def delete_task(task_id):
    tasks = load_tasks()
    task = get_task_by_id(tasks=tasks,task_id=task_id)
    if task:
        tasks.remove(task)
        save_tasks(tasks)
        print(f'Task ID {task_id} was deleted successfully ')
    else:
        print(f'No task of ID {task_id} and fail to delete task')
    


def update_status(task_id, status):
    tasks = load_tasks()
    task = get_task_by_id(tasks=tasks, task_id=task_id)
    if task:
        task['status'] = status
        save_tasks(tasks)
        print('Status Updated')
    else:
        print('Error updating status')


def get_task_by_id(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None


def list_task(task_status='all'):
    tasks = load_tasks()
    if task_status == 'all':
        print_tasks(tasks)
    else:
        current_task = []
        for task in tasks:
            if task['status'] == task_status:
                current_task.append(task)
        print_tasks(current_task)


def print_tasks(tasks):
    if len(tasks) > 0:
        for task in tasks:
            print(
                f'Id - {task['id']} : {task['description']} , status is {task['status']}')
    else:
        print('No task')


def main():
    argv = sys.argv
    if len(argv) < 2:
        print('''Example Commands
python task_cli.py add "Buy groceries"
python task_cli.py update 1 "Buy groceries and cook dinner"
python task_cli.py delete 1
python task_cli.py mark-in-progress 1
python task_cli.py mark-done 1
python task_cli.py list
python task_cli.py list done
python task_cli.py list todo
python task_cli.py list in-progress''')
    else:
        command = argv[1]
        if command == 'add':
            task_desc = ''.join(argv[2:])
            add_task(task_desc=task_desc)
        elif command == 'update':
            task_id = argv[2]
            task_desc = argv[3]
            update_task(task_id=int(task_id), task_desc=task_desc)
        elif command == 'delete':
            task_id = argv[2]
            delete_task(task_id=int(task_id))
        elif command == 'list':
            if len(argv) == 2:
                list_task()
            else:
                task_status = argv[2]
                list_task(task_status=task_status)
        elif command.startswith('m'):
            task_id = argv[2]
            status = command[command.find('-')+1:]
            update_status(task_id=int(task_id), status=status)


if __name__ == '__main__':
    main()
