from app import create_app, db
from app.models import User, Place

app = create_app('default')

with app.app_context():
    print("Creating database tables...")
    db.create_all()
    
    # Create Admin User if not exists
    if not User.query.filter_by(email='admin@tourist.com').first():
        print("Creating default admin user (admin@tourist.com / admin123)...")
        admin = User(username='admin', email='admin@tourist.com', is_admin=True)
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
    
    print("Database initialized successfully!")
    print("You can now run 'python run.py'")
