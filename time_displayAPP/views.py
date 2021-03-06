from django.shortcuts import HttpResponse, render #, redirect
from time import gmtime, strftime

def index(request):
    context = {
        'fullDate' : strftime('%B %d, %Y', gmtime()),
        'time' : strftime('%I:%M %p', gmtime())
        }
    # x = context['fullDate']
    # y = context['time']
    # return HttpResponse(f'Date: {x} Time: {y}')
    return render(request, 'index.html', context)

# Example from couse materials in the next section on GET/POST
# def some_function(request):
#     if request.method == "GET":
#         print("a GET request is being made to this route")
#         return render(request, "index.html")
#     if request.method == "POST":
#         print("a POST request is being made to this route")
#         return redirect('/')