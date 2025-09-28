# Daily Reports

A Django-based task management application that allows users to quickly create daily reports from selected tasks.

## Technology Stack

- **Frontend**: HTMX, Alpine.js, TailwindCSS 4.1.13, DaisyUI 5.1.24
- **Backend**: Django 5.2.6, Python 3.13.0
- **Database**: SQLite (development), PostgreSQL (production)

## Installation

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/eldarsadykov/DailyReports
   cd DailyReports
   ```

2. **Create and activate virtual environment**
   ```bash
   # Create virtual environment (works on most systems)
   python -m venv venv || python3 -m venv venv
   
   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows (Command Prompt):
   # venv\Scripts\activate.bat
   # On Windows (PowerShell):
   # venv\Scripts\Activate.ps1
   ```

3. **Install Python dependencies**
   ```bash
   # Upgrade pip (recommended)
   python -m pip install --upgrade pip
   
   # Install project dependencies
   pip install -r requirements.txt
   ```

4. **Install Node.js dependencies**
   ```bash
   npm install
   ```

5. **Set up the database**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Build static CSS and JS files**
   ```bash
   npm run build
   ```

## Usage

### Development Server

1. **Start the Django development server**
   ```bash
   python manage.py runserver
   ```

2. **Watch for CSS changes (optional, in another terminal)**
   ```bash
   npm run tailwind:watch
   ```

3. **Access the application**
   - Main application: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin/

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Future Enhancements

- [ ] Task categories and tags
- [ ] Due dates and reminders
- [ ] Export to different formats (PDF, CSV)
- [ ] Team collaboration features
- [ ] Mobile application
- [ ] API for third-party integrations
- [ ] Advanced reporting and analytics