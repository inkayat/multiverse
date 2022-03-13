# multiverse-api
A system that performs scientific calculations on a database residing on a server and replies to queries submitted from Python.

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
 
 
## Web Page(frontend)

You can login via -> ```http login/```
using -> name:admin, password:admin

Main Page(Dashboard) -> ```http /```
Create New Data -> ```http multiverse/create```
 
## Console Application(cli)
requirements installation
```bash 
python -m pip install --user requests
```
### Usage

#### Help
```bash 
python3 app.py -h
```

#### Calculate and Get Mean Values from API endpoint
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
  POST /api/data/create/
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

You can find more details for data information at this [link](https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset)
.

#### List All Data

```http
  GET /api/data/list/
```
#### Get Specific Data <int:id>

```http
  GET /api/data/list/<id>
```
#### Get Last Created Data

```http
  GET /api/data/last
```

#### Create New Data

```http
  POST /api/data/create
```

#### Calculate Mean Values

```http
  GET /api/compute/mean
```

#### Get Most Important 10 Feature in Data (Feature Importance for Machine Learning)

```http
  POST /api/compute/feature-importance
```

#### Get The Nth Most ımportant Feature <int:order>

```http
  POST /api/compute/feature-importance/order
```


