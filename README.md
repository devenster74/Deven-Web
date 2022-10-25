# Deven-Web
A simple Operating System, featuring a browser: HTML, JavaScript, CSS and Python

Some notes:

- To get the PyQt5 libraries: Follow these steps.
  win + r
  type in cmd
  in the command prompt type in pip install pyqt5

- For the calendar in the HTML, you will need to update it everyday.
  Line 294: <ul class="days"> <!-- copy paste for updating the current day: <li><span class="active">date goes here</span></li>--> 

- You will need to change these parts in browser.py to your own file location:
  Line 23:# setting default browser url as Deven web
  self.browser.setUrl(QUrl("file:///C:/Users/nsetp/OneDrive/Desktop/school/Deven's%20HTML/Simple%20Website.html"))
  Line 119:# open deven web
  self.browser.setUrl(QUrl("file:///C:/Users/nsetp/OneDrive/Desktop/school/Deven's%20HTML/Simple%20Website.html"))

- Download images along with the source code.
  
- You don't need to do the startup.py part, startup.py is the simple OS and is not required for browser.py to run.
