###Prerequisites:
* Python3 is installed and the 'requests' module is installed (python3 -m pip install requests)

###API Access Required:
* Zoom API key is located in your shell environment variables, such as ~/.bashrc or ~/.zshrc - grab the JWT from Zoom App Marketplace. You will need to change the expiration so that it activates the credential, because we only use short expirations (90 mins - maximum of 1 week)
* assistants.py file contains the correct array of assistants whom you want to be granted delegate access


###zoom_delegates.py instructions:

This tool adds delegates (assistants) to a zoom user.

How to use:
1. In terminal, run "python3 zoom_delegates.py [username]"