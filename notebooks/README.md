# 📓 SmartCart AI - Model Training Notebooks

This directory contains Jupyter notebooks for training and evaluating the SmartCart AI recommendation models.

## 📋 Contents

- **`model_training.ipynb`** - Complete model training pipeline
- **`notebook_utils.py`** - Helper utilities for notebooks
- **`requirements.txt`** - Python dependencies
- **`outputs/`** - Training outputs and visualizations
- **`checkpoints/`** - Model checkpoints during training

---

## 🚀 Quick Start

### 1. Setup Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Keys (Optional)

Create a `.env` file in the project root:

```env
# Optional - for Pinecone vector database
PINECONE_API_KEY=your_pinecone_api_key

# Optional - for GenAI features
OPENAI_API_KEY=your_openai_api_key
```

### 3. Run the Notebook

```bash
# Start Jupyter
jupyter notebook

# Or use Jupyter Lab
jupyter lab
```

Open `model_training.ipynb` and run the cells sequentially.

---

## 📚 What Gets Trained

### 1. **Text Embeddings (NLP)**
- **Model**: Sentence-BERT (`all-MiniLM-L6-v2`)
- **Purpose**: Semantic search and text similarity
- **Output**: 384-dimensional embeddings
- **Use Case**: Finding products based on text descriptions

### 2. **Image Features (CV)**
- **Model**: ResNet50 (pre-trained on ImageNet)
- **Purpose**: Visual similarity
- **Output**: 2048-dimensional feature vectors
- **Use Case**: Finding visually similar products

### 3. **Hybrid Embeddings**
- **Combination**: Weighted average of text + image features
- **Weights**: α=0.7 (text), β=0.3 (image)
- **Purpose**: Best of both worlds - semantic + visual similarity
- **Use Case**: Primary recommendation engine

### 4. **Vector Database (Optional)**
- **Service**: Pinecone
- **Purpose**: Fast similarity search at scale
- **Fallback**: Local cosine similarity search

### 5. **GenAI Integration (Optional)**
- **Service**: OpenAI GPT
- **Purpose**: Enhanced product descriptions
- **Use Case**: Generate compelling copy for products

---

## 📊 Training Pipeline

The notebook follows this pipeline:

```
Data Loading
    ↓
Preprocessing
    ↓
Text Embedding Generation (Sentence-BERT)
    ↓
Image Feature Extraction (ResNet50)
    ↓
Normalization & Combination
    ↓
Vector Database Upload (Optional)
    ↓
Evaluation & Testing
    ↓
Model Saving
```

---

## 🔧 Configuration

### Hyperparameters

You can modify these in the notebook:

```python
# Embedding combination weights
ALPHA = 0.7  # Text weight
BETA = 0.3   # Image weight

# Batch sizes
TEXT_BATCH_SIZE = 32
IMAGE_BATCH_SIZE = 16

# Random seed
RANDOM_SEED = 42
```

### Model Selection

Change the embedding model:

```python
# Default
model_name = 'sentence-transformers/all-MiniLM-L6-v2'

# Alternatives (better quality, slower)
# model_name = 'sentence-transformers/all-mpnet-base-v2'
# model_name = 'sentence-transformers/multi-qa-mpnet-base-dot-v1'
```

---

## 📁 Output Files

After training, these files are saved to `backend/models/`:

| File | Description | Size |
|------|-------------|------|
| `text_embeddings.npy` | Text embeddings (Sentence-BERT) | ~5-50 MB |
| `image_features.npy` | Image features (ResNet50) | ~10-100 MB |
| `combined_embeddings.npy` | Hybrid embeddings | ~5-50 MB |
| `scaler_text.pkl` | Text embedding scaler | <1 MB |
| `scaler_image.pkl` | Image feature scaler | <1 MB |
| `config.pkl` | Model configuration | <1 MB |
| `processed_data.pkl` | Processed product data | ~5-50 MB |
| `metadata.pkl` | Product metadata | ~5-50 MB |

---

## 🧪 Evaluation Metrics

The notebook calculates:

### Recommendation Quality
- **Precision@K**: Accuracy of top-K recommendations
- **Recall@K**: Coverage of relevant items in top-K
- **NDCG@K**: Ranking quality (Normalized Discounted Cumulative Gain)
- **MAP**: Mean Average Precision

### Embedding Quality
- **Mean Similarity**: Average cosine similarity between products
- **Diversity**: Distribution of similarities
- **Category Match Rate**: % of recommendations in same category

### Example Output:
```
Precision@5: 0.850
Recall@5: 0.420
NDCG@5: 0.892
MAP: 0.745
Category Match Rate: 78.3%
```

---

## 🎯 Usage Examples

### Example 1: Basic Search

```python
from notebook_utils import *

# Search for products
query = "modern black leather chair"
results = search_products(query, top_k=5)

for i, result in enumerate(results, 1):
    print(f"{i}. {result['metadata']['title']}")
    print(f"   Score: {result['score']:.3f}")
```

### Example 2: Evaluate Recommendations

