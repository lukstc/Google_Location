# Google_Location
<hr>
 Google_Location_App
<hr>


## Info:
- This is a simple python app using Google Map API to translate Address to Lag/Lng Translation or reverse.
![img_app_demo](doc/img/add_demo.png)

## Memo:
- if you don't have a Google API key yet, you could get one from [here](https://developers.google.com/maps/documentation/geocoding/get-api-key)
- currently, the app will only fetch the best match (the first result)
- next step: error handler

## Background:
- Recently, for one of my school projects, I have to heavily use Google Map API.During the development, to debug and to validate some results, I have to repeatedly translate the Address to Lat/Lng or from Lat/Lng to human-readable strings.

- To speed up the process, I designed this tool with a graphical user interface (GUI). The GUI system is depended on Tkinter, which is a standard package that comes with Python.

- I found Tkinter is very handy, especially when you wish to have some tool kits to speed up your daily work or you want to distribute some tools kits for the user who are not very familiar with coding.

- This project is still in the naive stage. I am also learning and exploring the power of Tkinter. I will keep working on this tool and summarize my discovery or understanding of Tkinter in this doc.
- If I find any useful articles or tutorials, I will also update that in this doc. If you have any cool ideas or interesting features that want to add to this tool, please don't hesitate to let me know.

## Reference, Useful links & Tutorial:
- Doc:
    - Google API Key: -[Link](https://developers.google.com/maps/documentation/geocoding/get-api-key)
    - Python Tkinter Official Doc: -[Link](https://docs.python.org/3/library/tkinter.html)
- Tutorial:
    - Tkinter Quick Start: -[Link](https://www.geeksforgeeks.org/python-gui-tkinter/)
        - by geeksforgeeks.com
        - their tutorial could give you a big picture of tkinter (and how does it work) at the very beginning 
    - An Introduction To Tkinter: -[Link](https://effbot.org/tkinterbook/tkinter-index.htm)
        - by effbot.org
        - very comprehensive! (recommend)
    - Make a Music Player with tkinter: [Link](https://www.youtube.com/playlist?list=PLhTjy8cBISEp6lNKUO3iwbB1DKAkRwutl)
        - by [buildwithpython](https://www.youtube.com/channel/UCirPbvoHzD78Lnyll6YYUpg)
        - youtube video
        - very stright forward (recommend)
