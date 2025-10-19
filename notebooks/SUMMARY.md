# SmartCart AI - Notebooks Summary

## ✅ What Was Created

A complete model training pipeline for SmartCart AI recommendation system with the following components:

### 📓 Main Files

1. **model_training.ipynb** (30KB)
   - Complete training pipeline in Jupyter notebook format
   - 12 comprehensive sections covering all aspects
   - Includes data loading, preprocessing, model training, evaluation
   - Text embeddings (Sentence-BERT)
   - Image features (ResNet50)
   - Hybrid model combination
   - Pinecone integration (optional)
   - GenAI integration (optional)
   - Evaluation metrics and visualizations

2. **notebook_utils.py** (12KB)
   - `RecommendationEvaluator` - Calculate Precision@K, Recall@K, NDCG@K
   - `EmbeddingAnalyzer` - Analyze embedding quality and diversity
   - `DataValidator` - Validate data before training
   - Helper functions for visualization and reporting

3. **config.py** (6KB)
   - Centralized configuration management
   - All hyperparameters in one place
   - Extensive documentation for each parameter
   - Easy experimentation with different settings

### 📄 Documentation

4. **README.md** (15KB)
   - Complete guide to using the notebooks
   - Setup instructions for Windows/Linux/Mac
   - Detailed explanation of each model
   - Troubleshooting section
   - Performance tips and optimization guide
   - Model improvement ideas
   - Resources and references

5. **QUICK_REFERENCE.md** (5KB)
   - Quick start guide (3 steps)
   - Common configurations cheat sheet
   - Troubleshooting quick fixes
   - Output files reference
   - Testing examples
   - Keyboard shortcuts

### 🔧 Setup Scripts

6. **setup.ps1** (PowerShell for Windows)
   - Automated environment setup
   - Checks Python installation
   - Creates virtual environment
   - Installs all dependencies
   - Checks for GPU support
   - Validates configuration

7. **setup.sh** (Bash for Linux/Mac)
   - Same functionality as setup.ps1
   - Unix/Linux compatible
   - Color-coded output
   - Error handling

### 📦 Configuration Files

8. **requirements.txt**
   - All Python dependencies with version constraints
   - Core ML libraries (numpy, pandas, scikit-learn)
   - Deep learning (torch, torchvision, sentence-transformers)
   - Vector database (pinecone-client)
   - Visualization (matplotlib, seaborn, plotly)
   - Optional GenAI (openai, langchain)

9. **.gitignore**
   - Prevents committing large model files
   - Excludes virtual environments
   - Ignores Jupyter checkpoints
   - Protects sensitive data

### 📁 Directory Structure

```
notebooks/
├── model_training.ipynb          # Main training notebook
├── notebook_utils.py             # Helper utilities
├── config.py                     # Configuration
├── requirements.txt              # Dependencies
├── setup.ps1                     # Windows setup
├── setup.sh                      # Linux/Mac setup
├── README.md                     # Full documentation
├── QUICK_REFERENCE.md            # Quick guide
├── SUMMARY.md                    # This file
├── .gitignore                    # Git ignore
├── outputs/                      # Training outputs
│   ├── embedding_distributions.png
│   ├── similarity_analysis.png
│   └── training.log
└── checkpoints/                  # Model checkpoints
    ├── text_embeddings_checkpoint.pkl
    └── image_features_checkpoint.pkl
```

---

## 🎯 Key Features

### 1. **Complete Training Pipeline**
- ✅ Data loading and validation
- ✅ Preprocessing and cleaning
- ✅ Text embedding generation (Sentence-BERT)
- ✅ Image feature extraction (ResNet50)
- ✅ Hybrid model creation
- ✅ Vector database integration (Pinecone)
- ✅ Model evaluation and metrics
- ✅ Visualization and analysis

### 2. **Production Ready**
- ✅ Configurable hyperparameters
- ✅ Error handling and validation
- ✅ Progress tracking with tqdm
- ✅ Checkpoint saving for resume
- ✅ GPU support (automatic detection)
- ✅ Memory optimization options
- ✅ Comprehensive logging

