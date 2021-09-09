from django.shortcuts import render

# Create Home-Page-View
def HomePage(request):
    return render(request,'Home-Page.html',context={})