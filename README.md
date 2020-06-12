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

* List Pages:```127.0.0:8000/pcreator/v1/```
>Accepts get method

* Add Pages: ```127.0.0:8000/pcreator/v1/add-page/```
>Accepts post method only
* Set Page Markdown: ```127.0.0.1:8000/v1/set-page-markdown/<int:pk>/```   
>Accepts get put and patch methods
* Get Page HTML: ```127.0.0.1:8000/v1/get-page-html/<int:pk>/```
>Accepts get method
>get page html will return the html of the page and also generate the file and save on the server.
>Accessible at ```pages.microapi.dev/pages/page-slug/``` 

>NOTE: "int:pk" means id. 

### User auth
* Register: ```127.0.0:800/v1/register```
> NOTE: You will not be logged in automatically
>Accepts only post method
* Login: ```127.0.0:800/v1/login```
>The login page takes two parameters;Username and password
>Accepts only post method

>A token will be assigned upon login if the user exists. Else an error will be returned 