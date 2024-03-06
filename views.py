from django.http import HttpResponse
from django.shortcuts import render
from django import forms
import markdown2
# from markdown2 import Markdown
from . import util


class DjangoForm(forms.Form):
    name = forms.CharField(label="Your name in the Django form:", max_length=100)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def show_topic(request, topic):
    current_entry = util.get_entry(topic)
    if topic.lower in [name.lower() for name in util.list_entries()]:
        current_entry = util.get_entry(topic)
    if current_entry != None:
        md = markdown2.markdown(current_entry)
        # print(md)
        # markdowner = Markdown()
        # markdown_entry = markdowner.convert(current_entry)        
        # entry_md_neshto_si = markdown.markdown(current_entry)
        # entry_to_html = markdown.convert(current_entry)
        print(f"{request=}")
        return render(request, "encyclopedia/show_topic.html", {
        "title": topic, 
        "body": md
    })
    else: 
        # return HttpResponse("else si raboti")
        return not_found(request, topic)
        
        # return render(request, "encyclopedia/new_topic.html", {
        #     "title": "Not found",
        #     "topic": topic
        # })

def new_topic(request):
    dj_form = DjangoForm
    # print(dj_form)
    return render(request, "encyclopedia/new_topic.html", {
        "title": "Add new topic",
        "topic": "nesyshtestvusasht_topic",
        "form_from_Django": dj_form
    })

def not_found(request, topic):
    # return render(request, "encyclopedia/new_topic.html", {
    #     "title": "Not found",
    #     "topic": topic
    # })

    return HttpResponse(f"tuk e not found {request=}")
    # dj_form = DjangoForm
    # print(dj_form)
    # return render(request, "encyclopedia/not_found.html", {
    #     "title": "Add???",
    #     "topic": "nesyshtestvusasht_topic",
    #     "form_from_Django": dj_form
    # })

def random_topic(request):
    return HttpResponse("todo: Random page")

def search(request):
    return HttpResponse("todo: Search")


    

