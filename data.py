# Mock data for RentIt - Used as fallback when Firebase is not available
# All existing listings are pre-verified for demo purposes

MOCK_LISTINGS = {
    "products": [
        # Cameras & Photography (4 items)
        {"title": "Canon EOS R5", "price": "₹2,500", "rating": "4.9", "img": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?auto=format&fit=crop&w=600&q=80", "unit": "/day", "tag": "Hot", "status": "verified", "pincode": "400001", "description": "Professional mirrorless camera with 45MP sensor"},
        {"title": "Sony A7 III", "price": "₹2,000", "rating": "4.8", "img": "https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?auto=format&fit=crop&w=600&q=80", "unit": "/day", "tag": "Pro", "status": "verified", "pincode": "400002", "description": "Full-frame mirrorless camera perfect for photography"},
        {"title": "DJI Mavic Air 2", "price": "₹3,000", "rating": "4.7", "img": "https://images.unsplash.com/photo-1579829366248-204fe8413f31?auto=format&fit=crop&w=600&q=80", "unit": "/day", "tag": "New", "status": "verified", "pincode": "400003", "description": "Professional drone with 4K camera"},
        {"title": "GoPro Hero 11", "price": "₹800", "rating": "4.6", "img": "https://images.unsplash.com/photo-1519638399535-1b036603ac77?auto=format&fit=crop&w=600&q=80", "unit": "/day", "tag": None, "status": "verified", "pincode": "400004", "description": "Action camera for adventure sports"},
        
        # Electronics (4 items)
        {"title": "Sony PS5", "price": "₹800", "rating": "5.0", "img": "https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?auto=format&fit=crop&w=600&q=80", "unit": "/day", "tag": "Hot", "status": "verified", "pincode": "400005", "description": "Latest gaming console with amazing graphics"},
        {"title": "MacBook Pro M2", "price": "₹1,500", "rating": "4.9", "img": "https://images.unsplash.com/photo-1517336714731-489689fd1ca4?auto=format&fit=crop&w=600&q=80", "unit": "/day", "tag": "Pro", "status": "verified", "pincode": "400006", "description": "Powerful laptop for professionals"},
        {"title": "iPad Pro 12.9", "price": "₹1,000", "rating": "4.8", "img": "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?auto=format&fit=crop&w=600&q=80", "unit": "/day", "tag": None, "status": "verified", "pincode": "400007", "description": "Large screen tablet for creative work"},
        {"title": "Gaming PC RTX 4090", "price": "₹2,000", "rating": "4.9", "img": "https://images.unsplash.com/photo-1587202372634-32705e3bf49c?auto=format&fit=crop&w=600&q=80", "unit": "/day", "tag": "Beast", "status": "verified", "pincode": "400008", "description": "High-end gaming PC with RTX 4090"},
        
        # Vehicles (4 items)
        {"title": "Royal Enfield 350", "price": "₹1,200", "rating": "4.8", "img": "https://images.unsplash.com/photo-1558981403-c5f9899a28bc?auto=format&fit=crop&w=600&q=80", "unit": "/day", "tag": "Vintage", "status": "verified", "pincode": "400009", "description": "Classic motorcycle for long rides"},
        {"title": "KTM Duke 390", "price": "₹1,500", "rating": "4.7", "img": "https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?auto=format&fit=crop&w=600&q=80", "unit": "/day", "tag": "Sport", "status": "verified", "pincode": "400010", "description": "Sporty bike for thrill seekers"},
        {"title": "Activa 6G", "price": "₹400", "rating": "4.5", "img": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?auto=format&fit=crop&w=600&q=80", "unit": "/day", "tag": None, "status": "verified", "pincode": "400011", "description": "Comfortable scooter for daily commute"},
        {"title": "Maruti Swift", "price": "₹2,000", "rating": "4.6", "img": "https://images.unsplash.com/photo-1583121274602-3e2820c69888?auto=format&fit=crop&w=600&q=80", "unit": "/day", "tag": None, "status": "verified", "pincode": "400012", "description": "Compact car perfect for city driving"},
        
        # Outdoor & Camping (3 items)
        {"title": "Camping Tent 4P", "price": "₹500", "rating": "4.5", "img": "https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?auto=format&fit=crop&w=600&q=80", "unit": "/day", "tag": None, "status": "verified", "pincode": "400013", "description": "4-person camping tent waterproof"},
        {"title": "Trekking Backpack", "price": "₹200", "rating": "4.4", "img": "https://images.unsplash.com/photo-1622260614153-03223fb72052?auto=format&fit=crop&w=600&q=80", "unit": "/day", "tag": None, "status": "verified", "pincode": "400014", "description": "60L backpack for trekking adventures"},
        {"title": "Sleeping Bag", "price": "₹150", "rating": "4.3", "img": "https://images.unsplash.com/photo-1520095972714-909e91b038e5?auto=format&fit=crop&w=600&q=80", "unit": "/day", "tag": None, "status": "verified", "pincode": "400015", "description": "Warm sleeping bag for cold nights"},
        
        # Furniture (3 items)
        {"title": "Modern Sofa Set", "price": "₹900", "rating": "4.6", "img": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=600&q=80", "unit": "/month", "tag": None, "status": "verified", "pincode": "400016", "description": "3-seater modern sofa set"},
        {"title": "King Size Bed", "price": "₹1,200", "rating": "4.7", "img": "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?auto=format&fit=crop&w=600&q=80", "unit": "/month", "tag": None, "status": "verified", "pincode": "400017", "description": "Comfortable king size bed with mattress"},
        {"title": "Study Table", "price": "₹300", "rating": "4.4", "img": "https://images.unsplash.com/photo-1518455027359-f3f8164ba6bd?auto=format&fit=crop&w=600&q=80", "unit": "/month", "tag": None, "status": "verified", "pincode": "400018", "description": "Wooden study table with drawer"},
        
        # Books (2 items)
        {"title": "Harry Potter Set", "price": "₹200", "rating": "4.9", "img": "https://images.unsplash.com/photo-1544947950-fa07a98d237f?auto=format&fit=crop&w=600&q=80", "unit": "/week", "tag": "Bestseller", "status": "verified", "pincode": "400019", "description": "Complete Harry Potter book series"},
        {"title": "NCERT Complete Set", "price": "₹150", "rating": "4.5", "img": "https://images.unsplash.com/photo-1495446815901-a7297e633e8d?auto=format&fit=crop&w=600&q=80", "unit": "/month", "tag": None, "status": "verified", "pincode": "400020", "description": "NCERT books for class 11-12"}
    ],
    
    "services": [
        # Tech Services (4 items)
        {"title": "Python Developer", "price": "₹1,000", "rating": "5.0", "img": "https://images.unsplash.com/photo-1537511446984-935f663eb1f4?auto=format&fit=crop&w=600&q=80", "unit": "/hr", "tag": "Top Rated", "status": "verified", "pincode": "400021", "description": "Expert Python developer for web apps"},
        {"title": "Web Designer", "price": "₹800", "rating": "4.9", "img": "https://images.unsplash.com/photo-1561070791-2526d30994b5?auto=format&fit=crop&w=600&q=80", "unit": "/hr", "tag": "Expert", "status": "verified", "pincode": "400022", "description": "Professional web designer with 5+ years exp"},
        {"title": "Mobile App Dev", "price": "₹1,200", "rating": "4.8", "img": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?auto=format&fit=crop&w=600&q=80", "unit": "/hr", "tag": "Pro", "status": "verified", "pincode": "400023", "description": "iOS and Android app development"},
        {"title": "Data Analyst", "price": "₹900", "rating": "4.7", "img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=600&q=80", "unit": "/hr", "tag": None, "status": "verified", "pincode": "400024", "description": "Data analysis and visualization expert"},
        
        # Home Services (4 items)
        {"title": "House Cleaning", "price": "₹800", "rating": "4.8", "img": "https://images.unsplash.com/photo-1581578731117-10d52143b0d8?auto=format&fit=crop&w=600&q=80", "unit": "/service", "tag": None, "status": "verified", "pincode": "400025", "description": "Professional house cleaning service"},
        {"title": "Plumber Service", "price": "₹500", "rating": "4.6", "img": "https://images.unsplash.com/photo-1607472586893-edb57bdc0e39?auto=format&fit=crop&w=600&q=80", "unit": "/service", "tag": None, "status": "verified", "pincode": "400026", "description": "24/7 plumbing services"},
        {"title": "Electrician", "price": "₹600", "rating": "4.7", "img": "https://images.unsplash.com/photo-1621905251189-08b45d6a269e?auto=format&fit=crop&w=600&q=80", "unit": "/service", "tag": None, "status": "verified", "pincode": "400027", "description": "Licensed electrician for all repairs"},
        {"title": "Carpenter", "price": "₹700", "rating": "4.5", "img": "https://images.unsplash.com/photo-1504148455328-c376907d081c?auto=format&fit=crop&w=600&q=80", "unit": "/service", "tag": None, "status": "verified", "pincode": "400028", "description": "Skilled carpenter for furniture work"},
        
        # Personal Services (4 items)
        {"title": "Yoga Instructor", "price": "₹500", "rating": "4.9", "img": "https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?auto=format&fit=crop&w=600&q=80", "unit": "/session", "tag": "Wellness", "status": "verified", "pincode": "400029", "description": "Certified yoga instructor"},
        {"title": "Personal Trainer", "price": "₹600", "rating": "4.8", "img": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=600&q=80", "unit": "/session", "tag": None, "status": "verified", "pincode": "400030", "description": "Fitness trainer with nutrition guidance"},
        {"title": "Math Tutor", "price": "₹400", "rating": "4.7", "img": "https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=600&q=80", "unit": "/hr", "tag": None, "status": "verified", "pincode": "400031", "description": "Math tutor for class 8-12"},
        {"title": "Guitar Teacher", "price": "₹500", "rating": "4.6", "img": "https://images.unsplash.com/photo-1510915361894-db8b60106cb1?auto=format&fit=crop&w=600&q=80", "unit": "/session", "tag": None, "status": "verified", "pincode": "400032", "description": "Learn guitar from basics to advanced"},
        
        # Event Services (4 items)
        {"title": "Wedding Planner", "price": "₹15,000", "rating": "4.9", "img": "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=600&q=80", "unit": "/event", "tag": "Expert", "status": "verified", "pincode": "400033", "description": "Complete wedding planning services"},
        {"title": "Photographer", "price": "₹5,000", "rating": "4.8", "img": "https://images.unsplash.com/photo-1542038784456-1ea8e935640e?auto=format&fit=crop&w=600&q=80", "unit": "/event", "tag": "Pro", "status": "verified", "pincode": "400034", "description": "Professional event photography"},
        {"title": "DJ Service", "price": "₹8,000", "rating": "4.7", "img": "https://images.unsplash.com/photo-1571266028243-d220c6e2e2e2?auto=format&fit=crop&w=600&q=80", "unit": "/event", "tag": None, "status": "verified", "pincode": "400035", "description": "DJ with sound system for events"},
        {"title": "Catering Service", "price": "₹300", "rating": "4.6", "img": "https://images.unsplash.com/photo-1555244162-803834f70033?auto=format&fit=crop&w=600&q=80", "unit": "/person", "tag": None, "status": "verified", "pincode": "400036", "description": "Multi-cuisine catering service"},
        
        # Moving Services (2 items)
        {"title": "Packers & Movers", "price": "₹5,000", "rating": "4.7", "img": "https://images.unsplash.com/photo-1603732551681-2e91159b9dc2?auto=format&fit=crop&w=600&q=80", "unit": "/move", "tag": None, "status": "verified", "pincode": "400037", "description": "Professional packing and moving service"},
        {"title": "Bike Transport", "price": "₹2,000", "rating": "4.5", "img": "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?auto=format&fit=crop&w=600&q=80", "unit": "/service", "tag": None, "status": "verified", "pincode": "400038", "description": "Safe bike transportation service"}
    ],
    
    "spaces": [
        # Vacation Rentals (4 items)
        {"title": "Goa Beach Villa", "price": "₹12,000", "rating": "4.9", "img": "https://images.unsplash.com/photo-1613490493576-7fde63acd811?auto=format&fit=crop&w=600&q=80", "unit": "/night", "tag": "Luxe", "status": "verified", "pincode": "403001", "description": "Luxury beach villa with private pool"},
        {"title": "Manali Cottage", "price": "₹8,000", "rating": "4.8", "img": "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=600&q=80", "unit": "/night", "tag": "Mountain", "status": "verified", "pincode": "175131", "description": "Cozy cottage in the mountains"},
        {"title": "Udaipur Palace", "price": "₹15,000", "rating": "4.9", "img": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=600&q=80", "unit": "/night", "tag": "Royal", "status": "verified", "pincode": "313001", "description": "Heritage palace stay experience"},
        {"title": "Kerala Houseboat", "price": "₹10,000", "rating": "4.7", "img": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=600&q=80", "unit": "/night", "tag": "Unique", "status": "verified", "pincode": "688001", "description": "Traditional houseboat in backwaters"},
        
        # Apartments (3 items)
        {"title": "Cozy Studio Apt", "price": "₹2,500", "rating": "4.6", "img": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&w=600&q=80", "unit": "/night", "tag": None, "status": "verified", "pincode": "400039", "description": "Fully furnished studio apartment"},
        {"title": "2BHK Apartment", "price": "₹4,000", "rating": "4.7", "img": "https://images.unsplash.com/photo-1502672260066-6bc35f0a1f4c?auto=format&fit=crop&w=600&q=80", "unit": "/night", "tag": None, "status": "verified", "pincode": "400040", "description": "Spacious 2BHK with modern amenities"},
        {"title": "Penthouse Suite", "price": "₹8,000", "rating": "4.8", "img": "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?auto=format&fit=crop&w=600&q=80", "unit": "/night", "tag": "Premium", "status": "verified", "pincode": "400041", "description": "Luxury penthouse with city view"},
        
        # Commercial Spaces (3 items)
        {"title": "Co-working Space", "price": "₹500", "rating": "4.5", "img": "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=600&q=80", "unit": "/day", "tag": None, "status": "verified", "pincode": "400042", "description": "Modern co-working space with WiFi"},
        {"title": "Office Space 1000sqft", "price": "₹40,000", "rating": "4.8", "img": "https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=600&q=80", "unit": "/month", "tag": "Business", "status": "verified", "pincode": "400043", "description": "Prime location office space"},
        {"title": "Meeting Room", "price": "₹1,000", "rating": "4.6", "img": "https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=600&q=80", "unit": "/hr", "tag": None, "status": "verified", "pincode": "400044", "description": "Professional meeting room with projector"},
        
        # Event Venues (4 items)
        {"title": "Banquet Hall", "price": "₹20,000", "rating": "4.7", "img": "https://images.unsplash.com/photo-1519167758481-83f550bb49b3?auto=format&fit=crop&w=600&q=80", "unit": "/day", "tag": None, "status": "verified", "pincode": "400045", "description": "Spacious banquet hall for 200+ guests"},
        {"title": "Garden Venue", "price": "₹30,000", "rating": "4.9", "img": "https://images.unsplash.com/photo-1587574293340-933051b916c4?auto=format&fit=crop&w=600&q=80", "unit": "/event", "tag": "Scenic", "status": "verified", "pincode": "400046", "description": "Beautiful garden venue for weddings"},
        {"title": "Rooftop Lounge", "price": "₹25,000", "rating": "4.8", "img": "https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?auto=format&fit=crop&w=600&q=80", "unit": "/event", "tag": "Premium", "status": "verified", "pincode": "400047", "description": "Rooftop venue with city skyline view"},
        {"title": "Conference Hall", "price": "₹15,000", "rating": "4.6", "img": "https://images.unsplash.com/photo-1505373877841-8d25f7d46678?auto=format&fit=crop&w=600&q=80", "unit": "/day", "tag": None, "status": "verified", "pincode": "400048", "description": "Conference hall with AV equipment"},
        
        # Studios (2 items)
        {"title": "Photography Studio", "price": "₹3,000", "rating": "4.7", "img": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?auto=format&fit=crop&w=600&q=80", "unit": "/day", "tag": None, "status": "verified", "pincode": "400049", "description": "Professional photography studio with lights"},
        {"title": "Music Recording Studio", "price": "₹2,000", "rating": "4.8", "img": "https://images.unsplash.com/photo-1598488035139-bdbb2231ce04?auto=format&fit=crop&w=600&q=80", "unit": "/hr", "tag": "Pro", "status": "verified", "pincode": "400050", "description": "Soundproof recording studio"}
    ]
}
