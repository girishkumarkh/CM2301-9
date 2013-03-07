from django.shortcuts import render, redirect
from django.http import HttpResponse
from learn.forms import TestForm
from learn.models import *
from uuidfield import UUIDField
from django.contrib.auth.decorators import login_required
from datetime import datetime


@login_required
def test(request, test_id):
    values = {}
    values['test'] = Test.objects.get(pk=test_id)
    values['lectures'] = values['test'].lecture.module.lecture_set.all()
    values['questions'] = values['test'].get_random_questions()
    values['testform'] = TestForm()
    values['testform'].initialise(questions=values['questions'])

    values['breadcrumb'] = ("LCARS", "%s (%s)"%(values['test'].title,values['test'].description))

    if request.method == 'POST':
        form = TestForm(request.POST)

        test_instance = TestInstance()
        test_instance.student = request.user
        test_instance.test =  values['test']
        test_instance.save()

        if form.is_valid():
            for question in values['questions']:
                result = Result()
                result.test_instance = test_instance
                result.question = Question.objects.get(pk=question.id)
                result.answer = Answer.objects.get(pk=form.data[str(question.id)])
                result.save()
                test_instance.time_completed = datetime.now()
                return redirect(test_instance.get_absolute_url())


    return render(request, 'test.html', values)

@login_required
def test_results(request, test_instance_id):
    return HttpResponse("poo")