---
hide:
    - navigation
---

#

__Our containers are prepared for serverless solutions.__

!!!warning
    Documentations on all containers are under development!



## [Cloud RUN ![](/static/icons/link18.svg)](/projects/cloudrun){target=_blank}

The base container for running an application in Google Cloud Platform. This container contains
Python 3.10.5, some Google SDK for Python packages and other packages that you need to run an
application.

The Cloud Run container can mount multiple Google Cloud Storage buckets or their folders to local
filesystem.


## [DASK ![](/static/icons/link18.svg)](/projects/dask){target=_blank}

Python 3.10.5 container with Dask packages.


## [ODOO ![](/static/icons/link18.svg)](/projects/odoo){target=_blank}

Based on `Cloud Run` container with preloaded [Odoo](https://odoo.com){target=_blank}, postgres-client
and contains startup script for Odoo.

Container can uses Google Cloud Storage as media folder, connect to a postgres through ssl and get
login, passwords and certificates from Google Cloud Secret Manager.

In the near future will be added support of Redis.


## Bash

Serverless infrastructure is very useful and economically conception. But during testing or debugging
this infrastructure or application in it you frequently need to have access into container. For this
case you can use SkyANT Bash container.

This container based on [pyxterm.js](https://github.com/cs01/pyxtermjs){target=_blank}

## LabelStudio 

[Label Studio](https://labelstud.io/){traget=_blank} is a magic tools for labeling tasks.[^1]


## MLFlow

[MLFlow](https://mlflow.org/){target=_blank} is one of the most popular tools for machine learning
pipeline.[^1]


## PGAdmin

[PGAdmin](https://www.pgadmin.org/) is an administrative user interface for PostgreSQL.[^1]


<br/><br/>
[^1]:
    It is a ROADMAP task.