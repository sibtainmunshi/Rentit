from flask import Flask, render_template, jsonify, request
import firebase_admin
from firebase_admin import credentials, firestore
import os

# Case 3: Importing our custom Data Structure Logic
from utils.dsa_logic import sort_listings_by_price, search_products_linear
from data import MOCK_LISTINGS

app = Flask(__name__)

# --- Firebase Initialization ---
db = None
USE_FIREBASE = False

try:
    if os.path.exists("serviceAccountKey.json"):
        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        USE_FIREBASE = True
        print("✅ Firebase Connected Successfully!")
    else:
        print("⚠️  Firebase credentials not found. Using mock data.")
except Exception as e:
    print(f"⚠️  Firebase initialization failed: {e}. Using mock data.")


def fetch_from_firebase(category):
    """Fetch listings from Firebase Firestore"""
    try:
        docs = db.collection(category).stream()
        data = []
        for doc in docs:
            item = doc.to_dict()
            item['id'] = doc.id  # Add document ID
            data.append(item)
        return data
    except Exception as e:
        print(f"Error fetching from Firebase: {e}")
        return []

def filter_by_pincode(listings, user_pincode, max_distance_km=50):
    """Filter listings by pincode proximity"""
    filtered = []
    
    for item in listings:
        item_pincode = str(item.get('pincode', ''))
        
        if not item_pincode:
            continue
        
        # Calculate distance (simplified based on pincode difference)
        distance = calculate_pincode_distance(user_pincode, item_pincode)
        
        if distance <= max_distance_km:
            item['distance'] = distance
            filtered.append(item)
    
    # Sort by distance (nearest first)
    filtered.sort(key=lambda x: x.get('distance', 999))
    
    return filtered

def calculate_pincode_distance(pincode1, pincode2):
    """Calculate approximate distance between pincodes in km"""
    try:
        diff = abs(int(pincode1) - int(pincode2))
        
        # Simplified distance calculation
        # In production, use actual geocoding with lat/long
        if diff == 0:
            return 0
        elif diff < 10:
            return 1
        elif diff < 100:
            return 5
        elif diff < 1000:
            return 20
        elif diff < 10000:
            return 50
        else:
            return 100
    except:
        return 999  # Invalid pincode

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/list-item')
def list_item():
    return render_template('list_item.html')

@app.route('/my-listings')
def my_listings():
    return render_template('my_listings.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/booking-confirmation')
def booking_confirmation():
    return render_template('booking_confirmation.html')

@app.route('/api/listings', methods=['GET'])
def get_listings():
    category = request.args.get('category', 'products')
    sort_order = request.args.get('sort')  # 'asc' or 'desc'
    search_query = request.args.get('search', '').strip()
    show_all = request.args.get('show_all', 'false')  # For admin/my-listings
    pincode = request.args.get('pincode', '').strip()  # Pincode filter
    
    # Fetch data from Firebase or mock
    if USE_FIREBASE:
        data = fetch_from_firebase(category)
    else:
        data = MOCK_LISTINGS.get(category, [])
    
    # Filter by verification status (only show verified listings to public)
    if show_all != 'true':
        data = [item for item in data if item.get('status') == 'verified' or item.get('status') is None]
    
    # Filter by pincode if provided
    if pincode:
        data = filter_by_pincode(data, pincode)
    
    # Case 3 Integration: Apply search if query provided
    if search_query:
        data = search_products_linear(data, search_query)
    
    # Case 3 Integration: Apply sorting if requested
    if sort_order:
        is_asc = True if sort_order == 'asc' else False
        data = sort_listings_by_price(data, ascending=is_asc)
        
    return jsonify(data)

@app.route('/api/listing/<listing_id>', methods=['GET'])
def get_listing_detail(listing_id):
    """Get single listing details"""
    category = request.args.get('category', 'products')
    
    if USE_FIREBASE:
        try:
            doc = db.collection(category).document(listing_id).get()
            if doc.exists:
                data = doc.to_dict()
                data['id'] = doc.id
                return jsonify(data)
            else:
                return jsonify({"error": "Listing not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        # Search in mock data
        items = MOCK_LISTINGS.get(category, [])
        for item in items:
            if item.get('title') == listing_id:  # Using title as ID for mock
                return jsonify(item)
        return jsonify({"error": "Listing not found"}), 404

@app.route('/api/add-listing', methods=['POST'])
def add_listing():
    """Add new listing to database with verification status"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['title', 'price', 'category', 'description', 'pincode', 'hostId']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        category = data.pop('category')
        
        # Add default values if not present
        if 'rating' not in data:
            data['rating'] = '0.0'
        if 'tag' not in data:
            data['tag'] = None
        if 'unit' not in data:
            data['unit'] = '/day'
        if 'status' not in data:
            data['status'] = 'pending'  # Default status
        if 'totalRentals' not in data:
            data['totalRentals'] = 0
        if 'createdAt' not in data:
            from datetime import datetime
            data['createdAt'] = datetime.now().isoformat()
        
        if USE_FIREBASE:
            # Add to Firebase
            doc_ref = db.collection(category).add(data)
            return jsonify({
                "success": True,
                "message": "Listing submitted for review!",
                "id": doc_ref[1].id,
                "status": data['status']
            }), 201
        else:
            # Add to mock data (for testing)
            MOCK_LISTINGS.setdefault(category, []).append(data)
            return jsonify({
                "success": True,
                "message": "Listing submitted for review!",
                "status": data['status']
            }), 201
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/search', methods=['GET'])
def search_listings():
    """Search across all categories"""
    query = request.args.get('q', '').strip()
    
    if not query:
        return jsonify([])
    
    results = []
    categories = ['products', 'services', 'spaces']
    
    for category in categories:
        if USE_FIREBASE:
            data = fetch_from_firebase(category)
        else:
            data = MOCK_LISTINGS.get(category, [])
        
        # Apply search using our custom algorithm
        matches = search_products_linear(data, query)
        
        # Add category info to each result
        for match in matches:
            match['category'] = category
            results.append(match)
    
    return jsonify(results)

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get platform statistics"""
    stats = {
        "total_products": 0,
        "total_services": 0,
        "total_spaces": 0,
        "total_listings": 0
    }
    
    categories = ['products', 'services', 'spaces']
    
    for category in categories:
        if USE_FIREBASE:
            count = len(fetch_from_firebase(category))
        else:
            count = len(MOCK_LISTINGS.get(category, []))
        
        stats[f"total_{category}"] = count
        stats["total_listings"] += count
    
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True)
