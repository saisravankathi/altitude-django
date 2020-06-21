from django.shortcuts import render, redirect
from .models import Story, Publisher, Content
# Create your views here.



def home_page(request):
    # Here should filter by publish date to show only the Articles for today, a load more button, which will be having a collection.
    # we can add lazy loading as well based on the number of Articles daily published
    stories = Story.objects.all()
    context = {"stories": stories}
    return render(request, 'magazine/index.html', context)
def story_detail(request, story_id):
    story = Story.objects.filter(story_id=story_id)[0]
    context = {"story": story}
    return render(request, 'magazine/detailstory.html', context)

def create_story_page(request):
    return render(request, 'magazine/create.html')

def create_story(request):
    data = request.POST
    p = Publisher.objects.filter(email="email@email.com")[0]
    # context = {"story_id": }
    try:
        s = Story(publisher=p, story_id=data['story_id'], title=data['title'], image_url=data['url'])
        s.save()
        # stories = Story.objects.all()
        # context = {"stories": stories}
        response = redirect('/create-content')
        return response
    except Exception as e:
        print(e)
        return render(request, 'magazine/create.html')

def create_content_page(request):
    stories = Story.objects.all()
    context = {"stories": stories}
    return render(request, 'magazine/createcontent.html', context)

def create_content(request):
    data = request.POST
    print(data)
    s = Story.objects.filter(story_id=data['story'])[0]
    print(s)
    try:
        c = Content(story=s, content=data['content'])
        c.save()
        print('content has been saved')
    except Exception as e:
        print(e)
    print('redirecting to home page')
    resp = redirect('/home')
    return resp