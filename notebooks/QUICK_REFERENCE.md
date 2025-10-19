# SmartCart AI - Notebooks Quick Reference

## 📁 Directory Structure

```
notebooks/
├── model_training.ipynb      # Main training notebook
├── notebook_utils.py         # Helper utilities
├── config.py                 # Configuration parameters
├── requirements.txt          # Python dependencies
├── setup.ps1                 # Windows setup script
├── setup.sh                  # Linux/Mac setup script
├── README.md                 # Full documentation
├── QUICK_REFERENCE.md        # This file
├── .gitignore               # Git ignore rules
├── outputs/                 # Training outputs
└── checkpoints/             # Model checkpoints
```

---

## 🚀 Quick Start (3 Steps)

### Windows:
```powershell
.\setup.ps1
jupyter notebook
# Open model_training.ipynb and run all cells
```

### Linux/Mac:
```bash
chmod +x setup.sh
./setup.sh
jupyter notebook
# Open model_training.ipynb and run all cells
```

---

## 📊 What Gets Trained

| Model | Input | Output | Size | Purpose |
|-------|-------|--------|------|---------|
| **Sentence-BERT** | Product text | 384-dim vectors | ~10 MB | Semantic search |
| **ResNet50** | Product images | 2048-dim vectors | ~50 MB | Visual similarity |
| **Hybrid** | Text + Image | 384-dim vectors | ~10 MB | Combined recommendations |

---

## ⚙️ Common Configurations

### High Quality (Slower)
```python
TEXT_MODEL_NAME = 'all-mpnet-base-v2'
ALPHA = 0.6
BETA = 0.4
TEXT_BATCH_SIZE = 16
```

### Balanced (Default)
```python
TEXT_MODEL_NAME = 'all-MiniLM-L6-v2'
ALPHA = 0.7
BETA = 0.3
TEXT_BATCH_SIZE = 32
```

### Fast (Lower Quality)
```python
TEXT_MODEL_NAME = 'all-MiniLM-L6-v2'
ALPHA = 1.0  # Text only, skip images
BETA = 0.0
TEXT_BATCH_SIZE = 64
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Out of Memory | Reduce `TEXT_BATCH_SIZE` and `IMAGE_BATCH_SIZE` |
| Slow Training | Use GPU, increase batch size, or skip images |
| Import Errors | Run `pip install -r requirements.txt --upgrade` |
| Pinecone Errors | Set `USE_PINECONE = False` in notebook |
| Missing Dataset | Ensure `intern_data_ikarus.csv` is in parent directory |

---

## 📈 Expected Results

### Performance Metrics (Typical)
- **Precision@5**: 0.75 - 0.90
- **Recall@5**: 0.35 - 0.55
- **NDCG@5**: 0.80 - 0.95
- **Category Match Rate**: 70% - 85%

### Training Time (Approximate)
- **1,000 products**: ~5-10 minutes
- **10,000 products**: ~30-60 minutes
- **100,000 products**: ~3-6 hours

*Times assume GPU available. CPU is 5-10x slower.*

---

## 🔧 Customization Cheat Sheet

### Change Text Model
```python
# In notebook, modify:
model_name = 'sentence-transformers/YOUR_MODEL_NAME'
```

### Adjust Embedding Weights
```python
# More text-focused
ALPHA = 0.8
BETA = 0.2

# More image-focused
ALPHA = 0.5
BETA = 0.5

# Text only (fastest)
ALPHA = 1.0
BETA = 0.0
```

### Enable Pinecone
```python
# In notebook:
USE_PINECONE = True

# In .env file:
PINECONE_API_KEY=your_key_here
```

### Enable GenAI
```python
# In notebook:
USE_GENAI = True

# In .env file:
OPENAI_API_KEY=your_key_here
```

---

## 📊 Output Files Reference

### Essential Files (Required for API)
```
backend/models/
├── text_embeddings.npy       # Text vectors
├── combined_embeddings.npy   # Hybrid vectors (MAIN)
├── scaler_text.pkl          # Text normalizer
├── scaler_image.pkl         # Image normalizer
├── config.pkl               # Model config
└── metadata.pkl             # Product data
```

### Optional Files
```
backend/models/
├── image_features.npy       # Raw image vectors
└── processed_data.pkl       # Full processed dataset
```

### Checkpoints (For Resume)
```
notebooks/checkpoints/
├── text_embeddings_checkpoint.pkl
└── image_features_checkpoint.pkl
```

---

## 🧪 Testing Your Models

### Test Search (Python)
```python
from notebook_utils import search_products

# Search
results = search_products("modern chair", top_k=5)

# Print results
for i, r in enumerate(results, 1):
    print(f"{i}. {r['metadata']['title']} (Score: {r['score']:.3f})")
```

### Test Search (cURL)
```bash
curl -X POST http://localhost:5000/api/search \
  -H "Content-Type: application/json" \
  -d '{"query": "modern chair", "top_k": 5}'
```

---

## 📚 Common Tasks

### Update Models After New Data
```bash
1. Update intern_data_ikarus.csv with new products
2. Run model_training.ipynb (all cells)
3. Restart backend: cd backend && python api.py
```

### Experiment with Different Settings
```bash
1. Modify ALPHA/BETA in notebook
2. Run Part 6 onwards (skip embedding generation)
3. Compare evaluation metrics
4. Keep best configuration
```

### Export for Production
```bash
1. Complete training successfully
2. Check backend/models/ has all .npy and .pkl files
3. Set USE_PINECONE=True (optional)
4. Upload combined_embeddings.npy to Pinecone
5. Deploy backend API
```

---

## 💡 Tips & Best Practices

1. **Always run cells sequentially** - Don't skip cells or run out of order
2. **Save checkpoints** - Large datasets can fail midway
3. **Monitor memory** - Close other applications during training
4. **Test incrementally** - Start with small dataset subset
5. **Version your models** - Keep track of different configurations
6. **Document experiments** - Note ALPHA/BETA values and results

---

## 🔗 Useful Links

- **Sentence-BERT Models**: https://www.sbert.net/docs/pretrained_models.html
- **PyTorch Models**: https://pytorch.org/vision/stable/models.html
- **Pinecone Docs**: https://docs.pinecone.io/
- **Full README**: [README.md](README.md)

---

## ⌨️ Keyboard Shortcuts (Jupyter)

- **Run cell**: `Shift + Enter`
- **Run all cells**: `Kernel → Restart & Run All`
- **Add cell below**: `B`
- **Add cell above**: `A`
- **Delete cell**: `D, D` (press D twice)
- **Command mode**: `Esc`
- **Edit mode**: `Enter`

---

## 📞 Getting Help

1. Check the [full README](README.md)
2. Review error messages in notebook output
3. Check [GitHub Issues](https://github.com/YOUR_REPO/issues)
4. Ask on GitHub Discussions

---

**Last Updated**: 2025-10-19
