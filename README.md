# EmailTracker
Allows you to check when someone has read your emails, should work with any provider.

## Usage:  
1) Clone directory  
2) Change the `BASE_PATH` in `EmailTracker.py`. 
3) Replace the file `image.jpg` if necesary, this will be the file served. 
4) Run: `python3 EmailTracker.py new <NAME>`, This will create a new entry named `<NAME>` to look for and print the url of the image.
5) Add the image url as an HTML `<img />` tag on the email you want to track and send!
6) Start the server: `python3 EmailTracker.py start`

When the user loads the image it will generate an entry in `storage.json` (also generates one when its atached to the email).
There you can check the date from every time they opened it and their ip (in the case of gmail the ip is incorrect since it uses a proxy to load images).

This can probably also be used in any other service that allows you to load images from external urls, or as a visits counter.

## How does it work?
When a new name is added its stored in `storage.json` and an url is generated, when the user requests that url an entry is added to the file with the users ip and date.

## Nginx
By default this script is intended to work with NGINX as a reverse proxy, the minimum necesary configuration is in `nginx.conf`. But using HTTPS its recommended as always.
