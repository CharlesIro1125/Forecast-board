# Forecast-board
App repository

the Forecast-board has directories to different part of the Django files.

To view the major files for the application, go to Forecast-board directory under Forecast-board. 
in this directory are the  

board folder
forecast folder
templates folder

The board folder

this folder contains the settings and configuration of the Django application. it also contains the URL file for routing request made on the webpage to the appropriate resource  on the server.

The forecast folder contains 

1) Models.py 
this contains code for the formation of the database by setting the various database attribute
2) Views.py
this is the file where the quering of the database is done and all the coding required for computation and prediction.
it fetches data from the database, performs all neccesary process on the data and sends it to an html file where it is displayed on the webpage.
for forecasting, it loads a pickled (already trained model saved as a file) file containing the trianed model and uses this file to perform forecast,
begining from the last entry in the datetime attribute of the database to two months ahead of the last datetime result retrieved from the database.


The templates folder contains the various html code to display the output in a webfront.

1) base html 
this is the base structure for the webpage
2) home html
this is the home page that contains code to display the total load consumed from the content available in the database.
3) grid import html
this is the page that contains code to display the imported power from the content available in the database.
4) grid export html
this is the page that contains code to display the exported power from the content available in the database.
5) solar html
this is the page that contains code to display the photo-voltaic power from the content available in the database.
6) predict html
this is the page that contains code to display the forecasted total load consumed using an ARIMA model. for some irregularity in our main data. 
the forecast was done to some time point.
7) dense.html
this is the page that contains the code to display the forecasted total load consumed using a DENSE Neural network.


Another directory under the Forecast-board is the 

research folder.
