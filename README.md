messageboard
============

student project building a simple messageboard


install requirements
--------------------
    
**download and install**
 
    - virtualbox https://www.virtualbox.org/wiki/Downloads
    - uppdatera er mmessageboard app från github - dom här filerna
    
        

create, activate and update virtualenv
------------------------------

ska redan vara gjort under lektionstid
aktivera er virtualenv 

vi ska installera lite nya bibliotek

    - fabric och fabtool, för att kunna automatisera installationer
    - python-vagrant för att enkelt kunna installera en virtuell linux på er dator 
    
vi gör det med pip
    
    cd till /path_to_messageboard

där borde ni hitta en fil requirements.txt, glöm inte **virtualenv**

    pip install -r requirements.txt


install linux and couchdb
-------------------------

fortfarande i terminalen 
    
    fab install_couchdb

första gången kan det ta ett litet tag, vagrant hämtar ner en linux-image 


vad ska vi göra med det här, vänta och se på onsdags lektionen



TODO
====

**API ENDPOINTS**

/ shows hot posts

**Jakob och Anton**

/user/<name>   show user posts and comments

/user/<name>/comments  show user comments

/user/<name>/submitted show user posts

**Isak**
/user/<name>/settings shows user settings 


**Timothy**
/login   

/logout

**Viktor**
/signup




