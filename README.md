# Advanced Intelligent Tourist Guide System 🌍✈️

An AI-powered web application that generates personalized travel itineraries, explores tourist attractions across India, and offers a premium mobile-friendly user experience.

![Hero]((https://images.unsplash.com/photo-1532559685660-72133499426f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80))

## ✨ Key Features

- **🤖 AI Itinerary Planner**: optimized trip generation based on your budget, city, and interests using an advanced genetic algorithm.
- **📱 Mobile-First Design**: Fully responsive UI with a native-app feel, including a bottom-sheet Chat Widget.
- **🗺️ Interactive Exploration**: Explore places via an interactive map and filter by category (Historical, Nature, Parks).
- **🎨 Premium UI**: Glassmorphism effects, smooth animations, and a polished "Popup Card" aesthetic.
- **🔐 Secure Authentication**: User login and registration with strong password hashing.
- **🛠️ Admin Panel**: comprehensive dashboard for managing destinations and user feedback.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
    cd AntiGravity
    ```

2.  **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Initialize the Database**:
    ```bash
    python init_db.py
    python seed_places.py # Populates the DB with initial tourist data
    ```

5.  **Run the Application**:
    ```bash
    python run.py
    ```

Visit `http://localhost:5000` in your browser.

## 📱 Mobile Access

To run the app on your mobile device (on the same Wi-Fi network):

1.  Run the server: `python run.py` (It is configured to listen on `0.0.0.0`).
2.  Find your computer's local IP (e.g., `192.168.1.101`).
3.  Open your mobile browser and go to `http://<YOUR_IP>:5000`.

## 🛠️ Tech Stack

-   **Backend**: Flask (Python), SQLAlchemy (SQLite)
-   **Frontend**: HTML5, CSS3, JavaScript
-   **Mapping**: Leaflet.js, OpenStreetMap
-   **Algorithms**: Custom Genetic Algorithm for route optimization

## 📂 Project Structure

```
AntiGravity/
├── app/
│   ├── routes/       # Route handlers (main, auth, admin)
│   ├── static/       # CSS, JS, Images, Uploads
│   ├── templates/    # HTML Templates
│   ├── models.py     # Database Models
│   └── utils/        # Recommendation logic
├── init_db.py        # Database setup script
├── seed_places.py    # Data seeding script
├── run.py            # Entry point
└── requirements.txt  # Dependencies
```

## 🛡️ License

This project is open-source and available under the [MIT License](LICENSE).
