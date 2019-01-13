from markdown import Markdown
from django.shortcuts import render
from .models import IndexPicture, Project, News
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage


def getSecondLasts(i):
    indexAllPictures = IndexPicture.objects.all()
    try:
        secondLasts = indexAllPictures.filter(pk=indexAllPictures.last().pk - i)
        if secondLasts:
            secondLast = secondLasts[0]
            return secondLast, i
        else:
            i = i + 1
            return getSecondLasts(i)
    except:
        i = i + 1
        return getSecondLasts(i)

def getThirdLasts(i):
    indexAllPictures = IndexPicture.objects.all()
    try:
        thirdLasts = indexAllPictures.filter(pk=indexAllPictures.last().pk - i)
        if thirdLasts:
            thirdLast = thirdLasts[0]
            return thirdLast
        else:
            i = i + 1
            return getThirdLasts(i)
    except:
        i = i + 1
        return getThirdLasts(i)

def index(request):
    indexAllPictures = IndexPicture.objects.all()
    context = {}
    Last = indexAllPictures.last()
    i = 1
    secondLast, i = getSecondLasts(i)
    thirdLast = getThirdLasts(i+1)

    context['Last'] = Last
    context['secondLast'] = secondLast
    context['thirdLast'] = thirdLast
    return render(request, 'init/index.html', context)


def services(request):
    allType = [{'nameEN': 'all', 'nameCN': '所有'},
               {'nameEN': 'OfficeBuilding', 'nameCN': '办公楼'},
               {'nameEN': 'EducationResearch', 'nameCN': '教育及研究'},
               {'nameEN': 'Residential', 'nameCN': '住宅'},
               {'nameEN': 'Infrastructure', 'nameCN': '基础设施'},
               ]
    category = request.GET.get('category', 'all')
    if not category == 'all':
        for aType in allType:
            if aType['nameEN'] == category:
                findType = aType['nameCN']
                break
        allProject = Project.objects.filter(projectType=findType)
    else:
        allProject = Project.objects.all()
    paginator = Paginator(allProject, 6)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        projectList = paginator.page(page)
    except PageNotAnInteger:
        projectList = paginator.page(1)
    except EmptyPage:
        projectList = paginator.page(paginator.num_pages)

    context = {}
    context['category'] = category
    context['allType'] = allType
    context['projectList'] = projectList
    context['paginator'] = paginator
    context['currentPage'] = currentPage
    context['allProject'] = allProject
    return render(request, 'init/services.html', context)


def test1(request):
    return render(request, 'init/test1.html')


def detail(request, id):
    finds = Project.objects.filter(id=id)
    if finds:
        find = finds[0]
    else:
        find = None

    markdowner = Markdown()
    find.content = markdowner.convert(find.content)

    context = {}
    context['find'] = find
    return render(request, 'init/detail.html', context)


def contact(request):
    return render(request, 'init/contact.html')


def about(request):
    return render(request, 'init/about.html')


def news(request):
    context = {}
    news = News.objects.order_by('-time')
    paginator = Paginator(news, 6)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        news_list = paginator.page(page)
    except PageNotAnInteger:
        news_list = paginator.page(1)
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)
    context['news_list'] = news_list
    print(news_list)
    return render(request, 'web/news.html', context)


def news_detail(request, id):
    finds = News.objects.filter(id=id)
    if finds:
        find = finds[0]
    else:
        find = None

    markdowner = Markdown()
    find.content = markdowner.convert(find.content)

    context = {}
    context['find'] = find
    return render(request, 'web/news_detail.html', context)
