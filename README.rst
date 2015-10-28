==========
Kolmackovi
==========


How to
------

Deploy Nginx Python Cartridge for hosting:

.. code-block:: bash
    
    rhc app create -a pelican -t http://cartreflect-claytondev.rhcloud.com/github/gsterjov/openshift-advanced-python-cartridge --from-code https://github.com/phoracek/vytvarna.cz.git

Clone this custom repo:

.. code-block:: bash
    
    git clone https://github.com/phoracek/vytvarna.cz.git

Commit changes and push them to travis. It will handle deployment to OpenShift
on its own. This could be done via GitHub GUI as well.

.. code-block:: bash
    
    git status  # this lists all changes
    git add path/to/changed/file
    git commit -m 'Short commit message'
    git push
