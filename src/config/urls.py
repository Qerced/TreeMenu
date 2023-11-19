from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(
        url=reverse_lazy('menu:index', args=('main_menu',))
    )),
    path('menu/', include('menu.urls', namespace='app'))
]
