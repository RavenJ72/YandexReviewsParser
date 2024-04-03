# This project
Yandex Task  
A simple single-module Yandex maps parser, parsing 600 reviews due to Yandex restrictions. 
The process takes about five minutes, it takes a very long time to convert into objects 
that are sent to Postgresql DB.

### Project Overview
Type: Console Application
Data Storage: PostgreSQL  

### Requirements
Build and Run: The project's README.MD includes instructions on how to build and run the project.

## Building and running

DB
```
docker-compose up -d
```
Running the main script
```
python run.py --org_id 1124715036
```
Instead of the org_id parameter, you must specify the organization identifier.

| `url`                                                  | `org_id`   | `name`           |
|--------------------------------------------------------|------------|------------------|
| https://yandex.ru/maps/org/yandeks/1062848432/reviews/ | 1062848432 | Курский вокзал   |
| https://yandex.ru/maps/org/yandeks/1079518466/reviews/ | 1079518466 | Казанский вокзал |
| https://yandex.ru/maps/org/yandeks/1106208056/reviews/ | 1106208056 | Ленинградский    |
| https://yandex.ru/maps/org/yandeks/1085018813/reviews/ | 1085018813 | Ярославский      |