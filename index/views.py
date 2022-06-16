from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Project, Summary, Experience, Language, Library, Software, Education, Extracurricular, Category

# Create your views here.
def index(request):
    #get entries from database
    summary_list = Summary.objects.all()
    education_list = Education.objects.all()
    exp_list = Experience.objects.all()
    ext_list = Extracurricular.objects.all().order_by('-time')
    project_list = Project.objects.all()
    lang_list = Language.objects.all().order_by('-profession')
    lib_list = Library.objects.all().order_by('-profession')
    soft_list = Software.objects.all().order_by('-profession')
    cat_list = Category.objects.all()
    
    #load template file
    template = loader.get_template('iPortfolio/index.html')
    
    #data to be injected into the template
    context = {
        'summary_list' : summary_list,
        'education_list' : education_list,
        'exp_list' : exp_list,
        'ext_list' : ext_list,
        'project_list' : project_list,
        'lang_list' : lang_list,
        'lib_list' : lib_list,
        'soft_list' : soft_list,
        'cat_list' : cat_list,
    }

    
    return HttpResponse(template.render(context, request))

def detail(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project is not in database")
    
    template = loader.get_template('iPortfolio/portfolio-details.html')
    
    return HttpResponse(template.render({'project': project}, request))
    #return render(request, template, {'project': project})

