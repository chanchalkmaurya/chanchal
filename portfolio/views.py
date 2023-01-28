from django.shortcuts import render, redirect
from django.http import HttpResponse
from portfolio.models import send_a_query, newsletteremail, project_details
from portfolio.forms import SendQueryForm, NewsLetterForm
from django.contrib import messages
from django.core.paginator import Paginator



# List of views
def homepage(request):
    context = {
    'name': 'Welcome Home!',
    'current_page': ''
    }
    return render(request, 'index.html', context)


def contact(request):
    if request.method =="POST":
        if 'sendquerysubmit' in request.POST:
            form = SendQueryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, ("Query sent successfully."))
            return redirect("contact")
        
    else:
        # import all the queries from database model - contact_details
        all_queries = send_a_query.objects.all().reverse()
        paginator = Paginator(all_queries, 5) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        all_queries = paginator.get_page(page_number)
        
        context = {
            'name': 'Welcome to Contact Page',
            'all_queries': all_queries,
            'current_page': 'Contact'
        }
        return render(request, 'contact.html', context)


def projects(request):
    all_projects = project_details.objects.all()
    paginator = Paginator(all_projects, 3) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    all_projects = paginator.get_page(page_number)
    context = {
    'name': 'Project Details',
    'current_page': 'Projects',
    'all_projects': all_projects
    }
    return render(request, 'projects.html', context)

def gallery(request):
    context = {
    'name': 'Welcome to Gallery Page',
    'current_page': 'Gallery'
    }
    return render(request, 'gallery.html', context)

