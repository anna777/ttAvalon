from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth import authenticate, login

from django.contrib import auth
from django.views.generic import CreateView
from django.core.context_processors import csrf
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field, Layout, HTML
from crispy_forms.bootstrap import FormActions
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Event, EventMember
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username,password)
        user.save()
        return HttpResponseRedirect('/home/')
    return render(request, "login.html", {})
def logout(request):
    return HttpResponseRedirect('/start_page/')

class EventForm(forms.ModelForm):
    class Meta:
        model = Event

    def __init__(self, *args, **kwargs):


        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['user_id'].widget = forms.HiddenInput()
        #self.fields['members'].widget = forms.HiddenInput()
        self.helper = FormHelper(self)
        # set form tag attributes
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

            # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

            # add buttons
        self.helper.layout.append(FormActions(
        Submit('add_button', 'Submit',css_class="btn btn-primary"),
        HTML("""<a role="button" class="btn btn-default"
                        href="{% url "start_page" %}">Cancel</a>""")

          ))

class EventCreateView(CreateView):
    model = Event
    template_name = "event_add.html"
    form_class = EventForm



def start_page(request):
    list_event = Event.objects.all()
    return render(request, 'events_list.html',
{'events': list_event})

def appointment_page(request,pk):
    choosed_event = Event.objects.get(pk=pk)

    return render(request, 'appointment_page.html',
{'choosed_event': choosed_event})

def event_member_add(request):
    if request.method == "POST":
        errors = {}
        data = {}
        fullname = request.POST.get('fullname', '').strip()
        if not fullname:
            print("dfdfdf")
            errors['fullname'] = "Name is required"
        else:
            data['fullname'] = fullname
            print('111111')
        email = request.POST.get('email', '').strip()
        if not email:
            errors['email'] = "Email is required"
        else:
            data['email'] = email
            print('2222')

        choosed_date = request.POST.get('choosed_date', '').strip()
        if not choosed_date:
            errors['choosed_date'] = "Date is required"
        else:
            from datetime import datetime
            received_datetime_repr = choosed_date
            received_datetime = datetime.strptime(received_datetime_repr, '%Y-%m-%d')
            my_date_obj = received_datetime.date()
            data['choosed_date'] = my_date_obj

        choosed_time = request.POST.get('choosed_time', '').strip()
        if not choosed_time:
            errors['choosed_time'] = "Time is required"
        else:
            data['choosed_time'] = choosed_time
            print("4444")

        if not errors:
            print('dfdfdf')
            event_member = EventMember(**data)
            event_member.save()
            return render(request, 'start_page.html',
                    {})
        else:
            return render(request, 'appointment_page.html',
                    {})
