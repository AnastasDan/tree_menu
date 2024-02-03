from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Класс представления для отображения главной страницы."""

    template_name = "app_menu/index.html"
