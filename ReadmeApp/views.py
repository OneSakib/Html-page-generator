from django.shortcuts import render
from django.views.generic import TemplateView, View


# Create your views here.
class Index(TemplateView):
    template_name = 'Readme/index.html'


class HTMLGenerator(View):
    def post(self, request):
        data = request.POST.get('data')
        context = {
            'data': data
        }
        return render(request, 'Readme/htmlpage.html', context)