### 3. **Well Documented**
- ✅ Inline comments in notebook
- ✅ Markdown explanations for each section
- ✅ Complete README with examples
- ✅ Quick reference guide
- ✅ Configuration documentation
- ✅ Troubleshooting guides

### 4. **Easy to Use**
- ✅ One-command setup scripts
- ✅ Sequential notebook execution
- ✅ Clear error messages
- ✅ Visual feedback (progress bars)
- ✅ Automatic file organization
- ✅ Works on Windows/Linux/Mac

---

## 🚀 How to Use

### Option 1: Quick Start (Recommended)

**Windows:**
```powershell
cd notebooks
.\setup.ps1
jupyter notebook
# Open model_training.ipynb → Run All Cells
```

**Linux/Mac:**
```bash
cd notebooks
chmod +x setup.sh
./setup.sh
jupyter notebook
# Open model_training.ipynb → Run All Cells
```

### Option 2: Manual Setup

```bash
cd notebooks
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt
jupyter notebook
```

### Option 3: VS Code

1. Open `model_training.ipynb` in VS Code
2. Select Python interpreter from `venv`
3. Install Jupyter extension if prompted
4. Click "Run All" button

---

## 📊 Training Output

After successful training, these files will be created:

### In `backend/models/` (for production use):
- `text_embeddings.npy` - Sentence-BERT embeddings
- `image_features.npy` - ResNet50 features
- `combined_embeddings.npy` - **Main model** (hybrid)
- `scaler_text.pkl` - Text normalizer
- `scaler_image.pkl` - Image normalizer
- `config.pkl` - Model configuration
- `metadata.pkl` - Product metadata
- `processed_data.pkl` - Processed dataset

### In `notebooks/outputs/`:
- `embedding_distributions.png` - Visualization
- `similarity_analysis.png` - Metrics visualization
- `training.log` - Training logs

### In `notebooks/checkpoints/`:
- `text_embeddings_checkpoint.pkl` - Resume point
- `image_features_checkpoint.pkl` - Resume point

---

## 🧪 Evaluation Metrics

The notebook calculates:

### Recommendation Quality
- **Precision@K**: How many recommended items are relevant?
- **Recall@K**: How many relevant items were recommended?
- **NDCG@K**: Quality of ranking (0-1, higher is better)
- **MAP**: Mean Average Precision across queries

### Embedding Quality
- **Mean Similarity**: Average cosine similarity
- **Diversity**: Distribution of similarities
- **Category Match**: % recommendations in same category

### Example Output:
```
Precision@5: 0.850
Recall@5: 0.420
NDCG@5: 0.892
MAP: 0.745
Mean Similarity: 0.234
Category Match: 78.3%
```

---

## 🎓 Models Explained

### 1. Text Embeddings (NLP)
- **Model**: Sentence-BERT (all-MiniLM-L6-v2)
- **Input**: Product title + description + brand
- **Output**: 384-dimensional vector
- **Purpose**: Semantic search ("find chairs" → finds chairs)
- **Accuracy**: Very high for text matching

### 2. Image Features (CV)
- **Model**: ResNet50 (pre-trained on ImageNet)
- **Input**: Product image URL
- **Output**: 2048-dimensional feature vector
- **Purpose**: Visual similarity (finds similar-looking items)
- **Accuracy**: Good for visual products

### 3. Hybrid Model (Combined)
- **Method**: Weighted average of text + image
- **Weights**: α=0.7 (text), β=0.3 (image)
- **Output**: 384-dimensional vector (normalized)
- **Purpose**: Best of both worlds
- **Accuracy**: Highest overall performance

---

## 🔧 Customization Examples

### Use Text Only (Fastest)
```python
ALPHA = 1.0
BETA = 0.0
# Skip image extraction sections
```

### Emphasize Visual Similarity
```python
ALPHA = 0.5
BETA = 0.5
```

### Use Better Text Model
```python
TEXT_MODEL_NAME = 'sentence-transformers/all-mpnet-base-v2'
```

