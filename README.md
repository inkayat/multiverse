# multiverse-api
A system that performs scientific calculations on a database residing on a server and replies to queries submitted from Python.


## Motivation and Assumptions
While developing this service, I aimed to be modular so that different functions can be added in the future. A frontend development was made to observe the data in the database and to help the user make scientific calculations with the help of the interface. In addition, the same calculations can be made through the console application. Since I was an Artificial Intelligence developer before, I preferred to calculate the feature importance from this dataset and also to calculate the average of the data because it helps to observe possible anomalies in the data.


## Teck Stacks
</details>
<details open="open">
    <summary>scientific calculations</summary>
  </ol>  
    <li><a>Scikit-learn</a></li>
    <li><a>Pandas</a></li>
  </ol>
</details>
<details open="open">
    <summary>backend</summary>
  <ol>
    <li><a>Python</a></li>
    <li><a>Django</a></li>
    <li><a>Docker</a></li>
    <li><a>Redis</a></li>
    <li><a>PostgreSQL</a></li>
    <li><a>sqlite3</a></li>
  </ol>
</details>
<details open="open">
  <summary>frontend</summary>
   <ol>
    <li><a>Boostrap</a></li>
    <li><a>Javascript</a></li>
  </ol>
 </details>


## Installation 

```bash 
  docker-compose build
  docker-compose up
```

Running on http://0.0.0.0:8000/

 
## Web Page(frontend)

You can login via (Login is not required for now)
```http://0.0.0.0:8000/login```
You need to create superuser, but it is not required to use other page.

Main Page(Dashboard)
```http://0.0.0.0:8000```

Create New Data 
```http://0.0.0.0:8000/multiverse/create```
 
 
 
## Console Application(cli)
requirements installation
```bash 
python -m pip install --user requests
or
python3 -m pip install --user requests

```

### Usage

#### Help
```bash 
python3 app.py -h
```

#### Calculate and Get Mean Values from API Endpoint
```bash 
python3 app.py -cm
```

#### Get Most Important Features
```bash 
python3 app.py -f paramater
paramater can be used as below
all =====> List of all 10 most important features
(1-10) =====> Get nth most important feature
```

#### Save this data as Excel Spreadsheet
```bash 
python3 app.py -s 
```


## API 

#### Create New Data

```http
  http://0.0.0.0:8000/api/data/create
  ```

| Paramater | Type     | 
| :-------- | :------- | 
| `age` | `int` |  |
| `attrition` | `string` 
| `bussines_travel` | `string` 
| `daily_rate` | `int` 
| `department` | `string`
| `distance_from_home` | `int`
| `education` | `int` |
| `education_field` | `string`
| `employee_count` | `int`
| `employee_number` | `int` 
| `environment_satisfaction` | `int` 
| `gender` | `string`
| `.` | `.` 
| `.` | `.` 
| `.` | `.` 
| `years_at_compan` | `int`
| `years_in_current_role` | `int`
| `years_since_last_promotion` | `int`
| `years_with_current_manager` | `int`

You can find more details for data information at this [link](https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset).

'

#### List All Data

Be Carefull, huge amount of data may cause the browser to crash.

```http
  http://0.0.0.0:8000/api/data/list/
  ```
#### Get Specific Data <int:id>

```http
  http://0.0.0.0:8000/api/data/<id>
```
#### Get Last Created Data

```http
  http://0.0.0.0:8000/api/data/last
```

#### Create New Data

```http
  http://0.0.0.0:8000/api/data/create
```

#### Calculate Mean Values

```http
  http://0.0.0.0:8000/api/compute/mean
```

#### Get Most Important 10 Feature in Data (Feature Importance for Machine Learning)

```http
  http://0.0.0.0:8000/api/compute/feature-importance
```

#### Get The Nth Most ımportant Feature <int:order>

order can be between 0 and 10

```http
  http://0.0.0.0:8000/api/compute/feature-importance/<int:order>
```


