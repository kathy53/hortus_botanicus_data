# Extracting information from a website to plant lovers who enjoy visiting the Hortus-Botanicus 
This work is a complete pipeline that includes the next phases 
### Data extraction
To gather data from the hortus botanicus website it was implemented a Python script based on __Playwright__ in async mode and it is called `get_hortus_data.py`. In this phase two data sources are requested from the same website.
1. The first source is a series of flowers cards. The information for each card is stored as an object in a __JSON file__, in total twelve objects are created. The file is store in a new directory that is created if it does not exits once the script is executed and it is called `data_flowers`. 
2. The second source is the header carrusel of blogs, each blog is extracted as an html file. The html files are stored in a new directory `blog_html_files`.

### Data processing (in-progress)
1. The data is prepoceed using Pandas .encode().decode('unicode_escape')
2. Extracting main ideas using OpenAI API 
### Saving data (in-progress)
1. Storing data in a Google Sheet using the Google Sheets API.
2. Storing text in a Postgress database. 
### Data access (in-progress)
Create an API to 
1. Visualizing data from the flowers JSON a API
2. Requsting information from a blog.