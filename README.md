# cclib web repository

Web platform to parse data from chemistry logfiles using cclib

### Setup

**Note** : Python 3 is recommended. Just change the version numbers in steps below for Python 2.

* Install python pip and virtualenv  
  ```sudo apt-get install python3-pip```  
  ```pip3 install virtualenv```  
* Clone repository and setup virtualenv for project  
  ```git clone https://github.com/nitish6174/cclib-web.git```  
  ```cd cclib-web```  
  ```virtualenv -p python3 venv```  
* Download [cclib](https://github.com/cclib/cclib) inside the ```cclib-web``` folder:  
  ```git clone https://github.com/cclib/cclib.git```
* Install pip dependencies and build cclib inside virtual environment  
  ```source venv/bin/activate```  
  ```pip3 install -r requirements.txt```  
  (alternately: ```pip3 install numpy flask flask_compress flask_assets cssmin jsmin```)  
  ```cd cclib```  
  ```python3 setup.py build```  
  ```python3 setup.py install```  

### Running server and usage

* Go to ```cclib-web``` directory (root of repo) and make sure virtualenv is activated.  
  (Run ```source venv/bin/activate``` to enter virtual environment)
* Run ```python3 app.py```  
  This will start flask server on the machine at port 5000.
* When flask server is running, open [localhost:5000](http://localhost:5000) in your browser.
* Upload a chemistry logfile to get parsed data from it.
* Use the sample files in ```cclib/data``` folder and make sure that you provide the correct log file type in the form on website.
* Stop flask server with ```Ctrl-C``` and deactivate virtualenv using ```deactivate``` command
