# Forecast-board
App repository

the Forecast-board has directories to different part of the Django files.

To view the major files for the application, go to Forecast-board directory under Forecast-board. 
In this directory are the  

a)board folder

b)forecast folder

c)templates folder

d)static/css folder

e)research folder



a) The board folder

this folder contains the settings and configuration of the Django application. it also contains the URL file for routing request made by the client to the appropriate resource  on the server.

b) The forecast folder contains 

1) Models.py 
this contains code for the formation of the database by setting the various database attribute
2) Views.py
this is the file where the quering of the database is done and all the coding required for computation and prediction.
it fetches data from the database, performs all neccesary process on the data and sends it to an html file where it is displayed on the webpage.
for forecasting, it loads a pickled (already trained model saved as a file) file containing the trianed model and uses this file to perform forecast,
begining from the last entry in the datetime attribute of the database to two months ahead of the last datetime result retrieved from the database.


c) The templates folder contains the various html code to display the output in a webfront.

1) base html 
This is the base structure for the webpage
2) home html
This file contains the code required to display the total load consumed from the content available in the database.
3) predict html
This file contains has the code required to display the forecasted total load consumed using an ARIMA model. for some irregularity in our main data. 
the forecast was done to some time point.
4) dense.html
This file contains has the code required to display the forecasted total load consumed using a DENSE Neural network.
5) grid import html
This file contains has thes code required to display the imported power from the content available in the database.
6) grid export html
This file contains has the code required to display the exported power from the content available in the database.
7) solar html
This file contains has the code required to display the photo-voltaic power from the content available in the database.




d) The research folder contains the various models (ARIMA and DENSE neural network) saved as a state file for making prediction 


e) The static/css folder contains all bootstrap and css scripts used in the front-end


Another seperate files outside the Forecast-board folder are the files required for deploying the Django application to a server. This files are

a) NGINX file

b) Supervisor file

c) Gunicorn file

a) The NGINX is configured with HTTPS certificates. Meaning it will only accept requests via HTTPS. If the client tries to request via HTTP, NGINX will first redirect the user to the HTTPS, and only then it will decide what to do with the request.


b) The Gunicorn is an application server. Depending on the number of processors the server has, it can spawn multiple workers to process multiple requests in parallel. It manages the workload and executes the Python and Django code.

c) The Supervisor is a process control system and it will keep an eye on Gunicorn and Django to make sure everything runs smoothly. If the server restarts, or if Gunicorn crashes, it will automatically restart it.
