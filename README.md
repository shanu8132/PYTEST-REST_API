# PYTEST-REST_API
Basic CRUD Operations using Pytest and Requests (https://pypi.org/project/requests/) packages in python with API server hosted locally.

To install the node server locally:
1. install node.js
2. Command to install the npm-server : npm install -g json-server
3. Command to start the server : json-server --watch db.json #db.json will get created from the triggered location


To start the test use below command:
1. To run the sanity : pytest -v -s sanity --html=reports/report.html
2. To run the smoke : pytest -v -s smoke --html=reports/report.html
3. To run the regression : pytest -v -s regression --html=reports/report.html
4. To run all the tests : pytest -v -s --html=reports/report.html

