# Visualizing YouTube WebApp
Data Science Project CAU Kiel.

## Description
Visualizing YouTube is a web application built using Dash, a Python web framework. It provides interactive visualizations of YouTube data, including trends, categories, comments, and other relevant metrics.
For more information on Dash, refer to the [Dash documentation](https://dash.plotly.com/).

## Installation
1. **Packages Dependencies**: The required packages and their versions are listed in the `requirements.txt` file. To install these packages, run the following command:
   ```bash
   pip install -r requirements.txt
   ```
   This command will install all the packages necessary to run the application and their dependencies.

**Optional Steps**: It is recommended to create a virtual environment for your project to isolate the package installation. You can use `pipenv` for managing dependencies and creating a virtual environment. If `pipenv`is not installed, you can install it using pip:
   ```bash
   pip install pipenv
   ```
   Once `pipenv`is installed, you can create a virtual environment, activate it, and install dependencies with the following commands:
   ```bash
   pipenv shell
   pipenv install -r requirements
   ```
   This will create a virtual environment and install all the dependencies specified in the `requirements.txt` file.

## Usage
To run the application, execute the `app.py` file:
   ```bash
   python app.py
   ```
Open a web browser and navigate to `http://127.0.0.1:8050/` to access the application. The application allows users to explore various aspects of YouTube data through interactive visualizations.
Once the application is running, users can navigate through different pages to view trends, categories, comments, and other metrics. Use the navigation menu or links provided within the application to explore different features.

## Repository Structure
* **app.py**: This file contains the main code for the Dash web application.

* **requirements.txt**: This file lists all the Python dependencies required to run the application.

* **assets/**:

  * **bootstrap.min.css**: CSS file for Bootstrap styling.
  
  * **logo.png**: Logo image for the application.
  
* **data/**:

  * **Trends100vRegions/**: Folder containing processed trend data.
  
  * **categoryData/**: Folder containing processed category data.
  
  * **comments/**: Folder containing processed comment data.
  
  * **covidComments/**: Folder containing processed COVID-related comment data.
  
  * **duration/**: Folder containing processed video duration data.
  
  * **keyWordClouds/**: Folder containing keyword cloud data.
  
  * **Categories.csv**: CSV file containing category information.
  
  * **europe.geojson**: GeoJSON file for European region data.
  
* **pages/**:

  * **categoriesInteractions.py**: Python file for category interactions page.
  **commentBehavior.py**: Python file for comment behavior page.
  
  * **covidComments.py**: Python file for COVID-related comments page.
  
  * **durationInteractions.py**: Python file for duration interactions page.
  
  * **home.py**: Python file for home page.
  
  * **imprint.py**: Python file for imprint page.
  
  * **keyWordAnalysis.py**: Python file for keyword analysis page.
  
  * **trendsCategorys.py**: Python file for trends by category page.
  
  * **videoLength.py**: Python file for video length page.

## Additional Notes:
* The `data/` directory contains processed data for various aspects of YouTube analysis, which are utilized by different pages in the application.
* The `pages/` directory contains Python files corresponding to different pages of the web application, each focusing on specific aspects of YouTube data visualization.

## Support
If you have any problems or need help, you can contact us here: stu237116@mail.uni-kiel.deIf you have any problems or need help, you can contact us here: stu237116@mail.uni-kiel.de

## Roadmap
* The Daily Trend will be updated with the current data for a certain period of time

## Authors:
* Anton Ach
* Dante Bartoli
* Konstantin Hamann


  


