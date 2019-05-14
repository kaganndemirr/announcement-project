# Django
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView
from django.views.static import serve


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context.update({
            'domain_documentation': '/documentation/',
        })

        return context


class DocumentationView(View):
    def get(self, request, path='index.html', **kwargs):
        return serve(
            request, path, document_root=settings.DOCUMENTATION_ROOT, **kwargs
        )


class MainView(LoginRequiredMixin, TemplateView):
    login_url = settings.LOGIN_URL
    template_name = 'main.html'



