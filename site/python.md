# Python packages


## [Adept](https://skyant.dev/projects/adept)


Pckages in this namespace provide the hi-level method for manipulating a data from 
[pydantic](https://pydantic-docs.helpmanual.io/) objects.


Adept's methods provide features for fast & useful:

- save/load the data to or from:
    
    - [Google Cloud Storage bucket](https://cloud.google.com/storage/) or local file in 
    additional formats;
    
    - Google noSQL database [Firestore](https://cloud.google.com/firestore) and thanks to our special field references between any documents will be transparently processed;  
    Adept also support save/load internationalisation string in multiple languages (in development).


- send the data to both asyc queues in Google Cloud Platform - 
[PubSub](https://cloud.google.com/pubsub) & [Google Tasks](https://cloud.google.com/tasks)

- send or load data using REST (or gRPC in the future) interface.

- configuring pydantic models using python polimorphism.


## [REST](https://skyant.dev/projects/rest)

The namemespace skyant.rest provides packages for more simple build REST API endpoint with 
[FastAPI](https://fastapi.tiangolo.com/) and integrate it in Google Cloud Platform.

SkyANT REST contains interied from FastAPI class which run as default ReDoc documentation & 
has a tools to get an authentication user id from [Google Identity-Aware Proxy](https://cloud.google.com/iap). Authentication Proxy from a cloud vendor makes your infrastructire more safe and protect 
you from DDoS attack!

Conbining whith our [Runner for Google CloudRun](https://skyant.dev/projects/runners-cloudrun)
your endpoin will works on HTTP/2 protokol and uses [Google Cloud Storage bucket](https://cloud.google.com/storage/) as a local folder.


## Web

A very beautiful package [Plotly Dash])(https://dash.plotly.com/) provide features to make live,
interactive web application wiht ReactJS UI with no JS coding.



## Scrapping


## gRPC
