# Boltons Challenge


## Getting Started

1. Clone the repository:
```
git clone https://github.com/gabrielcocenza/boltons_challenge.git
cd cs-helper
```

2. Run Docker
```
docker-compose up --build
```
3. First populate the db:
```
curl --location --request GET 'http://localhost:7273/db/repopulate'
```
you should receive an answer like this:
```
{
  "response": "Database Repopulated"
}
```
4. After populating the DB you can check how many Nfe are available on the DB
```
curl --location --request GET 'http://localhost:7273/nfe/'
```
you should receive an answer like this:
```
{
  "response": "Currently 50 notes registered"
}
```
5. To access the total value of an Nfe just follow the pattern ```/nfe/<string:key>'``` where the key is the access_key from the Nfe
```
curl --location --request GET 'http://localhost:7273/nfe/<string:key>'
```

You should receive an answer like this if the access_key is found:
```
{
  "access_key": "<string:key>",
  "total_value": Float
}
```
If the access_key is not found you should receive  an answer like this:
```
{
  "response": "key <string:key>" not found"
}
```

6. Is also possible to clean the db using the command:
```
curl --location --request GET 'http://localhost:7273/db/clear'
```
You should receive an answer like this:
```
{
  "response": "Database Clear"
}
```

Supporting Technology:
- Flask
- Postgre
- SQLAlchemy

