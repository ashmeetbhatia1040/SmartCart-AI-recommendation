# 📋 SmartCart AI - Training Checklist

Use this checklist to ensure successful model training.

---

## ⚙️ Pre-Training Checklist

### Environment Setup
- [ ] Python 3.8+ installed
- [ ] Virtual environment created (`venv/`)
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Jupyter installed and working
- [ ] VS Code Jupyter extension (if using VS Code)

### Data Preparation
- [ ] Dataset file exists: `../intern_data_ikarus.csv`
- [ ] Dataset has required columns: `uniq_id`, `title`, `description`, `brand`, `images`
- [ ] Dataset size verified (know how many products)
- [ ] Sample data reviewed for quality

### Optional Configuration
- [ ] GPU drivers installed (optional, for speed)
- [ ] CUDA-enabled PyTorch (if using GPU)
- [ ] Pinecone API key in `.env` (optional)
- [ ] OpenAI API key in `.env` (optional, for GenAI)

### Directory Structure
- [ ] `notebooks/` folder exists
- [ ] `notebooks/outputs/` created
- [ ] `notebooks/checkpoints/` created
- [ ] `backend/models/` exists (or will be created)

---

## 📓 Training Checklist

### Before Starting
- [ ] Reviewed `README.md` for instructions
- [ ] Checked `QUICK_REFERENCE.md` for quick tips
- [ ] Understood what models will be trained
- [ ] Estimated training time based on dataset size

### During Training (Sequential Execution)

#### Part 1-2: Setup & Data Loading ✓
- [ ] All imports successful (no errors)
- [ ] Project paths correctly set
- [ ] Dataset loaded successfully
- [ ] Row count matches expectations
- [ ] Required columns present

#### Part 3: Preprocessing ✓
- [ ] Missing values handled
- [ ] Images parsed correctly
- [ ] Prices extracted as numeric
- [ ] Combined text created
- [ ] Categories identified

#### Part 4: Text Embeddings ✓
- [ ] Sentence-BERT model loaded
- [ ] Embeddings generated (shape correct)
- [ ] No NaN or Inf values
- [ ] Files saved to `backend/models/`
- [ ] Checkpoint saved

#### Part 5: Image Features ✓
- [ ] ResNet50 model loaded
- [ ] GPU/CPU device detected
- [ ] Image features extracted
- [ ] Acceptable failure rate (<30%)
- [ ] Files saved successfully

#### Part 6: Combined Embeddings ✓
- [ ] Embeddings normalized
- [ ] ALPHA + BETA = 1.0
- [ ] Combined embeddings created
- [ ] Distribution visualizations generated
- [ ] Scalers saved

#### Part 7: Vector Database ✓
- [ ] Pinecone setup (if enabled) OR local mode
- [ ] Metadata prepared
- [ ] Index created (if using Pinecone)
- [ ] Embeddings uploaded successfully

#### Part 8: Testing ✓
- [ ] Search function works
- [ ] Test queries return results
- [ ] Results are relevant
- [ ] Scores make sense (0-1 range)

#### Part 9: Evaluation ✓
- [ ] Similarity statistics calculated
- [ ] Visualizations generated
- [ ] Metrics reasonable (Precision, Recall, etc.)
- [ ] Category match rate acceptable

#### Part 10: Model Saving ✓
- [ ] Configuration saved (`config.pkl`)
- [ ] All model files in `backend/models/`
- [ ] File sizes reasonable
- [ ] No corrupted files

#### Part 11: Summary ✓
- [ ] Training completed without errors
- [ ] All expected files created
- [ ] Summary printed correctly

#### Part 12: GenAI (Optional) ✓
- [ ] OpenAI integration tested (if enabled)
- [ ] Descriptions generated successfully
- [ ] Quality acceptable

---

## 🔍 Post-Training Verification

### File Verification
- [ ] `backend/models/text_embeddings.npy` exists
- [ ] `backend/models/image_features.npy` exists
- [ ] `backend/models/combined_embeddings.npy` exists ⭐ (MAIN)
- [ ] `backend/models/scaler_text.pkl` exists
- [ ] `backend/models/scaler_image.pkl` exists
- [ ] `backend/models/config.pkl` exists
- [ ] `backend/models/metadata.pkl` exists

### File Size Check
```python
import os

files = [
    'backend/models/text_embeddings.npy',
    'backend/models/image_features.npy',
    'backend/models/combined_embeddings.npy',
    'backend/models/scaler_text.pkl',
    'backend/models/scaler_image.pkl',
    'backend/models/config.pkl',
    'backend/models/metadata.pkl'
]

for f in files:
    if os.path.exists(f):
        size_mb = os.path.getsize(f) / 1024 / 1024
        print(f"✓ {f}: {size_mb:.2f} MB")
    else:
        print(f"✗ {f}: MISSING!")
```

### Quality Verification
- [ ] Precision@5 > 0.6 (good) or > 0.7 (excellent)
- [ ] NDCG@5 > 0.7 (good) or > 0.8 (excellent)
- [ ] Mean similarity < 0.5 (diverse embeddings)
- [ ] Category match rate > 60%
- [ ] No error messages in output

### Functional Testing

