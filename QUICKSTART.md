# SmartCart AI - Quick Start Guide

## 🚀 Development Setup (5 minutes)

### Step 1: Backend Setup

Open a terminal in the project directory and run:

```bash
cd backend
pip install -r requirements.txt
python api.py
```

✅ Backend should now be running at http://localhost:8000
✅ Visit http://localhost:8000/api/health to verify

### Step 2: Frontend Setup

Open a NEW terminal (keep backend running) and run:

```bash
cd frontend
npm install
npm run dev
```

✅ Frontend should open automatically at http://localhost:3000
✅ You should see the SmartCart AI homepage

## 🧪 Testing the Application

### Test the Search
1. Open http://localhost:3000
2. Type "smartphone" in the search bar
3. Click "Search" or press Enter
4. You should see product results

### Test Filters
1. Try selecting different categories (Smartphones, Laptops, etc.)
2. Set a price range (e.g., $500-$1500)
3. Select a minimum rating (4.5+)
4. Click "Search" to apply filters

### Test Analytics
1. Click the "📊 Analytics" pill in the navigation
2. View charts showing:
   - Price distribution
   - Top brands
   - Category distribution
   - Average prices by category
3. Toggle dark mode with the 🌙 button

## 🌐 Deployment to Vercel

### Prerequisites
```bash
npm install -g vercel
```

### Deploy Backend (Step 1)

```bash
cd backend
vercel --prod
```

Follow the prompts:
- Set up and deploy? **Y**
- Which scope? Select your account
- Link to existing project? **N**
- Project name? **smartcart-ai-backend**
- Directory? **./backend** (or press Enter)
- Override settings? **N**

✅ Note your deployment URL (e.g., https://smartcart-ai-backend.vercel.app)

### Deploy Frontend (Step 2)

1. Update the API URL in frontend/.env:
```bash
VITE_API_URL=https://your-backend-url.vercel.app
```

2. Deploy:
```bash
cd frontend
vercel --prod
```

Follow the prompts:
- Set up and deploy? **Y**
- Which scope? Select your account
- Link to existing project? **N**
- Project name? **smartcart-ai-frontend**
- Directory? **./frontend** (or press Enter)
- Override settings? **N**

✅ Your app is now live at https://smartcart-ai-frontend.vercel.app

## 🔧 Troubleshooting

### Backend won't start
```bash
# Check if port 8000 is in use
netstat -ano | findstr :8000

# Kill the process (Windows PowerShell)
Stop-Process -Id <PID> -Force

# Or try a different port
uvicorn api:app --host 0.0.0.0 --port 8001
```

### Frontend won't start
```bash
# Clear node_modules and reinstall
Remove-Item -Recurse -Force node_modules
Remove-Item package-lock.json
npm install
npm run dev
```

### CORS errors
Update backend/api.py CORS settings:
```python
allow_origins=["http://localhost:3000", "https://your-frontend-url.vercel.app"]
```

### Products not loading
1. Check backend is running: http://localhost:8000/api/health
2. Check browser console for errors (F12)
3. Verify .env file has correct API URL

## 📊 API Testing

Test endpoints with curl or Postman:

```bash
# Health check
curl http://localhost:8000/api/health

# Get all products
curl http://localhost:8000/api/recommend

# Search for smartphones
curl "http://localhost:8000/api/recommend?query=smartphone&limit=5"

# Get analytics
curl http://localhost:8000/api/analytics
```

## 🎯 Success Checklist

- ✅ Backend running on port 8000
- ✅ Frontend running on port 3000
- ✅ Can search for products
- ✅ Filters work correctly
- ✅ Analytics dashboard displays charts
- ✅ Dark mode toggle works
- ✅ Product cards display properly
- ✅ Mobile responsive design works

## 📱 Mobile Testing

1. Find your local IP address:
```bash
ipconfig  # Windows
ifconfig  # Mac/Linux
```

2. Update frontend/.env:
```bash
VITE_API_URL=http://YOUR_LOCAL_IP:8000
```

3. Access from phone:
```
http://YOUR_LOCAL_IP:3000
```

## 🚀 Production Optimization

Before deploying:

1. ✅ Update CORS origins in backend/api.py
2. ✅ Set production API URL in frontend/.env
3. ✅ Test all features locally
4. ✅ Check for console errors
5. ✅ Verify mobile responsiveness
6. ✅ Test on different browsers

## 📝 Environment Variables

### Backend (.env) - Optional
```bash
# Add if needed
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
```

### Frontend (.env) - Required
```bash
VITE_API_URL=http://localhost:8000  # Development
# VITE_API_URL=https://your-backend.vercel.app  # Production
```

## 🎓 Next Steps

1. **Customize Products**: Edit `backend/products_data.py` to add your own products
2. **Enhance UI**: Modify Tailwind config in `frontend/tailwind.config.js`
3. **Add Features**: 
   - User authentication
   - Shopping cart
   - Product reviews
   - Wishlist functionality
4. **Deploy**: Follow deployment steps above

## 💡 Tips

- Keep backend terminal open while developing
- Use React DevTools for debugging
- Check Network tab in browser for API calls
- Use Vercel CLI for deployment previews
- Monitor Vercel logs for errors

---

**Need Help?** Check the main README.md for detailed documentation.

**Happy Coding! 🎉**
