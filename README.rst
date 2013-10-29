.. contents::

Introduction
============

**mr.bob** templates : http://mrbob.readthedocs.org/en/latest/

+ basic_namespace : provide a zopeskel-like (basic_namespace) template


installation
---------------

::
 
 easy_install bobtemplates.jpcw

or simply add bobtemplates.jpcw to your eggs zc.buildout section 

or with pip

:: 
 
 pip install mr.bob
 pip install bobtemplates.jpcw



templates
------------

basic_namespace
++++++++++++++++++

:: 
   
 --> Namespace Package Name [paulla]:
 --> Package Name [paste]:
 --> Description:
 --> Author: 
 --> Author Email:
 --> Keywords ['']:
 --> Project URL ['']: 
 --> Project License [BSD|GPL] [BSD]:
 --> Zip-Safe [true/false] [false]:

pkg_ns (namespace) and pkg_project (package name) are guessed from -O option 

::
 
 bin/mrbob -O paulla.paste bobtemplates.jpcw:basic_namespace

return ::
 
 --> Namespace Package Name [paulla]:
 --> Package Name [paste]:


