# D&D Inventory

## Groups Members
- Eric "Klee" Baumhover
- Matt Cooney
- Blake Shea
- Ben R-G

# Running the Project

## Step 0: Clone This Repository

Unless otherwise specified, all commands mentioned below should be run within the root directory of this repository.

## Step 1: Secure Configuration

To configure the password for the database and other settings, you will need to write them in a `.env` file. Follow these steps:

1. Copy `.env.example` to `.env`
2. Run `chmod 600 .env` to prevent other users from reading your `.env` file
3. Edit `.env`, changing:
  - The text `RANDOM_PASSWORD` to a password which is actually random
  - The text `SOMETHING_LONG_AND_RANDOM` to random text, ideally generated using the Python one-liner below:

```
python3 -c "import string,random; uni=string.ascii_letters+string.digits; print(''.join([random.SystemRandom().choice(uni) for i in range(random.randint(45,50))]))"
```

## Step 2: Start the Docker Services

Run:
```
docker compose up
```

The first time you run it, this command will take a few minutes to complete.

When you are done running the application, you can stop it by typing `Control-C`.

## Step 3: Run Migrations

Follow the instructions below to run the database migrations. This will ensure the database has the schema for the applications.

## Step 4: Load Equipment Data

Follow the instructions below to load the equipment data. These contain preexisting items from the D&D 5th Edition SRD and other sourcebooks.

## Step 5: Load the Application

Load <http://localhost:8080> and you will be directed to the home page. 

### Signup and Login
First create a user using the signup page.

Login, and you will be able to access the user page where you can create a character. The user page lists all of your characters with their corresponding links.

### Character Creation
Once you create a character, you will be redirected to the new character's page.

First add an inventory named "Inventory"

Finally add items based on preexisting ones, or add custom items. Example existing item to search: "Potion of Healing"

Items can be removed individually, as can entire inventories.

## Hints

### Database Operations

#### Migrations
To create the database, run the following command.

```
docker compose exec django python manage.py migrate
```

#### Load Equipment

To load the equipment data from existing dump files, use the following commands.

```
> docker compose exec postgres bash
# psql --username="$POSTGRES_USER" --dbname="$POSTGRES_DB" --set ON_ERROR_STOP=on --file postgres_files/equipment.sql
# psql --username="$POSTGRES_USER" --dbname="$POSTGRES_DB" --set ON_ERROR_STOP=on --file postgres_files/equipment_property.sql
# psql --username="$POSTGRES_USER" --dbname="$POSTGRES_DB" --set ON_ERROR_STOP=on --file postgres_files/weapon.sql
```
