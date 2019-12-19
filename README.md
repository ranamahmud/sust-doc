# SUST DOC

A web application to fill up and generate filled pdf official forms/ documents of the university. Developed using the django python framework.



## Objectives

1. Help students fill up necessary documents quickly.

2. Get the pdf version of the forms/documents for printing.



## Getting Running

1. Install Python. I used Python 3.4.3 at the moment but 2.7.x works fine too.

2. Install a ``virtualenv`` and requirements:

        $ cd sust-doc
        $ virtualenv mypy
        $ . mypy/bin/activate
        $ pip install -r requirements.txt

3. Set up and Run:

   I used a ``Makefile``. You don't have to. You can look inside the ``Makefile``
   and see how it's run.

        $ make configure   # Builds a seed.sql that can be used in `make rebuild`
        $ make rebuild     # A bit better than `python manage.py syncdb`
        $ make run         # The same as `python manage.py runserver`


4. Visit http://127.0.0.1:8000/


