# Scraping_project

Documentation :
Scraping project at Elba :

This directory contains a web scraper for the website welcometothejungle and a processing script for the results of the scraper

If you want to launch the scraper, all commands are reminded in “Scrapers/COMMANDS.txt”

-Go to the Scraping directory, in my case on the Desktop
 
 ![dir scraping](https://user-images.githubusercontent.com/59396030/179989053-8d657b26-1ce7-486e-b07c-f1bc03dfec19.png)

-Go to the virtual environment directory

![dir venv](https://user-images.githubusercontent.com/59396030/179989361-94456da3-9a40-4146-882a-23f4c33481c4.png)

 
-Activate the virtual environment

![activate venv](https://user-images.githubusercontent.com/59396030/179989415-f2327a06-4602-4195-be79-ed41d64e0257.png)

 
-Go to the spider directory

![cd spiders](https://user-images.githubusercontent.com/59396030/179989453-4858f715-360d-459f-b5cf-056fc02eba0f.png)

 
-Run the spider and download the data
 
 ![run spider](https://user-images.githubusercontent.com/59396030/179989531-11b03f0f-309b-4487-b605-e238dd16872d.png)

 
-Check if your data were well saved

![liste file](https://user-images.githubusercontent.com/59396030/179989573-e10ca8a6-998a-4fc6-9cc2-4ea4b68447c7.png)

 
-Move data for processing
 
 ![moving data](https://user-images.githubusercontent.com/59396030/179989631-c40989cb-d90e-420b-98b0-a93bfc454621.png)


-Finally execute the Processing_scraper_data file in the Data Processing directory or if you do not work on windows execute the python script this way :

![process dir](https://user-images.githubusercontent.com/59396030/179989809-4d115321-b9d0-43c4-b814-e5a57f816d1f.png)


![running python script](https://user-images.githubusercontent.com/59396030/179989853-9fb46a52-138e-42ad-b422-0d19cfac1f94.png)

-You will find the results of your analysis in the Results directory


If you want to know which settings were changed or added for the scraper, check the spider settings in the files directory.

If you don’t want to use chrome, you will have to change the path towards the user agents json file in the settings file of the spider. Other lists of user-agents are in “files/User agents”
You will also have to modify the w_scrap.py file, replacing all chrome features by the chosen web driver’s 

Then if you want to generate a new .exe file, go back to your terminal, activate the virtual environment and type this command :
 
 ![auto_py_to_exe](https://user-images.githubusercontent.com/59396030/179989945-1ef94a8a-c785-4f95-8e66-c09957b3a05e.png)

 
It will open this window :
 
![auto window](https://user-images.githubusercontent.com/59396030/179989898-9c6620ce-c5df-4cba-8769-d9e31897162c.png)


-Enter the script location, which is “Scraping/Data_processing/Processing_scraper/welcome_data_processor.py”

-Click on “One Directory”

-Click on “Console Based”

-In “Additional Files”, click on “Add Folder” and add the “Data” and “Results” folders

-In “Settings” select the “Output Directory”

-Finally click on “Convert .PY to .EXE”
