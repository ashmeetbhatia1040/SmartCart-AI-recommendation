# 🛒 SmartCart AI - AI-Powered Electronics Recommendation System

![SmartCart AI](https://img.shields.io/badge/AI-Powered-emerald?style=for-the-badge)
![React](https://img.shields.io/badge/React-18.2-61DAFB?style=for-the-badge&logo=react)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688?style=for-the-badge&logo=fastapi)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.3-38B2AC?style=for-the-badge&logo=tailwind-css)

A modern, AI-powered product recommendation system for electronics shopping. Built with React, FastAPI, and Tailwind CSS featuring a stunning emerald/teal glassmorphism design.

## ✨ Features

- 🤖 **AI-Powered Recommendations** - Smart product search with relevance scoring
- 📊 **Analytics Dashboard** - Comprehensive insights with interactive charts
- 🎨 **Modern UI/UX** - Glassmorphism design with smooth animations
- 🔍 **Advanced Filters** - Search by category, brand, price, and rating
- ⚡ **Lightning Fast** - Optimized performance with Vite
- 📱 **Fully Responsive** - Works seamlessly on all devices
- 🌙 **Dark Mode** - Toggle between light and dark themes in analytics

## 🏗️ Project Structure

```
SmartCart AI/
├── backend/                    # FastAPI Backend
│   ├── api.py                 # Main API endpoints
│   ├── products_data.py       # Product database (300+ items)
│   ├── requirements.txt       # Python dependencies
│   └── vercel.json           # Vercel serverless config
│
└── frontend/                  # React Frontend
    ├── src/
    │   ├── components/        # Reusable UI components
    │   │   ├── ProductCard.jsx
    │   │   ├── SearchBar.jsx
    │   │   ├── LoadingSpinner.jsx
    │   │   └── ErrorBoundary.jsx
    │   ├── pages/            # Page components
    │   │   ├── HomePage.jsx
    │   │   └── AnalyticsPage.jsx
    │   ├── utils/            # Utility functions
    │   │   └── api.js
    │   ├── App.jsx           # Main app component
    │   ├── main.jsx          # Entry point
    │   └── index.css         # Global styles
    ├── package.json
    ├── tailwind.config.js    # Custom theme
    ├── vite.config.js
    └── vercel.json           # Vercel deployment config
```

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ and npm
- Python 3.9+
- Git

### Local Development

#### 1️⃣ Clone and Setup

```bash
cd "d:\Projects\Furniture Recomendation Model"
```

#### 2️⃣ Backend Setup

```bash
# Navigate to backend
cd backend

# Install dependencies
pip install -r requirements.txt

# Run the API server
python api.py
# Server runs at http://localhost:8000
```

#### 3️⃣ Frontend Setup

```bash
# Navigate to frontend (new terminal)
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
# App opens at http://localhost:3000
```

### 🌐 API Endpoints

- `GET /` - API info
- `GET /api/health` - Health check
- `GET /api/recommend` - Get product recommendations
  - Query params: `query`, `category`, `brand`, `min_price`, `max_price`, `min_rating`, `limit`
- `GET /api/analytics` - Get analytics data
- `GET /api/categories` - Get all categories
- `GET /api/brands` - Get all brands

## 📊 Dataset

The system includes **300+ electronics products** across categories:

- 📱 **Smartphones** (Apple, Samsung, Google, OnePlus, Xiaomi)
- 💻 **Laptops** (MacBook, Dell, Lenovo, ASUS, HP)
- 🎧 **Headphones** (Sony, Apple, Bose, Sennheiser, Beats)
- 📷 **Cameras** (Sony, Canon, Nikon, Fujifilm, Panasonic)
- 🎮 **Gaming** (PlayStation, Xbox, Nintendo, PC Gaming)
- 📱 **Tablets** (iPad, Galaxy Tab, Surface, Kindle)
- ⌚ **Smartwatches** (Apple Watch, Galaxy Watch, Garmin, Fitbit)

## 🎨 Design System

### Color Palette

- **Primary**: Emerald (#10b981) & Teal (#14b8a6)
- **Accents**: Cyan, Blue gradients
- **Text**: Gray scale for optimal readability

### Typography

- **Headings**: Poppins (Display font)
- **Body**: Inter (System font)

### Key Design Features

- ✨ Glassmorphism effects with backdrop blur
- 🎯 Pill-style navigation with active indicators
- 🔄 Smooth hover transitions and animations
- 📦 Card-based grid layout
- 🌈 Gradient backgrounds and buttons

## 🧠 AI Features

### Recommendation Algorithm

```python
# Scoring System:
- Title match: +3 points
- Description match: +2 points
- Category match: +2 points
- Brand match: +1 point
- Features match: +1 point
```

### Analytics Insights

- Price distribution histograms
- Brand popularity analysis
- Category distribution pie charts
- Average price trends
- Product count statistics

## 🚀 Deployment

### Backend (Vercel Serverless)

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Deploy backend:
```bash
cd backend
vercel --prod
```

3. Note your backend URL (e.g., `https://your-api.vercel.app`)

### Frontend (Vercel)

1. Update `.env` with production API URL:
```bash
VITE_API_URL=https://your-api.vercel.app
```

2. Deploy frontend:
```bash
cd frontend
vercel --prod
```

### Environment Variables

**Frontend (.env)**
```
VITE_API_URL=your_backend_url
```

**Backend** (No env vars needed for basic setup)

## 📱 Usage Examples

### Search for Products

```javascript
// Search for smartphones
GET /api/recommend?query=smartphone&category=Smartphones&min_rating=4.5

// Search within price range
GET /api/recommend?min_price=500&max_price=1500&brand=Apple

// Get top-rated laptops
GET /api/recommend?category=Laptops&min_rating=4.7&limit=10
```

## 🛠️ Tech Stack

### Frontend
- ⚛️ React 18.2
- ⚡ Vite 5.0
- 🎨 Tailwind CSS 3.3
- 📈 Recharts 2.10
- 🔄 React Router 6.20
- 📡 Axios 1.6

### Backend
- 🐍 Python 3.9+
- 🚀 FastAPI 0.104
- 🔧 Pydantic 2.5
- 🦄 Uvicorn 0.24

### Deployment
- ☁️ Vercel (Serverless Functions)
- 🌐 CDN for static assets

## 🎯 Key Differentiators

Compared to similar projects, SmartCart AI features:

1. ✅ **Emerald/Teal color scheme** vs blue/indigo
2. ✅ **Card-grid layout** vs list view
3. ✅ **Pill navigation** vs underlined tabs
4. ✅ **Glassmorphism design** vs flat UI
5. ✅ **Electronics theme** vs furniture
6. ✅ **Dark mode toggle** for analytics
7. ✅ **Custom animations** and loading states
8. ✅ **Separate product cards** with hover effects

## 🔧 Development Scripts

### Backend
```bash
python api.py              # Start API server
```

### Frontend
```bash
npm run dev               # Start development server
npm run build            # Build for production
npm run preview          # Preview production build
```

## 📈 Performance Optimizations

- ⚡ Vite for fast HMR and builds
- 🎯 Code splitting with React Router
- 🖼️ Lazy image loading
- 📦 Optimized bundle size
- 🔄 Efficient API calls with caching
- 🎨 CSS purging in production

## 🐛 Troubleshooting

### Port Already in Use

```bash
# Kill process on port 8000 (backend)
npx kill-port 8000

# Kill process on port 3000 (frontend)
npx kill-port 3000
```

### CORS Issues

Ensure backend `api.py` has proper CORS configuration:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Dependencies Not Installing

```bash
# Clear npm cache
npm cache clean --force
rm -rf node_modules package-lock.json
npm install

# Clear pip cache
pip cache purge
pip install -r requirements.txt --no-cache-dir
```

## 📝 License

This project was created for a 2-day development challenge. Feel free to use and modify for your own projects.

## 🙏 Acknowledgments

- Unsplash for product images
- Tailwind CSS for the amazing utility framework
- FastAPI for the blazing-fast backend framework
- React and Vite teams for excellent developer experience

## 🎓 Learning Resources

This project demonstrates:
- Modern React patterns and hooks
- RESTful API design
- Responsive web design
- Data visualization
- AI-powered search algorithms
- Deployment to production

---

**Built with ❤️ in 2 days** | [Live Demo](#) | [Report Bug](#) | [Request Feature](#)

