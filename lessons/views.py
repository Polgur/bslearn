from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Book

# Create your views here.
class IndexPage(ListView):
    #model = Book
    queryset = Book.objects.all().prefetch_related("lessons")

class LessonPage(TemplateView):

    def get_template_names(self):
        return ['{}/{}.html'.format(self.kwargs['book'],self.kwargs['template'])]
    #def get_context_data(self, **kwargs):
     #   ctx = super().get_context_data(**kwargs)
      #  ctx['template_name'] = kwargs.get('numb')
       # return ctx