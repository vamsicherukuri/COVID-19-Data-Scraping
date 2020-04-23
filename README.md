# COVID-19 Visualizations using Web Data Scraping by Python Libraries 

COVID-19 Data scraped from worldometers website is stored in AWS MySql Database using python libraries.
Finally Data is visulized using Tableau Application and published onto tableau public.

## Getting Started

Install Dependent python libraries used in the project. 
MySql Instance free tire on Amazon RDS. (can able to have a free aws account ans stand up the free Msql instances without any cost).
JupyterNotebook with python libraries. 

### Prerequisites - Installing

Python Libraries used need to be installed as shown below

```
pip install pandas
```
```
pip install requests
```
```
pip install jsonlib
```
```
pip install beautifulsoup4
```
```
pip install SQLAlchemy
```

### Importing Python Libraries 

Import the installed python libraries used in the code.

```
Pandas to use dataframes.
Import pandas as pd
```
```
To send all kinds of HTTP request.
import requests
```
```
To part in JSON format.
Import json
```
```
Pandas to use dataframes
Import pandas as pd
```
```
beautifulsoup basically converts a complex html page into different python objects.
from bs4 import BeautifulSoup
```
```
Object Relational Mapper (ORM) is a comprehensive set of tools for working with databases and Python
Import sqlalchemy
```

## Web Scraping

Tools used for web scraping

```
beautifulsoup4
```
```
lxml
```

### Database used
MySql Instance free tire on Amazon RDS

```
MySql DB
```

### Visualization used

Tableau Desktop
Tableau public for publishing the dashboard.

Access Tableau Public live/intreactive Visualization here : 
https://public.tableau.com/views/COVID-19WORLD/COVID-19Global?:display_count=y&:origin=viz_share_link
https://public.tableau.com/views/COVID-19_15876011297410/COVID-19USA?:display_count=y&:origin=viz_share_link
https://public.tableau.com/views/COVID-19USASTATS/COVID-19USAByStates?:display_count=y&publish=yes&:origin=viz_share_link


## Built With

* [Worldometers Data Source URL](https://www.worldometers.info/coronavirus/#countries) - The web Site used to scrape
* [Database Used](https://aws.amazon.com/rds/mysql/) - Amazon RDS for MySQL
* [Visualization Tool used](https://public.tableau.com/s/) - connect to DB, create Visualizations and publish to public.

## Authors

* **Vamsi Cherukuri** - *Initial work* 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

