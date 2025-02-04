import random
from django.shortcuts import render
from . import utill
from markdown2 import Markdown
# Create your views here.


def convert_md_to_html(title):
    content = utill.get_entry(title)
    markdown = Markdown()
    if content == None:
        return None
    else:
        return markdown.convert(content)







def index(request):

    return render(request, 'encyclopedia/index.html',{
        'entries': utill.list_entries()
        
    })


def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content == None:
        return render(request, 'encyclopedia/eror.html', {
            'massage': 'Page not Fount Error, This entry does not exist!!'
        })
    else:
        return render(request, 'encyclopedia/entry.html',{
            'title': title,
            'content': html_content
        })
    

def search(request):
    if request.method == 'POST':
        entry_search = request.POST['q']
        html_content = convert_md_to_html(entry_search)
        if html_content is not None:
            return render(request, 'encyclopedia/entry.html',{
                'title': entry_search,
                'content': html_content
            })
        else:
            all_entries = utill.list_entries()
            recomm = []
            for entry in all_entries:
                if entry_search.lower() in entry.lower():
                    recomm.append(entry)
            return render(request, 'encyclopedia/search.html', {
                "recomm": recomm,
                'se': entry_search
            })


def new_page(request):
    if request.method == 'GET':
        return render(request, 'encyclopedia/new.html')
    else:
        title = request.POST['title']
        content = request.POST['content']
        titlee = utill.get_entry(title)
        if titlee is not None:
            return render(request, 'encyclopedia/eror.html', {
                'massage' : 'Entry Page Already exits'
            })
        else:
            utill.save_entry(title, content)
            html_content = convert_md_to_html(title)
            return render(request, 'encyclopedia/entry.html', {
                'title': title,
                'content': html_content
            })


def edit(request):
    if request.method == "POST":
        title = request.POST['title']
        contect = utill.get_entry(title)
        return render(request, 'encyclopedia/edit.html', {
            'title':title,
            'contect':contect
        })
    

def save_edit(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        utill.save_entry(title, content)
        html_content = convert_md_to_html(title)
        return render(request, 'encyclopedia/entry.html', {
            'title': title,
            'content': html_content
        })
        


def rand(request):
    all = utill.list_entries()
    rand_entry = random.choice(all)
    html_content = convert_md_to_html(rand_entry)
    return render(request, 'encyclopedia/entry.html', {
        'title': rand_entry,
        'content': html_content
    })
