# OpenChemVault

This project is a framework which can be used to setup a data repository of computational chemistry format log files and deploy a (public) server providing REST API and web interface to browse and view the documents in the repository, search/filter using parsed attributes available, add new files to the database, download a document’s data and instantly parse a log file with [cclib](https://github.com/cclib/cclib) just by uploading the file in browser.


## Setup

### With Docker

* Install ```docker``` and ```docker-compose``` on your machine  
* Clone this repository  
  ```bash
  git clone https://github.com/nitish6174/openchemvault
  ```
* Setup the docker environment file
  ```bash
  cp .env.example .env
  ```
  * Set ```SETUP_DB``` as ```1``` to seed database with parsed files else set ```0```
  * ```DATA_FOLDER_PATH``` is the local path to the directory of log files which will be parsed and inserted in dockerized image's database if ```SETUP_DB``` is ```1```
  * Setting ```PRODUCTION``` to ```0``` runs flaskapp in ```debug``` mode
* Build the Docker setup and run it 
  ```bash
  sudo docker-compose build
  sudo docker-compose up
  ```  
* The flask application can now be accessed in browser at ```localhost:5000```


### Using python virtual environment

**Note** : Use Python 3. [OpenBabel](http://openbabel.org/docs/current/) setup is not added in the below steps.

Below instructions are given for ubuntu

* Install python pip and virtualenv  
  ```bash
  sudo apt-get install python3 python3-pip
  pip3 install virtualenv
  ```  
* Install MongoDB and start MongoDB server  
  ```bash
  sudo apt-get install mongo
  sudo service mongodb start
  ```  
* Clone repository and setup virtualenv for project  
  ```bash
  git clone https://github.com/nitish6174/openchemvault.git
  cd openchemvault
  virtualenv -p python3 venv_py3
  ```  
* Download [cclib](https://github.com/cclib/cclib) repository inside the ```openchemvault``` folder:  
  ```bash
  git clone https://github.com/cclib/cclib.git
  ```  
* Install pip dependencies and build cclib inside virtual environment  
  ```bash
  source venv_py3/bin/activate
  pip3 install -r requirements.txt
  cd cclib
  python3 setup.py build
  python3 setup.py install
  ```  
* Set configuration  
  ```
  cp config.py.example config.py
  ```  
  Change the variable values in ```config.py``` as suitable
* Running :  
  * Go to ```openchemvault``` directory (root of repo) and make sure virtualenv is activated.  
    (Run ```source venv_py3/bin/activate``` to enter virtual environment)
  * Run ```python run.py <SETUP_DB> <PRODUCTION> <DATA_FOLDER_PATH>``` with suitable arguments:  
    - ```SETUP_DB``` : Set as ```1``` to seed database with files in specified folder (Default: ```0``` )
    - ```PRODUCTION``` : Setting to ```0``` runs flaskapp in ```debug``` mode (Default: ```1``` )
    - ```DATA_FOLDER_PATH``` : Path to the directory containing log files which will be parsed and inserted in host's MongoDB database (provided ```SETUP_DB``` is ```1```) (Default value taken from ```config.py```)

    **Note** : All the 3 arguments are optional
  * Then, flask server will start on the machine at port 5000.  
  * The application can now be accessed in browser at ```localhost:5000```
  * Stop flask server with ```Ctrl-C``` and deactivate virtualenv using ```deactivate``` command


## Project structure

This project is a framework having 3 modules :
* Script which processes computational chemistry output files in specified folder and builds a MongoDB database (planned schema given below).
* API for browsing & searching documents in data repository.
* Web-interface based on above API allowing document browsing, searching, adding new files to data repository etc.


## Available functionality

Details can be found in the [TODO list](https://github.com/nitish6174/openchemvault/issues/1)

Here are the features available in web front-end as of now:

* Any computational chemistry log file (of format supported by cclib) can be uploaded on the webpage to view the parsed data from it
* A 3D rendering of the molecule if atom coordinates information is available
* Browse menu listing the various molecular formulas for which documents are available in the deployed instance's data repository
* Listing of documents corresponding to a molecular formula
* Search page supporting filtering with various attributes of logfiles
* Displaying details of a document selected from browsing menu or search results
* Download data of a particular document
* Page to upload and add a log file to the data repository


### MongoDB schema

The current schema design has 3 collections:

* **parsed_file** : Documents containing the parsed data from each of the logfile. Contains parsed attributes and molecular formula.
* **molecule** : List of unique molecular formulas of the various parsed_files. Each document contains a list of ObjectIDs of the parsed_file documents corresponding to that molecular formula.
* **attr_stats** : Contains a single document containing min and max value for some parsed attributes (used for setting range in searching/filtering).
