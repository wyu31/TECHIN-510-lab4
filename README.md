# TECHIN-510-lab4
This repo is about Real-time streamlit.
An App including world clock and world currency is created.
This is link to App:  
https://worldclockandcurrency.azurewebsites.net/

And there are some exercise about datetime and periodically running workflows.

## How to run
 Open the terminal and run the following commands:
```bash
pip install -r requirements.txt
streamlit run app.py
```

## What is included
```datetime.ipynb```: Contains the code for the datetime exercise.  
```app.py```: The world clock and world currency app.  
```hello.py```: A hello world file to test github action.  
```requirements.txt```: Required packages to run the application.  
```.gitignore```: Include the file names that should be ignored.  
```action.yml```: To trigger hellp.py.  
```main_worldclockandcurrency.yml```: To trigger the world clock and world currency App.  

**As for bonus**
- The link to show the periodically running web scraper script:  
https://github.com/wyu31/TECHIN-510-lab2
- A UNIX timestamp display is included
- A separate page for converting UNIX timestamp to Human time is included
- Fetch real-time currency and integrated currency converting function.

## Lesson Learned
- How to use streamlit to control tags and sidebar for better interface arrangement and user experience.
- How to convert UNIX Timestamp to Human-Readable Time.
- How to use free API resources online.
- requirements.txt file cannot be put into the .gitignore if I want to run .yml file in the workflow.
- A unique key shouldn't be added under a loop, since loops or dynamic content might regenerate widgets

## Questions
- what's the advantage of Azure Postgres compared to the workflow function inside the GitHub?
- I want to learn more about API applications. Currently I can only read simple API resource websites.