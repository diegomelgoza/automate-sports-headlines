# Automate Sports Headlines

Using Selenium we will access https://www.thesun.co.uk/sport/football/ to scrape the top headlines in Football today.  
In the headlines.py file you will find the code used to automate this process. 

### Things accomplished with this project:
* Converted the python script into an executable file using pyinstaller --onefile.
* Ran Selenium headless so that it doesn't open a chrome window.
* To find **ALL** elements I used **.find_elements** 
* Only used XPATH rather than ID or class names.
* Created lists that were then stored in a dictionary.
* Used pandas to create a dataframe and convert it to a csv file.
* Used the datetime package to make things more organized.
* Added comments that explain the code used
