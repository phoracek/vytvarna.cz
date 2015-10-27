==========
Kolmackovi
==========


How to
------

Deploy Nginx Cartridge for hosting:

.. code-block:: bash
    
    rhc create-app vytvarna http://cartreflect-claytondev.rhcloud.com/reflect?github=gsterjov/openshift-nginx-cartridge --no-git

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
