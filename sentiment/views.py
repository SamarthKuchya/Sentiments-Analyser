from django.http import HttpResponse
from django.shortcuts import render
import api

def home(request):
    return render(request, "index.html")

def post(request):
    try:
        content=request.GET['sentence']
        print(len(content))
        if (len(content))==0:
            return render(request,"index.html",{'sentiment':'enter something'})
        
        sentiment=api.predict(content)
        
        content={'content':content,'sentiment':sentiment[0],'url' :sentiment[1]}    
        return render(request, "index.html",{'im':content['url'],'text':content['content'],'sentiment':content['sentiment'],'Sentiment_Result':'Sentiment Result'})
    except:
        return render(request, "index.html")
    # img_url={'url' : "{%static 'img/positive.png' %}"}   
    # render(request, "index.html",{'text':content['content'],'sentiment':content['sentiment'],'Sentiment_Result':'Sentiment Result','image':img_url['url']})
