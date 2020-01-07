# python-django
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It's free and open source. 

# Django Installation:

- Step 1 Download [Python](https://www.python.org/downloads/)
- Step 2 Install pip

    python 2:
    ```
    sudo apt install python-pip
    ```
    python 3:
    ```
    sudo apt install python3-pip
    ```
    
-Step 3 Create a folder for django project
-Step 4 Create a virtual environment
 python 2:
 ```
pip install virtualenv
python -m virtualenv nameofthevirtualenv

```
python3:

 ```
pip3 install virtualenv
python3 -m virtualenv nameofthevirtualenv

```
-Step 5 install Django


```
pip install django

```
-Step 6 Create django project
```
django-admin startproject projectname .

```
# Run an app 
To run a Django project on localhost

   python 2:
    
    ```
    python manage.py run server
    ```
    
   python 3:
    
    ```
    python3 manage.py run server
    ```
