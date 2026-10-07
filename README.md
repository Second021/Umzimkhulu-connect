# Umzimkhulu Connect

A desktop community platform for Umzimkhulu, KwaZulu-Natal, built with Python and Tkinter. It gives residents one place to find local businesses, jobs, events, news and emergency contacts, and to report problems to the municipality.

## Features

**For residents**
- Create an account and sign in (passwords are stored hashed and salted)
- Dashboard with community statistics and charts
- Search the local business directory
- Browse jobs and opportunities, with requirements for each job
- View community events and news
- Report a community problem (water, roads, electricity, waste, safety) with an optional attached document or image
- Track the status of your own reports
- Emergency services contact list
- Settings: light/dark theme, notifications, change display name and password

**For administrators**
- Add, update and delete businesses, jobs and events
- Add and delete community news
- Manage reports and mark them as In Progress or Resolved

## Requirements

- Python 3.9 or newer
- Pillow (image support)
- Windows (opening attached documents uses `os.startfile`)

Tkinter and SQLite come with Python, so only Pillow needs installing:

```
pip install Pillow
```

## How to run

1. Download or clone this repository.
2. Keep the image files in the same folder as the Python file.
3. Run:

```
python Umzimkhulu_Connect.py
```

On first run the app creates its own database (`umzimkhulu_connect.db`) and fills in default jobs and local businesses. No database file is needed in the repository.

## Project files

| File | Purpose |
|------|---------|
| `Umzimkhulu_Connect.py` | The whole application |
| `umzimkhulu_CoA.png.png` | Background image for the login pages |
| `umzimkhulu_logo.png` | Logo on the welcome page (optional) |

Created automatically when the app runs:

- `umzimkhulu_connect.db` – the database
- `uploads/` – documents attached to reports

## Admin access

Administrator sign-in uses fixed demo credentials set in the code (`ADMIN_EMAIL` and `ADMIN_PASSWORD`). Change them before using the app for anything real.

## Notes

- This is a demo/learning project. The admin password reset screen does not change the fixed admin password.
- The database and uploads contain user data, so they are not stored in this repository.

## Author

Tshangase Sinentlantla – Final-year BSc IT student, North-West University
