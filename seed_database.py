import firebase_admin
from firebase_admin import credentials, firestore
import os
from datetime import datetime

# Import data from data.py
from data import MOCK_LISTINGS

def seed_data():
    if not os.path.exists("serviceAccountKey.json"):
        print("❌ Error: serviceAccountKey.json nahi mili! Check kar file wahin hai na?")
        return

    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    print("✅ Firebase Connected! Uploading data...")

    for category, items in MOCK_LISTINGS.items():
        print(f"📂 Uploading category: {category}...")
        col_ref = db.collection(category)
        
        # Pehle purana data delete karte hain (safai)
        docs = col_ref.stream()
        for doc in docs:
            doc.reference.delete()
            
        # Naya data daalte hain with all fields
        for item in items:
            # Ensure all required fields are present
            if 'status' not in item:
                item['status'] = 'verified'
            if 'createdAt' not in item:
                item['createdAt'] = datetime.now().isoformat()
            if 'totalRentals' not in item:
                item['totalRentals'] = 0
            if 'hostId' not in item:
                item['hostId'] = 'admin@rentit.com'
            if 'hostName' not in item:
                item['hostName'] = 'Rentit Admin'
            if 'hostEmail' not in item:
                item['hostEmail'] = 'admin@rentit.com'
            if 'hostVerified' not in item:
                item['hostVerified'] = True
                
            col_ref.add(item)
            print(f"   -> Added: {item['title']}")
    
    print("\n🎉 Success! Sara data Firebase Database me chala gaya hai with all fields.")
    print("📝 Note: All listings are marked as 'verified' and have host information.")

if __name__ == "__main__":
    seed_data()