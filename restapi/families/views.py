from django.shortcuts import render

from families.models import Familia, Persona
from families.forms import FamiliaForm, PersonaForm


def index(request):

    families = Familia.objects.all()

    return render(
        request,
        'families/index.html',
        {
            'families': families
        }
    )


def family_detail(request, family_id):

    family = Familia.objects.get(pk=family_id)

    return render(
        request,
        'families/detail.html',
        {
            'family': family
        }
    )


def new_family(request):
    message = ''
    if request.method == 'GET':
        familia_form = FamiliaForm()

    elif request.method == 'POST':
        familia_form = FamiliaForm(request.POST)
        message = "Familia exitosamente guardada"
        if familia_form.is_valid():
            familia_form.save()
            familia_form = FamiliaForm()

    else:
        pass

    return render(
        request,
        'families/new_family.html',
        {
            'familia_form': familia_form,
            'message': message
        }
    )


def list_people(request):
    people = Persona.objects.all()

    return render(
        request,
        'families/list_people.html',
        {
            'people': people
        }
    )


def new_person(request):
    message = ''
    if request.method == 'GET':
        person_form = PersonaForm()

    elif request.method == 'POST':
        person_form = PersonaForm(request.POST)
        message = "Persona exitosamente guardada"
        if person_form.is_valid():
            person_form.save()
            person_form = PersonaForm()

    else:
        pass

    return render(
        request,
        'families/new_person.html',
        {
            'person_form': person_form,
            'message': message
        }
    )


def edit_person(request, persona_id):
    persona = Persona.objects.get(pk=persona_id)
    message = ''
    if request.method == 'GET':
        person_form = PersonaForm(initial=persona)

    elif request.method == 'POST':
        person_form = PersonaForm(request.POST)
        message = "Persona exitosamente guardada"
        if person_form.is_valid():
            person_form.save()
            person_form = PersonaForm()

    else:
        pass

    return render(
        request,
        'families/edit_person.html',
        {
            'person_form': person_form,
            'message': message
        }
    )
