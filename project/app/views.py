from django.shortcuts import render,HttpResponse

# Create your views here.
def new(request):
    print("fourth changing happening")
    # print('.........................................')
    return HttpResponse("hai")