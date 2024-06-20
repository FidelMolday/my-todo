from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem

def todo_list(request):
    items = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        text = request.POST['text']
        TodoItem.objects.create(text=text)
        return redirect('todo_list')
    else:
        return render(request, 'todo/add_item.html')

def toggle_complete(request, item_id):
    item = get_object_or_404(TodoItem, id=item_id)
    item.complete = not item.complete
    item.save()
    return redirect('todo_list')

def delete_item(request, item_id):
    item = get_object_or_404(TodoItem, id=item_id)
    item.delete()
    return redirect('todo_list')
