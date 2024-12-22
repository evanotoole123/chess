# First time setup

## Automated
1. give read write permissions to setup.sh ```chmod u+x setup.sh```
2. run the script: ```./setup.sh```
3. done :)

## Manual 
1. setup python virtual environment(venv), run: ```python3 -m .venv```
2. activate venv by running: ```source .venv/bin/activate```
3. verify venv is active: ```which python3```
    output should look like: ```path/to/server/.venv/bin/python3```

Note:
    every time a new package is installed, such as running ```pip install <package-name>```
    the environment needs to be activated again.

