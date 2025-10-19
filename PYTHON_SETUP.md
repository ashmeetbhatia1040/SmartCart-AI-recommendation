# 🐍 Python Setup Guide for SmartCart AI

## Python Installation Required

The backend of SmartCart AI requires **Python 3.9+** to be installed on your system.

## 📥 Installing Python on Windows

### Method 1: Official Python Installer (Recommended)

1. **Download Python**
   - Visit: https://www.python.org/downloads/
   - Download **Python 3.11** or **Python 3.12** (latest stable)
   - Click the big yellow "Download Python" button

2. **Install Python**
   - Run the downloaded installer
   - ⚠️ **IMPORTANT**: Check "Add Python to PATH" at the bottom
   - Click "Install Now"
   - Wait for installation to complete
   - Click "Close"

3. **Verify Installation**
   Open PowerShell and run:
   ```powershell
   python --version
   # Should output: Python 3.11.x or 3.12.x
   
   pip --version
   # Should output: pip 23.x.x from ...
   ```

### Method 2: Microsoft Store

1. Open Microsoft Store
2. Search for "Python 3.11" or "Python 3.12"
3. Click "Get" or "Install"
4. Wait for installation
5. Verify in PowerShell (same as above)

### Method 3: Chocolatey (Package Manager)

If you have Chocolatey installed:
```powershell
choco install python
```

## 🚀 After Python Installation

### Step 1: Verify Installation

```powershell
python --version
pip --version
```

Both commands should work without errors.

### Step 2: Install Backend Dependencies

```powershell
cd "d:\Projects\Furniture Recomendation Model\backend"
pip install -r requirements.txt
```

### Step 3: Run Backend Server

```powershell
cd "d:\Projects\Furniture Recomendation Model\backend"
python api.py
```

✅ You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Step 4: Test Backend

Open a browser and visit:
- http://localhost:8000 - API info
- http://localhost:8000/api/health - Health check
- http://localhost:8000/api/recommend - Get products

## 🔧 Troubleshooting

### "python is not recognized"

**Solution 1: Add to PATH manually**
1. Search "Environment Variables" in Windows
2. Click "Environment Variables"
3. Under "System variables", find "Path"
4. Click "Edit"
5. Click "New"
6. Add: `C:\Users\YOUR_USERNAME\AppData\Local\Programs\Python\Python311`
7. Add: `C:\Users\YOUR_USERNAME\AppData\Local\Programs\Python\Python311\Scripts`
8. Click OK on all windows
9. **Restart PowerShell**

**Solution 2: Use py launcher**
```powershell
py --version
py -m pip install -r requirements.txt
py api.py
```

### "pip is not recognized"

```powershell
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```

### Port 8000 Already in Use

```powershell
# Check what's using port 8000
netstat -ano | findstr :8000

# Kill the process (replace <PID> with actual number)
Stop-Process -Id <PID> -Force

# Or use a different port
python -m uvicorn api:app --host 0.0.0.0 --port 8001
```

### Module Not Found Errors

```powershell
# Reinstall all dependencies
cd backend
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

### Permission Errors

Run PowerShell as Administrator:
1. Right-click PowerShell
2. Select "Run as Administrator"
3. Navigate to backend folder
4. Install dependencies

## 🌐 Alternative: Docker Setup (Advanced)

If you prefer using Docker:

### Create Dockerfile in backend folder:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "api.py"]
```

### Run with Docker:

```powershell
cd backend
docker build -t smartcart-backend .
docker run -p 8000:8000 smartcart-backend
```

## 📝 Quick Commands Reference

### Backend Commands
```powershell
# Navigate to backend
cd "d:\Projects\Furniture Recomendation Model\backend"

# Install dependencies
pip install -r requirements.txt

# Run server
python api.py

# Run with auto-reload
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Commands (in new terminal)
```powershell
# Navigate to frontend
cd "d:\Projects\Furniture Recomendation Model\frontend"

# Install dependencies (already done)
npm install

# Run development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## ✅ Verification Checklist

After Python installation and setup:

- [ ] `python --version` works
- [ ] `pip --version` works
- [ ] Backend dependencies installed without errors
- [ ] Backend server starts on port 8000
- [ ] http://localhost:8000/api/health returns healthy status
- [ ] Frontend can connect to backend
- [ ] Products load in the application

## 🎯 Complete Development Setup

### Terminal 1: Backend
```powershell
cd "d:\Projects\Furniture Recomendation Model\backend"
python api.py
```

### Terminal 2: Frontend
```powershell
cd "d:\Projects\Furniture Recomendation Model\frontend"
npm run dev
```

### Browser
- Open http://localhost:3000
- Test search functionality
- Check analytics dashboard
- Verify all features work

## 📚 Additional Resources

- **Python Documentation**: https://docs.python.org/3/
- **FastAPI Documentation**: https://fastapi.tiangolo.com/
- **Uvicorn Documentation**: https://www.uvicorn.org/

## 🆘 Still Having Issues?

1. **Check Python version**: Must be 3.9 or higher
2. **Restart computer**: After PATH changes
3. **Use py launcher**: `py` instead of `python`
4. **Check firewall**: May block port 8000
5. **Antivirus**: May block Python execution

---

**Once Python is installed and working, return to QUICKSTART.md to continue! 🚀**