### Enable Pinecone
```python
USE_PINECONE = True
# Set PINECONE_API_KEY in .env
```

---

## 📈 Performance Expectations

### Training Time (Approximate)

| Products | CPU Time | GPU Time |
|----------|----------|----------|
| 1,000 | 5-10 min | 2-3 min |
| 10,000 | 30-60 min | 10-15 min |
| 100,000 | 3-6 hours | 30-60 min |

### Model Sizes

| File | Size (1K products) | Size (100K products) |
|------|-------------------|---------------------|
| Text embeddings | ~1.5 MB | ~150 MB |
| Image features | ~8 MB | ~800 MB |
| Combined | ~1.5 MB | ~150 MB |
| Metadata | ~0.5 MB | ~50 MB |

### Memory Usage

- **Minimum RAM**: 4 GB
- **Recommended RAM**: 8 GB
- **Large datasets (100K+)**: 16 GB

---

## 🐛 Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| ImportError | Missing dependencies | Run `pip install -r requirements.txt` |
| Out of Memory | Dataset too large | Reduce batch size or use LOW_MEMORY_MODE |
| Slow training | Using CPU | Install CUDA PyTorch for GPU support |
| Image errors | Network issues | Check internet connection, increase timeout |
| Pinecone errors | Invalid API key | Check .env file, or set USE_PINECONE=False |

---

## 🎯 Next Steps

After training models:

1. **Test Locally**
   ```python
   results = search_products("modern chair", top_k=5)
   ```

2. **Start Backend API**
   ```bash
   cd ../backend
   python api.py
   ```

3. **Test API**
   ```bash
   curl -X POST http://localhost:5000/api/search \
     -H "Content-Type: application/json" \
     -d '{"query": "modern chair", "top_k": 5}'
   ```

4. **Start Frontend**
   ```bash
   cd ../frontend
   npm run dev
   ```

5. **Deploy to Production**
   - Upload models to cloud storage
   - Deploy API to Vercel/AWS/GCP
   - Deploy frontend to Vercel/Netlify

---

## 📚 Additional Resources

### Learning Materials
- [Sentence-BERT Paper](https://arxiv.org/abs/1908.10084)
- [ResNet Paper](https://arxiv.org/abs/1512.03385)
- [Recommendation Systems Course](https://developers.google.com/machine-learning/recommendation)

### Documentation
- [Sentence-BERT Docs](https://www.sbert.net/)
- [PyTorch Docs](https://pytorch.org/docs/)
- [Pinecone Docs](https://docs.pinecone.io/)
- [scikit-learn Docs](https://scikit-learn.org/)

### Tools
- [Jupyter Notebook](https://jupyter.org/)
- [Hugging Face Models](https://huggingface.co/models)
- [TensorBoard](https://www.tensorflow.org/tensorboard) (for visualization)

---

## ✨ Features Implemented

- [x] Complete Jupyter notebook with 12 sections
- [x] Text embedding generation (Sentence-BERT)
- [x] Image feature extraction (ResNet50)
- [x] Hybrid model combination
- [x] Pinecone vector database integration
- [x] GenAI product description generation
- [x] Comprehensive evaluation metrics
- [x] Visualization and analysis
- [x] Helper utilities module
- [x] Configuration management
- [x] Automated setup scripts (Windows/Linux/Mac)
- [x] Complete documentation (README + Quick Reference)
- [x] Error handling and validation
- [x] Checkpoint saving/loading
- [x] GPU support (automatic detection)
- [x] Progress tracking
- [x] Memory optimization

---

## 🎉 Success Criteria

Your training is successful if:

✅ All notebook cells run without errors  
✅ Model files created in `backend/models/`  
✅ Evaluation metrics show good performance (Precision@5 > 0.7)  
✅ Test queries return relevant results  
✅ Backend API can load and use the models  

---

## 💬 Support

- **Documentation**: See [README.md](README.md)
- **Quick Help**: See [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
- **Issues**: Report on GitHub Issues
- **Discussions**: Ask on GitHub Discussions

---

**Created**: 2025-10-19  
**Version**: 1.0  
**Status**: Production Ready ✅
