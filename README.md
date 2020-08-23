**Mark most usable app as favorite in django admin**

https://admin-favorite.herokuapp.com/admin/

**Author :** Achintya Ranjan Chaudhary

![alt text](https://img.shields.io/website?url=https://admin-favorite.herokuapp.com/admin)
![alt text](https://img.shields.io/apm/l/docker)

----

Steps to add this library to your project
    
**Step 1 :** Install library in your project by running command below
   
    `pip install admin-favorite` 

**Step 2 :** Add app name in your INSTALLED_APPS, make sure this is above 'django.contrib.admin' in your project
            
     'admin_favorite',

**Step 3 :** Add the path in your django project urls.py file 
    
    `path('', include('admin_favorite.urls'))`

