giferror
========

.. image:: https://travis-ci.org/briancurtin/giferror.svg?branch=master
    :target: https://travis-ci.org/briancurtin/giferror

A very useful exception class which identifies GIF links within exception
messages and presents them to the user in a web browser.

Installation
============

   pip install giferror

Simple Usage
============

.. code-block:: python

   >>> from giferror import GIFError
   >>> raise GIFError("Boom. http://i.imgur.com/o6Yj0bP.gif")

The above code would conveniently display the following image in your
operating system's default web browser.

.. image:: http://i.imgur.com/o6Yj0bP.gif
