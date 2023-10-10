# GenMod
SQLAlchemy ORM Model generator from ER diagram

## How to use
1. Download the project
2. Go to the `util` directory
3. Enter the commands in the terminal
```
> pip install -r requirements.txt

> python main.py init -a=../example/app -d=src/database

> python main.py create -a=../example/app -e=../example/er.drawio -p=Page-1
```
Where:
1. `../example/app` is the path to the app
2. `../example/er.drawio` is the path to the file with the ER diagram
3. `src/database` is an optional path to the directory with database in the application.
By default, the directory with database will be created in the root of the application
4. `Page-1` is the name of the page with the diagram in drawio
