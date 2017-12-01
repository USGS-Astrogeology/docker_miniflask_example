# Docker MiniFlask Example
This repository stores a very simple flask app that runs inside of a docker
container.  By default, the app exposes port 80 and loads the app.py project.
This project contains a single root ("/") with a response that contains the
packages installed into the iamge by default.

To build: `docker build -t miniflask_example .`
To run: `docker run -v /data/example_miniflask/app:/app -p 5000:80
miniflask_example`

Then, in a browser, navigate to localhost:5000.  The response should look like:

```json
{
  "response": [
    "wheel", 
    "Werkzeug", 
    "SQLAlchemy", 
    "six", 
    "Shapely", 
    "setuptools", 
    "requests", 
    "pyparsing", 
    "pyOpenSSL", 
    "pycparser", 
    "pycosat", 
    "pyasn1", 
    "pip", 
    "packaging", 
    "numpy", 
    "MarkupSafe", 
    "Jinja2", 
    "itsdangerous", 
    "idna", 
    "geojson", 
    "GeoAlchemy2", 
    "GDAL", 
    "Flask", 
    "Flask-SQLAlchemy", 
    "cryptography", 
    "conda", 
    "click", 
    "cffi", 
    "certifi", 
    "asn1crypto"
  ]
}
```
