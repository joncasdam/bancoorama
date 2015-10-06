Internet Banking Órama
======================

Projeto teste de um pseudo Internet Banking da Órama usando Django 1.8 com Angular.


Instruções de setup
-------------------

Dado que você já tenha python 2.7+, sqlite e pip instalado em sua máquina, faça

::

    $ cd ~/www
    $ git clone https://github.com/joncasdam/bancoorama/
    $ virtualenv bancoenv
    $ source bancoenv/bin/activate
    $ cd bancoorama
    $ pip install -r requirements.txt
    $ cd banco
    $ ./manage.py syncdb
    # ./manage.py cria_base_sistema
    $ ./manage.py runserver

