---
hide:
    - navigation
---

#

## [DATA ![](/static/icons/link18.svg)](/projects/data){target=_blank}

The module `skyant-data` provides features for working with various data & datasets.

At this moment, defined a few objects that are inherited from `pydantic`, so they give you methods
for working with structured data. You will save/load files on Google Cloud Storage or send PubSub
or send/load data to REST endpoint by a single line of code from a pydantic model.


## [UI ![](/static/icons/link18.svg)](/projects/ui){target=_blank}

The cool project [Plotly Dash](https://dash.plotly.com){target=_blank} that brings a React.js in Python
ecosystem, is a core of UI component of SkyANT.

Extended objects of SkyANT have integrated Bootstrap, Material & Awesome icons, Google fonts. In the
ROADMAP are integrating Google Analytics and Sentry. In combination with
[`skyant-tools`](/projects/tools){target=_blank} you can easy use Google Identity Access Manager or
Identity Aware Proxy.


## [REST ![](/static/icons/link18.svg)](/projects/rest){target=_blank}


FastAPI is one of the most popular REST APIs frameworks become the base of `skyant-rest`. FastAPI
uses pydantic, so the combination of `skyant-data` & `skyant-rest` provides easy and functional
instruments for build REST API in a cloud (at the moment in Google Cloud).

Additionally the `skyant-rest` is adapted for working behind load balancer and it can uses the
`skyant-tools` for authentication in cloud infrastructure.


## [TOOLS ![](/static/icons/link18.svg)](/projects/tools){target=_blank}

Any other litle tools.

## [SCRAPPER ![](/static/icons/link18.svg)](/projects/scrapper){target=_blank}

The `skyant-scrapper` is a hi-level interface for making web scrappers based on selenium.
Our scrappers can wait a javascript uploading, click on any buttons and build a nested JSON from a
source web page.

!!!warning
    User documentation on this project is under development!
