
<!-- ---------------------------------------------------------------saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts -->
$ cd 'd:/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/frontend-basic'

---------------------------------------------------------------
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/frontend-basic (main)
$ ls -a
./                                                          node_modules/
../                                                         notes------v-v-sh-------IMP-----.md
.git/                                                       package.json
.gitignore                                                  package-lock.json
.next/                                                      postcss.config.mjs
app/                                                        public/
git-------already-created-by---next-js--project-------.txt  README.md
git----done-----not-github00---------july30------.txt       tailwind.config.ts
next.config.mjs                                             tsconfig.json
next-env.d.ts                                               z---------------------location--find---nitro--.txt.txt

<!-- --------------------------------------------------------------- -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/frontend-basic (main)
$ git add .

---------------------------------------------------------------
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/frontend-basic (main)
$ git commit -am "frontend--original-code--copied-pasted---edited-little---before-backend-start--.txt"
[main 3483107] frontend--original-code--copied-pasted---edited-little---before-backend-start--.txt
 32 files changed, 786 insertions(+), 139 deletions(-)
 create mode 100644 app/components/Categories.tsx
 create mode 100644 app/components/ContactButton.tsx
 create mode 100644 app/components/forms/CustomButton.tsx
 create mode 100644 app/components/inbox/Conversation.tsx
 create mode 100644 app/components/inbox/ConversationDetail.tsx
 create mode 100644 app/components/modals/LoginModal.tsx
 create mode 100644 app/components/modals/Modal.tsx
 create mode 100644 app/components/modals/SignupModal.tsx
 create mode 100644 app/components/navbar/AddPropertyButton.tsx
 create mode 100644 app/components/navbar/MenuLink.tsx
 create mode 100644 app/components/navbar/Navbar.tsx
 create mode 100644 app/components/navbar/SearchFilters.tsx
 create mode 100644 app/components/navbar/UserNav.tsx
 create mode 100644 app/components/properties/PropertyList.tsx
 create mode 100644 app/components/properties/PropertyListItem.tsx
 create mode 100644 app/components/properties/ReservationSidebar.tsx
 create mode 100644 app/hooks/useLoginModal.ts
 create mode 100644 app/hooks/useSignupModal.ts
 create mode 100644 app/inbox/[id]/page.tsx
 create mode 100644 app/inbox/page.tsx
 create mode 100644 app/landlords/[id]/page.tsx
 create mode 100644 app/myproperties/page.tsx
 create mode 100644 app/myreservations/page.tsx
 create mode 100644 app/properties/[id]/page.tsx
 create mode 100644 public/beach_1.jpg
 create mode 100644 public/icn_category_beach.jpeg
 create mode 100644 public/logo.png
 create mode 100644 public/profile_pic_1.jpg
 create mode 100644 z---------------------location--find---nitro--.txt.txt

<!-- --------------------------------------------------------------- -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/frontend-basic (main)
$ git add .

---------------------------------------------------------------
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/frontend-basic (main)
$ git commit -am "before--creating-django-project--backend--in--backend-basic-folder--part-3-start-now"
[main 29bacd8] before--creating-django-project--backend--in--backend-basic-folder--part-3-start-now
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 z-----------frontend--original-code--copied-pasted---edited-little---before-backend-start--222-.txt

<!-- --------------------------------------------------------------- -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/frontend-basic (main)
$ cd 'd:/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic'

---------------------------------------------------------------
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic
$ git init
Initialized empty Git repository in D:/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic/.git/

<!-- --------------------------------------------------------------- -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (master)
$ git add .

---------------------------------------------------------------
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (master)
$ git commit -am "before--creating-django-project--backend--in--backend-basic-folder--part-3-start-now--backend"
[master (root-commit) 7a679ba] before--creating-django-project--backend--in--backend-basic-folder--part-3-start-now--backend
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 z-----------frontend--original-code--copied-pasted---edited-little---before-backend-start--.txt

<!-- --------------------------------------------------------------- -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (master)
$ ls -a
./     z-----------frontend--original-code--copied-pasted---edited-little---before-backend-start--.txt
../    z---------------------github-done---.txt
.git/  z---------------------location--find---nitro--backend-.txt

---------------------------------------------------------------
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (master)
$ git remote add origin git@github.com:pankaj-basnet/django-next-js-airbnb-basic-4parts--backend--G.git
git branch -M main
git push -u origin main
Enter passphrase for key '/c/Users/saurav/.ssh/id_rsa': 
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 336 bytes | 168.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To github.com:pankaj-basnet/django-next-js-airbnb-basic-4parts--backend--G.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.

