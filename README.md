# Sweety
Sweety is voice assistant with limited features
When you the call assistant as 'sweety' then only it will respond.

The main features are
# Timetable
User is requested to add or update the 5 days (Mon-Fri) time table in which each day has fixed time table from 8 am to 5pm with one hour intervals.
When you ask assistant  'what is the monday timetable?', Sweety will tell the timetable of monday in sequential order with timings.
# Website urls
User requested to give command with corresponding website url
here command is a nick name to website that user can give.
Suppose 
command is 'gaana' and url is https://gaana.com
when user say 'open gaana' it will open the website in chrome.

There will be a user authentication (used django auth models).
So that any number of users can be registered and set up their time tables and most viewed website urls.

# Extra Features
There will be extra features.
Like read mode and write mode.
you have to say 'go to read mode',
it will take you to the read mode.
In read mode, 
if you say 'down', page will go down, 
if you say 'top' , page will go up.
you have to say 'go to write mode' and open a file that you want to write and put cursor position in it.
Not only files you just put cursor position in whatsapp and facebook messengers.
what ever you say it will write.
These two modes will be terminated by saying 'over'.

