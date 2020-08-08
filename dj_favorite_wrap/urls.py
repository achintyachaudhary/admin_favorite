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
from django.urls import path
from django.urls import path, re_path
from django.http import JsonResponse


# Create your views here.
def get_district(request):
    """
    give a state id, returns district mapped to that state
    :param request: state_id
    :return:
    """
    x = """<table>
        <caption>
          <a href="/admin/admin_favorite/" class="section" title="Models in the lol application">lol</a>
        </caption>

          <tbody><tr class="model-favorite">

              <th scope="row"><a href="/admin/admin_favorite/favorite/">Favorites</a></th>

             <td><a href="/admin/admin_favorite/favorite/" class="viewlink">favorite</a></td>



          </tr>

      </tbody>
          <tbody><tr class="model-favorite">

              <th scope="row"><a href="/admin/admin_favorite/favorite/">Favorites</a></th>

             <td><a href="/admin/admin_favorite/favorite/" class="viewlink">favorite</a></td>



          </tr>

      </tbody>
      </table>"""
    return JsonResponse({"dist_data": x})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/favorite', get_district, name='favorite'),

]
