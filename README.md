# Daily Reports - Task Manager

A Django-based task management application that allows users to create, manage, and track their daily tasks with progress tracking. The application features a modern, responsive interface built with TailwindCSS, DaisyUI, and HTMX for dynamic interactions.

## Features

- 🔐 **User Authentication** - Secure login/logout functionality
- ✅ **Task Management** - Create, read, update, and delete tasks
- 📊 **Progress Tracking** - Track task completion with percentage progress (0-100%)
- 🔍 **Real-time Search** - Search tasks by key or name with live updates
- 📋 **Clipboard Integration** - Copy selected tasks with formatted date for daily reports
- 📱 **Responsive Design** - Mobile-friendly interface using TailwindCSS and DaisyUI
- ⚡ **Dynamic UI** - HTMX-powered interactions without page refreshes
- 🎨 **Modern Styling** - Clean, professional interface with Alpine.js components

## Technology Stack

- **Backend**: Django 5.2.6
- **Database**: SQLite (development)
- **Frontend**: TailwindCSS 4.1.13, DaisyUI 5.1.24
- **JavaScript**: HTMX, Alpine.js
- **Python**: 3.13.0

## Project Structure

```
DailyReports/
├── DailyReports/          # Django project configuration
│   ├── settings.py        # Project settings
│   ├── urls.py           # URL routing
│   └── wsgi.py           # WSGI configuration
├── tasks/                # Main application
│   ├── models.py         # User and Task models
│   ├── views.py          # View functions
│   ├── forms.py          # Django forms
│   ├── urls.py           # App URL patterns
│   └── templates/        # HTML templates
├── manage.py             # Django management script
├── package.json          # Node.js dependencies
├── Pipfile              # Python dependencies
└── README.md            # This file
```

## Installation

### Prerequisites

- Python 3.13.0
- Node.js (for TailwindCSS compilation)
- pip and pipenv

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd DailyReports
   ```

2. **Install Python dependencies**
   ```bash
   pipenv install
   pipenv shell
   ```

3. **Install Node.js dependencies**
   ```bash
   npm install
   ```

4. **Set up the database**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Build CSS assets**
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
   npm run watch
   ```

3. **Access the application**
   - Main application: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin/

### Application Features

#### Task Management
- **Add Task**: Click "Add New Task" to create a new task with a unique key, name, and progress percentage
- **Edit Task**: Click on any task row to edit its details
- **Delete Task**: Use the delete button to remove tasks
- **Search**: Use the search bar to find tasks by key or name in real-time

#### Daily Reports
- **Select Tasks**: Use checkboxes to select completed or in-progress tasks
- **Copy to Clipboard**: Click "Copy To Clipboard" to generate a formatted daily report with today's date
- **Format**: Reports include the current date in Russian format followed by selected task details

## Models

### User Model
Extends Django's AbstractUser for authentication.

### Task Model
- `key`: Unique identifier for the task (max 10 characters)
- `name`: Task description (max 255 characters)
- `progress`: Integer field (0-100) representing completion percentage
- `created_at`: Timestamp of task creation
- `user`: Foreign key to User model

## API Endpoints

- `GET /` - Task list and management interface
- `GET /search/` - Search tasks (HTMX endpoint)
- `POST /create/` - Create new task (HTMX endpoint)
- `GET /edit/<pk>/` - Edit task form (HTMX endpoint)
- `POST /update/<pk>/` - Update task (HTMX endpoint)
- `DELETE /delete/<pk>/` - Delete task (HTMX endpoint)

## Scripts

- `npm run build` - Build TailwindCSS for production
- `npm run watch` - Watch for changes and rebuild CSS automatically
- `python manage.py runserver` - Start development server
- `python manage.py migrate` - Apply database migrations
- `python manage.py createsuperuser` - Create admin user

## Configuration

### Environment Settings
- Debug mode is enabled by default
- SQLite database for development
- Custom User model defined in `tasks.User`
- Login redirects to `/admin/`

### Security Notes
⚠️ **Important**: This project includes a hardcoded Django secret key and has DEBUG=True. These settings are suitable for development only and should be properly configured for production deployment.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is for personal/educational use. Please add an appropriate license file if you plan to distribute it.

## Future Enhancements

- [ ] Task categories and tags
- [ ] Due dates and reminders
- [ ] Export to different formats (PDF, CSV)
- [ ] Team collaboration features
- [ ] Mobile application
- [ ] API for third-party integrations
- [ ] Advanced reporting and analytics