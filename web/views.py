from markdown import Markdown
from django.shortcuts import render
from .models import IndexPicture, Project
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage


def index(request):
    indexAllPictures = IndexPicture.objects.all()
    context = {}
    Last = indexAllPictures.last()
    secondLasts = indexAllPictures.filter(pk=indexAllPictures.last().pk - 1)
    if secondLasts:
        secondLast = secondLasts[0]
    thirdLasts = indexAllPictures.filter(pk=indexAllPictures.last().pk - 2)
    if thirdLasts:
        thirdLast = thirdLasts[0]
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

