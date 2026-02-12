# 🍽️ La Cantine - Restaurant Website

A beautiful and functional restaurant website built with Flask, featuring online reservations, menu display, and contact information for "Amine La Cantine" restaurant.

## ✨ Features

- **Home Page**: Elegant landing page with video backgrounds and restaurant information
- **Interactive Menu**: Complete food and beverage menu with prices
- **Online Reservations**: Form-based reservation system with validation
- **Navigation**: Smooth navigation between pages with home buttons
- **Responsive Design**: Modern CSS styling with gradients and animations
- **Database Integration**: SQLite database with proper client-reservation relationships

## 🛠️ Technologies Used

- **Backend**: Flask 3.1.1
- **Database**: SQLAlchemy with SQLite
- **Forms**: Flask-WTF with validation
- **Frontend**: HTML5, CSS3, JavaScript
- **Fonts**: Google Fonts (Great Vibes, Yeseva One, Monoton, Roboto Mono)
- **Icons**: Font Awesome 6.5.0

## 📁 Project Structure

```
restaurant-project/
├── app.py                 # Main Flask application
├── database.py            # Database configuration
├── models.py              # Database models (Client, Reservation)
├── forms.py               # WTForms for reservation
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore file
├── static/               # Static files
│   ├── css/             # Stylesheets
│   ├── images/          # Images and videos
│   └── js/              # JavaScript files
└── templates/            # HTML templates
    ├── index.html       # Home page
    ├── menu.html        # Menu page
    ├── reservation.html # Reservation form
    ├── merci.html       # Thank you page
    └── contact.html     # Contact page
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone or download the project**
   ```bash
   cd restaurant-project
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   - Navigate to: `http://127.0.0.1:5000/`

## 📊 Database Schema

### Client Table
- `id` (Primary Key)
- `nom` (String, 50 chars)
- `prenom` (String, 50 chars)
- `telephone` (String, 15 chars)

### Reservation Table
- `id` (Primary Key)
- `date` (Date)
- `heure` (Time)
- `type_reservation` (String: VIP, Fête privée, À table)
- `nbr_person` (Integer)
- `notes` (String, 200 chars, optional)
- `client_id` (Foreign Key → Client)

**Relationship**: One client can have multiple reservations (One-to-Many)

## 🎯 Usage

### Making a Reservation

1. Navigate to the reservation page
2. Fill in the required information:
   - Name and surname
   - Phone number (5-15 digits)
   - Type of reservation (VIP, Private party, Table)
   - Number of guests (minimum 1)
   - Date (must be in the future)
   - Time
   - Optional notes
3. Submit the form
4. You'll be redirected to a confirmation page

### Viewing the Menu

- Click "menu" in the navigation or visit `/menu`
- Browse through different sections:
  - Cold appetizers
  - Hot appetizers
  - Salads
  - Main dishes
  - Pasta
  - Drinks (hot & cold)
  - Desserts
  - Special items (Paella, Mechoui)

## 🔒 Security Features

- CSRF protection on all forms
- Server-side form validation
- SQL injection prevention via SQLAlchemy ORM
- Secure secret key configuration

## 📝 Configuration

The application uses environment variables for configuration:

- `SECRET_KEY`: Flask secret key (defaults to 'dev-secret-key-change-in-production')
- `DATABASE_URL`: Database connection string (defaults to 'sqlite:///amine.db')

## 🌐 Restaurant Locations

### Hydra
- Phone: 0 20 30 77 77 / 06 66 19 93 17
- [View on Maps](https://maps.app.goo.gl/pXwmHHzTbZz3c9Rs8)

### Staoueli
- Phone: 05 60 09 73 92
- [View on Maps](https://maps.app.goo.gl/w1spLWZ9cZaKoE7V8)

## 📱 Social Media

- Instagram: [@amine_la_cantine](https://www.instagram.com/amine_la_cantine/)

## 👨‍💻 Development

### Running in Debug Mode

The application runs in debug mode by default when executed with `python app.py`. This provides:
- Auto-reload on code changes
- Detailed error pages
- Interactive debugger

### Database Migrations

To reset the database:
1. Stop the application
2. Delete `instance/amine.db`
3. Restart the application (database will be recreated automatically)

## 📄 License

This project is created for "Amine La Cantine" restaurant.

## 🤝 Credits

- Design & Development: [@zaki](https://api.whatsapp.com/send/?phone=%2B213549337621)
- Restaurant: Amine La Cantine (Since 2021)

---

**Made with ❤️ for  better food  experience **
