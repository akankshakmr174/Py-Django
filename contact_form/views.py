from django.http import Http404, HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>The time right now is %s!</body></html>" % now
    return HttpResponse(html)
    
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
    
# Import the render shortcut to render the templates in the response
from django.shortcuts import render

# Import the ContactForm class from the forms.py in the same module
from contact_form.forms import ContactForm
from django.core.mail import send_mail
# This function-based view handles the requests to the root URL /. See
# urls.py for the mapping.
def contact_form(request):
  # If the request method is POST, it means that the form has been submitted
  # and we need to validate it.
  if request.method == 'POST':
    # Create a ContactForm instance with the submitted data
    form = ContactForm(request.POST)
    
    # is_valid validates a form and returns True if it is valid and
    # False if it is invalid.
    if form.is_valid():
      # The form is valid and you could save it to a database
      # by creating a model object and populating the
      # data from the form object, but here we are just
      # rendering a success template page.
      cd = form.cleaned_data
      send_mail(cd['subject'],
                cd['message'],
                cd.get('email','noreply@example.com'),
                ['akankshakmr174@gmail.com'], fail_silently=False,
                )
      return render(request, 'contact_form/success.html')
  
  # This means that the request is a GET request. So we need to
  # create an instance of the ContactForm class and render it in
  # the template
  else:
    form = ContactForm()
  
  # Render the contact form template with a ContactForm instance. If the
  # form was submitted and the data found to be invalid, the template will
  # be rendered with the entered data and error messages. Otherwise an empty
  # form will be rendered. Check the comments in the contact_form.html template
  # to understand how this is done.
  return render(request, 'contact_form/contact_form.html', {'form':form})

    
    
        
