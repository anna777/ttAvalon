from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.views.generic import CreateView
from django.core.context_processors import csrf
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field
from crispy_forms.bootstrap import FormActions
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Event
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
class EventForm(ModelForm):
    class Meta:
        model = Event
    def __init__(self, *args, **kwargs):

        super(EventForm, self).__init__(*args, **kwargs)
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
        self.helper.layout[-1] = FormActions(
        Submit('add_button', 'Submit',css_class="btn btn-primary"),
        Submit('cancel_button', 'Cancel', css_class="btn btn-link"),
          )
class EventCreateView(CreateView):
    model = Event
    template_name = "event_add.html"
    form_class = EventForm
    #@method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventCreateView, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        return HttpResponseRedirect('/start_page/')

    def post(self, request, *args, **kwargs):
        if 'cancel_button' in request.POST:
            return HttpResponseRedirect('/start_page/')
        else:
            return super(EventCreateView, self).post(request, *args, **kwargs)
def start_page(request):
    pass
