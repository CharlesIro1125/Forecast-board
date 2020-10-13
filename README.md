# Forecast-board
App repository

# Forecast-board

the Forecast-board has directories to different part of the Django files.

To view the major files for the application, go to Forecast-board directory under Forecast-board. 
in the Forecast directory are the 
1) Models.py 
which contains the formation of the database by setting the various database attribute
2) Views.py
this is the file where the quering of the database is done and all the coding required is done in this file.
it fetches data from the database, performs all neccesary process on the data and sends it to the html file where it is displayed on the webpage.
for forecasting, it loads a pickled (already trained model saved as a file) file containing the trianed model and uses this file to perform forecast, 
begining from the last entry in the datetime attribute of the database to two months ahead of the last datetime result retrieved from the database.

To view the various html files, go to templete directory, under Forecast-board.
it contains the various html code to display the output in a webfront.

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
this is the page that contains code to display the forecasted total load consumed for the duration used. for some irregularity in our main data. 
the forecast was done to some time point.
