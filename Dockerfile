# --- Build backend ---
    FROM python:3.11
    ENV PYTHONDONTWRITEBYTECODE 1
    ENV PYTHONUNBUFFERED 1
    
    # Set workdir to /app
    WORKDIR /app
    
    # Copy ALL files (including manage.py and requirements.txt)
    COPY . .
    
    # Install dependencies
    RUN pip install -r requirements.txt
    
    # Collect static files
    RUN python manage.py collectstatic --noinput
    
    # Run Gunicorn
    CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000", "--timeout", "120"]