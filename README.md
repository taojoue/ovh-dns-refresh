# ovh-dns-refresh
### A service to automate the refresh of the IP address in OVH.

## A few steps to use it:
    
    1.  Install the libraries ovh, requests, os, dotenv.
    2.  Get your OVH credentials and add a ".env" file with them. You'll find a template bellow.

## To run it:

    -  To run localy it use "python main.py"
    -  To run in a Docker container use docker "build . -t ovh-dns-refresh" then "docker run ovh-dns-refresh"
    -  You can edit the crontab file if you want to modify when the command is running. 
       By default it runs every 10min.

## .env file template:

Your endpoint, in my case it is ovh-eu : ENDPOINT = " "
Your Application Key : APPLICATION_KEY = " "
Your Application Secret : APPLICATION_SECRET = " "
Your Consumer Key : CONSUMER_KEY = " "
Your website url as written in your DNS zone on OVH's website : WEBSITE = " "
