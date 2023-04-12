============
Contributing
============

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at
https://github.com/udaycruise2903/musica/issues.


Get Started!
------------

Ready to contribute? Here's how to set up `musica` for local
development. Please note this documentation assumes you already have
`poetry` and `Git` installed and ready to go.

| 1. Fork the `musica` repo on GitHub. 

| 2. Clone your fork locally:

   .. code-block:: bash

        cd <directory_in_which_repo_should_be_created>
        git clone git@github.com:YOUR_NAME/musica.git


| 3. Now we need to install the environment. Navigate into the directory

   .. code-block:: bash

       cd musica

   If you are using ``pyenv``, select a version to use locally. (See installed versions with ``pyenv versions``)

   .. code-block:: bash

       pyenv local <x.y.z>

   Then, install and activate the environment with:

   .. code-block:: bash

        poetry install
        poetry shell

| 4. Install pre-commit to run linters/formatters at commit time:

   .. code-block:: bash

        poetry run pre-commit install

| 5. Create a branch for local development:

   .. code-block:: bash

        git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.


| 6. Don't forget to add test cases for your added functionality to the ``tests`` directory.

| 7. When you're done making changes, check that your changes pass the formatting tests.

   .. code-block:: bash

        make check

| 8. Now, validate that all unit tests are passing:

   .. code-block:: bash

        make test

| 9. Before raising a pull request you should also run tox. This will run the
   tests across different versions of Python:

   .. code-block:: bash

        tox

   This requires you to have multiple versions of python installed. 
   This step is also triggered in the CI/CD pipeline, so you could also choose to skip this
   step locally.

| 10. Commit your changes and push your branch to GitHub:

   .. code-block:: bash

        git add .
        git commit -m "Your detailed description of your changes."
        git push origin name-of-your-bugfix-or-feature

| 11. Submit a pull request through the GitHub website.


