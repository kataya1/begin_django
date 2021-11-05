from django.shortcuts import redirect, render
from django.http import HttpResponse
from random import random


my_task_list = [
    {
        'index': 0,
        'id': 1,
        'name': 'Movie-1',
        'priority': 1,
        'description': "hello iam studying at iti sahdjka shkdj sahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    },
    {
        'index': 1,
        'id': 2,
        'name': 'Movie-2',
        'priority': 4,
        'description': "hello iam studying at iti sahdjka shkdj sahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    },
    {
        'index': 2,
        'id': 3,
        'name': 'Movie-3',
        'priority': 2,
        'description': "hello iam studying at iti sahdjka shkdj sahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    },
    {
        'index': 2,
        'id': 4,
        'name': 'Movie-3',
        'priority': 2,
        'description': "hello iam studying at iti sahdjka shkdj sahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    },
    {
        'index': 2,
        'id': 5,
        'name': 'Movie-5',
        'priority': 2,
        'description': "hello iam studying at iti sahdjka shkdj sahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    },
    {
        'index': 2,
        'id': 6,
        'name': 'Movie-3',
        'priority': 2,
        'description': "hello iam stsdfasffffffffadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    },
]

def _get_target_task(target_id):
    # Filter the list based on the task id sent and compare it toward each dictionary item in the list
    filter_result = filter(lambda d: d.get('id') == target_id, my_task_list)
    final_list = list(filter_result)
    # print(f"\n\n{final_list}\n\n")
    # Getting index of the required task from my_task_list
    if len(final_list) == 0:
        return -1
    else:
        index_of_task = my_task_list.index(final_list[0])
        return index_of_task

# Create your views here.
def index(request):
    if request.method == 'POST':
        p = request.POST
        new_task = {
            'index': len(my_task_list),
            'id': int(random()*10000),
            'name': p.get('task'),
            'priority': p.get('priority'),
            'description': p.get('description')
        }
        my_task_list.append(new_task)
        return redirect('tasks')
    return render(request, 'task_list.html', context={"my_task_list": my_task_list})


def tasks(request, **kwargs):
    print(f"taskid --> {kwargs.get('task_id')}")
    t = _get_target_task(kwargs.get('task_id'))
    if t == -1:
        return HttpResponse("404 man, there is no task with that id")

    if request.method == 'POST':
        p = request.POST
        if p.get('op') == 'DELETE':
            print('\n\n-------------\nit wonts to be deleted\n\n')
            my_task_list.pop(t)
            return redirect('index')

        elif p.get('op') == 'UPDATE':
            print('\n\n-------------\nit wonts to be updated\n\n')
            


    return render(request, 'task.html', context=my_task_list[t])

    # return render(request, 'task.html', context={
    #     'index': 2,
    #     'id': 3,
    #     'name': 'Movie-3',
    #     'priority': 2,
    #     'description': "hello iam studying at iti sahdjka shkdj sahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    # })

def form(request):
    if request.method == 'POST':
        pass
    return render(request, 'form.html')
    
