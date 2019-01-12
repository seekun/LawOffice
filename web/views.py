from markdown import Markdown
from django.shortcuts import render
from .models import IndexPicture, Project
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.utils.safestring import mark_safe


def index(request):
    indexAllPictures = IndexPicture.objects.all()
    context = {}
    Last = indexAllPictures.last()
    secondLasts = indexAllPictures.filter(pk=indexAllPictures.last().pk - 1)
    if secondLasts:
        secondLast = secondLasts[0]
    thirdLasts = indexAllPictures.filter(pk=indexAllPictures.last().pk - 1)
    if thirdLasts:
        thirdLast = thirdLasts[0]
    context['Last'] = Last
    context['secondLasts'] = secondLast
    context['thirdLasts'] = thirdLast
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

    projectFilter = """
        <ul class="filter">
            <li><a class="active" href="#" data-filter="*">所有</a></li>
            <li><a href="{% url 'web:services' 'OfficeBuilding' %}" data-filter=".web">办公楼</a></li>
            <li><a href="{% url 'web:services' 'EducationResearch' %}" data-filter=".graphic">教育及研究</a></li>
            <li><a href="{% url 'web:services' 'Residential' %}" data-filter=".photo">住宅</a></li>
            <li><a href="{% url 'web:services' 'Infrastructure' %}" data-filter=".motion">基础设施</a></li>
        </ul>
    """
    pageStr = mark_safe(projectFilter)




    context = {}
    context['category'] = category
    context['allType'] = allType
    context['pageStr'] = pageStr
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

#
# def servicesOther(request, displayProject, page):
#     allType = [{'nameEN': 'all', 'nameCN': '所有'},
#                {'nameEN': 'OfficeBuilding', 'nameCN': '办公楼'},
#                {'nameEN': 'EducationResearch', 'nameCN': '教育及研究'},
#                {'nameEN': 'Residential', 'nameCN': '住宅'},
#                {'nameEN': 'Infrastructure', 'nameCN': '基础设施'},
#                ]
#     allProject = Project.objects.all()
#     paginator = Paginator(allProject, 9)
#     # page = request.GET.get('page', 1)
#     page = '1'
#     currentPage = int(page)
#     try:
#         projectList = paginator.page(page)
#     except PageNotAnInteger:
#         projectList = paginator.page(1)
#     except EmptyPage:
#         projectList = paginator.page(paginator.num_pages)
#
#     # projectFilter = """
#     #         <ul class="filter">
#     #             <li><a class="active" href="#" data-filter="*">所有</a></li>
#     #             <li><a href="{% url 'web:services' 'OfficeBuilding' %}" data-filter=".web">办公楼</a></li>
#     #             <li><a href="{% url 'web:services' 'EducationResearch' %}" data-filter=".graphic">教育及研究</a></li>
#     #             <li><a href="{% url 'web:services' 'Residential' %}" data-filter=".photo">住宅</a></li>
#     #             <li><a href="{% url 'web:services' 'Infrastructure' %}" data-filter=".motion">基础设施</a></li>
#     #         </ul>
#     #     """
#     # pageStr = mark_safe(projectFilter)
#     # displayProject = 'all'
#     # displayProject = request.GET.get('projectType', 'all')
#     print(type)
#     print(page)
#     # print(projectType)
#
#     context = {}
#     context['type'] = type
#     context['allType'] = allType
#
#     context['projectList'] = projectList
#     context['paginator'] = paginator
#     context['currentPage'] = currentPage
#     context['allProject'] = allProject
#     return render(request, 'init/services.html', context)