"""dj_favorite_wrap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponse
from django.urls import path
from django.conf import settings
from admin_favorite import models

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_district(request):
    table = f"""<table class="tableclass">
        <caption style="background-color:#11ba8a" >
          <div  title="Favorite apps used frequently">{settings.ADMIN_FAVORITE}</div>
        </caption>"""
    # <caption>
    #   <a href="/{settings.ADMIN_PATH}/admin_favorite/" class="section" title="Models in the lol application">{settings.ADMIN_FAVORITE}</a>
    # </caption>"""
    table_body = ""
    x = """
    <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
width="20" height="20"
viewBox="0 0 172 172"
style=" fill:#000000;"><g fill="none" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><path d="M0,172v-172h172v172z" fill="none"></path><g><path d="M9.675,9.675h152.65v152.65h-152.65z" fill="#ffffff"></path><path d="M161.25,10.75v150.5h-150.5v-150.5h150.5M163.4,8.6h-154.8v154.8h154.8v-154.8z" fill="#ffffff"></path><g fill="#fa7575"><path d="M45.71205,54.83497l9.12152,-9.12184l71.45439,71.45189l-9.12152,9.12184z"></path><path d="M45.71314,117.16643l71.45189,-71.45439l9.12184,9.12152l-71.45189,71.45439z"></path></g></g></g></svg>"""
    favorites = models.Favorite.objects.all()
    for favorite in favorites:
        table_body += f"""        
        <tbody class="favoriteSelectorss" id="x">
            <tr>
                <th scope="row"><a href="/{settings.ADMIN_PATH}/{favorite.model.app_label}/{favorite.model.name}/">{favorite.model.name.capitalize()}</a></th>
                <td><a href="#" onclick="trolled( '{favorite.model.app_label}', '{favorite.model.name}', this )">{x} </a></td>
            </tr>
        </tbody>"""
    table = table + table_body + "</table>"
    return JsonResponse({"dist_data": table, "count": favorites.count()})


from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def unfavorite(request):
    print('here')
    body = request.POST
    label = body['label'].replace(' ', '').lower()
    name = body['name'].replace(' ', '').lower()
    model = ContentType.objects.filter(app_label=label, model=name).first()
    models.Favorite.objects.filter(model=model).delete()
    return HttpResponse(models.Favorite.objects.all().count())


@csrf_exempt
def addfav(request):
    body = request.POST
    label = body['label'].replace(' ', '').lower()
    name = body['name'].replace(' ', '').lower()
    try:
        model = ContentType.objects.filter(app_label=label, model=name).first()
        obj, created = models.Favorite.objects.get_or_create(model=model)
        if not created:
            obj.delete()
    except IntegrityError as err:
        print(f'Please migrate your model - "{name}" with app name - "{label}" in your admin.py', )
    return HttpResponse("post request success")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/favorite', get_district, name='favorite'),
    path('admin/unfavorite', unfavorite, name='unfavorite'),
    path('admin/addfav', addfav, name='addfav'),

]
