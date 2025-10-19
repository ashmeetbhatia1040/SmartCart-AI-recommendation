# 🚀 Deployment Guide - SmartCart AI

Complete guide for deploying SmartCart AI to Vercel (Free Tier)

## 🌍 Live Deployments

- **Frontend**: https://smart-cart-ai-recommendation-98k7.vercel.app/
- **Backend**: https://smart-cart-ai-recommendation.vercel.app/

## ⚠️ IMPORTANT: Fix Connection Issue

If you see "Failed to load products" or search doesn't work:

### Quick Fix (Vercel Dashboard):

1. Go to: https://vercel.com/dashboard
2. Select your **frontend project** (smart-cart-ai-recommendation-98k7)
3. Click **Settings** → **Environment Variables**
4. Add new variable:
   - **Name**: `VITE_API_URL`
   - **Value**: `https://smart-cart-ai-recommendation.vercel.app`
   - **Environments**: Check all (Production, Preview, Development)
5. Click **Save**
6. Go to **Deployments** → Click **...** on latest → **Redeploy**
7. Wait for deployment (2-3 minutes)
8. Test: https://smart-cart-ai-recommendation-98k7.vercel.app/

---

## 📋 Pre-Deployment Checklist

- ✅ Application works locally
- ✅ Backend runs without errors
- ✅ Frontend connects to backend
- ✅ All features tested
- ✅ Git repository initialized (optional)
- ✅ Vercel account created

## 🌐 Create Vercel Account

1. Go to https://vercel.com
2. Click "Sign Up"
3. Sign up with:
   - GitHub (recommended)
   - GitLab
   - Bitbucket
   - Email
4. Complete email verification

## 📦 Install Vercel CLI

Open PowerShell and run:

```powershell
npm install -g vercel
```

Verify installation:
```powershell
vercel --version
```

Login to Vercel:
```powershell
vercel login
```

Choose your login method and authenticate.

## 🔧 Backend Deployment

### Step 1: Prepare Backend

Navigate to backend:
```powershell
cd "d:\Projects\Furniture Recomendation Model\backend"
```

Verify files exist:
```powershell
dir
# Should show: api.py, products_data.py, requirements.txt, vercel.json
```

### Step 2: Deploy Backend

```powershell
vercel --prod
```

**Follow the prompts:**

```
? Set up and deploy "backend"? [Y/n] Y
? Which scope do you want to deploy to? [Select your account]
? Link to existing project? [y/N] N
? What's your project's name? smartcart-ai-backend
? In which directory is your code located? ./
? Want to override the settings? [y/N] N
```

**Wait for deployment...**

✅ **Success!** Note your deployment URL:
```
✅  Production: https://smartcart-ai-backend-xxxxx.vercel.app
```

### Step 3: Test Backend

Visit these URLs (replace with your actual URL):

```
https://smartcart-ai-backend-xxxxx.vercel.app
https://smartcart-ai-backend-xxxxx.vercel.app/api/health
https://smartcart-ai-backend-xxxxx.vercel.app/api/recommend?limit=5
```

All should return valid JSON responses.

## 🎨 Frontend Deployment

### Step 1: Update API URL

Navigate to frontend:
```powershell
cd "d:\Projects\Furniture Recomendation Model\frontend"
```

Edit `.env` file:
```bash
VITE_API_URL=https://smartcart-ai-backend-xxxxx.vercel.app
```

**Replace** `xxxxx` with your actual backend URL!

### Step 2: Test Locally with Production Backend

```powershell
npm run dev
```

- Open http://localhost:3000
- Test search functionality
- Verify products load
- Check analytics dashboard
- **IMPORTANT**: Make sure everything works!

### Step 3: Deploy Frontend

```powershell
vercel --prod
```

**Follow the prompts:**

```
? Set up and deploy "frontend"? [Y/n] Y
? Which scope do you want to deploy to? [Select your account]
? Link to existing project? [y/N] N
? What's your project's name? smartcart-ai-frontend
? In which directory is your code located? ./
? Want to override the settings? [y/N] N
```

**Wait for deployment...**

✅ **Success!** Your app is live:
```
✅  Production: https://smartcart-ai-frontend-xxxxx.vercel.app
```

### Step 4: Test Production App

Visit your frontend URL and test:

- ✅ Homepage loads
- ✅ Search works
- ✅ Product cards display
- ✅ Filters work
- ✅ Analytics page loads
- ✅ Charts render
- ✅ Dark mode toggle works
- ✅ Mobile responsive
- ✅ No console errors

## 🔒 Update CORS Settings

After deployment, update backend CORS for security:

