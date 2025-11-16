# stadcal
Name stadcal comes from städalliansen and calendar.
Starts a webserver that provides downloads of a ics file, which calendars can subscribe to

## technology stack from bottom to top
1. Python
    a. playwright to parse stadalliansen.se and get the calendar events data
    b. icalendar to create the event data to a icalendar format
    b. apscheduler to periodically refresh the events
    c. flask to serve the events, making them subscribable by calendar applications
    d. toml to configure the application
2. Gunicorn as http server
3. setuptools and pyproject.toml to build the python package
4. Nix to package stadcal as a package and as a nixos systemd service, made available through flake


## Features

### broken ics
If the application fails it will display a calendar with an event today with summary text "stadalliansen broken" to inform the user to take action

### service file
Can enable, set listenAddress, and port.

## Miscellaneous

### Enable browsers in nix
Source here https://nixos.wiki/wiki/Playwright will inline summary
For playwright to work in nix, one has to set two environment variables:
PLAYWRIGHT_BROWSERS_PATH=${pkgs.playwright-driver.browsers}
PLAYWRIGHT_SKIP_VALIDATE_HOST_REQUIREMENTS=true
That is because if playwright installs the browsers themselves they wont work in nixos.