```python
evaluator = RecommendationEvaluator(k_values=[1, 3, 5, 10])

recommended = ['prod1', 'prod2', 'prod3', 'prod4', 'prod5']
relevant = ['prod2', 'prod5', 'prod8']

metrics = evaluator.evaluate_all(recommended, relevant)
print(metrics)
```

### Example 3: Analyze Embeddings

```python
analyzer = EmbeddingAnalyzer()

diversity = analyzer.calculate_diversity(text_embeddings)
print(f"Mean similarity: {diversity['mean_similarity']:.3f}")
print(f"Diversity (std): {diversity['std_similarity']:.3f}")
```

---

## 🐛 Troubleshooting

### Issue: Out of Memory (OOM)

**Solution**: Reduce batch sizes

```python
# In the notebook
TEXT_BATCH_SIZE = 16  # Instead of 32
IMAGE_BATCH_SIZE = 8   # Instead of 16
```

### Issue: Slow Image Processing

**Solutions**:
1. Use GPU: Install `torch` with CUDA support
2. Reduce dataset: Process a subset first
3. Skip images: Set `BETA = 0` for text-only

```python
# Text-only mode
ALPHA = 1.0
BETA = 0.0
```

### Issue: Pinecone Connection Errors

**Solutions**:
1. Check API key is set correctly
2. Set `USE_PINECONE = False` to use local search
3. Check internet connection

### Issue: Missing Dependencies

```bash
# Reinstall all dependencies
pip install -r requirements.txt --upgrade

# Or install specific package
pip install sentence-transformers
```

---

## ⚡ Performance Tips

### 1. Use GPU for Image Processing

```python
# The notebook automatically detects GPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
```

**Expected speedup**: 5-10x faster with GPU

### 2. Batch Processing

```python
# Increase batch size if you have enough memory
TEXT_BATCH_SIZE = 64  # Default: 32
IMAGE_BATCH_SIZE = 32  # Default: 16
```

### 3. Parallel Processing

For very large datasets:

```python
# Use multiprocessing for image downloads
from multiprocessing import Pool

def process_batch(urls):
    return [extract_image_features(url) for url in urls]

with Pool(processes=4) as pool:
    results = pool.map(process_batch, url_batches)
```

### 4. Caching

Save checkpoints during training:

```python
# The notebook auto-saves checkpoints to:
# notebooks/checkpoints/
# 
# Resume training by loading:
import pickle

with open('checkpoints/text_embeddings_checkpoint.pkl', 'rb') as f:
    checkpoint = pickle.load(f)
    text_embeddings = checkpoint['embeddings']
```

---

## 🔄 Retraining

### When to Retrain:

1. **New products added** - Retrain to include new items
2. **Product data updated** - When descriptions, prices, or images change
3. **Performance degradation** - If recommendation quality drops
4. **Model updates** - When new/better embedding models are available

### How to Retrain:

1. Update the dataset (`intern_data_ikarus.csv`)
2. Run the notebook from start to finish
3. Models are automatically overwritten
4. Restart the backend API to load new models

```bash
# After retraining
cd backend
python api.py
```

---

## 📈 Model Improvement Ideas

### 1. Better Text Models
```python
# Try larger models for better quality
model_name = 'sentence-transformers/all-mpnet-base-v2'  # 768 dims
model_name = 'sentence-transformers/multi-qa-mpnet-base-dot-v1'
```

### 2. Fine-tune Weights
```python
# Experiment with different α, β values
ALPHA = 0.8  # More emphasis on text
BETA = 0.2

# Or
ALPHA = 0.5  # Equal weight
BETA = 0.5
```

### 3. Add Category Embeddings
```python
# Include category as additional feature
category_embeddings = encode_categories(df['category'])
combined = α*text + β*image + γ*category
```

### 4. User Behavior Data
```python
# If you have click/purchase data
user_embeddings = train_collaborative_filtering(user_data)
combined = α*text + β*image + γ*user_behavior
```

### 5. A/B Testing
Track metrics in production:
- Click-through rate (CTR)
- Conversion rate
- User engagement time

---

## 📖 Additional Resources

### Documentation
- [Sentence-BERT](https://www.sbert.net/) - Text embedding models
- [PyTorch Torchvision](https://pytorch.org/vision/stable/models.html) - Computer vision models
- [Pinecone Docs](https://docs.pinecone.io/) - Vector database
- [scikit-learn](https://scikit-learn.org/) - ML utilities

### Tutorials
- [Sentence-BERT Tutorial](https://www.sbert.net/docs/quickstart.html)
- [Transfer Learning with PyTorch](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)
- [Building Recommender Systems](https://developers.google.com/machine-learning/recommendation)

### Papers
- [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://arxiv.org/abs/1908.10084)
- [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385) (ResNet)

---

## 🤝 Contributing

To improve the training pipeline:

1. Fork the repository
2. Make improvements to the notebook
3. Test thoroughly with different datasets
4. Submit a pull request with:
   - Clear description of changes
   - Performance comparisons
   - Updated documentation

---

## 📝 License

This project is part of SmartCart AI. See main README for license information.

---

## 💬 Support

- **Issues**: Report bugs on GitHub Issues
- **Questions**: Start a GitHub Discussion
- **Email**: [Your contact email]

---

**Happy Training! 🚀**

Last updated: 2025-10-19
