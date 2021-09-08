from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'home.html')
def reverse(request):
    text_user=request.GET['comment']
    words=text_user.split()
    number=len(words)
    reversed=text_user[::-1]
    return render(request,'reverse.html',{'comment':text_user,'reversedtext':reversed,'number':number,})