# Livestock Management System - Backend API

Django REST Framework backend for the Livestock Management System.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Installation

1. **Create and activate virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables:**
```bash
cp .env.example .env
# Edit .env with your settings
```

4. **Run migrations:**
```bash
python manage.py migrate
```

5. **Create superuser:**
```bash
python manage.py createsuperuser
```

6. **Populate with sample data (optional):**
```bash
python manage.py populate_data
```

7. **Run development server:**
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

## 📚 API Documentation

### Interactive API Documentation
- **Swagger UI**: http://localhost:8000/api/docs/
- **API Schema**: http://localhost:8000/api/schema/

### Admin Panel
- **URL**: http://localhost:8000/admin/
- **Default credentials** (if using populate_data):
  - Username: `admin`
  - Password: `admin123`

## 🔐 Authentication

The API uses JWT (JSON Web Token) authentication.

### Obtain Token
```bash
POST /api/token/
{
    "username": "your_username",
    "password": "your_password"
}
```

### Refresh Token
```bash
POST /api/token/refresh/
{
    "refresh": "your_refresh_token"
}
```

### Using Token in Requests
```bash
Authorization: Bearer <your_access_token>
```

## 📡 API Endpoints

### Animals
- `GET /api/animals/` - List all animals
- `POST /api/animals/` - Create new animal
- `GET /api/animals/{id}/` - Get animal details
- `PUT /api/animals/{id}/` - Update animal
- `PATCH /api/animals/{id}/` - Partial update animal
- `DELETE /api/animals/{id}/` - Delete animal

### Owners
- `GET /api/owners/` - List all owners
- `POST /api/owners/` - Create new owner
- `GET /api/owners/{id}/` - Get owner details
- `PUT /api/owners/{id}/` - Update owner
- `PATCH /api/owners/{id}/` - Partial update owner
- `DELETE /api/owners/{id}/` - Delete owner

### Events
- `GET /api/events/` - List all events
- `POST /api/events/` - Create new event
- `GET /api/events/{id}/` - Get event details
- `PUT /api/events/{id}/` - Update event
- `PATCH /api/events/{id}/` - Partial update event
- `DELETE /api/events/{id}/` - Delete event

### Inventory
- `GET /api/inventory/` - List all inventory items
- `POST /api/inventory/` - Create new item
- `GET /api/inventory/{id}/` - Get item details
- `PUT /api/inventory/{id}/` - Update item
- `PATCH /api/inventory/{id}/` - Partial update item
- `DELETE /api/inventory/{id}/` - Delete item

### Reports
- `GET /api/reports/` - List all reports
- `POST /api/reports/` - Create new report
- `GET /api/reports/{id}/` - Get report details
- `PUT /api/reports/{id}/` - Update report
- `PATCH /api/reports/{id}/` - Partial update report
- `DELETE /api/reports/{id}/` - Delete report

## 🔍 Filtering & Search

All list endpoints support:
- **Filtering**: `?field=value`
- **Search**: `?search=query`
- **Ordering**: `?ordering=field` or `?ordering=-field` (descending)
- **Pagination**: `?page=1&page_size=10`

### Examples

```bash
# Filter animals by species
GET /api/animals/?species=cattle

# Search animals
GET /api/animals/?search=Holstein

# Order by weight descending
GET /api/animals/?ordering=-weight

# Combine filters
GET /api/animals/?species=cattle&status=healthy&ordering=tag_id
```

## 🗄️ Database Models

### Animal
- Basic info: tag_id, name, species, breed, gender, date_of_birth
- Physical: color, weight, image
- Ownership: owner, acquisition_date, acquisition_price
- Health: status, last_checkup, health_notes
- Breeding: mother_tag, father_tag

### Owner
- Personal: first_name, last_name, email, phone
- Address: address, city, state, zip_code, country
- Business: farm_name, farm_size, tax_id
- Status: is_active, notes

### Event
- event_type, animal, date, time
- title, description, cost
- veterinarian, location, notes
- attachments

### InventoryItem
- name, category, description, sku
- quantity, unit, reorder_level
- unit_price, supplier info
- last_purchased, expiry_date

### Report
- title, report_type, description
- data (JSON field)
- start_date, end_date
- file

## 🛠️ Development Commands

```bash
# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Populate sample data
python manage.py populate_data

# Run tests
python manage.py test

# Collect static files
python manage.py collectstatic
```

## 🚀 Production Deployment

1. **Update settings:**
   - Set `DEBUG=False`
   - Update `ALLOWED_HOSTS`
   - Use PostgreSQL instead of SQLite
   - Configure proper SECRET_KEY

2. **Environment variables:**
```env
DEBUG=False
SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=yourdomain.com
DB_ENGINE=django.db.backends.postgresql
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=5432
```

3. **Collect static files:**
```bash
python manage.py collectstatic --noinput
```

4. **Use production server:**
   - Gunicorn
   - uWSGI
   - Daphne (for ASGI)

## 📝 License

MIT License

## 👥 Support

For issues and questions, please create an issue in the repository.
