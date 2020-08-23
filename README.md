![alt text](https://img.shields.io/website?url=https://admin-favorite.herokuapp.com/admin)
![alt text](https://img.shields.io/apm/l/docker)

**Mark most usable app as favorite in django admin**

**Author :** Achintya Ranjan Chaudhary

**License :** MIT

**Documentation :** https://admin-favorite.readthedocs.io/en/stable/

**Demo :** https://admin-favorite.herokuapp.com/admin/ (username: admin | password: admin)

----

**Steps to add this library in your project**
    
**Step 1 :** Install library in your project by running command below
   
    pip install admin-favorite

**Step 2 :** Add app name in your INSTALLED_APPS, make sure this is above 'django.contrib.admin' in your project
            
     'admin_favorite',

**Step 3 :** Add the path in your django project urls.py file 
    
    path('', include('admin_favorite.urls'))

**Step 4 :** migrate admin-favorite app to your project
            
     python manage.py migrate
