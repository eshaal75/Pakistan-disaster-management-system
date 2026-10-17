# Pakistan Disaster Management System

## Project Overview
Pakistan faces many natural disasters every year, such as floods, heatwaves,
earthquakes and landslides. Information about these dangers is often spread
across different websites and is hard for ordinary people to follow.

This project is a web application, built mainly in Python, that brings this
information into one place. It will show live weather forecasts and recent
earthquakes for districts across Pakistan, automatically generate warnings
when conditions become dangerous, and display everything on an interactive map.
It will also show safety precautions and emergency numbers for each type of
disaster.


## Planned Features
- Live weather forecast (current + 7 days) using the Open-Meteo API
- Recent earthquakes using the USGS Earthquake API
- Automatic warnings (heavy rain, flood, landslide, heatwave, snow, strong wind,
  earthquake, smog) with severity levels: moderate, high, severe
- History of past disasters shown with warnings
- Interactive map with icons for each hazard
- Precautions (before, during, after) and emergency numbers
- User registration and login with a home district
- Admin panel to add incidents and post official alerts
- Dark-themed interface

## Technologies
- Python (Flask)
- requests library (for API calls)
- SQLite (using Python's sqlite3)
- HTML/CSS templates, with minimal JavaScript for the map

## Group Members
-Eshaal Nazir
-Sarah Arif 
-Hudaibia Rehman

## Current Status
**Milestone 1 – Requirements (completed)**
- [x] GitHub repository created
- [x] README added
- [x] Requirements document (docs/requirements.md and PDF)
- [x] Product backlog (docs/backlog.md)

**Next:** Milestone 2 – Flask setup and weather data (v0.2.0)

## Folder Structure
pakistan-disaster-management-system/
├── README.md
├── .gitignore
├── docs/
│ ├── requirements.md
│ ├── requirements.pdf
│ └── backlog.md
└── src/ (Python code will be added in later milestones)


## Version Plan
| Version | Content |
|---------|---------|
| v0.1.0 | Requirements and project setup |
| v0.2.0 | Flask setup and weather data |
| v0.3.0 | Map and warning rules |
| v0.4.0 | Earthquakes, disaster history and precautions |
| v0.5.0 | Login and admin panel |
| v0.6.0 | Air quality and tests (pytest) |
| v1.0.0 | First complete release |

## Emergency Numbers (Pakistan)
- Rescue: 1122
- Police: 15
- Fire Brigade: 16
- Edhi Ambulance: 115
