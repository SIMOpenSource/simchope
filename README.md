# SIMChope

## Installation
This flask application requires a PostgreSQL instance and performs CRUD operations on serving the web requests.

### Database Setup
Any PostgreSQL server will work - please configure the `DB_URI` in `config.py` accordingly. For example our default configurations amount to the equivalent `DB_URI` as follows -
```python
DB_URI = 'postgresql://simchope:simchope@localhost:5432/simchope'
```
Recommended approach to set up would be to pull a PostgreSQL image from docker and run the image.


### Application Setup
Create an environment and activate it following this [tutorial](https://dev.to/sahilrajput/install-flask-and-create-your-first-web-application-2dba)

When the environment is activated, install the dependencies with the package manager [pip](https://pypi.org/project/pip/)
```shell script
pip install -r requirements.txt
```
Once the dependencies are installed, export the `FLASK_APP` environment variable and run it accordingly.
```shell script
export FLASK_APP=server.py
python -m flask run
```
Find the application running at [http://localhost:5000](http://localhost:5000)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[GNU]()