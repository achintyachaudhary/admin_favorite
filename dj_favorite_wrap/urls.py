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
    favorites = models.Favorite.objects.all()
    for favorite in favorites:
        table_body += f"""        
        <tbody class="favoriteSelectorss" id="x">
            <tr>
                <th scope="row"><a href="/{settings.ADMIN_PATH}/{favorite.model.app_label}/{favorite.model.name}/">{favorite.model.name.capitalize()}</a></th>
                <td><a href="#" onclick="trolled( '{favorite.model.app_label}', '{favorite.model.name}', this )" class="viewlink">Not Favorite</a></td>
            </tr>
        </tbody>"""
    table = table + table_body + "</table>"
    return JsonResponse({"dist_data": table})


from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def unfavorite(request):
    print('here')
    body = request.POST
    label = body['label'].replace(' ', '')
    name = body['name'].replace(' ', '')
    model = ContentType.objects.filter(app_label=label, model=name).first()
    models.Favorite.objects.filter(model=model).delete()
    return HttpResponse("post request success")


@csrf_exempt
def addfav(request):
    body = request.POST
    label = body['label'].replace(' ', '')
    name = body['name'].replace(' ', '')
    model = ContentType.objects.filter(app_label=label, model=name).first()
    obj, created = models.Favorite.objects.get_or_create(model=model)
    if not created:
        obj.delete()
    return HttpResponse("post request success")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/favorite', get_district, name='favorite'),
    path('admin/unfavorite', unfavorite, name='unfavorite'),
    path('admin/addfav', addfav, name='addfav'),

]