<!-- --------------------------------------------------------------- -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ ls -a
./     z-----------frontend--original-code--copied-pasted---edited-little---before-backend-start--.txt
../    z---------------------github-done---.txt
.git/  z---------------------location--find---nitro--backend-.txt

---------------------------------------------------------------
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ python -m venv venv-0731

<!-- --------------------------------------------------------------- -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ source venv-0731/Scripts/activate

---------------------------------------------------------------(venv-0731) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ which python
/d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic/venv-0731/Scripts/python

<!-- ---------------------------------------------------------------(venv-0731)  -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ which python
/d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic/venv-0731/Scripts/python

---------------------------------------------------------------(venv-0731) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ ls -a
./                z-----------frontend--original-code--copied-pasted---edited-little---before-backend-start--.txt
../               z---------------------github-done---.txt
.git/             z---------------------location--find---nitro--backend-.txt
requirements.txt  z----------venv---latest------venv-0731-.txt
venv-0731/

<!-- ---------------------------------------------------------------(venv-0731)  -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ pip install -r requirements.txt
Collecting Django==5.0.2 (from -r requirements.txt (line 1))
  Downloading Django-5.0.2-py3-none-any.whl.metadata (4.1 kB)
Collecting psycopg2-binary==2.9.9 (from -r requirements.txt (line 2))
  Using cached psycopg2_binary-2.9.9-cp312-cp312-win_amd64.whl.metadata (4.6 kB)
