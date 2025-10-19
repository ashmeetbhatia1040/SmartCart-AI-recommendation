"""
SmartCart AI - FastAPI Backend
Lightweight API for product recommendations and analytics
"""

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import products_data
from collections import Counter

app = FastAPI(title="SmartCart AI API", version="1.0.0")

# CORS configuration for frontend access
# Allow both local development and production frontend URLs
allowed_origins = [
    "http://localhost:5173",  # Local Vite dev server
    "http://localhost:3000",  # Alternative local port
    "https://smart-cart-ai-recommendation-98k7.vercel.app",  # Production frontend
    "https://*.vercel.app",  # Any Vercel preview deployments
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for now (configure specific origins above for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Response models
class Product(BaseModel):
    id: int
    title: str
    brand: str
    price: float
    categories: List[str]
    description: str
    image_url: str
    rating: float
    features: List[str]
    specifications: str

class RecommendationResponse(BaseModel):
    products: List[Product]
    total: int
    query: Optional[str] = None

class AnalyticsResponse(BaseModel):
    total_products: int
    total_brands: int
    total_categories: int
    avg_price: float
    price_ranges: dict
    brand_distribution: dict
    category_distribution: dict
    rating_distribution: dict
    top_brands: List[dict]
    price_by_category: dict

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "SmartCart AI API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/api/health",
            "recommend": "/api/recommend",
            "analytics": "/api/analytics"
        }
    }

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    products = products_data.get_all_products()
    return {
        "status": "healthy",
        "products_loaded": len(products),
        "categories": len(products_data.get_categories()),
        "brands": len(products_data.get_brands())
    }

def calculate_relevance_score(product: dict, query: str, filters: dict) -> float:
    """
    Calculate relevance score for product recommendations
    Scoring system:
    - Title match: +3 points
    - Description match: +2 points
    - Category match: +2 points
    - Brand match: +1 point
    - Features match: +1 point
    """
    if not query:
        return 5.0  # Base score for no query
    
    score = 0.0
    query_lower = query.lower()
    query_words = query_lower.split()
    
    # Title matching
    title_lower = product['title'].lower()
    for word in query_words:
        if word in title_lower:
            score += 3.0
    
    # Description matching
    desc_lower = product['description'].lower()
    for word in query_words:
        if word in desc_lower:
            score += 2.0
    
    # Category matching
    for category in product['categories']:
        if query_lower in category.lower():
            score += 2.0
    
    # Brand matching
    if query_lower in product['brand'].lower():
        score += 1.0
    
    # Features matching
    for feature in product['features']:
        feature_lower = feature.lower()
        for word in query_words:
            if word in feature_lower:
                score += 1.0
    
    # Specifications matching
    if query_lower in product['specifications'].lower():
        score += 1.0
    
    return score

@app.get("/api/recommend", response_model=RecommendationResponse)
async def recommend_products(
    query: Optional[str] = Query(None, description="Search query"),
    category: Optional[str] = Query(None, description="Filter by category"),
    brand: Optional[str] = Query(None, description="Filter by brand"),
    min_price: Optional[float] = Query(None, description="Minimum price"),
    max_price: Optional[float] = Query(None, description="Maximum price"),
    min_rating: Optional[float] = Query(None, description="Minimum rating"),
    limit: int = Query(20, description="Number of results")
):
    """
    Get product recommendations based on query and filters
    """
    products = products_data.get_all_products()
    
    # Apply filters
    filtered_products = []
    for product in products:
        # Category filter
        if category and category not in product['categories']:
            continue
        
        # Brand filter
        if brand and product['brand'] != brand:
            continue
        
        # Price filters
        if min_price is not None and product['price'] < min_price:
            continue
        if max_price is not None and product['price'] > max_price:
            continue
        
        # Rating filter
        if min_rating is not None and product['rating'] < min_rating:
            continue
        
        filtered_products.append(product)
    
    # Calculate relevance scores if query provided
    if query:
        product_scores = []
        for product in filtered_products:
            score = calculate_relevance_score(product, query, {})
            if score > 0:  # Only include products with some relevance
                product_scores.append((product, score))
        
        # Sort by score (descending) and rating (descending)
        product_scores.sort(key=lambda x: (x[1], x[0]['rating']), reverse=True)
        filtered_products = [p[0] for p in product_scores]
    else:
        # Sort by rating if no query
        filtered_products.sort(key=lambda x: x['rating'], reverse=True)
    
    # Limit results
    limited_products = filtered_products[:limit]
    
    return {
        "products": limited_products,
        "total": len(filtered_products),
        "query": query
    }

@app.get("/api/analytics", response_model=AnalyticsResponse)
async def get_analytics():
    """
    Get analytics and statistics about the product catalog
    """
    products = products_data.get_all_products()
    
    # Basic stats
    total_products = len(products)
    brands = products_data.get_brands()
    categories = products_data.get_categories()
    
    # Price statistics
    prices = [p['price'] for p in products]
    avg_price = sum(prices) / len(prices) if prices else 0
    
    # Price ranges
    price_ranges = {
        "Under $100": len([p for p in products if p['price'] < 100]),
        "$100-$500": len([p for p in products if 100 <= p['price'] < 500]),
        "$500-$1000": len([p for p in products if 500 <= p['price'] < 1000]),
        "$1000-$2000": len([p for p in products if 1000 <= p['price'] < 2000]),
        "$2000+": len([p for p in products if p['price'] >= 2000])
    }
    
    # Brand distribution
    brand_counts = Counter(p['brand'] for p in products)
    brand_distribution = dict(brand_counts)
    
    # Top brands
    top_brands = [
        {"brand": brand, "count": count} 
        for brand, count in brand_counts.most_common(10)
    ]
    
    # Category distribution
    category_counts = Counter()
    for product in products:
        for category in product['categories']:
            category_counts[category] += 1
    category_distribution = dict(category_counts)
    
    # Rating distribution
    rating_counts = Counter()
    for product in products:
        rating_bucket = f"{int(product['rating'])}.0-{int(product['rating'])}.9"
        rating_counts[rating_bucket] += 1
    rating_distribution = dict(rating_counts)
    
    # Average price by category
    price_by_category = {}
    for category in categories:
        category_products = [
            p for p in products 
            if category in p['categories']
        ]
        if category_products:
            avg = sum(p['price'] for p in category_products) / len(category_products)
            price_by_category[category] = round(avg, 2)
    
    return {
        "total_products": total_products,
        "total_brands": len(brands),
        "total_categories": len(categories),
        "avg_price": round(avg_price, 2),
        "price_ranges": price_ranges,
        "brand_distribution": brand_distribution,
        "category_distribution": category_distribution,
        "rating_distribution": rating_distribution,
        "top_brands": top_brands,
        "price_by_category": price_by_category
    }

@app.get("/api/categories")
async def get_categories():
    """Get all available categories"""
    return {"categories": products_data.get_categories()}

@app.get("/api/brands")
async def get_brands():
    """Get all available brands"""
    return {"brands": products_data.get_brands()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
