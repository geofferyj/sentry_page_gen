# REPO: team_sentry_pages

### Installing requirements.
``` sh
$ cd team_sentry_pages
$ pip install -r requirements.txt
```
>will install all necessary dependencies.
### Running server.
``` sh
$ python manage.py runserver
```
>System check identified no issues (0 silenced).
>June 10, 2020 - 03:04:21
>Django version 2.2.6, using settings 'core.settings'
>Starting development server at http://127.0.0.1:8000/
>Quit the server with CONTROL-C.

click on the address to redirect to home page.

## Admin Route..
```127.0.0.1/admin/```
### Admin interface login 
``` sh
Username: admin
Password: admin
```
>Credentials will be change on deployment for security reasons.

### Routes

* List Pages:```127.0.0:8000/list-pages/```
* Add Pages: ```127.0.0:8000/add-page/```
* Set Page Markdown: ```127.0.0.1:8000/set-page-markdown/<int:pk>/```   
* Get Page HTML: ```127.0.0.1:8000get-page-html/<int:pk>/```