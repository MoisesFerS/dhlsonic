# CHANGELOG

All changes made to the project will be listed here.

Format based on:

- [Keep a Changelog](https://keepachangelog.com/)
- [Semantic Versioning](https://semver.org/)

## [0.4.0] - 2025-08-08 - App Creation: Schedule

### Added

- Created the `schedule` app to manage work schedules.
- Created the `schedule/templates/schedule/` folder containing:
    - `index.html` – Page containing the calendar for each schedule.
- Created the `static/schedule/` folder containing:
    - `index.css` – Styles for the calendar page.

### Changed

- Updated `dhlsonic/urls.py` to route the `/schedule` path to the `schedule` app.
- Updated the navbar to redirect the corresponding button to the `schedule` page.
- Registered the `schedule` app in `INSTALLED_APPS` in `settings.py`.

## [0.3.0] - 2025-08-07 - Docker and phpMyAdmin

### Added

- Created the `docker-compose.yml` file to configure and coordinate containers.
- Created the `Dockerfile` to build the Docker image.

### Changed

- Updated `settings.py` to connect to the dockerized database.
- Updated the requirements section in `README.md` to include Docker.
- Updated `requirements.txt` to include `mysqlclient`.

## [0.2.0] - 2025-08-07 - App Creation: Core

### Added

- Created the `core` app to manage the main views and templates.
- Created the `core/templates/` folder containing:
    - `base.html` – Base structure used across all pages.
    - `index.html` – Main landing page.
    - `partials/` – Stores partial components used in `base.html`:
        - `header.html` – Header structure of the page.
        - `footer.html` – Footer structure of the page.
- Created the `static/` folder containing:
    - `css/` – Stores stylesheets used in the project.
        - `core/` – Contains styles specific to the `core` app:
            - `styles.css` – Main stylesheet of the project.
            - `header.css` – Styles for the header section.
            - `footer.css` – Styles for the footer section.
    - `fonts/` – Stores fonts used in the project.
    - `icons/` – Stores icon files.
    - `images/` – Stores image assets.
    - `js/` – Stores JavaScript files used in the project.
- Added views to `core/views.py`:
    - `index` – Renders the main page.
- Added `logo.png` to `static/images/`.
- Added `favicon.ico` to `static/icons/`.

### Changed

- Registered the `core` app in `INSTALLED_APPS` in `settings.py`.
- Updated `dhlsonic/urls.py` to route the default path to the `core` app.

## [0.1.0] - 2025-08-07 - Project Initialization

### Added

- Created files:
    - `.gitignore` – Keeps unwanted files out of the repository.
    - `CHANGELOG.md` – Track changes made to the project.
    - `README.md` – Describes the purpose of the project and lists its features.
    - `requirements.txt` – Lists the project's dependencies.
- Created the django project `dhlsonic` and made basic configurations.

### Changed

- Updated the `README.md`.