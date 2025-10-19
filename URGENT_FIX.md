# 🔧 URGENT FIX - SmartCart AI Connection Issue

## ⚠️ Problem
Frontend shows "Failed to load products" because it's trying to connect to `localhost:8000` instead of the production backend.

## ✅ Solution (5 Minutes)

### Step 1: Set Environment Variable in Vercel

1. **Open Vercel Dashboard**: https://vercel.com/dashboard

2. **Select Frontend Project**: 
   - Look for: `smart-cart-ai-recommendation-98k7` or similar
   - Click on it

3. **Go to Settings**:
   - Click **Settings** tab (top menu)
   - Click **Environment Variables** (left sidebar)

4. **Add Variable**:
   - Click **Add New** button
   - Enter:
     ```
     Key: VITE_API_URL
     Value: https://smart-cart-ai-recommendation.vercel.app
     ```
   - Select environments: ✓ Production ✓ Preview ✓ Development
   - Click **Save**

5. **Redeploy**:
   - Go to **Deployments** tab
   - Click **•••** (three dots) on the latest deployment
   - Click **Redeploy**
   - Wait 2-3 minutes for deployment to complete

6. **Test**:
   - Visit: https://smart-cart-ai-recommendation-98k7.vercel.app/
   - Search for "apple" or "laptop"
   - Should see products now! ✅

---

## 🖼️ Visual Guide

### Finding Environment Variables

```
Vercel Dashboard
  └── Your Project (smart-cart-ai-recommendation-98k7)
        └── Settings
              └── Environment Variables
                    └── Add New
                          ├── Key: VITE_API_URL
                          ├── Value: https://smart-cart-ai-recommendation.vercel.app
                          └── Environments: [✓] Production [✓] Preview [✓] Development
```

### Redeploying

```
Vercel Dashboard
  └── Your Project
        └── Deployments
              └── Latest Deployment
                    └── ••• (menu)
                          └── Redeploy
```

---

## 🧪 Verify It's Working

After redeployment:

1. **Open**: https://smart-cart-ai-recommendation-98k7.vercel.app/
2. **Search**: Type "laptop" and click Search
3. **Expected**: Should see product cards
4. **Check Analytics**: Click Analytics button
5. **Expected**: Should see charts and statistics

---

## 🐛 If Still Not Working

### Check 1: Environment Variable Set Correctly

```bash
# In browser console (F12):
console.log(import.meta.env.VITE_API_URL)
# Should show: https://smart-cart-ai-recommendation.vercel.app
```

### Check 2: Backend is Working

Open: https://smart-cart-ai-recommendation.vercel.app/api/health

Should see:
```json
{
  "status": "healthy",
  "products_loaded": 20,
  "categories": 5,
  "brands": 8
}
```

### Check 3: Test API Directly

Open: https://smart-cart-ai-recommendation.vercel.app/api/recommend?query=laptop&limit=5

Should see JSON with products.

### Check 4: Browser Console Errors

1. Open site: https://smart-cart-ai-recommendation-98k7.vercel.app/
2. Press F12 (DevTools)
3. Go to Console tab
4. Search for a product
5. Look for errors (should be none)

---

## 📞 Still Having Issues?

If none of the above works:

1. **Clear browser cache**: Ctrl+Shift+Delete
2. **Try incognito mode**: Ctrl+Shift+N
3. **Wait 5 minutes**: Vercel propagation can take time
4. **Check Vercel logs**: Deployments → Click deployment → View Function Logs

---

## ✅ Success Indicators

You'll know it's working when:
- ✅ Search returns product cards
- ✅ Analytics page shows charts
- ✅ No error messages in console
- ✅ "Powered by AI" badge visible

---

## 🚀 After Fix

Once working:
1. Test all features (Search, Filters, Analytics)
2. Share the link with your team
3. Monitor for any errors
4. Plan for ML model integration (see notebooks/)

---

**Time to Fix**: ~5 minutes  
**Difficulty**: Easy  
**Cost**: Free (Vercel Free Tier)

---

**Last Updated**: October 19, 2025
