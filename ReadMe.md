# SbaClean

SbaClean is a project that link **Sidi Bel Abbes City hall** and its **citizens** witch are able to report any anomaly found.

# SbaClean Back End

The project Back End is built using `Django` and `Django Rest Freamwork` all the requirement are included in the  `requirements.txt`.

the project is composed of 5 django apps:
 - Account
 - Address
 - Post
 - Anomaly
 - Event

## Setting up the Back End

Clone the project using `git`

    git clone github.com/ilyes24/SbaClean
    python manage.py makemigrations
    python manage.py migrate
Download the project requirements

	pip install -r requirements.txt
	
FIRE IT UP!

    pyhton manage.py runserver
## API Road-Map

**Register**
    
    method : POST
    URL : hostname/api/v1/accounts/register/

**Get Token**

    method : POST 
    URL : hostname/api-token-auth/
    
`add Token to the HTTP method header
[Authorization Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]`
    
**List Users**
    
    method : GET
    URL : hostname/api/v1/accounts/

**Retrieve and Update User**
    
    method : GET and (PUT | PATCH) 
    URL : hostname/api/v1/accounts/<pk>
    
**List and Create State**
    
    method : GET and POST
    URL : hostname/api/v1/address/state/

**Retrieve, Update and Delete a State**
    
    method : GET, (PUT || PATCH) and DELETE
    URL : hostname/api/v1/address/state/<pk>
    
**List and Create City**
    
    method : GET and POST
    URL : hostname/api/v1/address/city/

**Retrieve, Update and Delete a City**
    
    method : GET, (PUT || PATCH) and DELETE
    URL : hostname/api/v1/address/city/<pk>
    
**List and Create Post**
    
    method : GET and POST
    URL : hostname/api/v1/posts/post/

**Retrieve, Update and Delete a Post**
    
    method : GET, (PUT || PATCH) and DELETE
    URL : hostname/api/v1/posts/post/<pk>
    
**List and Create Comment**
    
    method : GET and POST
    URL : hostname/api/v1/posts/comment/

**Retrieve, Update and Delete a Comment**
    
    method : GET, (PUT || PATCH) and DELETE
    URL : hostname/api/v1/posts/comment/<pk>
    
**List and Create Reaction**
    
    method : GET and POST
    URL : hostname/api/v1/posts/reaction/

**Retrieve, Update and Delete a Reaction**
    
    method : GET, (PUT || PATCH) and DELETE
    URL : hostname/api/v1/posts/reaction/<pk>

**List and Create Anomaly**
    
    method : GET and POST
    URL : hostname/api/v1/anomalys/

**Retrieve, Update and Delete a Anomaly**
    
    method : GET, (PUT || PATCH) and DELETE
    URL : hostname/api/v1/anomalys/<pk>
    
**List and Create Event**
    
    method : GET and POST
    URL : hostname/api/v1/events/

**Retrieve, Update and Delete a Event**
    
    method : GET, (PUT || PATCH) and DELETE
    URL : hostname/api/v1/events/<pk>