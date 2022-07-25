from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from rake_nltk import Rake
import nltk
import collections
import difflib
from .models import Tag,Advert

#nltk.download('stopwords')
#nltk.download('punkt')

# Create your views here.

def index(request):
    if request.method=='POST':
        url=request.POST.get('url')
        response=requests.get(url=url)
        soup=BeautifulSoup(response.content,'html.parser')
        all_text=''
        for para in soup.find_all('p'):
            all_text+=str(para.get_text())
        #print(all_text)
        rake_var=Rake()
        rake_var.extract_keywords_from_text(all_text)
        keywords_extracted=rake_var.get_ranked_phrases()
        #print(keywords_extracted)
        adtag=[]
        tags=Tag.objects.all()
        for tag in tags:
            adtag.append(tag.tagname)
        seta=set(keywords_extracted)
        setb=set(adtag)
        # we have to find commomn words and extract it
        commonWords=[]
        if (seta & setb):
            commonWords=list(seta & setb)
        #print(commonWords)

        # we need to find relevent ad
        releventAd=[]
        for advert in Advert.objects.all():
            for tag in advert.tags.all():
                if tag.tagname in commonWords:
                    releventAd.append(advert)
                    #to remove duplicates of same add
                    releventAd=set(releventAd)
                    releventAd=list(releventAd)
        #print(releventAd)
        context={
            'releventAd':releventAd,
            'commonWords':commonWords
        }
        return render(request,'myapp/index.html',context)



    return render(request,'myapp/index.html')