Edit `backend/api.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://smartcart-ai-frontend-xxxxx.vercel.app",
        "http://localhost:3000"  # Keep for local development
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Redeploy backend:
```powershell
cd backend
vercel --prod
```

## 📱 Custom Domain (Optional)

### Add Custom Domain to Frontend

1. Go to https://vercel.com/dashboard
2. Select your frontend project
3. Click "Settings" → "Domains"
4. Add your domain: `smartcart.yourdomain.com`
5. Follow DNS configuration instructions
6. Wait for SSL certificate (automatic)

### Update Backend CORS

Add your custom domain to CORS origins:
```python
allow_origins=[
    "https://smartcart.yourdomain.com",
    # ... existing origins
]
```

## 🔄 Updating Your Deployment

### Update Backend

```powershell
cd "d:\Projects\Furniture Recomendation Model\backend"
# Make your changes to api.py or products_data.py
vercel --prod
```

### Update Frontend

```powershell
cd "d:\Projects\Furniture Recomendation Model\frontend"
# Make your changes
vercel --prod
```

## 📊 Monitoring

### View Deployment Logs

```powershell
vercel logs [deployment-url]
```

### Dashboard Monitoring

1. Go to https://vercel.com/dashboard
2. Select your project
3. View:
   - Deployment history
   - Real-time logs
   - Performance metrics
   - Bandwidth usage

## 🐛 Troubleshooting Deployment

### Backend Issues

**Problem**: Backend deployment fails

**Solutions**:
```powershell
# Check vercel.json syntax
cat backend/vercel.json

# Verify requirements.txt
cat backend/requirements.txt

# Check for syntax errors
python backend/api.py
```

**Problem**: API returns 404

**Solution**: Check vercel.json routes configuration

**Problem**: Module import errors

**Solution**: Ensure all dependencies in requirements.txt

### Frontend Issues

**Problem**: Frontend can't connect to backend

**Solutions**:
1. Check `.env` file has correct VITE_API_URL
2. Verify backend is deployed and working
3. Check browser console for CORS errors
4. Update backend CORS settings

**Problem**: Build fails

**Solutions**:
```powershell
# Clear build cache
npm run build

# Check for TypeScript errors
# Check for missing dependencies
npm install
```

**Problem**: Environment variables not working

**Solutions**:
1. Variables must start with `VITE_`
2. Re-deploy after changing `.env`
3. Set in Vercel dashboard: Settings → Environment Variables

### CORS Issues

If you see CORS errors:

1. **Backend** `api.py`:
```python
allow_origins=["*"]  # For testing only
# Or specific origins:
allow_origins=["https://your-frontend.vercel.app"]
```

2. Redeploy backend
3. Clear browser cache
4. Test again

## 📈 Performance Optimization

### Backend Optimization

1. **Use caching**:
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def get_all_products():
    return PRODUCTS
```

2. **Enable compression** (Vercel does this automatically)

### Frontend Optimization

1. **Code splitting** (already configured with Vite)
2. **Image optimization**:
```jsx
loading="lazy"
```

3. **Build optimization**:
```powershell
npm run build
# Check dist/ folder size
```

## 💰 Vercel Free Tier Limits

- ✅ **Bandwidth**: 100GB/month
- ✅ **Serverless executions**: 100GB-hours
- ✅ **Builds**: 100 hours/month
- ✅ **Deployments**: Unlimited
- ✅ **Projects**: Unlimited
- ✅ **Team members**: 1 (Hobby plan)

**Your app should stay well within free limits!**

## 🎯 Post-Deployment Checklist

- [ ] Backend deployed successfully
- [ ] Frontend deployed successfully
- [ ] API endpoints working
- [ ] Products loading correctly
- [ ] Search functionality working
- [ ] Filters working
- [ ] Analytics charts displaying
- [ ] Dark mode toggle working
- [ ] Mobile responsive
- [ ] No console errors
- [ ] CORS configured correctly
- [ ] Custom domain configured (optional)
- [ ] Tested on multiple devices
- [ ] Tested on different browsers

## 🔗 Share Your Project

Once deployed, you can share:

```
🚀 SmartCart AI - Live Demo
Frontend: https://smartcart-ai-frontend-xxxxx.vercel.app
Backend API: https://smartcart-ai-backend-xxxxx.vercel.app/api/health

Features:
- 🤖 AI-powered product search
- 📊 Interactive analytics dashboard
- 🎨 Modern glassmorphism UI
- 📱 Fully responsive design
- 🌙 Dark mode support
```

## 📚 Additional Resources

- **Vercel Documentation**: https://vercel.com/docs
- **Vercel CLI Reference**: https://vercel.com/docs/cli
- **Vercel Serverless Functions**: https://vercel.com/docs/serverless-functions/introduction
- **Deployment FAQ**: https://vercel.com/support

## 🎓 Next Steps

1. **Monitor Usage**: Check Vercel dashboard regularly
2. **Gather Feedback**: Share with friends/colleagues
3. **Iterate**: Make improvements based on feedback
4. **Scale**: Upgrade to Pro plan if needed
5. **Add Features**: Continue development
6. **Portfolio**: Add to your portfolio with deployment link

---

**Congratulations! Your SmartCart AI is now live! 🎉**

**Demo URLs**: 
- Frontend: `your-frontend-url.vercel.app`
- Backend: `your-backend-url.vercel.app`

**Next**: Share your project and showcase your work! 🚀
