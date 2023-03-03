from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'connectes/index.html')

def documentation(request):
    return render(request, 'connectes/documentation/documentation.html')

def chartjs(request):
    return render(request, 'connectes/pages/charts/chartjs.html')

def basic_elements(request):
    return render(request, 'connectes/pages/forms/basic_elements.html')

def mdi(request):
    return render(request, 'connectes/pages/icons/mdi.html')

def blank_page(request):
    return render(request, 'connectes/pages/samples/blank-page.html')

def error_404s(request):
    return render(request, 'connectes/pages/samples/error-404.html')

def error_500s(request):
    return render(request, 'connectes/pages/samples/error-500.html')

def login(request):
    return render(request, 'connectes/pages/samples/login.html')

def register(request):
    return render(request, 'connectes/pages/samples/register.html')

def basic_table(request):
    return render(request, 'connectes/pages/tables/basic-table.html')

def buttons(request):
    return render(request, 'connectes/pages/ui-features/buttons.html')

def dropdowns(request):
    return render(request, 'connectes/pages/ui-features/dropdowns.html')

def typography(request):
    return render(request, 'connectes/pages/ui-features/typography.html')