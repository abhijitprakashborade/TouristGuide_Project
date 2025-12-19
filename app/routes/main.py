from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app.models import Place, Feedback
from app import db
import time

main = Blueprint('main', __name__)

@main.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_msg = data.get('message', '').lower()
    
    # Simple RAG Logic (Keyword Search)
    response = ""
    
    # 1. Keywords Extraction
    keywords = {
        'historical': 'Historical', 'history': 'Historical', 'fort': 'Historical',
        'nature': 'Nature', 'park': 'Park', 'green': 'Nature',
        'temple': 'divine', 'spiritual': 'divine',
        'cheap': 'budget', 'budget': 'budget', 'free': 'free'
    }
    
    found_places = []
    
    # 2. Search DB
    places = Place.query.all()
    for place in places:
        # Check against mapped keywords or direct name match
        matched = False
        if user_msg in place.name.lower():
            matched = True
        
        for k, v in keywords.items():
            if k in user_msg and (v == place.category or (k == 'cheap' and place.entry_fee < 500) or (k == 'free' and place.entry_fee == 0)):
                matched = True
                
        if matched:
            found_places.append(place)
            
    # 3. Generate Response
    if found_places:
        top_places = found_places[:3] # Limit to 3
        response = f"I found {len(found_places)} places that might interest you!\n\n"
        for p in top_places:
            response += f"📍 **{p.name}** ({p.category})\n{p.description[:80]}...\n💰 Fee: ₹{p.entry_fee}\n\n"
        if len(found_places) > 3:
            response += f"And {len(found_places)-3} more! Check the Explore page for details."
    else:
        response = "I couldn't find specific places matching that exactly. \n\nTry asking for 'Historical places', 'Nature spots', or specific cities like 'Delhi' or 'Mumbai'."

    return jsonify({'reply': response})

@main.route('/')
def index():
    # User requested to see ALL places on the main page
    featured_places = Place.query.all()
    return render_template('index.html', featured_places=featured_places)

@main.route('/explore')
def explore():
    page = request.args.get('page', 1, type=int)
    state_filter = request.args.get('state')
    category_filter = request.args.get('category')
    
    query = Place.query
    
    if state_filter and state_filter != 'All':
        query = query.filter(Place.location_address.like(f'%{state_filter}%'))
    
    if category_filter and category_filter != 'All' and category_filter != 'None':
         query = query.filter_by(category=category_filter)

    places = query.paginate(page=page, per_page=12)
    
    # Get all unique states from addresses for the dropdown
    all_places = Place.query.with_entities(Place.location_address).all()
    states = set()
    for p in all_places:
        if ',' in p.location_address:
            # Assumes format "City, State"
            state_part = p.location_address.split(',')[-1].strip()
            states.add(state_part)
            
    sorted_states = sorted(list(states))
    
    return render_template('explore.html', places=places, states=sorted_states, current_state=state_filter)

@main.route('/plan_trip', methods=['GET', 'POST'])
def plan_trip():
    if request.method == 'POST':
        try:
            budget = float(request.form.get('budget'))
            city = request.form.get('city')
            interests = request.form.getlist('interests')
            
            # Smart Logic: Filter places where entry_fee <= budget
            # And match categories if selected
            query = Place.query.filter(Place.entry_fee <= budget)
            
            if interests:
                # Basic OR filtering for interests
                query = query.filter(Place.category.in_(interests))
            
            recommended_places = query.limit(5).all()
            
            return render_template('trip_results.html', places=recommended_places, budget=budget, city=city)
        except ValueError:
             flash('Please enter a valid budget amount.', 'error')
             return redirect(url_for('main.plan_trip'))
             
    return render_template('plan_trip.html')

@main.route('/plan')
def plan_tour():
    return render_template('plan_trip.html') # Alias old route if exists

@main.route('/place/<int:place_id>')
def place_details(place_id):
    place = Place.query.get_or_404(place_id)
    return render_template('place_details.html', place=place)

@main.route('/place/<int:place_id>/review', methods=['POST'])
@login_required
def add_review(place_id):
    place = Place.query.get_or_404(place_id)
    rating = request.form.get('rating')
    comment = request.form.get('comment')
    
    if not rating:
        flash('Please select a rating.', 'warning')
        return redirect(url_for('main.place_details', place_id=place_id))
        
    feedback = Feedback(user_id=current_user.id, place_id=place.id,
                        rating=int(rating), comment=comment)
    db.session.add(feedback)
    db.session.commit()
    flash('Thank you for your review!', 'success')
    return redirect(url_for('main.place_details', place_id=place.id))
