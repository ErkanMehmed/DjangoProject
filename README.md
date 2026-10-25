# DjangoProject
# AutoMarket

A small vehicle marketplace built with **Django** and **PostgreSQL**. Keep a catalog of car manufacturers, list vehicles for sale, attach equipment features, and search through the listings. There is no login: every page is open and all data is created through the website.

## Features

- **Manufacturers**: create, list, view, edit, delete
- **Vehicles**: create, list, view, edit, delete, with search, filters and sorting
- **Features**: equipment items (e.g. "Heated seats") attached to vehicles
- Pagination, success/error messages and delete confirmation pages
- A manufacturer with vehicles cannot be deleted (friendly message instead)
- Custom 404 page, responsive design with Bootstrap 5

## Quick start

You need Python 3.12+, PostgreSQL 17+ and Git. Run the commands from the folder that contains `manage.py`.

**1. Get the code and create a virtual environment**

```
git clone <repository-url>
cd <repository-folder>
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows PowerShell
# source .venv/bin/activate       # macOS / Linux
pip install -r requirements.txt
```

**2. Create the database** (in `psql` or pgAdmin)

```sql
CREATE DATABASE auto_market_db;
```

By default the project connects as the user `postgres` with the password `admin`. If your PostgreSQL user has a different password, change the PASSWORD before running the project.

**3. Migrate and run**

```
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/.

## Try it

1. **+ Add → Manufacturer** (name, country and founding year are required)
2. **+ Add → Feature** (e.g. "Cruise control")
3. **+ Add → Vehicle**: pick the manufacturer and tick some features
4. Open **Vehicles** and try the search, manufacturer filter, price filter and sorting
5. Edit a vehicle (its manufacturer is locked), then delete it
6. Try deleting a manufacturer that still has vehicles

## Custom 404 page

With `DEBUG=True` Django shows its own error page. To see the custom one, set `DEBUG=False`, restart the server and open any unknown address, such as `/no-such-page/`. The stylesheet may not load in this mode, which is normal.

## Project structure

| App | Responsibility |
|---|---|
| `common` | Shared code: abstract base model, validators, home, about and error pages |
| `manufacturers` | The `Manufacturer` model, forms, views and templates |
| `vehicles` | The `Vehicle` and `Feature` models, forms, views and templates |

Templates live in `templates/` (a `base.html`, reusable `partials/`, and one folder per app) and the stylesheet in `static/css/`.

## Database design

```
Manufacturer ----< Vehicle >---- (many-to-many) ---- Feature
```

- `Vehicle` → `Manufacturer`: many-to-one (`PROTECT`)
- `Vehicle` ↔ `Feature`: many-to-many
- All models inherit from the abstract `TimeStampedModel` (`created_at`, `updated_at`)

## Forms and validation

- Custom labels, help texts, placeholders and error messages
- Disabled fields on the edit forms (manufacturer name, vehicle manufacturer)
- Validators for years, price, mileage and doors, and unique names
- Search and filter form on the vehicle list
- Redirect after every successful submission

## Notes

- Authentication and user management are intentionally not included.
- Logos and photos are links to images on other websites. Logos belong to their respective owners and are shown for demonstration only.
- Prices are shown in euros.

## Author

Erkan Mehmed
