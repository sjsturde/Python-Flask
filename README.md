# Python-Flask
Stephen Sturdevant
Python-Flask 1/27/2021
This project creates 2 clocks. The project assumes that the user is in the EST. From there it edits the view of the second clock to display what the different times are
in the respective time zones (CST, MST, and PST). The program takes a selection from the dropdown menu and puts the value into a list. The function returns the last value
added to the list and uses that as a key from pre-determined time zones with given values. The returned value then adjusts the clock accordingly. 
To get the project working follow the steps. 
1)	Flask Setup
a.	$mkdir flask-vue(On desktop)
b.	$cd flask-vue
c.	$python3 –m venv env
d.	$source env/bin/activate
e.	$pip install Flask Flask-Cors
f.	Add the file app.py(github) into the server directory. 
g.	$Python3 app.py
h.	(This will start the app)
2)	Vue Setup 
a.	$npm install –g @vue/cli
b.	$cd flask-vue
c.	$vue create client
d.	This will ask you to fill out Manually select features enter
e.	Select Babel Router and Linter/Formatter
f.	$cd client
g.	$npm install axios
h.	$npm run serve
3)	Adding My project files in the correct directory 
a.	Add app.vue in client/src directory replacing the file  
b.	Add index.js(github) to the client/src/router directory replacing the file
c.	Add clock.vue(github) to clinet/src/components
4)	 Go to localhost:8080 in a browser and click on Clock to get to the app
