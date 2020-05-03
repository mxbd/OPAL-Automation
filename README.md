## OPAL-Automation

**Using Python with Selenium to save time by automating certain repetitive browser actions**

Due to the Covid-19 outbreak all uni courses at TU Dresden have been moved online which makes the e-learning platform "OPAL" particularly relevant and useful this semester. This code was created in order to save time logging into the platform with my uni credentials and navigating to the course favourites page showing my current course list multiple times a day. I used Selenium and chromedriver to automate entering information and navigating through the webpage.

Pyinstaller was needed in order to create executeable file from .py with all imported scripts so that the program can be run externally and not just in an IDE.

Create .exe (for future reference):

Find folder with .py files -> click on path in explorer -> "cmd" Enter

pip install pyinstaller
python -m PyInstaller --onefile --windowed --name="fileName" OPAL.py

--> move OPAL.exe into main folder and delete "dist" folder
