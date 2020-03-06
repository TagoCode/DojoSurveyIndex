from django.shortcuts import render
def index(request):

    return render(request, "index.html")
def func(request):
    print("Got Post Info....................")
    print(request.POST)
    name_from_form = request.POST['first_name']
    description = request.POST['description']
    location_frm = request.POST['location']
    description = request.POST['description']
    language = request.POST['language']
    print(name_from_form)
    print(description)
    context = {
        "name_on_template" : name_from_form,
        "description" : description,
        "location_post" : location_frm,
        "language_post" : language
    }

    return render(request, "next.html", context)
