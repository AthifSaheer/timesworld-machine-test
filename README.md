# TimesWorld machine test

- Clone The project :- https://github.com/AthifSaheer/timesworld-machine-test-backend.git

### Built With

* Backend - `Python Django rest framework` `SQLite3`
* Frontend - `Reactjs`
* Libraries - `pydantic` `SQLAlchemy` `uvicorn` `geopy`

<!-- GETTING STARTED -->
## Getting Started

If you would love to run this project on your local env I will walk you through:

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/AthifSaheer/timesworld-machine-test-backend.git
   ```

2. Navigate to the project
   ```sh
   cd timesworld-machine-test-backend
   ```
   
3. Create virutal environment
   ```sh
   virtualenv venv
   ```

4. Activate virtualenv
   ```sh
   source venv/bin/activate
   ```
   
5. Install requirements.txt
   ```sh
   pip install -r requirements.txt
   ```
   
6. Migrate the project:
   ```sh
   python3 manage.py makemigrations
   ```
   ```sh
   python3 manage.py migrate
   ```
7. Access the project's API over view:
   ```sh
   http://127.0.0.1:8000/
   ```