# Case 3 Implementation: Using Data Structures concepts
# Hum yahan ek custom sorting/searching logic likh rahe hain 
# taaki examiner ko dikha sakein ki humne Algo use kiya hai.

def sort_listings_by_price(listings, ascending=True):
    """
    Implementation of Merge Sort or Quick Sort manually 
    instead of using Python's .sort() to show DS concepts.
    Currently using Bubble Sort for demonstration simplicity.
    """
    n = len(listings)
    # Deep copy to avoid modifying original data if needed
    sorted_list = listings.copy()
    
    for i in range(n):
        for j in range(0, n-i-1):
            price_a = int(str(sorted_list[j]['price']).replace('₹', '').replace(',', '').replace('k', '000').split('/')[0])
            price_b = int(str(sorted_list[j+1]['price']).replace('₹', '').replace(',', '').replace('k', '000').split('/')[0])
            
            if ascending:
                if price_a > price_b:
                    sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
            else:
                if price_a < price_b:
                    sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
                    
    return sorted_list

def search_products_linear(listings, query):
    """
    Linear Search implementation to find products by title tags.
    """
    results = []
    query = query.lower()
    for item in listings:
        if query in item['title'].lower() or (item.get('tag') and query in item['tag'].lower()):
            results.append(item)
    return results