#### Test 1: Load Models
```python
import numpy as np
import pickle

# Load embeddings
embeddings = np.load('backend/models/combined_embeddings.npy')
print(f"Shape: {embeddings.shape}")  # Should be (n_products, 384)
print(f"No NaN: {not np.isnan(embeddings).any()}")  # Should be True
print(f"No Inf: {not np.isinf(embeddings).any()}")  # Should be True
```
- [ ] Embeddings load successfully
- [ ] Shape is correct
- [ ] No NaN or Inf values

#### Test 2: Search Functionality
```python
from notebook_utils import search_products

results = search_products("modern chair", top_k=5)
print(f"Results: {len(results)}")  # Should be 5
print(f"First result: {results[0]['metadata']['title']}")
```
- [ ] Search returns results
- [ ] Results count matches top_k
- [ ] Results contain metadata
- [ ] Scores are reasonable (0-1)

#### Test 3: Backend API Integration
```bash
cd ../backend
python api.py
# In another terminal:
curl http://localhost:5000/api/health
```
- [ ] Backend starts without errors
- [ ] Models load successfully
- [ ] Health check returns OK

---

## 🐛 Troubleshooting Checklist

If training failed, check:

### Import Errors
- [ ] Reinstall dependencies: `pip install -r requirements.txt --upgrade`
- [ ] Check Python version: `python --version` (need 3.8+)
- [ ] Virtual environment activated

### Memory Errors
- [ ] Reduce `TEXT_BATCH_SIZE` (try 16 instead of 32)
- [ ] Reduce `IMAGE_BATCH_SIZE` (try 8 instead of 16)
- [ ] Enable `LOW_MEMORY_MODE` in config
- [ ] Close other applications
- [ ] Restart Jupyter kernel

### Image Download Errors
- [ ] Check internet connection
- [ ] Increase `IMAGE_TIMEOUT` (try 10 instead of 5)
- [ ] Accept some failures (<30% is normal)
- [ ] Consider text-only mode (BETA=0)

### Pinecone Errors
- [ ] Verify `PINECONE_API_KEY` in `.env`
- [ ] Check Pinecone dashboard for quota
- [ ] Try `USE_PINECONE = False` for local mode
- [ ] Check internet connection

### Slow Performance
- [ ] Enable GPU: check `torch.cuda.is_available()`
- [ ] Install CUDA PyTorch: see PyTorch website
- [ ] Increase batch sizes (if RAM allows)
- [ ] Skip image extraction (fastest)

### Quality Issues
- [ ] Try better text model: `all-mpnet-base-v2`
- [ ] Adjust ALPHA/BETA weights
- [ ] Clean dataset (remove bad entries)
- [ ] Check if images are loading correctly

---

## 📊 Success Metrics

### Minimum Acceptable
- ✅ Precision@5 > 0.50
- ✅ NDCG@5 > 0.60
- ✅ No NaN/Inf in embeddings
- ✅ All files saved correctly

### Good Performance
- ✅ Precision@5 > 0.70
- ✅ NDCG@5 > 0.80
- ✅ Category match > 70%
- ✅ Test queries return relevant results

### Excellent Performance
- ✅ Precision@5 > 0.85
- ✅ NDCG@5 > 0.90
- ✅ Category match > 80%
- ✅ Search results highly relevant

---

## 🚀 Next Steps After Success

1. **Test Backend API**
   ```bash
   cd ../backend
   python api.py
   ```
   - [ ] API starts successfully
   - [ ] Models load correctly
   - [ ] Search endpoint works

2. **Test Frontend**
   ```bash
   cd ../frontend
   npm install
   npm run dev
   ```
   - [ ] Frontend connects to backend
   - [ ] Search functionality works
   - [ ] Results display correctly

3. **Deploy to Production**
   - [ ] Upload models to cloud storage
   - [ ] Configure production API keys
   - [ ] Deploy backend (Vercel/AWS/GCP)
   - [ ] Deploy frontend (Vercel/Netlify)
   - [ ] Test production deployment

4. **Monitor Performance**
   - [ ] Track search quality metrics
   - [ ] Monitor API response times
   - [ ] Collect user feedback
   - [ ] Plan model retraining schedule

---

## 📅 Retraining Schedule

Plan to retrain when:
- [ ] New products added (monthly or quarterly)
- [ ] Product data significantly updated
- [ ] Performance degrades
- [ ] Better models become available

---

## 📝 Training Log Template

Record your training runs:

```
Date: ___________
Dataset size: ___________
Text model: ___________
ALPHA/BETA: _____ / _____
Training time: ___________
GPU used: Yes / No

Metrics:
- Precision@5: _____
- Recall@5: _____
- NDCG@5: _____
- Category match: _____%

Issues encountered:
_______________________
_______________________

Notes:
_______________________
_______________________
```

---

## ✅ Final Sign-Off

I confirm that:
- [ ] All checklist items completed
- [ ] All tests passed
- [ ] Models saved correctly
- [ ] Backend API tested
- [ ] Ready for production

**Trained by**: _______________  
**Date**: _______________  
**Dataset version**: _______________  
**Model version**: _______________

---

**Ready to deploy!** 🚀
