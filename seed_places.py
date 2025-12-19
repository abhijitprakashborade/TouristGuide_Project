from app import create_app, db
from app.models import Place
import os

app = create_app('default')

def seed_places():
    # Helper to create if not exists
    def add_place(data):
        existing = Place.query.filter_by(name=data['name']).first()
        if not existing:
            place = Place(**data)
            db.session.add(place)
            print(f"Added {place.name}")
        else:
            # Update existing to ensure data matches exactly
            existing.description = data['description']
            existing.entry_fee = data['entry_fee']
            existing.category = data['category']
            existing.location_address = data['location_address']
            existing.image_file = data['image_file'] # Force update image
            existing.latitude = data['latitude']
            existing.longitude = data['longitude']
            print(f"Updated {existing.name}")

    places_data = [
        {
            "name": "Red Fort",
            "category": "Historical",
            "location_address": "New Delhi, Delhi",
            "description": "A massive red sandstone fort that was the main home of the Mughal emperors for nearly 200 years. Famous for its stunning architecture and history.",
            "entry_fee": 35.0,
            "image_file": "red_fort.png",
            "latitude": 28.6562,
            "longitude": 77.2410
        },
        {
            "name": "Taj Mahal",
            "category": "Historical",
            "location_address": "Agra, Uttar Pradesh",
            "description": "One of the Seven Wonders of the World. A beautiful white marble mausoleum built by Mughal emperor Shah Jahan for his wife Mumtaz Mahal.",
            "entry_fee": 50.0,
            "image_file": "taj_mahal.png",
            "latitude": 27.1751,
            "longitude": 78.0421
        },
        {
            "name": "Golden Temple",
            "category": "Historical",
            "location_address": "Amritsar, Punjab",
            "description": "The holiest shrine of Sikhism. It is plated with real gold and surrounded by a sacred pool. Open to people of all faiths.",
            "entry_fee": 0.0,
            "image_file": "golden_temple.png",
            "latitude": 31.6200,
            "longitude": 74.8765
        },
        {
            "name": "Dal Lake",
            "category": "Nature",
            "location_address": "Srinagar, Jammu & Kashmir",
            "description": "Known as the 'Jewel in the crown of Kashmir'. Famous for its houseboats, shikaras, and floating gardens.",
            "entry_fee": 0.0,
            "image_file": "dal_lake.png",
            "latitude": 34.1124,
            "longitude": 74.8398
        },
        {
            "name": "Hadimba Devi Temple",
            "category": "Religious",
            "location_address": "Manali, Himachal Pradesh",
            "description": "An ancient cave temple dedicated to Hidimbi Devi, wife of Bhima. Surrounded by a cedar forest.",
            "entry_fee": 0.0,
            "image_file": "hadimba_devi_temple.png",
            "latitude": 32.2483,
            "longitude": 77.1805
        },
        {
            "name": "Sultanpur Bird Sanctuary",
            "category": "Park",
            "location_address": "Gurgaon, Haryana",
            "description": "A popular national park for bird watchers. Home to hundreds of migratory and resident bird species.",
            "entry_fee": 40.0,
            "image_file": "sultanpur_bird_sanctuary.png",
            "latitude": 28.4619,
            "longitude": 76.8923
        },
        {
            "name": "Gateway of India",
            "category": "Historical",
            "location_address": "Mumbai, Maharashtra",
            "description": "An arch monument built during the 20th century. It is the city's top tourist attraction and overlooks the Arabian Sea.",
            "entry_fee": 0.0,
            "image_file": "gateway_of_india.png",
            "latitude": 18.9220,
            "longitude": 72.8347
        },
        {
            "name": "Statue of Unity",
            "category": "Historical",
            "location_address": "Kevadia, Gujarat",
            "description": "The world's tallest statue, dedicated to Sardar Vallabhbhai Patel. It stands 182 meters high overlooking the Narmada dam.",
            "entry_fee": 150.0,
            "image_file": "statue_of_unity.png",
            "latitude": 21.8380,
            "longitude": 73.7191
        },
        {
            "name": "Amber Fort",
            "category": "Historical",
            "location_address": "Jaipur, Rajasthan",
            "description": "A majestic fort located on a high hill. Known for its artistic style elements, blending Hindu and Rajput elements.",
            "entry_fee": 100.0,
            "image_file": "amber_fort.png",
            "latitude": 26.9855,
            "longitude": 75.8513
        },
        {
            "name": "Hampi Ruins",
            "category": "Historical",
            "location_address": "Hampi, Karnataka",
            "description": "A UNESCO World Heritage site containing ruins of the ancient Vijayanagara Empire, featuring stunning stone temples.",
            "entry_fee": 40.0,
            "image_file": "hampi_ruins.png",
            "latitude": 15.3350,
            "longitude": 76.4600
        },
        {
            "name": "Alleppey Backwaters",
            "category": "Nature",
            "location_address": "Alleppey, Kerala",
            "description": "Famous backwaters of Kerala. A network of brackish lagoons and lakes known for houseboat cruises.",
            "entry_fee": 0.0,
            "image_file": "alleppey_backwaters.png",
            "latitude": 9.4981,
            "longitude": 76.3388
        },
        {
            "name": "Meenakshi Temple",
            "category": "Religious",
            "location_address": "Madurai, Tamil Nadu",
            "description": "A historic Hindu temple located on the southern bank of the Vaigai River. Known for its towering gopurams.",
            "entry_fee": 0.0,
            "image_file": "meenakshi_temple.png",
            "latitude": 9.9195,
            "longitude": 78.1198
        },
        {
            "name": "Charminar",
            "category": "Historical",
            "location_address": "Hyderabad, Telangana",
            "description": "The global icon of Hyderabad, listed among the most recognized structures in India. Built in 1591.",
            "entry_fee": 25.0,
            "image_file": "charminar.png",
            "latitude": 17.3616,
            "longitude": 78.4747
        },
        {
            "name": "Tirumala Temple",
            "category": "Religious",
            "location_address": "Tirupati, Andhra Pradesh",
            "description": "A Hindu temple dedicated to Venkateswara, a form of Vishnu. It is the richest temple in the world in terms of donations.",
            "entry_fee": 0.0,
            "image_file": "tirumala_temple.png",
            "latitude": 13.6833,
            "longitude": 79.3472
        },
        {
            "name": "Victoria Memorial",
            "category": "Historical",
            "location_address": "Kolkata, West Bengal",
            "description": "A large marble building dedicated to the memory of Queen Victoria. It is a museum and tourist destination.",
            "entry_fee": 30.0,
            "image_file": "victoria_memorial.png",
            "latitude": 22.5448,
            "longitude": 88.3426
        },
        {
            "name": "Konark Sun Temple",
            "category": "Historical",
            "location_address": "Konark, Odisha",
            "description": "A 13th-century Sun Temple. The temple is attributed to king Narasimhadeva I of the Eastern Ganga Dynasty.",
            "entry_fee": 40.0,
            "image_file": "konark_sun_temple.png",
            "latitude": 19.8876,
            "longitude": 86.0945
        },
        {
            "name": "Mahabodhi Temple",
            "category": "Religious",
            "location_address": "Bodh Gaya, Bihar",
            "description": "A UNESCO World Heritage Site, it says this is where the Buddha is said to have attained enlightenment.",
            "entry_fee": 0.0,
            "image_file": "mahabodhi_temple.png",
            "latitude": 24.6960,
            "longitude": 84.9914
        },
        {
            "name": "Khajuraho Temples",
            "category": "Historical",
            "location_address": "Chhatarpur, Madhya Pradesh",
            "description": "A group of Hindu and Jain temples famous for their nagara-style architectural symbolism and erotic sculptures.",
            "entry_fee": 40.0,
            "image_file": "khajuraho_temples.png",
            "latitude": 24.8318,
            "longitude": 79.9199
        },
        {
            "name": "Chitrakote Falls",
            "category": "Nature",
            "location_address": "Bastar, Chhattisgarh",
            "description": "Often called the Niagara Falls of India. The widest waterfall in India, located on the Indravati River.",
            "entry_fee": 0.0,
            "image_file": "chitrakote_falls.png",
            "latitude": 19.2056,
            "longitude": 81.7088
        },
        {
            "name": "Kaziranga National Park",
            "category": "Park",
            "location_address": "Kanchanst, Assam",
            "description": "A World Heritage Site, hosting two-thirds of the world's great one-horned rhinoceroses.",
            "entry_fee": 100.0,
            "image_file": "kaziranga_national_park.png",
            "latitude": 26.5775,
            "longitude": 93.1711
        },
        {
            "name": "Living Root Bridges",
            "category": "Nature",
            "location_address": "Meghalaya",
            "description": "Suspension bridges formed of living plant roots by tree shaping. A unique attraction of Meghalaya.",
            "entry_fee": 0.0,
            "image_file": "living_root_bridges.png",
            "latitude": 25.2533,
            "longitude": 91.6826
        }
    ]

    with app.app_context():
        print("Seeding places...")
        for p_data in places_data:
            add_place(p_data)
        
        db.session.commit()
        print("Seeding complete!")

if __name__ == '__main__':
    seed_places()
