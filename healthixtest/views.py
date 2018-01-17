from django.shortcuts import render
from django.http import HttpResponse
from .models import Laboratory_Test
from django.template import loader
from .forms import LaboratoryTestForm


def index(request):
    """this function provides the landing page and provides links
     to all the links partinate to a specific use-case depending
     on the person currently logged in
    """
    template = loader.get_template('healthixtest/index.html')
    return HttpResponse(template.render(request))


def view_tests(request):
    """this returns a list of tests. this is especially for the doctors
    though it can be refined to  work for the lab tecs too. the actual
    presentation is handled in the template for this """
    all_tests = Laboratory_Test.objects.order_by('-date_requested')
    template = loader.get_template('healthixtest/view_tests_template.html')
    context = {'all_tests': all_tests, }
    output = '\n '.join(q.result for q in all_tests)
    return HttpResponse(template.render(context, request))


def request_test(request):
    if request.method == "Post":
        form = LaboratoryTestForm(request.POST)
        if form.is_valid():
            #include action here
            return HttpResponse("<p>Thank you</p>")
    else:
        form = LaboratoryTestForm()
    return render(request, 'request_test.html', form)
