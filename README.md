# Quotes app

This application allows you to add, delete, or update your favorite quotes.
This little project was created to practice Flask web framework.

----------

## To Run

1. Clone this repo and go to the quotes-app directory
```
git clone https://github.com/Sashanity/quotes-app.git
cd quotes-app
```

2. Create virtual environment, activate it, and load with requirements
```sh
# create
$ python3 -m venv env

# activate
$ . venv/bin/activate

# load
$ pip install -r requirements.txt 
```
3. Create `.env` file and set link to MongoDB Atlas Cluster in it.
```sh
# in quotes-app directory
# create .env file
$ touch .env

# edit
$ nano .env

# once the editor opens, add your link in this format
$ MONGO_URI="mongodb+srv:// ....."
```

4. Run the application on local host
```sh
$ python app.py
```
