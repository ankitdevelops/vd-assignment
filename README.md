# Assignment Solution

- [Assignment Solution](#assignment-solution)
  - [Installations](#installations)
  - [Commands to run each solutions.](#commands-to-run-each-solutions)
    - [Question 1](#question-1)
    - [Question 2](#question-2)
    - [Question 3](#question-3)
    - [Question 4](#question-4)
    - [Question 5](#question-5)


## Installations

- **Create a Virtual environment**
  
  -  using any or the following command.
    ```sh
    python -m venv env

    // or

    python3 -m venv env
    ```
- **Activate the Virtual environment.**
    - On Linux/MacOS:
    ```sh
    source env/bin/activate
    ```
    - On Windows:
    ```sh
    env\Scripts\activate
    ```
- **Install the requirements**
    ```sh
    pip install -r requirements.txt
    ```

## Commands to run each solutions.

### [Question 1](./01_scrapper/main.py)

```sh
cd 01_scrapper

python main.py
```
### [Question 2](./02_parse_csv/main.py)

```sh
cd 02_parse_csv

python main.py
```

### [Question 3](./03_dj_query/)

```sh
cd 03_dj_query

python manage.py migrate

python manage.py generate_orders

python manage.py runserver

```
- visit  [your local host port 8000](http://127.0.0.1:8000/)

### [Question 4](./04_rate_limiter/main.py)

```sh
cd 04_rate_limiter

uvicorn main:app --reload

```
- visit  [send get requeset on your local host port 8000](http://127.0.0.1:8000/)

### [Question 5](./05_aggegrate_data/main.py)

```sh
cd 05_aggegrate_data

python main.py

```