Collecting dj-rest-auth==4.0.0 (from -r requirements.txt (line 3))
  Downloading dj-rest-auth-4.0.0.tar.gz (155 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 155.6/155.6 kB 1.5 MB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting django-allauth==0.52.0 (from -r requirements.txt (line 4))
  Downloading django-allauth-0.52.0.tar.gz (728 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 728.3/728.3 kB 5.7 MB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting django-cors-headers==4.3.1 (from -r requirements.txt (line 5))
  Using cached django_cors_headers-4.3.1-py3-none-any.whl.metadata (16 kB)
Collecting djangorestframework==3.14.0 (from -r requirements.txt (line 6))
  Downloading djangorestframework-3.14.0-py3-none-any.whl.metadata (10 kB)
Collecting djangorestframework-simplejwt==5.3.1 (from -r requirements.txt (line 7))
  Using cached djangorestframework_simplejwt-5.3.1-py3-none-any.whl.metadata (4.3 kB)
Collecting pillow==10.2.0 (from -r requirements.txt (line 8))
  Downloading pillow-10.2.0-cp312-cp312-win_amd64.whl.metadata (9.9 kB)
Collecting channels==4.0.0 (from -r requirements.txt (line 9))
  Downloading channels-4.0.0-py3-none-any.whl.metadata (1.5 kB)
Collecting daphne==4.0.0 (from -r requirements.txt (line 10))
  Downloading daphne-4.0.0-py3-none-any.whl.metadata (6.4 kB)
Collecting asgiref<4,>=3.7.0 (from Django==5.0.2->-r requirements.txt (line 1))
  Using cached asgiref-3.8.1-py3-none-any.whl.metadata (9.3 kB)
Collecting sqlparse>=0.3.1 (from Django==5.0.2->-r requirements.txt (line 1))
  Using cached sqlparse-0.5.1-py3-none-any.whl.metadata (3.9 kB)
Collecting tzdata (from Django==5.0.2->-r requirements.txt (line 1))
  Using cached tzdata-2024.1-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting python3-openid>=3.0.8 (from django-allauth==0.52.0->-r requirements.txt (line 4))
  Using cached python3_openid-3.2.0-py3-none-any.whl.metadata (1.6 kB)
Collecting requests-oauthlib>=0.3.0 (from django-allauth==0.52.0->-r requirements.txt (line 4))
  Using cached requests_oauthlib-2.0.0-py2.py3-none-any.whl.metadata (11 kB)
Collecting requests (from django-allauth==0.52.0->-r requirements.txt (line 4))
  Using cached requests-2.32.3-py3-none-any.whl.metadata (4.6 kB)
Collecting pyjwt>=1.7 (from pyjwt[crypto]>=1.7->django-allauth==0.52.0->-r requirements.txt (line 4))
  Using cached PyJWT-2.8.0-py3-none-any.whl.metadata (4.2 kB)
Collecting pytz (from djangorestframework==3.14.0->-r requirements.txt (line 6))
  Using cached pytz-2024.1-py2.py3-none-any.whl.metadata (22 kB)
Collecting twisted>=22.4 (from twisted[tls]>=22.4->daphne==4.0.0->-r requirements.txt (line 10))
  Downloading twisted-24.3.0-py3-none-any.whl.metadata (9.5 kB)
Collecting autobahn>=22.4.2 (from daphne==4.0.0->-r requirements.txt (line 10))
  Downloading autobahn-23.6.2.tar.gz (480 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 480.8/480.8 kB 7.6 MB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting txaio>=21.2.1 (from autobahn>=22.4.2->daphne==4.0.0->-r requirements.txt (line 10))
  Downloading txaio-23.1.1-py2.py3-none-any.whl.metadata (5.4 kB)
Collecting cryptography>=3.4.6 (from autobahn>=22.4.2->daphne==4.0.0->-r requirements.txt (line 10))
  Downloading cryptography-43.0.0-cp39-abi3-win_amd64.whl.metadata (5.4 kB)
Collecting hyperlink>=21.0.0 (from autobahn>=22.4.2->daphne==4.0.0->-r requirements.txt (line 10))
  Downloading hyperlink-21.0.0-py2.py3-none-any.whl.metadata (1.5 kB)
Collecting setuptools (from autobahn>=22.4.2->daphne==4.0.0->-r requirements.txt (line 10))
  Using cached setuptools-72.1.0-py3-none-any.whl.metadata (6.6 kB)
Collecting defusedxml (from python3-openid>=3.0.8->django-allauth==0.52.0->-r requirements.txt (line 4))
  Downloading defusedxml-0.7.1-py2.py3-none-any.whl.metadata (32 kB)
Collecting oauthlib>=3.0.0 (from requests-oauthlib>=0.3.0->django-allauth==0.52.0->-r requirements.txt (line 4))
  Using cached oauthlib-3.2.2-py3-none-any.whl.metadata (7.5 kB)
Collecting charset-normalizer<4,>=2 (from requests->django-allauth==0.52.0->-r requirements.txt (line 4))
  Using cached charset_normalizer-3.3.2-cp312-cp312-win_amd64.whl.metadata (34 kB)
Collecting idna<4,>=2.5 (from requests->django-allauth==0.52.0->-r requirements.txt (line 4))
  Using cached idna-3.7-py3-none-any.whl.metadata (9.9 kB)
Collecting urllib3<3,>=1.21.1 (from requests->django-allauth==0.52.0->-r requirements.txt (line 4))
  Using cached urllib3-2.2.2-py3-none-any.whl.metadata (6.4 kB)
Collecting certifi>=2017.4.17 (from requests->django-allauth==0.52.0->-r requirements.txt (line 4))
  Using cached certifi-2024.7.4-py3-none-any.whl.metadata (2.2 kB)
Collecting attrs>=21.3.0 (from twisted>=22.4->twisted[tls]>=22.4->daphne==4.0.0->-r requirements.txt (line 10))
  Downloading attrs-23.2.0-py3-none-any.whl.metadata (9.5 kB)
Collecting automat>=0.8.0 (from twisted>=22.4->twisted[tls]>=22.4->daphne==4.0.0->-r requirements.txt (line 10))
  Downloading Automat-22.10.0-py2.py3-none-any.whl.metadata (1.0 kB)
Collecting constantly>=15.1 (from twisted>=22.4->twisted[tls]>=22.4->daphne==4.0.0->-r requirements.txt (line 10))
  Downloading constantly-23.10.4-py3-none-any.whl.metadata (1.8 kB)
Collecting incremental>=22.10.0 (from twisted>=22.4->twisted[tls]>=22.4->daphne==4.0.0->-r requirements.txt (line 10))
  Downloading incremental-24.7.2-py3-none-any.whl.metadata (8.1 kB)
Collecting twisted-iocpsupport<2,>=1.0.2 (from twisted>=22.4->twisted[tls]>=22.4->daphne==4.0.0->-r requirements.txt (line 10))
  Downloading twisted_iocpsupport-1.0.4-cp312-cp312-win_amd64.whl.metadata (2.2 kB)
Collecting typing-extensions>=4.2.0 (from twisted>=22.4->twisted[tls]>=22.4->daphne==4.0.0->-r requirements.txt (line 10))
  Downloading typing_extensions-4.12.2-py3-none-any.whl.metadata (3.0 kB)
Collecting zope-interface>=5 (from twisted>=22.4->twisted[tls]>=22.4->daphne==4.0.0->-r requirements.txt (line 10))
  Downloading zope.interface-6.4.post2-cp312-cp312-win_amd64.whl.metadata (44 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.1/44.1 kB ? eta 0:00:00
Collecting pyopenssl>=21.0.0 (from twisted[tls]>=22.4->daphne==4.0.0->-r requirements.txt (line 10))
  Downloading pyOpenSSL-24.2.1-py3-none-any.whl.metadata (13 kB)
Collecting service-identity>=18.1.0 (from twisted[tls]>=22.4->daphne==4.0.0->-r requirements.txt (line 10))
  Downloading service_identity-24.1.0-py3-none-any.whl.metadata (4.8 kB)
Collecting six (from automat>=0.8.0->twisted>=22.4->twisted[tls]>=22.4->daphne==4.0.0->-r requirements.txt (line 10))
  Downloading six-1.16.0-py2.py3-none-any.whl.metadata (1.8 kB)
Collecting cffi>=1.12 (from cryptography>=3.4.6->autobahn>=22.4.2->daphne==4.0.0->-r requirements.txt (line 10))
  Using cached cffi-1.16.0-cp312-cp312-win_amd64.whl.metadata (1.5 kB)
Collecting pyasn1 (from service-identity>=18.1.0->twisted[tls]>=22.4->daphne==4.0.0->-r requirements.txt (line 10))
  Downloading pyasn1-0.6.0-py2.py3-none-any.whl.metadata (8.3 kB)
Collecting pyasn1-modules (from service-identity>=18.1.0->twisted[tls]>=22.4->daphne==4.0.0->-r requirements.txt (line 10))
  Downloading pyasn1_modules-0.4.0-py3-none-any.whl.metadata (3.4 kB)
Collecting pycparser (from cffi>=1.12->cryptography>=3.4.6->autobahn>=22.4.2->daphne==4.0.0->-r requirements.txt (line 10))
  Using cached pycparser-2.22-py3-none-any.whl.metadata (943 bytes)
Downloading Django-5.0.2-py3-none-any.whl (8.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.2/8.2 MB 5.6 MB/s eta 0:00:00
Using cached psycopg2_binary-2.9.9-cp312-cp312-win_amd64.whl (1.2 MB)
Using cached django_cors_headers-4.3.1-py3-none-any.whl (12 kB)
Downloading djangorestframework-3.14.0-py3-none-any.whl (1.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 5.2 MB/s eta 0:00:00
Using cached djangorestframework_simplejwt-5.3.1-py3-none-any.whl (101 kB)
Downloading pillow-10.2.0-cp312-cp312-win_amd64.whl (2.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.6/2.6 MB 5.8 MB/s eta 0:00:00
Downloading channels-4.0.0-py3-none-any.whl (28 kB)
Downloading daphne-4.0.0-py3-none-any.whl (30 kB)
Using cached asgiref-3.8.1-py3-none-any.whl (23 kB)
Using cached PyJWT-2.8.0-py3-none-any.whl (22 kB)
Using cached python3_openid-3.2.0-py3-none-any.whl (133 kB)
Using cached requests_oauthlib-2.0.0-py2.py3-none-any.whl (24 kB)
Using cached requests-2.32.3-py3-none-any.whl (64 kB)
Using cached sqlparse-0.5.1-py3-none-any.whl (44 kB)
Downloading twisted-24.3.0-py3-none-any.whl (3.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.2/3.2 MB 6.1 MB/s eta 0:00:00
Using cached pytz-2024.1-py2.py3-none-any.whl (505 kB)
Using cached tzdata-2024.1-py2.py3-none-any.whl (345 kB)
Downloading attrs-23.2.0-py3-none-any.whl (60 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 60.8/60.8 kB 3.4 MB/s eta 0:00:00
Downloading Automat-22.10.0-py2.py3-none-any.whl (26 kB)
Using cached certifi-2024.7.4-py3-none-any.whl (162 kB)
Using cached charset_normalizer-3.3.2-cp312-cp312-win_amd64.whl (100 kB)
Downloading constantly-23.10.4-py3-none-any.whl (13 kB)
Downloading cryptography-43.0.0-cp39-abi3-win_amd64.whl (3.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 7.0 MB/s eta 0:00:00
Downloading hyperlink-21.0.0-py2.py3-none-any.whl (74 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 74.6/74.6 kB 4.0 MB/s eta 0:00:00
Using cached idna-3.7-py3-none-any.whl (66 kB)
Downloading incremental-24.7.2-py3-none-any.whl (20 kB)
Using cached oauthlib-3.2.2-py3-none-any.whl (151 kB)
Downloading pyOpenSSL-24.2.1-py3-none-any.whl (58 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.4/58.4 kB ? eta 0:00:00
Downloading service_identity-24.1.0-py3-none-any.whl (12 kB)
Using cached setuptools-72.1.0-py3-none-any.whl (2.3 MB)
Downloading twisted_iocpsupport-1.0.4-cp312-cp312-win_amd64.whl (47 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 47.6/47.6 kB ? eta 0:00:00
Downloading txaio-23.1.1-py2.py3-none-any.whl (30 kB)
Downloading typing_extensions-4.12.2-py3-none-any.whl (37 kB)
Using cached urllib3-2.2.2-py3-none-any.whl (121 kB)
Downloading zope.interface-6.4.post2-cp312-cp312-win_amd64.whl (206 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 206.5/206.5 kB 12.3 MB/s eta 0:00:00
Downloading defusedxml-0.7.1-py2.py3-none-any.whl (25 kB)
Using cached cffi-1.16.0-cp312-cp312-win_amd64.whl (181 kB)
Downloading pyasn1-0.6.0-py2.py3-none-any.whl (85 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 85.3/85.3 kB 5.0 MB/s eta 0:00:00
Downloading pyasn1_modules-0.4.0-py3-none-any.whl (181 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 181.2/181.2 kB 11.4 MB/s eta 0:00:00
Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Using cached pycparser-2.22-py3-none-any.whl (117 kB)
Building wheels for collected packages: dj-rest-auth, django-allauth, autobahn
  Building wheel for dj-rest-auth (pyproject.toml) ... done
  Created wheel for dj-rest-auth: filename=dj_rest_auth-4.0.0-py2.py3-none-any.whl size=158427 sha256=2340b2a05de825571573a32871a05de672129ea54ccd726d9cafc00937706f56
  Stored in directory: c:\users\saurav\appdata\local\pip\cache\wheels\66\46\94\20d5a0328ec46bd33cdde1c428f9b14c77039659c38829be1d
  Building wheel for django-allauth (pyproject.toml) ... done
  Created wheel for django-allauth: filename=django_allauth-0.52.0-py3-none-any.whl size=1063943 sha256=cd3e784238de2b7944e5cfbcc69e2ad93b507d92ac84e660993ea16d5a5a237f
  Stored in directory: c:\users\saurav\appdata\local\pip\cache\wheels\bf\6e\8f\73b567657113685083b6dccfed5dfab317a340f670eed818c4
  Building wheel for autobahn (pyproject.toml) ... done
  Created wheel for autobahn: filename=autobahn-23.6.2-py2.py3-none-any.whl size=666885 sha256=1cd800b6c46342cc9f5009328ff385cc9510f3420c7f110ae8bb8c5db40495dc
  Stored in directory: c:\users\saurav\appdata\local\pip\cache\wheels\0f\14\77\be73ce117195464cae399822b15e030b99c83428bd21bdc377
Successfully built dj-rest-auth django-allauth autobahn
Installing collected packages: twisted-iocpsupport, pytz, urllib3, tzdata, typing-extensions, txaio, sqlparse, six, setuptools, pyjwt, pycparser, pyasn1, psycopg2-binary, pillow, oauthlib, idna, defusedxml, constantly, charset-normalizer, certifi, attrs, asgiref, zope-interface, requests, python3-openid, pyasn1-modules, incremental, hyperlink, Django, cffi, automat, twisted, requests-oauthlib, djangorestframework, django-cors-headers, cryptography, channels, service-identity, pyopenssl, djangorestframework-simplejwt, dj-rest-auth, autobahn, django-allauth, daphne
Successfully installed Django-5.0.2 asgiref-3.8.1 attrs-23.2.0 autobahn-23.6.2 automat-22.10.0 certifi-2024.7.4 cffi-1.16.0 channels-4.0.0 charset-normalizer-3.3.2 constantly-23.10.4 cryptography-43.0.0 daphne-4.0.0 defusedxml-0.7.1 dj-rest-auth-4.0.0 django-allauth-0.52.0 django-cors-headers-4.3.1 djangorestframework-3.14.0 djangorestframework-simplejwt-5.3.1 hyperlink-21.0.0 idna-3.7 incremental-24.7.2 oauthlib-3.2.2 pillow-10.2.0 psycopg2-binary-2.9.9 pyasn1-0.6.0 pyasn1-modules-0.4.0 pycparser-2.22 pyjwt-2.8.0 pyopenssl-24.2.1 python3-openid-3.2.0 pytz-2024.1 requests-2.32.3 requests-oauthlib-2.0.0 service-identity-24.1.0 setuptools-72.1.0 six-1.16.0 sqlparse-0.5.1 twisted-24.3.0 twisted-iocpsupport-1.0.4 txaio-23.1.1 typing-extensions-4.12.2 tzdata-2024.1 urllib3-2.2.2 zope-interface-6.4.post2

[notice] A new release of pip is available: 24.0 -> 24.2
[notice] To update, run: python.exe -m pip install --upgrade pip

---------------------------------------------------------------(venv-0731)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ ls -a
./                z-----------frontend--original-code--copied-pasted---edited-little---before-backend-start--.txt
../               z---------------------github-done---.txt
.git/             z---------------------location--find---nitro--backend-.txt
requirements.txt  z----------venv---latest------venv-0731-.txt
venv-0731/

<!-- ---------------------------------------------------------------(venv-0731)  -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ django-admin startproject Django_Backend .

---------------------------------------------------------------(venv-0731) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ cd 'd:/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic/Django_Backend'

<!-- ---------------------------------------------------------------(venv-0731)  -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic/Django_Backend (main)
$ python manage.py startapp useraccount
C:\Users\saurav\AppData\Local\Programs\Python\Python312\python.exe: can't open file 'D:\\SIP-PYTHON\\django-3rd-mth-\\django-next-js-airbnb-basic-4parts\\backend-basic\\Django_Backend\\manage.py': [Errno 2] No such file or directory

---------------------------------------------------------------(venv-0731) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic/Django_Backend (main)
$ cd ..

<!-- ---------------------------------------------------------------(venv-0731)  -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ python manage.py startapp useraccount

---------------------------------------------------------------(venv-0731) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ python manage.py startapp property

<!-- ---------------------------------------------------------------(venv-0731)  -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ ls -a
./                                requirements.txt
../                               useraccount/
.git/                             venv-0731/
Django_Backend/                   z-----------frontend--original-code--copied-pasted---edited-little---before-backend-start--.txt
manage.py*                        z---------------------github-done---.txt
notes-------v-v--sh-----IMP--.md  z---------------------location--find---nitro--backend-.txt
property/                         z----------venv---latest------venv-0731-.txt

---------------------------------------------------------------(venv-0731)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ git add .

<!-- ---------------------------------------------------------------(venv-0731)  -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ git add .

---------------------------------------------------------------(venv-0731) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ git reset venv-0731

<!-- ---------------------------------------------------------------(venv-0731)  -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ git add .

---------------------------------------------------------------(venv-0731) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ git add commit -am "django project and app created"
error: unknown switch `a'
usage: git add [<options>] [--] <pathspec>...

    -n, --[no-]dry-run    dry run
    -v, --[no-]verbose    be verbose

    -i, --[no-]interactive
                          interactive picking
    -p, --[no-]patch      select hunks interactively
    -e, --[no-]edit       edit current diff and apply
    -f, --[no-]force      allow adding otherwise ignored files
    -u, --[no-]update     update tracked files
    --[no-]renormalize    renormalize EOL of tracked files (implies -u)
    -N, --[no-]intent-to-add
                          record only the fact that the path will be added later
    -A, --[no-]all        add changes from all tracked and untracked files
    --[no-]ignore-removal ignore paths removed in the working tree (same as --no-all)
    --[no-]refresh        don't add, only refresh the index
    --[no-]ignore-errors  just skip files which cannot be added because of errors
    --[no-]ignore-missing check if - even missing - files are ignored in dry run
    --[no-]sparse         allow updating entries outside of the sparse-checkout cone
    --[no-]chmod (+|-)x   override the executable bit of the listed files
    --[no-]pathspec-from-file <file>
                          read pathspec from file
    --[no-]pathspec-file-nul
                          with --pathspec-from-file, pathspec elements are separated with NUL character


<!-- ---------------------------------------------------------------(venv-0731)  -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ git commit -am "django project and app created"
Auto packing the repository in background for optimum performance.
See "git help gc" for manual housekeeping.
Enumerating objects: 28, done.
Counting objects: 100% (28/28), done.
Delta compression using up to 16 threads
Compressing objects: 100% (25/25), done.
Writing objects: 100% (28/28), done.
Total 28 (delta 4), reused 0 (delta 0), pack-reused 0 (from 0)
warning: There are too many unreachable loose objects; run 'git prune' to remove them.
[main fbdb00a] django project and app created
 28 files changed, 265 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 Django_Backend/__init__.py
 create mode 100644 Django_Backend/__pycache__/__init__.cpython-312.pyc
 create mode 100644 Django_Backend/__pycache__/settings.cpython-312.pyc
 create mode 100644 Django_Backend/asgi.py
 create mode 100644 Django_Backend/settings.py
 create mode 100644 Django_Backend/urls.py
 create mode 100644 Django_Backend/wsgi.py
 create mode 100644 manage.py
 create mode 100644 notes-------v-v--sh-----IMP--.md
 create mode 100644 property/__init__.py
 create mode 100644 property/admin.py
 create mode 100644 property/apps.py
 create mode 100644 property/migrations/__init__.py
 create mode 100644 property/models.py
 create mode 100644 property/tests.py
 create mode 100644 property/views.py
 create mode 100644 requirements.txt
 create mode 100644 useraccount/__init__.py
 create mode 100644 useraccount/admin.py
 create mode 100644 useraccount/apps.py
 create mode 100644 useraccount/migrations/__init__.py
 create mode 100644 useraccount/models.py
 create mode 100644 useraccount/tests.py
 create mode 100644 useraccount/views.py
 create mode 100644 z---------------------github-done---.txt
 create mode 100644 z---------------------location--find---nitro--backend-.txt
 create mode 100644 z----------venv---latest------venv-0731-.txt

---------------------------------------------------------------(venv-0731) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ git push
Enter passphrase for key '/c/Users/saurav/.ssh/id_rsa': 
Enumerating objects: 26, done.
Counting objects: 100% (26/26), done.
Delta compression using up to 16 threads
Compressing objects: 100% (20/20), done.
Writing objects: 100% (25/25), 6.21 KiB | 6.21 MiB/s, done.
Total 25 (delta 3), reused 25 (delta 3), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), done.
To github.com:pankaj-basnet/django-next-js-airbnb-basic-4parts--backend--G.git
   7a679ba..fbdb00a  main -> main

<!-- ---------------------------------------------------------------(venv-0731)  -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ ls -a
./                                requirements.txt
../                               useraccount/
.git/                             venv-0731/
.gitignore                        z-----------frontend--original-code--copied-pasted---edited-little---before-backend-start--.txt
Django_Backend/                   z---------------------github-done---.txt
manage.py*                        z---------------------location--find---nitro--backend-.txt
notes-------v-v--sh-----IMP--.md  z----------venv---latest------venv-0731-.txt
property/

---------------------------------------------------------------(venv-0731) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK

<!-- ---------------------------------------------------------------(venv-0731)  -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ git commit -am "django app migration done"
Auto packing the repository in background for optimum performance.
See "git help gc" for manual housekeeping.
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 16 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (7/7), done.
Total 7 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Checking connectivity: 12917, done.
warning: There are too many unreachable loose objects; run 'git prune' to remove them.
[main f4d054a] django app migration done
 3 files changed, 8 insertions(+), 1 deletion(-)

---------------------------------------------------------------(venv-0731)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ ls -a
./                                property/
../                               requirements.txt
.git/                             useraccount/
.gitignore                        venv-0731/
db.sqlite3                        z-----------frontend--original-code--copied-pasted---edited-little---before-backend-start--.txt
Django_Backend/                   z---------------------github-done---.txt
manage.py*                        z---------------------location--find---nitro--backend-.txt
notes-------v-v--sh-----IMP--.md  z----------venv---latest------venv-0731-.txt

<!-- ---------------------------------------------------------------(venv-0731)  -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ python manage.py runserver
Watching for file changes with StatReloader
Exception in thread django-main-thread:
Traceback (most recent call last):
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\apps\config.py", line 235, in get_model
    return self.models[model_name.lower()]
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
KeyError: 'user'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\contrib\auth\__init__.py", line 188, in get_user_model
    return django_apps.get_model(settings.AUTH_USER_MODEL, require_ready=False)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\apps\registry.py", line 213, in get_model
    return app_config.get_model(model_name, require_ready=require_ready)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\apps\config.py", line 237, in get_model
    raise LookupError(
LookupError: App 'useraccount' doesn't have a 'User' model.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1073, in _bootstrap_inner
    self.run()
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1010, in run
    self._target(*self._args, **self._kwargs)
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\core\management\commands\runserver.py", line 125, in inner_run
    autoreload.raise_last_exception()
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\utils\autoreload.py", line 87, in raise_last_exception
    raise _exception[1]
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\core\management\__init__.py", line 394, in execute
    autoreload.check_errors(django.setup)()
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\apps\registry.py", line 124, in populate
    app_config.ready()
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\contrib\admin\apps.py", line 27, in ready
    self.module.autodiscover()
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\contrib\admin\__init__.py", line 52, in autodiscover
    autodiscover_modules("admin", register_to=site)
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\utils\module_loading.py", line 58, in autodiscover_modules
    import_module("%s.%s" % (app_config.name, module_to_search))
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 995, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\contrib\auth\admin.py", line 6, in <module>
    from django.contrib.auth.forms import (
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\contrib\auth\forms.py", line 18, in <module>
    UserModel = get_user_model()
                ^^^^^^^^^^^^^^^^
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\contrib\auth\__init__.py", line 194, in get_user_model
    raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: AUTH_USER_MODEL refers to model 'useraccount.User' that has not been installed
D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\Django_Backend\settings.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 5 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): account, authtoken.
Run 'python manage.py migrate' to apply them.
July 31, 2024 - 16:29:46
Django version 5.0.2, using settings 'Django_Backend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[31/Jul/2024 16:29:56] "GET / HTTP/1.1" 200 10629
Not Found: /favicon.ico
[31/Jul/2024 16:29:56] "GET /favicon.ico HTTP/1.1" 404 2118


---------------------------------------------------------------(venv-0731) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ python manage.py migrate
Operations to perform:
  Apply all migrations: account, admin, auth, authtoken, contenttypes, sessions
Running migrations:
  Applying account.0001_initial... OK
  Applying account.0002_email_max_length... OK
  Applying authtoken.0001_initial... OK
  Applying authtoken.0002_auto_20160226_1747... OK
  Applying authtoken.0003_tokenproxy... OK

<!-- ---------------------------------------------------------------(venv-0731)  -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 31, 2024 - 16:30:33
Django version 5.0.2, using settings 'Django_Backend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[31/Jul/2024 16:30:50] "GET / HTTP/1.1" 200 10629
Not Found: /favicon.ico
[31/Jul/2024 16:30:50] "GET /favicon.ico HTTP/1.1" 404 2118


---------------------------------------------------------------(venv-0731) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 31, 2024 - 16:32:31
Django version 5.0.2, using settings 'Django_Backend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[31/Jul/2024 16:32:34] "GET / HTTP/1.1" 200 10629

<!-- ---------------------------------------------------------------(venv-0731)  -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ python manage.py check
SystemCheckError: System check identified some issues:

ERRORS:
auth.User.groups: (fields.E304) Reverse accessor 'Group.user_set' for 'auth.User.groups' clashes with reverse accessor for 'useraccount.User.groups'.
        HINT: Add or change a related_name argument to the definition for 'auth.User.groups' or 'useraccount.User.groups'.
auth.User.user_permissions: (fields.E304) Reverse accessor 'Permission.user_set' for 'auth.User.user_permissions' clashes with reverse accessor for 'useraccount.User.user_permissions'.
        HINT: Add or change a related_name argument to the definition for 'auth.User.user_permissions' or 'useraccount.User.user_permissions'.
useraccount.User.groups: (fields.E304) Reverse accessor 'Group.user_set' for 'useraccount.User.groups' clashes with reverse accessor for 'auth.User.groups'.
        HINT: Add or change a related_name argument to the definition for 'useraccount.User.groups' or 'auth.User.groups'.
useraccount.User.user_permissions: (fields.E304) Reverse accessor 'Permission.user_set' for 'useraccount.User.user_permissions' clashes with reverse accessor for 'auth.User.user_permissions'.
        HINT: Add or change a related_name argument to the definition for 'useraccount.User.user_permissions' or 'auth.User.user_permissions'.

System check identified 4 issues (0 silenced).

---------------------------------------------------------------(venv-0731)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ python manage.py check
System check identified no issues (0 silenced).

<!-- ---------------------------------------------------------------(venv-0731)  -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ python manage.py makemigration
Unknown command: 'makemigration'. Did you mean makemigrations?
Type 'manage.py help' for usage.

---------------------------------------------------------------(venv-0731) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ ls -a
./                                property/
../                               requirements.txt
.git/                             useraccount/
.gitignore                        venv-0731/
db.sqlite3                        z-----------frontend--original-code--copied-pasted---edited-little---before-backend-start--.txt
Django_Backend/                   z---------------------github-done---.txt
manage.py*                        z---------------------location--find---nitro--backend-.txt
notes-------v-v--sh-----IMP--.md  z----------venv---latest------venv-0731-.txt

<!-- ---------------------------------------------------------------(venv-0731)  -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ python manage.py makemigrations
Migrations for 'property':
  property\migrations\0001_initial.py
    - Create model Property
  property\migrations\0002_initial.py
    - Add field landlord to property
Migrations for 'useraccount':
  useraccount\migrations\0001_initial.py
    - Create model User

---------------------------------------------------------------(venv-0731) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$ python manage.py migrate
Traceback (most recent call last):
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\manage.py", line 22, in <module>
    main()
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\core\management\__init__.py", line 442, in execute_from_command_line
    utility.execute()
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\core\management\__init__.py", line 436, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\core\management\base.py", line 413, in run_from_argv
    self.execute(*args, **cmd_options)
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\core\management\base.py", line 459, in execute
    output = self.handle(*args, **options)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\core\management\base.py", line 107, in wrapper
    res = handle_func(*args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\core\management\commands\migrate.py", line 120, in handle
    executor.loader.check_consistent_history(connection)
  File "D:\SIP-PYTHON\django-3rd-mth-\django-next-js-airbnb-basic-4parts\backend-basic\venv-0731\Lib\site-packages\django\db\migrations\loader.py", line 327, in check_consistent_history
    raise InconsistentMigrationHistory(
django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency useraccount.0001_initial on database 'default'.

<!-- ---------------------------------------------------------------(venv-0731) -->
saurav@LAPTOP-JS10JJ6V MINGW64 /d/SIP-PYTHON/django-3rd-mth-/django-next-js-airbnb-basic-4parts/backend-basic (main)
$