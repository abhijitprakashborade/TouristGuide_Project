import os
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from app import db
from app.models import Place, User, Feedback
from functools import wraps

admin = Blueprint('admin', __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('You do not have permission to access this page.', 'danger')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

@admin.route('/dashboard')
@login_required
@admin_required
def dashboard():
    place_count = Place.query.count()
    user_count = User.query.count()
    feedback_count = Feedback.query.count()
    # Show ALL places in the dashboard table
    places = Place.query.all()
    
    users = User.query.all()
    
    return render_template('admin/dashboard.html', 
                         place_count=place_count, 
                         user_count=user_count, 
                         feedback_count=feedback_count,
                         places=places,
                         users=users)

@admin.route('/places/add', methods=['GET', 'POST'])
@login_required
@admin_required
def add_place():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            description = request.form.get('description')
            category = request.form.get('category')
            # Handle potentially empty coordinates
            lat = request.form.get('latitude', 0.0)
            lon = request.form.get('longitude', 0.0)
            latitude = float(lat) if lat else 0.0
            longitude = float(lon) if lon else 0.0
            
            address = request.form.get('address')
            fee = request.form.get('entry_fee', 0.0)
            entry_fee = float(fee) if fee else 0.0
            
            # Image Upload
            image_file = request.files.get('image')
            filename = 'default_place.jpg'
            
            if image_file and image_file.filename != '':
                filename = secure_filename(image_file.filename)
                # Ensure upload folder exists
                if not os.path.exists(current_app.config['UPLOAD_FOLDER']):
                    os.makedirs(current_app.config['UPLOAD_FOLDER'])
                image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                image_file.save(image_path)
            elif request.form.get('image_url'):
                 # Logic for handling pasted URL could go here if implemented
                 pass
                
            place = Place(name=name, description=description, category=category,
                          latitude=latitude, longitude=longitude,
                          location_address=address, entry_fee=entry_fee,
                          image_file=filename)
                          
            db.session.add(place)
            db.session.commit()
            flash('New tourist place added successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding place: {str(e)}', 'danger')
            
        return redirect(url_for('admin.dashboard'))
        
    return render_template('admin/add_place.html')

@admin.route('/places/edit/<int:place_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_place(place_id):
    place = Place.query.get_or_404(place_id)
    if request.method == 'POST':
        try:
            place.name = request.form.get('name')
            place.description = request.form.get('description')
            place.category = request.form.get('category')
            place.location_address = request.form.get('address')
            
            lat = request.form.get('latitude')
            lon = request.form.get('longitude')
            if lat: place.latitude = float(lat)
            if lon: place.longitude = float(lon)
            
            fee = request.form.get('entry_fee')
            if fee: place.entry_fee = float(fee)
            
            image_file = request.files.get('image')
            if image_file and image_file.filename != '':
                filename = secure_filename(image_file.filename)
                image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                image_file.save(image_path)
                place.image_file = filename
                
            db.session.commit()
            flash('Place updated successfully!', 'success')
            return redirect(url_for('admin.dashboard'))
        except Exception as e:
            flash(f'Error updating place: {str(e)}', 'danger')

    return render_template('admin/edit_place.html', place=place)

@admin.route('/places/delete/<int:place_id>', methods=['POST'])
@login_required
@admin_required
def delete_place(place_id):
    place = Place.query.get_or_404(place_id)
    db.session.delete(place)
    db.session.commit()
    flash('Place deleted successfully!', 'success')
    return redirect(url_for('admin.dashboard'))

@admin.route('/users/delete/<int:user_id>', methods=['POST'])
@login_required
@admin_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    if user.is_admin:
        flash('Cannot delete admin user!', 'danger')
        return redirect(url_for('admin.dashboard'))
        
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!', 'success')
    return redirect(url_for('admin.dashboard'))
