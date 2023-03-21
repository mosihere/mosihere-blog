from django.shortcuts import render



def resumeview(request):
    return render(request, 'resume/resume.html')
