from django.shortcuts import render
from .models import IndexPicture, Project, News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from markdown import Markdown

# Create your views here.

def index(request):
    return render(request, 'init/index.html')

def about(request):
    return render(request, 'init/about.html')


def news(request):
    context = {}
    news = News.objects.order_by('-time')
    page_items = 2
    page_robot = Paginator(news, page_items)
    page = request.GET.get('page') 
    news_list = page_robot.get_page(page)
    context['news_list'] = news_list
    print(news_list)
    return render(request, 'web/news.html', context)




def news_detail(request, id):
    print(News.objects.all())
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


def services(request):
    return render(request, 'web/news2.html')

    # allType = [{'nameEN': 'all', 'nameCN': '所有'},
    #            {'nameEN': 'OfficeBuilding', 'nameCN': '办公楼'},
    #            {'nameEN': 'EducationResearch', 'nameCN': '教育及研究'},
    #            {'nameEN': 'Residential', 'nameCN': '住宅'},
    #            {'nameEN': 'Infrastructure', 'nameCN': '基础设施'},
    #            ]
    # category = request.GET.get('category', 'all')
    # if not category == 'all':
    #     for aType in allType:
    #         if aType['nameEN'] == category:
    #             findType = aType['nameCN']
    #             break
    #     allProject = Project.objects.filter(projectType=findType)
    # else:
    #     allProject = Project.objects.all()
    # paginator = Paginator(allProject, 6)
    # page = request.GET.get('page', 1)
    # currentPage = int(page)
    # try:
    #     projectList = paginator.page(page)
    # except PageNotAnInteger:
    #     projectList = paginator.page(1)
    # except EmptyPage:
    #     projectList = paginator.page(paginator.num_pages)
    #
    # projectFilter = """
    #     <ul class="filter">
    #         <li><a class="active" href="#" data-filter="*">所有</a></li>
    #         <li><a href="{% url 'web:services' 'OfficeBuilding' %}" data-filter=".web">办公楼</a></li>
    #         <li><a href="{% url 'web:services' 'EducationResearch' %}" data-filter=".graphic">教育及研究</a></li>
    #         <li><a href="{% url 'web:services' 'Residential' %}" data-filter=".photo">住宅</a></li>
    #         <li><a href="{% url 'web:services' 'Infrastructure' %}" data-filter=".motion">基础设施</a></li>
    #     </ul>
    # """
    # # pageStr = mark_safe(projectFilter)
    #
    #
    #
    #
    # context = {}
    # context['category'] = category
    # context['allType'] = allType
    # context['pageStr'] = pageStr
    # context['projectList'] = projectList
    # context['paginator'] = paginator
    # context['currentPage'] = currentPage
    # context['allProject'] = allProject
    # return render(request, 'init/services.html', context)