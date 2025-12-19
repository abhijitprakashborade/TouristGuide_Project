import requests
import os

UPLOAD_FOLDER = 'app/static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Full list of 21 places with reliable Unsplash High-Res URLs
places = [
    ("Red Fort", "red_fort.png", "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?q=80&w=1080&auto=format&fit=crop"),
    ("Taj Mahal", "taj_mahal.png", "https://images.unsplash.com/photo-1564507592333-c60657eea523?q=80&w=1080&auto=format&fit=crop"),
    ("Golden Temple", "golden_temple.png", "https://images.unsplash.com/photo-1582500445579-22a466904646?q=80&w=1080&auto=format&fit=crop"),
    ("Dal Lake", "dal_lake.png", "https://images.unsplash.com/photo-1598091383021-15ddea10925d?q=80&w=1080&auto=format&fit=crop"),
    ("Hadimba Devi Temple", "hadimba_devi_temple.png", "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?q=80&w=1080&auto=format&fit=crop"),
    ("Sultanpur Bird Sanctuary", "sultanpur_bird_sanctuary.png", "https://images.unsplash.com/photo-1605307040440-ae764726588b?q=80&w=1080&auto=format&fit=crop"),
    ("Gateway of India", "gateway_of_india.png", "https://images.unsplash.com/photo-1570168007204-dfb528c6958f?q=80&w=1080&auto=format&fit=crop"),
    ("Statue of Unity", "statue_of_unity.png", "https://images.unsplash.com/photo-1627894218731-50e5647702a4?q=80&w=1080&auto=format&fit=crop"),
    ("Amber Fort", "amber_fort.png", "https://images.unsplash.com/photo-1599661046289-e31897846e41?q=80&w=1080&auto=format&fit=crop"),
    ("Hampi Ruins", "hampi_ruins.png", "https://images.unsplash.com/photo-1600100598004-8d4e27f05046?q=80&w=1080&auto=format&fit=crop"),
    ("Alleppey Backwaters", "alleppey_backwaters.png", "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?q=80&w=1080&auto=format&fit=crop"),
    ("Meenakshi Temple", "meenakshi_temple.png", "https://images.unsplash.com/photo-1621334862657-3aa564619b88?q=80&w=1080&auto=format&fit=crop"),
    ("Charminar", "charminar.png", "https://images.unsplash.com/photo-1573397340182-0129205566f6?q=80&w=1080&auto=format&fit=crop"),
    ("Tirumala Temple", "tirumala_temple.png", "https://images.unsplash.com/photo-1643265842823-7fa34520773d?q=80&w=1080&auto=format&fit=crop"),
    ("Victoria Memorial", "victoria_memorial.png", "https://images.unsplash.com/photo-1558431382-27e30314225d?q=80&w=1080&auto=format&fit=crop"),
    ("Konark Sun Temple", "konark_sun_temple.png", "https://images.unsplash.com/photo-1626014902100-36d7a599689e?q=80&w=1080&auto=format&fit=crop"),
    ("Mahabodhi Temple", "mahabodhi_temple.png", "https://images.unsplash.com/photo-1628151015968-3a4429e9ef04?q=80&w=1080&auto=format&fit=crop"),
    ("Khajuraho Temples", "khajuraho_temples.png", "https://images.unsplash.com/photo-1590422749870-13f63125e04b?q=80&w=1080&auto=format&fit=crop"),
    ("Chitrakote Falls", "chitrakote_falls.png", "https://images.unsplash.com/photo-1624891122187-5f113a7c36a4?q=80&w=1080&auto=format&fit=crop"),
    ("Kaziranga National Park", "kaziranga_national_park.png", "https://images.unsplash.com/photo-1534177616072-ef7dc12044f9?q=80&w=1080&auto=format&fit=crop"),
    ("Living Root Bridges", "living_root_bridges.png", "https://images.unsplash.com/photo-1629864275069-4e76a6b8c8d2?q=80&w=1080&auto=format&fit=crop")
]

def download_images():
    print("Starting image downloads for all 21 places...")
    for name, filename, url in places:
        path = os.path.join(UPLOAD_FOLDER, filename)
        try:
            print(f"Downloading {name}...")
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                with open(path, "wb") as f:
                    f.write(response.content)
                print(f"MATCH: {filename}")
            else:
                print(f"FAILED: {name} (HTTP {response.status_code})")
        except Exception as e:
            print(f"ERROR: {name} - {e}")

if __name__ == "__main__":
    download_images()
