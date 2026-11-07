# 🌦️ Weather Reporter Bot

A Python-based Weather Reporting Application that fetches real-time weather
information using the OpenWeatherMap API.

## 🚀 Features

- Search weather information by city name.
- Get real-time temperature.
- Display feels-like temperature.
- Show humidity levels.
- Display wind speed and direction.
- Handle API errors and exceptions.
- Logging system for error tracking.
- Secure API key management using environment variables.

## 🛠️ Technologies Used

- Python
- Requests
- OpenWeatherMap API
- Python-dotenv
- Logging
- Git & GitHub

## 📁 Project Structure

```text
Weather_Reporter_Bot/
│
├── venv/
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
│
├── config.py
├── logger_setup.py
├── localization.py
├── weather_client.py
└── main.py
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Weather-Reporter-Bot.git
```

### 2. Navigate to the Project Folder

```bash
cd Weather-Reporter-Bot
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure API Key

Create a `.env` file in the project root directory.

Add your OpenWeatherMap API key:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

Get your API key from:

https://openweathermap.org/api

### 7. Run the Application

```bash
python main.py
```

## 📡 API Information

This project uses the OpenWeatherMap Current Weather API to retrieve real-time
weather data.

API Documentation:

https://openweathermap.org/current

## 🔐 Security

- API keys are stored in environment variables.
- The `.env` file is excluded using `.gitignore`.
- Never upload your private API key to GitHub.

## 📚 What I Learned

Through this project, I practiced:

- Python functions and modules.
- REST API integration.
- HTTP requests using Requests.
- JSON data processing.
- Exception handling.
- Logging and debugging.
- Environment variable management.
- Virtual environments.
- Git and GitHub.

## 👨‍💻 Author

**Jinnatul Islam Tain**

GitHub: https://github.com/Tain-13

---

⭐ If you find this project useful, consider giving it a star!
