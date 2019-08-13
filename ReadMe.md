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

**SwaggerUI**

    method : GET
    URL : hostname/api/v1/

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
    
**Filtering State By `name` and|or `code`**

    method : GET
    URL : hostname/api/v1/address/state?name=XXX&code=00
    "`name` contains XXX" "`zip_code` exact value 00"
    
**List and Create City**
    
    method : GET and POST
    URL : hostname/api/v1/address/city/

**Retrieve, Update and Delete a City**
    
    method : GET, (PUT || PATCH) and DELETE
    URL : hostname/api/v1/address/city/<pk>
    
**Filtering City By `name` and|or `zip_code`**

    method : GET
    URL : hostname/api/v1/address/city?name=XXX&zipcode=00&state=11
    "`name` contains XXX" "`zip_code` exact value 00" "`state` exact value 11"
    
**List and Create Post**
    
    method : GET and POST
    URL : hostname/api/v1/posts/post/

**Retrieve, Update and Delete a Post**
    
    method : GET, (PUT || PATCH) and DELETE
    URL : hostname/api/v1/posts/post/<pk>
    
**Filtering Post**

    method : GET
    URL : hostname/api/v1/posts/post?owner=idOwner&title=title&city=idCity&discription=azerty
    "`owner` exact idOwner" "`title` exact title" "`city` exact idCity" "`discription` exact azerty"
    
**List and Create Comment**
    
    method : GET and POST
    URL : hostname/api/v1/posts/comment/

**Retrieve, Update and Delete a Comment**
    
    method : GET, (PUT || PATCH) and DELETE
    URL : hostname/api/v1/posts/comment/<pk>

**Filtering Comment By user and|or post**

    method : GET
    URL : hostname/api/v1/posts/comment?owner=idOwner&post=idPost
    "`owner` exact idOwner" "`post` exact idPost"

**List and Create Reaction**
    
    method : GET and POST
    URL : hostname/api/v1/posts/reaction/

**Retrieve, Update and Delete a Reaction**
    
    method : GET, (PUT || PATCH) and DELETE
    URL : hostname/api/v1/posts/reaction/<pk>
    
**Filtering Reaction By user and|or post**

    method : GET
    URL : hostname/api/v1/posts/reaction?owner=idOwner&post=idPost
    "`owner` exact idOwner" "`post` exact idPost"

**List and Create Anomaly**
    
    method : GET and POST
    URL : hostname/api/v1/anomalys/

**Retrieve, Update and Delete a Anomaly**
    
    method : GET, (PUT || PATCH) and DELETE
    URL : hostname/api/v1/anomalys/<pk>
    
**Filtering Anomaly**

    method : GET
    URL : hostname/api/v1/anomalys?post=idPost&owner=idOwner&title=title&city=idCity&discription=azerty
    "`post` exact idPost" "`owner` exact idOwner" "`title` exact title" "`city` exact idCity" "`discription` exact azerty"

**List and Create Anomaly Signal**
    
    method : GET and POST
    URL : hostname/api/v1/anomalys/signal

**Retrieve, Update and Delete a Anomaly Signal**
    
    method : GET, (PUT || PATCH) and DELETE
    URL : hostname/api/v1/anomalys/signal/<pk>
    
**Filtering Anomaly**

    method : GET
    URL : hostname/api/v1/anomalys/signal?post=idPost&signaledByBy=idUser&owner=idOwner&title=title&city=idCity&discription=azerty
    "`post` exact idPost" "`signaledBy` exact idUser" "`owner` exact idOwner" "`title` exact title" "`city` exact idCity" "`discription` exact azerty"

**List and Create Event**
    
    method : GET and POST
    URL : hostname/api/v1/events/

**Retrieve, Update and Delete a Event**
    
    method : GET, (PUT || PATCH) and DELETE
    URL : hostname/api/v1/events/<pk>
    
**Filtering Event**

    method : GET
    URL : hostname/api/v1/events?post=idPost&date=yyyy-mm-dd&owner=idOwner&title=title&city=idCity&discription=azerty
    "`post` exact idPost" "`date` littelOrEqual to yyyy-mm-dd" "`owner` exact idOwner" "`title` exact title" "`city` exact idCity" "`discription` exact azerty"
    
**List and Create EventParticipation**
    
    method : GET and POST
    URL : hostname/api/v1/events/participate

**Retrieve, Update and Delete a EventParticipation**
    
    method : GET, (PUT || PATCH) and DELETE
    URL : hostname/api/v1/events/participate<pk>
    
**Filtering EventParticipation**

    method : GET
    URL : hostname/api/v1/events/participate?post=idPost&user=idUser&date=yyyy-mm-dd&owner=idOwner&title=title&city=idCity&discription=azerty
    "`post` exact idPost" "`user` exact idUser" "`date` littelOrEqual to yyyy-mm-dd" "`owner` exact idOwner" "`title` exact title" "`city` exact idCity" "`discription` exact azerty"

**Get User Ranking**

    method : GET
    Parameters : limit, (user|city)
    URL : hostname/api/v1/accounts/ranking?limit=5&user=1 OR hostname/api/v1/accounts/ranking?limit=5&city=1
