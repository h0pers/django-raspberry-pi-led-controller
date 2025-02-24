from django.shortcuts import render

# Create your views here.


def home_page(request, *args, **kwargs):
    context = {
        'led_range': range(64)
    }

    return render(request, template_name="sensehat/index.html", context=context)
