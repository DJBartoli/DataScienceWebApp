# Visualizing YouTube WebApp
Data Science Project CAU Kiel.

## Description
Visualizing YouTube is a web application built using Dash, a Python web framework. It provides interactive visualizations of YouTube data, including trends, categories, comments, and other relevant metrics.
For more information on Dash, refer to the [Dash documentation](https://dash.plotly.com/).

## Installation
To install the required dependencies, use pipenv:
   ```bash
   pipenv install -r requirements.txt
   ```


## Repository Structure
**app.py**: This file contains the main code for the Dash web application.

**requirements.txt**: This file lists all the Python dependencies required to run the application.

**assets/**:

  **bootstrap.min.css**: CSS file for Bootstrap styling.
  
  **logo.png**: Logo image for the application.
  
**data/**:

  **Trends100vRegions/**: Folder containing processed trend data.
  
  **categoryData/**: Folder containing processed category data.
  
  **comments/**: Folder containing processed comment data.
  
  **covidComments/**: Folder containing processed COVID-related comment data.
  
  **duration/**: Folder containing processed video duration data.
  
  **keyWordClouds/**: Folder containing keyword cloud data.
  
  **Categories.csv**: CSV file containing category information.
  
  **europe.geojson**: GeoJSON file for European region data.
  
**pages/**:

  **categoriesInteractions.py**: Python file for category interactions page.
  
  **commentBehavior.py**: Python file for comment behavior page.
  
  **covidComments.py**: Python file for COVID-related comments page.
  
  **durationInteractions.py**: Python file for duration interactions page.
  
  **home.py**: Python file for home page.
  
  **imprint.py**: Python file for imprint page.
  
  **keyWordAnalysis.py**: Python file for keyword analysis page.
  
  **trendsCategorys.py**: Python file for trends by category page.
  
  **videoLength.py**: Python file for video length page.

## Running the Application
1. Install the required dependencies listed in `requirements.txt` using pipenv:
   ```bash
   pip install -r requirements.txt
   ```
2. Navigate to the project directory:
3. Execute the `app.py` file:
   ```bash
   python app.py
   ```
   4. Open a web browser and go to `http://127.0.0.1:8050/` to access the application.

## Additional Notes:
* The `data/` directory contains processed data for various aspects of YouTube analysis, which are utilized by different pages in the application.
* The `pages/` directory contains Python files corresponding to different pages of the web application, each focusing on specific aspects of YouTube data visualization.

## Contributors:
*
*
*


  


