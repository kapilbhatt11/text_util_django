from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    # return HttpResponse("WelCome To Home..!")

def analyze(request):
    # get the text
    djtext = request.POST.get("text","default")
    remove = request.POST.get("remove","off")
    uppercase = request.POST.get("uppercase","off")
    newlineremover = request.POST.get("newlineremover","off")
    extra_space_remover = request.POST.get("extra_space_remover","off")
    charcount = request.POST.get("charcount","off")
    if remove=='on':   
        analyzed = ""
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punc:
                analyzed = analyzed+char 
        params = {'purpose':"Remove text",'analyze_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
        
    if uppercase =='on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':"Change to upper",'analyze_text':analyzed}
        djtext = analyzed

        # return render(request,'analyze.html',params)
    
    if newlineremover =='on':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char!='\r':
                analyzed = analyzed + char
        params = {'purpose':"Remove New Lines",'analyze_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    
    if extra_space_remover =='on':
        analyzed = ' '
        for index,char in enumerate(djtext):
            if djtext[index]==' ' and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose':"Remove New Lines",'analyze_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    
    if charcount =='on':
        count = 0
        for char in djtext:
            count+=1
        params = {'purpose':"character counter",'analyze_text':count}
        # return render(request,'analyze.html',params)
    
    if remove!='on' and uppercase !='on'and newlineremover !='on' and extra_space_remover !='on' and charcount !='on':
        return render(request,"error.html")

    return render(request,'analyze.html',params)
 