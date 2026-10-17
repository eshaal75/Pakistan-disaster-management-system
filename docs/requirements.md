# Requirements Document
## Pakistan Disaster Management System

**Course:** Software Construction & Development
**Version:** 0.1 (this document will be updated as the project evolves, following an Agile approach)

## 1. Group Members
-ESHAAL NAZIR
-SARAH ARIF
-HUDAIBIA REHMAN
## 2. Problem Description

Pakistan is one of the countries most affected by natural disasters. Every year
people face floods, heavy rain, heatwaves, landslides, snowfall, smog and
earthquakes. The 2022 floods affected millions of people, and in 2025 flash
floods in Buner and Swat caused heavy loss of life.

Weather and disaster information is available, but it is spread across many
different websites and apps. Most of it is technical and hard for ordinary
people to understand. People often do not know if their own district is in
danger, how serious the danger is, or what they should do to stay safe.

Our project solves this by bringing live weather data, earthquake data,
automatic warnings, past disaster history and safety precautions together in
one simple web application with a map.

## 3. Objectives

1. Show live weather forecasts (current and 7 days) for districts across Pakistan.
2. Show recent earthquakes in and near Pakistan.
3. Automatically generate disaster warnings with severity levels
   (moderate, high, severe) using simple rules.
4. Show warnings and hazards on an interactive map so users can see danger
   areas easily.
5. Remind users of past disasters in their area so they take warnings seriously.
6. Give clear safety precautions and emergency numbers for each type of disaster.
7. Allow admins to post official alerts and add incidents.

## 4. Intended Users

**General Public:** Ordinary people in Pakistan who want to check weather and
danger warnings for their district. They can view the map and warnings without
logging in, and can register to save their home district.

**Registered Users:** Users who create an account and choose a home district,
so they can quickly see warnings for their own area.

**Admins:** Trusted people (for example, the project team acting as an
authority) who can post official alerts and add incidents on the map.

## 5. Functional Requirements

Functional requirements describe what the system must do.

**Weather and Earthquakes**
- FR1: The system shall fetch current weather and a 7-day forecast for
  Pakistani districts from the Open-Meteo API.
- FR2: The system shall fetch recent earthquakes in and around Pakistan from
  the USGS Earthquake API.
- FR3: The system shall store the list of districts with their names and
  map coordinates in the database.

**Warnings**
- FR4: The system shall automatically check weather and earthquake data
  against threshold rules written in Python.
- FR5: The system shall generate warnings for heavy rain, flood, landslide,
  heatwave, snow, strong wind, earthquake and smog.
- FR6: The system shall give each warning a severity level: moderate, high
  or severe.

**Map**
- FR7: The system shall display districts, warnings and earthquakes on an
  interactive map of Pakistan.
- FR8: The system shall use a different icon or emoji for each type of hazard.
- FR9: The system shall show warning details when a user clicks a map marker.

**Disaster History**
- FR10: The system shall store records of past disasters (such as the 2005
  earthquake, 2022 floods and 2025 Buner/Swat flash floods).
- FR11: The system shall show a history note with a warning when that area
  had a similar disaster before.

**Precautions**
- FR12: The system shall show precautions for before, during and after each
  type of disaster.
- FR13: The system shall show emergency numbers: Rescue 1122, Police 15,
  Fire 16 and Edhi 115.

**Users**
- FR14: The system shall allow users to register with a username and password.
- FR15: The system shall allow registered users to log in and log out.
- FR16: The system shall allow users to choose and change their home district.

**Admin**
- FR17: The system shall allow admins to add incidents on the map.
- FR18: The system shall allow admins to post official alerts.
- FR19: The system shall prevent normal users from opening admin pages.

## 6. Non-Functional Requirements

Non-functional requirements describe how well the system should work.

- NFR1 (Usability): The interface shall be simple, use clear language, and
  use a dark theme.
- NFR2 (Performance): Pages shall load within about 5 seconds on a normal
  internet connection.
- NFR3 (Security): User passwords shall be stored in hashed form, never as
  plain text.
- NFR4 (Reliability): If an external API fails, the system shall show an
  error message instead of crashing.
- NFR5 (Maintainability): The code shall be written mainly in Python, divided
  into small functions with clear names and comments.
- NFR6 (Portability): The system shall run on a normal Windows computer
  using free tools only.
- NFR7 (Cost): The system shall use only free APIs that do not need an
  API key.
- NFR8 (Testability): Important Python functions, such as the warning rules,
  shall be tested using pytest.
