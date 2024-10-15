
------------------------------------------------------<!-- s-aurav@LAPTOP-JS10JJ6V MINGW64 /d/src_dev/flutter/flutter-37hrs-misc/chap-24--step-8--33/backend-basic (main) -->
--------------------
$ python manage.py migrate
Operations to perform:
  Apply all migrations: account, admin, auth, authtoken, contenttypes, note, sessions, useraccount
Running migrations:

------------------------------------------------------  Applying note.0001_initial... OK
(venv-0731) 
s-aurav@LAPTOP-JS10JJ6V MINGW64 /d/src_dev/flutter/flutter-37hrs-misc/chap-24--step-8--33/backend-basic (main)
--------------------
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 14, 2024 - 13:39:31
Django version 5.0.2, using settings 'Django_Backend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

Not Found: /
[14/Oct/2024 13:39:39] "GET / HTTP/1.1" 404 2412
Not Found: /favicon.ico
[14/Oct/2024 13:39:40] "GET /favicon.ico HTTP/1.1" 404 2463
[14/Oct/2024 13:39:46] "GET /admin HTTP/1.1" 301 0
[14/Oct/2024 13:39:46] "GET /admin/ HTTP/1.1" 302 0
[14/Oct/2024 13:39:46] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 4155
[14/Oct/2024 13:39:46] "GET /static/admin/css/dark_mode.css HTTP/1.1" 200 2682
[14/Oct/2024 13:39:46] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 200 3063
[14/Oct/2024 13:39:46] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 200 2810
[14/Oct/2024 13:39:46] "GET /static/admin/js/theme.js HTTP/1.1" 200 1943
[14/Oct/2024 13:39:46] "GET /static/admin/css/login.css HTTP/1.1" 200 958
[14/Oct/2024 13:39:46] "GET /static/admin/css/base.css HTTP/1.1" 200 21544
[14/Oct/2024 13:39:46] "GET /static/admin/css/responsive.css HTTP/1.1" 200 17905
[14/Oct/2024 13:39:51] "POST /admin/login/?next=/admin/ HTTP/1.1" 200 4314

------------------------------------------------------
(venv-0731) 
<!-- s-aurav@LAPTOP-JS10JJ6V MINGW64 /d/src_dev/flutter/flutter-37hrs-misc/chap-24--step-8--33/backend-basic (main) -->
--------------------
$ python manage.py createsuperuser
Email: pankaj
Error: Enter a valid email address.
Email: pankajbasnet2020@hotmail.com
Name: pankaj
Password:
Password (again):

------------------------------------------------------Superuser created successfully.
(venv-0731)
s-aurav@LAPTOP-JS10JJ6V MINGW64 /d/src_dev/flutter/flutter-37hrs-misc/chap-24--step-8--33/backend-basic (main)
--------------------
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 14, 2024 - 13:41:57
Django version 5.0.2, using settings 'Django_Backend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.


====================================================================
====================================================================

