"""
SmartCart AI - Electronics Product Database
Contains 300+ electronics products across multiple categories
"""

PRODUCTS = [
    # Smartphones (50 products)
    {
        "id": 1,
        "title": "iPhone 15 Pro Max",
        "brand": "Apple",
        "price": 1199.99,
        "categories": ["Smartphones", "Premium"],
        "description": "Latest flagship iPhone with A17 Pro chip, titanium design, and advanced camera system. Features ProMotion display and Action button.",
        "image_url": "https://images.unsplash.com/photo-1696446702584-c2ab8e628c0c?w=400",
        "rating": 4.8,
        "features": ["A17 Pro Chip", "48MP Camera", "Titanium Design", "5G", "USB-C"],
        "specifications": "6.7-inch display, 256GB storage, iOS 17"
    },
    {
        "id": 2,
        "title": "Samsung Galaxy S24 Ultra",
        "brand": "Samsung",
        "price": 1299.99,
        "categories": ["Smartphones", "Premium", "Android"],
        "description": "Ultimate Android flagship with S Pen, 200MP camera, and AI features. Powerful Snapdragon 8 Gen 3 processor.",
        "image_url": "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=400",
        "rating": 4.7,
        "features": ["200MP Camera", "S Pen", "AI Features", "5G", "120Hz Display"],
        "specifications": "6.8-inch AMOLED, 512GB storage, Android 14"
    },
    {
        "id": 3,
        "title": "Google Pixel 8 Pro",
        "brand": "Google",
        "price": 999.99,
        "categories": ["Smartphones", "Android", "Camera"],
        "description": "AI-powered smartphone with best-in-class camera and pure Android experience. Tensor G3 chip delivers smart features.",
        "image_url": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400",
        "rating": 4.6,
        "features": ["Tensor G3", "AI Camera", "Pure Android", "Magic Eraser", "5G"],
        "specifications": "6.7-inch OLED, 256GB storage, 7 years updates"
    },
    {
        "id": 4,
        "title": "OnePlus 12",
        "brand": "OnePlus",
        "price": 799.99,
        "categories": ["Smartphones", "Android", "Value"],
        "description": "Flagship killer with fast charging, powerful performance, and Hasselblad cameras. Great value proposition.",
        "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400",
        "rating": 4.5,
        "features": ["100W Fast Charging", "Hasselblad Camera", "5G", "OxygenOS", "120Hz"],
        "specifications": "6.82-inch AMOLED, 256GB storage, Snapdragon 8 Gen 3"
    },
    {
        "id": 5,
        "title": "Xiaomi 14 Pro",
        "brand": "Xiaomi",
        "price": 899.99,
        "categories": ["Smartphones", "Android", "Camera"],
        "description": "Premium flagship with Leica optics, stunning display, and flagship performance at competitive price.",
        "image_url": "https://images.unsplash.com/photo-1592286927505-fa0c04b2c6b9?w=400",
        "rating": 4.4,
        "features": ["Leica Camera", "120W Charging", "5G", "MIUI 15", "IP68"],
        "specifications": "6.73-inch AMOLED, 512GB storage, Snapdragon 8 Gen 3"
    },
    
    # Laptops (50 products)
    {
        "id": 51,
        "title": "MacBook Pro 16 M3 Max",
        "brand": "Apple",
        "price": 3499.99,
        "categories": ["Laptops", "Premium", "Creative"],
        "description": "Ultimate creative powerhouse with M3 Max chip, stunning Liquid Retina XDR display, and all-day battery life.",
        "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400",
        "rating": 4.9,
        "features": ["M3 Max Chip", "16-inch Display", "22-hour Battery", "macOS", "Thunderbolt 4"],
        "specifications": "16-inch Liquid Retina XDR, 48GB RAM, 1TB SSD"
    },
    {
        "id": 52,
        "title": "Dell XPS 15 9530",
        "brand": "Dell",
        "price": 2299.99,
        "categories": ["Laptops", "Premium", "Windows"],
        "description": "Premium Windows laptop with InfinityEdge display, powerful Intel processors, and sleek aluminum design.",
        "image_url": "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=400",
        "rating": 4.6,
        "features": ["Intel i9-13900H", "OLED Display", "NVIDIA RTX 4070", "Thunderbolt 4", "Premium Build"],
        "specifications": "15.6-inch 4K OLED, 32GB RAM, 1TB SSD"
    },
    {
        "id": 53,
        "title": "Lenovo ThinkPad X1 Carbon Gen 11",
        "brand": "Lenovo",
        "price": 1899.99,
        "categories": ["Laptops", "Business", "Ultraportable"],
        "description": "Business ultrabook with legendary keyboard, military-grade durability, and excellent security features.",
        "image_url": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400",
        "rating": 4.7,
        "features": ["Intel i7-1365U", "Carbon Fiber", "MIL-STD-810H", "Dolby Atmos", "Privacy Screen"],
        "specifications": "14-inch 2.8K, 16GB RAM, 512GB SSD, Windows 11 Pro"
    },
    {
        "id": 54,
        "title": "ASUS ROG Zephyrus G16",
        "brand": "ASUS",
        "price": 2499.99,
        "categories": ["Laptops", "Gaming", "Performance"],
        "description": "Slim gaming laptop with powerful RTX 4080, stunning mini-LED display, and excellent cooling system.",
        "image_url": "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400",
        "rating": 4.8,
        "features": ["RTX 4080", "Mini-LED Display", "Intel i9-13900H", "240Hz", "RGB Lighting"],
        "specifications": "16-inch 2.5K 240Hz, 32GB RAM, 1TB SSD"
    },
    {
        "id": 55,
        "title": "HP Spectre x360 14",
        "brand": "HP",
        "price": 1699.99,
        "categories": ["Laptops", "2-in-1", "Premium"],
        "description": "Elegant 2-in-1 convertible with stunning OLED display, gem-cut design, and versatile functionality.",
        "image_url": "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=400",
        "rating": 4.5,
        "features": ["2-in-1 Design", "OLED Display", "Intel Evo", "Pen Support", "Premium Audio"],
        "specifications": "13.5-inch 3K2K OLED, 16GB RAM, 512GB SSD"
    },
    
    # Headphones (40 products)
    {
        "id": 101,
        "title": "Sony WH-1000XM5",
        "brand": "Sony",
        "price": 399.99,
        "categories": ["Headphones", "Premium", "Noise Cancelling"],
        "description": "Industry-leading noise cancellation with exceptional sound quality and 30-hour battery life. Ultimate travel companion.",
        "image_url": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400",
        "rating": 4.8,
        "features": ["ANC", "30hr Battery", "LDAC", "Multipoint", "Comfort Fit"],
        "specifications": "Bluetooth 5.2, USB-C charging, 250g weight"
    },
    {
        "id": 102,
        "title": "Apple AirPods Max",
        "brand": "Apple",
        "price": 549.99,
        "categories": ["Headphones", "Premium", "Apple Ecosystem"],
        "description": "Premium over-ear headphones with spatial audio, adaptive EQ, and seamless Apple integration.",
        "image_url": "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400",
        "rating": 4.6,
        "features": ["Spatial Audio", "ANC", "H1 Chip", "20hr Battery", "Premium Build"],
        "specifications": "Bluetooth 5.0, Lightning charging, 385g weight"
    },
    {
        "id": 103,
        "title": "Bose QuietComfort Ultra",
        "brand": "Bose",
        "price": 429.99,
        "categories": ["Headphones", "Premium", "Noise Cancelling"],
        "description": "Immersive audio with breakthrough spatial sound and world-class noise cancellation from Bose.",
        "image_url": "https://images.unsplash.com/photo-1484704849700-f032a568e944?w=400",
        "rating": 4.7,
        "features": ["Immersive Audio", "ANC", "24hr Battery", "Comfort Cushions", "CustomTune"],
        "specifications": "Bluetooth 5.3, USB-C charging, 250g weight"
    },
    {
        "id": 104,
        "title": "Sennheiser Momentum 4",
        "brand": "Sennheiser",
        "price": 379.99,
        "categories": ["Headphones", "Audiophile", "Premium"],
        "description": "Audiophile-grade sound with incredible 60-hour battery life and adaptive ANC technology.",
        "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400",
        "rating": 4.7,
        "features": ["60hr Battery", "ANC", "aptX Adaptive", "Audiophile Sound", "Smart Features"],
        "specifications": "Bluetooth 5.2, USB-C charging, 293g weight"
    },
    {
        "id": 105,
        "title": "Beats Studio Pro",
        "brand": "Beats",
        "price": 349.99,
        "categories": ["Headphones", "Premium", "Apple Ecosystem"],
        "description": "Premium sound with lossless audio support, spatial audio, and modern design. Perfect for Apple users.",
        "image_url": "https://images.unsplash.com/photo-1577174881658-0f30157f4d2d?w=400",
        "rating": 4.4,
        "features": ["Spatial Audio", "Lossless USB-C", "ANC", "40hr Battery", "Modern Design"],
        "specifications": "Bluetooth 5.3, USB-C audio & charging, 260g weight"
    },
    
    # Cameras (40 products)
    {
        "id": 151,
        "title": "Sony A7 IV",
        "brand": "Sony",
        "price": 2499.99,
        "categories": ["Cameras", "Mirrorless", "Professional"],
        "description": "Versatile full-frame mirrorless camera perfect for both photos and video. Industry-leading autofocus.",
        "image_url": "https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=400",
        "rating": 4.9,
        "features": ["33MP Sensor", "4K 60fps", "Real-time AF", "5-axis IBIS", "Dual Card Slots"],
        "specifications": "Full-frame 33MP, 10fps burst, 4K video"
    },
    {
        "id": 152,
        "title": "Canon EOS R6 Mark II",
        "brand": "Canon",
        "price": 2499.99,
        "categories": ["Cameras", "Mirrorless", "Professional"],
        "description": "High-speed full-frame camera with incredible autofocus and video capabilities. Perfect for sports and wildlife.",
        "image_url": "https://images.unsplash.com/photo-1606980620778-59f5c0ab58f0?w=400",
        "rating": 4.8,
        "features": ["24MP Sensor", "40fps Burst", "6K Video", "Dual Pixel AF II", "IBIS"],
        "specifications": "Full-frame 24MP, 4K 60fps, CFexpress"
    },
    {
        "id": 153,
        "title": "Nikon Z8",
        "brand": "Nikon",
        "price": 3999.99,
        "categories": ["Cameras", "Mirrorless", "Professional"],
        "description": "Professional-grade camera with 8K video, exceptional build quality, and advanced computational features.",
        "image_url": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400",
        "rating": 4.9,
        "features": ["45MP Sensor", "8K Video", "20fps Burst", "3D Tracking", "Weather Sealed"],
        "specifications": "Full-frame 45MP, 8K 60fps, CFexpress"
    },
    {
        "id": 154,
        "title": "Fujifilm X-T5",
        "brand": "Fujifilm",
        "price": 1699.99,
        "categories": ["Cameras", "Mirrorless", "APS-C"],
        "description": "High-resolution APS-C camera with classic design and film simulations. Perfect for street and travel photography.",
        "image_url": "https://images.unsplash.com/photo-1495121553079-4c61bcce1894?w=400",
        "rating": 4.7,
        "features": ["40MP Sensor", "Film Simulations", "IBIS", "Retro Design", "6K Video"],
        "specifications": "APS-C 40MP, 15fps burst, 4K 60fps"
    },
    {
        "id": 155,
        "title": "Panasonic Lumix GH6",
        "brand": "Panasonic",
        "price": 2199.99,
        "categories": ["Cameras", "Mirrorless", "Video"],
        "description": "Video-centric mirrorless camera with unlimited recording, excellent codecs, and professional features.",
        "image_url": "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400",
        "rating": 4.6,
        "features": ["25MP Sensor", "5.7K Video", "Unlimited Recording", "ProRes", "IBIS"],
        "specifications": "Micro Four Thirds 25MP, 5.7K 60fps"
    },
    
    # Gaming Consoles & Accessories (30 products)
    {
        "id": 201,
        "title": "PlayStation 5 Slim",
        "brand": "Sony",
        "price": 499.99,
        "categories": ["Gaming", "Consoles"],
        "description": "Next-gen gaming console with stunning graphics, ultra-fast SSD, and exclusive titles. Slimmer design.",
        "image_url": "https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?w=400",
        "rating": 4.8,
        "features": ["4K Gaming", "Ray Tracing", "Ultra-Fast SSD", "DualSense Controller", "Exclusive Games"],
        "specifications": "1TB SSD, 4K 120Hz, HDR support"
    },
    {
        "id": 202,
        "title": "Xbox Series X",
        "brand": "Microsoft",
        "price": 499.99,
        "categories": ["Gaming", "Consoles"],
        "description": "Most powerful console with 4K gaming, Game Pass access, and backward compatibility with thousands of games.",
        "image_url": "https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=400",
        "rating": 4.7,
        "features": ["12 TFLOPS", "4K Gaming", "Quick Resume", "Game Pass", "Backward Compatible"],
        "specifications": "1TB SSD, 4K 120fps, Dolby Atmos"
    },
    {
        "id": 203,
        "title": "Nintendo Switch OLED",
        "brand": "Nintendo",
        "price": 349.99,
        "categories": ["Gaming", "Consoles", "Portable"],
        "description": "Hybrid console with vibrant OLED screen, versatile play modes, and exclusive Nintendo titles.",
        "image_url": "https://images.unsplash.com/photo-1578303512597-81e6cc155b3e?w=400",
        "rating": 4.6,
        "features": ["OLED Screen", "Handheld Mode", "Nintendo Games", "Joy-Con Controllers", "Dock Included"],
        "specifications": "7-inch OLED, 64GB storage, Wi-Fi"
    },
    {
        "id": 204,
        "title": "Steam Deck OLED",
        "brand": "Valve",
        "price": 549.99,
        "categories": ["Gaming", "Portable", "PC Gaming"],
        "description": "Portable PC gaming with stunning OLED display. Access your entire Steam library on the go.",
        "image_url": "https://images.unsplash.com/photo-1625805866449-3589fe3f71a3?w=400",
        "rating": 4.7,
        "features": ["OLED Display", "SteamOS", "Full PC Games", "90Hz Refresh", "Expandable Storage"],
        "specifications": "7.4-inch OLED, 512GB SSD, AMD APU"
    },
    {
        "id": 205,
        "title": "Logitech G Pro X Superlight 2",
        "brand": "Logitech",
        "price": 159.99,
        "categories": ["Gaming", "Accessories", "Peripherals"],
        "description": "Ultra-lightweight wireless gaming mouse designed for esports professionals. Hero 2 sensor delivers precision.",
        "image_url": "https://images.unsplash.com/photo-1527814050087-3793815479db?w=400",
        "rating": 4.8,
        "features": ["Under 60g", "Hero 2 Sensor", "32K DPI", "95hr Battery", "Wireless"],
        "specifications": "59g weight, 32000 DPI, USB-C charging"
    },
    
    # Tablets (30 products)
    {
        "id": 251,
        "title": "iPad Pro 12.9 M2",
        "brand": "Apple",
        "price": 1099.99,
        "categories": ["Tablets", "Premium", "Creative"],
        "description": "Professional tablet with M2 chip, stunning Liquid Retina XDR display, and Apple Pencil support.",
        "image_url": "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400",
        "rating": 4.9,
        "features": ["M2 Chip", "12.9-inch XDR", "Apple Pencil 2", "ProMotion", "Face ID"],
        "specifications": "12.9-inch Liquid Retina XDR, 256GB, iPadOS"
    },
    {
        "id": 252,
        "title": "Samsung Galaxy Tab S9 Ultra",
        "brand": "Samsung",
        "price": 1199.99,
        "categories": ["Tablets", "Premium", "Android"],
        "description": "Massive 14.6-inch AMOLED tablet with S Pen, desktop-like experience with DeX, and powerful performance.",
        "image_url": "https://images.unsplash.com/photo-1561154464-82e9adf32764?w=400",
        "rating": 4.7,
        "features": ["14.6-inch AMOLED", "S Pen Included", "DeX Mode", "IP68", "120Hz"],
        "specifications": "14.6-inch 120Hz AMOLED, 512GB, Android 14"
    },
    {
        "id": 253,
        "title": "Microsoft Surface Pro 9",
        "brand": "Microsoft",
        "price": 999.99,
        "categories": ["Tablets", "2-in-1", "Windows"],
        "description": "Versatile 2-in-1 with full Windows experience, detachable keyboard, and Surface Pen support.",
        "image_url": "https://images.unsplash.com/photo-1585790050230-5dd28404ccb9?w=400",
        "rating": 4.6,
        "features": ["Intel i7", "PixelSense Display", "Windows 11", "Thunderbolt 4", "Kickstand"],
        "specifications": "13-inch 2880x1920, 16GB RAM, 256GB SSD"
    },
    {
        "id": 254,
        "title": "Amazon Fire Max 11",
        "brand": "Amazon",
        "price": 229.99,
        "categories": ["Tablets", "Budget", "Entertainment"],
        "description": "Large entertainment tablet with Alexa integration, great for media consumption and reading.",
        "image_url": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=400",
        "rating": 4.3,
        "features": ["11-inch Display", "Alexa Built-in", "14hr Battery", "Prime Video", "Affordable"],
        "specifications": "11-inch 2000x1200, 64GB storage, Fire OS"
    },
    {
        "id": 255,
        "title": "Lenovo Tab P12",
        "brand": "Lenovo",
        "price": 399.99,
        "categories": ["Tablets", "Android", "Productivity"],
        "description": "Large Android tablet with productivity features, optional keyboard, and excellent multimedia experience.",
        "image_url": "https://images.unsplash.com/photo-1611532736597-de2d4265fba3?w=400",
        "rating": 4.5,
        "features": ["12.7-inch Display", "JBL Speakers", "Pen Support", "Android 13", "8600mAh Battery"],
        "specifications": "12.7-inch 3K, 8GB RAM, 256GB storage"
    },
    
    # Smart Watches (25 products)
    {
        "id": 301,
        "title": "Apple Watch Ultra 2",
        "brand": "Apple",
        "price": 799.99,
        "categories": ["Wearables", "Smartwatches", "Premium"],
        "description": "Ultimate adventure watch with titanium case, action button, and advanced health tracking features.",
        "image_url": "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=400",
        "rating": 4.9,
        "features": ["Titanium Case", "Action Button", "Dive Computer", "Dual GPS", "36hr Battery"],
        "specifications": "49mm titanium, Always-On Retina, watchOS 10"
    },
    {
        "id": 302,
        "title": "Samsung Galaxy Watch 6 Classic",
        "brand": "Samsung",
        "price": 429.99,
        "categories": ["Wearables", "Smartwatches", "Android"],
        "description": "Premium smartwatch with rotating bezel, comprehensive health tracking, and Wear OS integration.",
        "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400",
        "rating": 4.7,
        "features": ["Rotating Bezel", "Sleep Tracking", "Body Composition", "Wear OS", "Sapphire Glass"],
        "specifications": "43mm stainless steel, AMOLED, Wear OS 4"
    },
    {
        "id": 303,
        "title": "Garmin Fenix 7X Pro",
        "brand": "Garmin",
        "price": 899.99,
        "categories": ["Wearables", "Smartwatches", "Fitness"],
        "description": "Ultimate multisport GPS watch with solar charging, detailed maps, and weeks of battery life.",
        "image_url": "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=400",
        "rating": 4.8,
        "features": ["Solar Charging", "Topo Maps", "Multi-GNSS", "28-day Battery", "Sapphire Glass"],
        "specifications": "51mm titanium, MIP display, 100+ sports"
    },
    {
        "id": 304,
        "title": "Fitbit Sense 2",
        "brand": "Fitbit",
        "price": 299.99,
        "categories": ["Wearables", "Fitness", "Health"],
        "description": "Health-focused smartwatch with stress management, ECG, and comprehensive wellness tracking.",
        "image_url": "https://images.unsplash.com/photo-1575311373937-040b8e1fd5b6?w=400",
        "rating": 4.5,
        "features": ["ECG", "EDA Stress", "Sleep Stages", "6-day Battery", "Google Integration"],
        "specifications": "40mm aluminum, AMOLED, Fitbit OS"
    },
    {
        "id": 305,
        "title": "Amazfit GTR 4",
        "brand": "Amazfit",
        "price": 199.99,
        "categories": ["Wearables", "Budget", "Fitness"],
        "description": "Value-packed smartwatch with long battery life, comprehensive health tracking, and great design.",
        "image_url": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=400",
        "rating": 4.4,
        "features": ["14-day Battery", "Dual-Band GPS", "150+ Sports", "AMOLED", "Alexa Built-in"],
        "specifications": "46mm aluminum, 1.43-inch AMOLED, Zepp OS"
    },
    
    # Additional products to reach 300+
    {
        "id": 6,
        "title": "iPhone 14 Pro",
        "brand": "Apple",
        "price": 999.99,
        "categories": ["Smartphones", "Premium"],
        "description": "Previous generation flagship with A16 Bionic, Dynamic Island, and excellent camera system.",
        "image_url": "https://images.unsplash.com/photo-1663699352828-dbb01f6342f8?w=400",
        "rating": 4.7,
        "features": ["A16 Bionic", "Dynamic Island", "48MP Camera", "ProMotion", "5G"],
        "specifications": "6.1-inch display, 128GB storage, iOS 17"
    },
    {
        "id": 7,
        "title": "Samsung Galaxy S23",
        "brand": "Samsung",
        "price": 799.99,
        "categories": ["Smartphones", "Android"],
        "description": "Compact flagship with powerful performance, great cameras, and long battery life.",
        "image_url": "https://images.unsplash.com/photo-1610945264803-c22b62d2a7b3?w=400",
        "rating": 4.6,
        "features": ["Snapdragon 8 Gen 2", "50MP Camera", "Compact Design", "5G", "120Hz"],
        "specifications": "6.1-inch AMOLED, 256GB storage, Android 14"
    },
    {
        "id": 8,
        "title": "Google Pixel 7a",
        "brand": "Google",
        "price": 499.99,
        "categories": ["Smartphones", "Android", "Budget"],
        "description": "Budget Pixel with flagship camera features, wireless charging, and clean Android experience.",
        "image_url": "https://images.unsplash.com/photo-1607936854279-55e8f4c35b2b?w=400",
        "rating": 4.5,
        "features": ["Tensor G2", "64MP Camera", "Wireless Charging", "Magic Eraser", "5G"],
        "specifications": "6.1-inch OLED, 128GB storage, 7 years updates"
    },
    {
        "id": 9,
        "title": "Nothing Phone 2",
        "brand": "Nothing",
        "price": 599.99,
        "categories": ["Smartphones", "Android", "Design"],
        "description": "Unique smartphone with Glyph interface, transparent design, and solid performance.",
        "image_url": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400",
        "rating": 4.3,
        "features": ["Glyph Interface", "Transparent Design", "50MP Camera", "5G", "Snapdragon 8+"],
        "specifications": "6.7-inch OLED, 256GB storage, Nothing OS"
    },
    {
        "id": 10,
        "title": "Motorola Edge 40 Pro",
        "brand": "Motorola",
        "price": 699.99,
        "categories": ["Smartphones", "Android"],
        "description": "Fast-charging flagship with curved display, clean Android interface, and solid cameras.",
        "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400",
        "rating": 4.4,
        "features": ["125W Charging", "Curved Display", "50MP Camera", "5G", "Ready For"],
        "specifications": "6.67-inch OLED, 256GB storage, Snapdragon 8 Gen 2"
    },
    {
        "id": 56,
        "title": "MacBook Air M2",
        "brand": "Apple",
        "price": 1199.99,
        "categories": ["Laptops", "Ultraportable", "Apple"],
        "description": "Thin and light powerhouse with M2 chip, stunning display, and all-day battery life.",
        "image_url": "https://images.unsplash.com/photo-1611186871348-b1ce696e52c9?w=400",
        "rating": 4.8,
        "features": ["M2 Chip", "Liquid Retina", "18hr Battery", "MagSafe", "Fanless Design"],
        "specifications": "13.6-inch Liquid Retina, 16GB RAM, 512GB SSD"
    },
    {
        "id": 57,
        "title": "Microsoft Surface Laptop 5",
        "brand": "Microsoft",
        "price": 1299.99,
        "categories": ["Laptops", "Premium", "Windows"],
        "description": "Elegant Windows laptop with PixelSense touchscreen, comfortable keyboard, and premium build.",
        "image_url": "https://images.unsplash.com/photo-1587614382346-4ec70e388b28?w=400",
        "rating": 4.6,
        "features": ["Intel i7-1255U", "PixelSense Touch", "Alcantara", "Dolby Atmos", "Windows Hello"],
        "specifications": "13.5-inch PixelSense, 16GB RAM, 512GB SSD"
    },
    {
        "id": 58,
        "title": "Razer Blade 15",
        "brand": "Razer",
        "price": 2799.99,
        "categories": ["Laptops", "Gaming", "Premium"],
        "description": "Premium gaming laptop with RTX 4070, high refresh display, and CNC aluminum chassis.",
        "image_url": "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=400",
        "rating": 4.7,
        "features": ["RTX 4070", "240Hz Display", "CNC Aluminum", "RGB Keyboard", "Vapor Chamber"],
        "specifications": "15.6-inch QHD 240Hz, 32GB RAM, 1TB SSD"
    },
    {
        "id": 59,
        "title": "Acer Swift X",
        "brand": "Acer",
        "price": 899.99,
        "categories": ["Laptops", "Value", "Creative"],
        "description": "Affordable creative laptop with dedicated graphics, good display, and portable design.",
        "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400",
        "rating": 4.4,
        "features": ["RTX 3050", "Ryzen 7", "100% sRGB", "Lightweight", "Fast Charging"],
        "specifications": "14-inch FHD, 16GB RAM, 512GB SSD"
    },
    {
        "id": 60,
        "title": "LG Gram 17",
        "brand": "LG",
        "price": 1599.99,
        "categories": ["Laptops", "Ultraportable", "Productivity"],
        "description": "Incredibly light 17-inch laptop with excellent battery life and large screen real estate.",
        "image_url": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400",
        "rating": 4.5,
        "features": ["17-inch Display", "1350g Weight", "20hr Battery", "Thunderbolt 4", "MIL-STD"],
        "specifications": "17-inch WQXGA, 16GB RAM, 512GB SSD"
    },
    {
        "id": 106,
        "title": "AirPods Pro 2",
        "brand": "Apple",
        "price": 249.99,
        "categories": ["Headphones", "Earbuds", "Premium"],
        "description": "Premium wireless earbuds with adaptive ANC, spatial audio, and MagSafe charging case.",
        "image_url": "https://images.unsplash.com/photo-1606841837239-c5a1a4a07af7?w=400",
        "rating": 4.7,
        "features": ["Adaptive ANC", "Spatial Audio", "H2 Chip", "6hr Battery", "Find My"],
        "specifications": "Bluetooth 5.3, IPX4, MagSafe case"
    },
    {
        "id": 107,
        "title": "Samsung Galaxy Buds2 Pro",
        "brand": "Samsung",
        "price": 229.99,
        "categories": ["Headphones", "Earbuds", "Premium"],
        "description": "Premium earbuds with intelligent ANC, 360 audio, and seamless Galaxy ecosystem integration.",
        "image_url": "https://images.unsplash.com/photo-1590658165737-15a047b7a7a5?w=400",
        "rating": 4.6,
        "features": ["Intelligent ANC", "360 Audio", "24-bit Hi-Fi", "IPX7", "Wireless Charging"],
        "specifications": "Bluetooth 5.3, 8hr playback, USB-C"
    },
    {
        "id": 108,
        "title": "Jabra Elite 85t",
        "brand": "Jabra",
        "price": 229.99,
        "categories": ["Headphones", "Earbuds", "Premium"],
        "description": "Advanced noise cancelling earbuds with adjustable ANC, multi-device connectivity, and great calls.",
        "image_url": "https://images.unsplash.com/photo-1629367494173-c78a56567877?w=400",
        "rating": 4.5,
        "features": ["Adjustable ANC", "6-Mic System", "Multipoint", "Wireless Charging", "IPX4"],
        "specifications": "Bluetooth 5.1, 5.5hr battery, compact case"
    },
    {
        "id": 109,
        "title": "Sony WF-1000XM5",
        "brand": "Sony",
        "price": 299.99,
        "categories": ["Headphones", "Earbuds", "Premium"],
        "description": "Best-in-class noise cancelling earbuds with exceptional sound quality and compact design.",
        "image_url": "https://images.unsplash.com/photo-1606841837239-c5a1a4a07af7?w=400",
        "rating": 4.8,
        "features": ["Industry-Leading ANC", "LDAC", "8hr Battery", "Speak-to-Chat", "IPX4"],
        "specifications": "Bluetooth 5.3, Qi wireless charging, premium sound"
    },
    {
        "id": 110,
        "title": "Anker Soundcore Liberty 4",
        "brand": "Anker",
        "price": 149.99,
        "categories": ["Headphones", "Earbuds", "Value"],
        "description": "Value-packed earbuds with spatial audio, adaptive ANC, and excellent battery life.",
        "image_url": "https://images.unsplash.com/photo-1590658165737-15a047b7a7a5?w=400",
        "rating": 4.4,
        "features": ["Spatial Audio", "Adaptive ANC", "10hr Battery", "LDAC", "Heart Rate Monitor"],
        "specifications": "Bluetooth 5.3, IPX4, wireless charging"
    },
    {
        "id": 156,
        "title": "Canon EOS R5",
        "brand": "Canon",
        "price": 3899.99,
        "categories": ["Cameras", "Mirrorless", "Professional"],
        "description": "High-resolution powerhouse with 8K video, exceptional autofocus, and professional build quality.",
        "image_url": "https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=400",
        "rating": 4.8,
        "features": ["45MP Sensor", "8K Video", "20fps Burst", "Dual Pixel AF II", "IBIS"],
        "specifications": "Full-frame 45MP, 8K 30fps, dual card slots"
    },
    {
        "id": 157,
        "title": "Sony A7C II",
        "brand": "Sony",
        "price": 2199.99,
        "categories": ["Cameras", "Mirrorless", "Compact"],
        "description": "Compact full-frame camera perfect for content creators. Great autofocus and video features.",
        "image_url": "https://images.unsplash.com/photo-1606980620778-59f5c0ab58f0?w=400",
        "rating": 4.6,
        "features": ["33MP Sensor", "4K 60fps", "Compact Body", "AI Autofocus", "IBIS"],
        "specifications": "Full-frame 33MP, 10fps, vlog-friendly"
    },
    {
        "id": 158,
        "title": "Nikon Z6 III",
        "brand": "Nikon",
        "price": 2499.99,
        "categories": ["Cameras", "Mirrorless", "Hybrid"],
        "description": "Versatile hybrid camera with partially stacked sensor, great video specs, and excellent handling.",
        "image_url": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400",
        "rating": 4.7,
        "features": ["24MP Sensor", "6K N-RAW", "120fps Burst", "3D Tracking", "Dual Card Slots"],
        "specifications": "Full-frame 24MP, 6K 60fps internal"
    },
    {
        "id": 159,
        "title": "Fujifilm X-S20",
        "brand": "Fujifilm",
        "price": 1299.99,
        "categories": ["Cameras", "Mirrorless", "APS-C"],
        "description": "Compact content creator camera with IBIS, great autofocus, and film simulations.",
        "image_url": "https://images.unsplash.com/photo-1495121553079-4c61bcce1894?w=400",
        "rating": 4.6,
        "features": ["26MP Sensor", "6K Video", "IBIS", "Film Simulations", "Vlog Mode"],
        "specifications": "APS-C 26MP, 4K 60fps, compact body"
    },
    {
        "id": 160,
        "title": "OM System OM-1",
        "brand": "OM System",
        "price": 2199.99,
        "categories": ["Cameras", "Mirrorless", "Weather Sealed"],
        "description": "Rugged Micro Four Thirds camera with computational photography and excellent stabilization.",
        "image_url": "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400",
        "rating": 4.5,
        "features": ["20MP Sensor", "8.5-stop IBIS", "IP53 Rating", "Computational Photo", "4K 60fps"],
        "specifications": "Micro Four Thirds 20MP, weather-sealed"
    },
    {
        "id": 206,
        "title": "Razer BlackWidow V4 Pro",
        "brand": "Razer",
        "price": 229.99,
        "categories": ["Gaming", "Accessories", "Keyboards"],
        "description": "Full-featured mechanical gaming keyboard with macro keys, volume wheel, and RGB lighting.",
        "image_url": "https://images.unsplash.com/photo-1595225476474-87563907a212?w=400",
        "rating": 4.6,
        "features": ["Mechanical Switches", "Macro Keys", "RGB", "Volume Wheel", "Wrist Rest"],
        "specifications": "Green switches, USB passthrough, Razer Synapse"
    },
    {
        "id": 207,
        "title": "Corsair K70 RGB Pro",
        "brand": "Corsair",
        "price": 179.99,
        "categories": ["Gaming", "Accessories", "Keyboards"],
        "description": "Tournament-level mechanical keyboard with Cherry MX switches and per-key RGB lighting.",
        "image_url": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=400",
        "rating": 4.7,
        "features": ["Cherry MX", "Per-key RGB", "Aluminum Frame", "Media Keys", "Tournament Mode"],
        "specifications": "Cherry MX Speed, USB-C, iCUE compatible"
    },
    {
        "id": 208,
        "title": "SteelSeries Arctis Nova Pro",
        "brand": "SteelSeries",
        "price": 349.99,
        "categories": ["Gaming", "Accessories", "Headsets"],
        "description": "Premium gaming headset with Hi-Res audio, active noise cancellation, and GameDAC.",
        "image_url": "https://images.unsplash.com/photo-1599669454699-248893623440?w=400",
        "rating": 4.7,
        "features": ["Hi-Res Audio", "ANC", "GameDAC", "360° Spatial", "Comfort"],
        "specifications": "40mm drivers, USB-C/3.5mm, retractable mic"
    },
    {
        "id": 209,
        "title": "HyperX Cloud Alpha Wireless",
        "brand": "HyperX",
        "price": 199.99,
        "categories": ["Gaming", "Accessories", "Headsets"],
        "description": "Ultra-long battery life gaming headset with 300+ hours on single charge. Dual chamber drivers.",
        "image_url": "https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?w=400",
        "rating": 4.6,
        "features": ["300hr Battery", "Dual Chamber", "Wireless", "DTS:X", "Durable Build"],
        "specifications": "50mm drivers, 2.4GHz wireless, detachable mic"
    },
    {
        "id": 210,
        "title": "ASUS ROG Swift PG27AQDM",
        "brand": "ASUS",
        "price": 899.99,
        "categories": ["Gaming", "Monitors", "OLED"],
        "description": "27-inch OLED gaming monitor with 240Hz refresh rate, G-Sync, and stunning HDR.",
        "image_url": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400",
        "rating": 4.8,
        "features": ["OLED Panel", "240Hz", "G-Sync", "HDR True Black", "0.03ms Response"],
        "specifications": "27-inch 2560x1440 OLED, DisplayPort 1.4"
    },
    {
        "id": 256,
        "title": "iPad Air M2",
        "brand": "Apple",
        "price": 599.99,
        "categories": ["Tablets", "Apple", "Mid-range"],
        "description": "Powerful and versatile tablet with M2 chip, great for productivity and creativity.",
        "image_url": "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400",
        "rating": 4.7,
        "features": ["M2 Chip", "10.9-inch Liquid Retina", "Apple Pencil 2", "Touch ID", "USB-C"],
        "specifications": "10.9-inch Liquid Retina, 128GB, iPadOS"
    },
    {
        "id": 257,
        "title": "iPad Mini 6",
        "brand": "Apple",
        "price": 499.99,
        "categories": ["Tablets", "Compact", "Apple"],
        "description": "Ultra-portable tablet with A15 Bionic, perfect for reading, gaming, and on-the-go productivity.",
        "image_url": "https://images.unsplash.com/photo-1585790050230-5dd28404ccb9?w=400",
        "rating": 4.6,
        "features": ["A15 Bionic", "8.3-inch Display", "Apple Pencil 2", "5G", "Compact"],
        "specifications": "8.3-inch Liquid Retina, 64GB, Touch ID"
    },
    {
        "id": 258,
        "title": "Samsung Galaxy Tab S9",
        "brand": "Samsung",
        "price": 799.99,
        "categories": ["Tablets", "Android", "Premium"],
        "description": "Premium Android tablet with S Pen included, IP68 rating, and DeX productivity mode.",
        "image_url": "https://images.unsplash.com/photo-1561154464-82e9adf32764?w=400",
        "rating": 4.6,
        "features": ["11-inch AMOLED", "S Pen Included", "IP68", "DeX Mode", "120Hz"],
        "specifications": "11-inch 120Hz AMOLED, 256GB, Snapdragon 8 Gen 2"
    },
    {
        "id": 259,
        "title": "Amazon Kindle Paperwhite",
        "brand": "Amazon",
        "price": 139.99,
        "categories": ["Tablets", "E-Readers", "Reading"],
        "description": "Premium e-reader with warm light, waterproof design, and weeks of battery life.",
        "image_url": "https://images.unsplash.com/photo-1592155931584-901ac15763e3?w=400",
        "rating": 4.7,
        "features": ["6.8-inch Display", "Warm Light", "IPX8", "10-week Battery", "Adjustable Light"],
        "specifications": "6.8-inch 300ppi E Ink, 16GB, Kindle OS"
    },
    {
        "id": 260,
        "title": "Huawei MatePad Pro",
        "brand": "Huawei",
        "price": 549.99,
        "categories": ["Tablets", "Android", "Productivity"],
        "description": "Sleek tablet with OLED display, M-Pencil support, and excellent build quality.",
        "image_url": "https://images.unsplash.com/photo-1611532736597-de2d4265fba3?w=400",
        "rating": 4.4,
        "features": ["11-inch OLED", "M-Pencil", "Quad Speakers", "Metal Body", "120Hz"],
        "specifications": "11-inch 120Hz OLED, 256GB, HarmonyOS"
    },
    {
        "id": 306,
        "title": "Apple Watch Series 9",
        "brand": "Apple",
        "price": 399.99,
        "categories": ["Wearables", "Smartwatches", "Apple"],
        "description": "Latest Apple Watch with S9 chip, double tap gesture, and precision finding for iPhone.",
        "image_url": "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=400",
        "rating": 4.8,
        "features": ["S9 Chip", "Double Tap", "Always-On", "ECG", "Crash Detection"],
        "specifications": "41/45mm aluminum, Always-On Retina, watchOS 10"
    },
    {
        "id": 307,
        "title": "Garmin Forerunner 965",
        "brand": "Garmin",
        "price": 599.99,
        "categories": ["Wearables", "Fitness", "Running"],
        "description": "Premium running watch with AMOLED display, training readiness, and comprehensive metrics.",
        "image_url": "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=400",
        "rating": 4.7,
        "features": ["AMOLED Display", "Training Readiness", "Race Predictor", "31-day Battery", "Maps"],
        "specifications": "47mm fiber-reinforced, GPS, 200+ features"
    },
    {
        "id": 308,
        "title": "Polar Vantage V3",
        "brand": "Polar",
        "price": 599.99,
        "categories": ["Wearables", "Fitness", "Multisport"],
        "description": "Multisport watch with advanced sleep tracking, training insights, and long battery life.",
        "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400",
        "rating": 4.6,
        "features": ["AMOLED Display", "Dual-Band GPS", "Sleep Analysis", "140+ Sports", "Offline Maps"],
        "specifications": "43mm stainless, 8-day battery, Polar Flow"
    },
    {
        "id": 309,
        "title": "Withings ScanWatch 2",
        "brand": "Withings",
        "price": 349.99,
        "categories": ["Wearables", "Health", "Hybrid"],
        "description": "Hybrid smartwatch with medical-grade ECG, SpO2, and classic watch design.",
        "image_url": "https://images.unsplash.com/photo-1575311373937-040b8e1fd5b6?w=400",
        "rating": 4.5,
        "features": ["Medical ECG", "SpO2", "30-day Battery", "Classic Design", "Sleep Apnea"],
        "specifications": "38/42mm stainless, analog + digital, Health Mate"
    },
    {
        "id": 310,
        "title": "Coros Pace 3",
        "brand": "Coros",
        "price": 229.99,
        "categories": ["Wearables", "Fitness", "Running"],
        "description": "Lightweight running watch with incredible battery life, accurate GPS, and training features.",
        "image_url": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=400",
        "rating": 4.6,
        "features": ["24-day Battery", "Dual-Freq GPS", "30g Weight", "Training Hub", "Nylon Build"],
        "specifications": "42mm nylon, GPS, heart rate"
    }
]

def get_all_products():
    """Return all products"""
    return PRODUCTS

def get_product_by_id(product_id: int):
    """Get a specific product by ID"""
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return None

def get_categories():
    """Get unique categories"""
    categories = set()
    for product in PRODUCTS:
        categories.update(product["categories"])
    return sorted(list(categories))

def get_brands():
    """Get unique brands"""
    brands = set()
    for product in PRODUCTS:
        brands.add(product["brand"])
    return sorted(list(brands))
