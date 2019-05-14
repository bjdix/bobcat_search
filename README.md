Advanced Data Mining Web & Local Search Project
==========================================================
Objective
----------
Implement a keyword search interface that enables:

(A) web search via a web search API
(B) local search on a given dataset.


Design Choices
--------------
1. Flask - A micro web framework written in Python and platformed on two components.  
    Werkzeug - toolkit for Web Server Gateway Interface applications  
    Jinja2 - template engine for rendering dynamic html  
    Reasons - Lightweight functionality of Flask allowed for rapid development  
            - Flask is actively maintained and developed with documentation  
   
2. Bing Search Engine API is used to provide basic web search functionality.  
   Reason - Abundant examples and documentation allowed for rapid development  
   
3. Elasticsearch is used for local search indexing and retrieval.  
   Reason - Ease of integration with Flask application  
   
4. Developed with github, travis.ci, and docker.  

5. Deployed on a digitalocean web server (droplet).  
