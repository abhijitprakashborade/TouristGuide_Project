import requests
import os

UPLOAD_FOLDER = 'app/static/uploads'

# Specific, reliable IDs for the problematic places
fixes = [
    # Golden Temple - Verified Alternative View
    {
        "filename": "golden_temple.png",
        "url": "https://plus.unsplash.com/premium_photo-1697729600773-5b8398cb74cb?q=80&w=1080&auto=format&fit=crop"
    },
    # Red Fort - Verified View
    {
        "filename": "red_fort.png",
        "url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?q=80&w=1080&auto=format&fit=crop"
    },
    # Living Root Bridges - Nature View
    {
        "filename": "living_root_bridges.png",
        "url": "https://images.unsplash.com/photo-1518005068251-37900150dfca?q=80&w=1080&auto=format&fit=crop"
    },
    # Chitrakote Falls - Waterfall View
    {
        "filename": "chitrakote_falls.png",
        "url": "https://images.unsplash.com/photo-1432405972618-c60b0225b8f9?q=80&w=1080&auto=format&fit=crop"
    },
    # Kaziranga - Rhino/Nature View
    {
        "filename": "kaziranga_national_park.png",
        "url": "https://images.unsplash.com/photo-1575550959106-5a7defe28b56?q=80&w=1080&auto=format&fit=crop"
    }
]

def fix_images():
    print("Fixing specific images...")
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
        
    for item in fixes:
        path = os.path.join(UPLOAD_FOLDER, item['filename'])
        try:
            print(f"Downloading {item['filename']}...")
            # Use specific headers to avoid some 403s
            headers = {'User-Agent': 'Mozilla/5.0'}
            r = requests.get(item['url'], headers=headers, timeout=15)
            if r.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(r.content)
                print(f"SUCCESS: Fixed {item['filename']}")
            else:
                print(f"FAILED: {item['filename']} (HTTP {r.status_code})")
        except Exception as e:
            print(f"ERROR: {item['filename']} - {e}")

if __name__ == "__main__":
    fix_images()
