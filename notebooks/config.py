"""
SmartCart AI - Training Configuration

This file contains all configurable parameters for model training.
Modify these values to customize your training pipeline.
"""

# ============================================================================
# MODEL CONFIGURATION
# ============================================================================

# Text Embedding Model
TEXT_MODEL_NAME = 'sentence-transformers/all-MiniLM-L6-v2'

# Alternative models (uncomment to use):
# TEXT_MODEL_NAME = 'sentence-transformers/all-mpnet-base-v2'  # Better quality, 768 dims
# TEXT_MODEL_NAME = 'sentence-transformers/multi-qa-mpnet-base-dot-v1'  # For Q&A
# TEXT_MODEL_NAME = 'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'  # Multilingual

# Image Feature Extractor
IMAGE_MODEL_NAME = 'resnet50'  # Options: resnet50, resnet101, vit_b_16

# ============================================================================
# HYPERPARAMETERS
# ============================================================================

# Embedding combination weights (must sum to 1.0)
ALPHA = 0.7  # Text embedding weight
BETA = 0.3   # Image feature weight

# Batch sizes
TEXT_BATCH_SIZE = 32
IMAGE_BATCH_SIZE = 16

# Random seed for reproducibility
RANDOM_SEED = 42

# ============================================================================
# DATA CONFIGURATION
# ============================================================================

# Dataset path (relative to project root)
DATA_PATH = '../intern_data_ikarus.csv'

# Required columns
REQUIRED_COLUMNS = ['uniq_id', 'title', 'description', 'brand', 'images']

# Optional columns
OPTIONAL_COLUMNS = ['price', 'main_category', 'sub_category']

# ============================================================================
# PREPROCESSING
# ============================================================================

# Text preprocessing
MAX_TEXT_LENGTH = 512  # Maximum characters for text fields
MIN_TEXT_LENGTH = 10   # Minimum characters for valid text

# Image preprocessing
IMAGE_TIMEOUT = 5      # Timeout for image downloads (seconds)
IMAGE_SIZE = (224, 224)  # Image resize dimensions

# Missing value handling
FILL_MISSING_BRAND = 'Generic'
FILL_MISSING_CATEGORY = 'Furniture'
FILL_MISSING_PRICE = 0.0

# ============================================================================
# VECTOR DATABASE (PINECONE)
# ============================================================================

# Pinecone configuration
USE_PINECONE = False  # Set to True if you have Pinecone API key
PINECONE_INDEX_NAME = 'smartcart-products'
PINECONE_CLOUD = 'aws'
PINECONE_REGION = 'us-east-1'
PINECONE_METRIC = 'cosine'  # Options: cosine, euclidean, dotproduct

# Upload batch size
PINECONE_BATCH_SIZE = 100

# ============================================================================
# GENAI CONFIGURATION
# ============================================================================

# GenAI integration
USE_GENAI = False  # Set to True if you have OpenAI API key
GENAI_MODEL = 'gpt-3.5-turbo'  # Options: gpt-3.5-turbo, gpt-4
GENAI_MAX_TOKENS = 150
GENAI_TEMPERATURE = 0.7

# ============================================================================
# EVALUATION
# ============================================================================

# Metrics to calculate
K_VALUES = [1, 3, 5, 10, 20]  # For Precision@K, Recall@K, NDCG@K

# Sample size for diversity analysis
DIVERSITY_SAMPLE_SIZE = 1000

# ============================================================================
# OUTPUT PATHS
# ============================================================================

# Model output directory
MODELS_DIR = '../backend/models'

# Notebook output directory
OUTPUTS_DIR = './outputs'

# Checkpoint directory
CHECKPOINTS_DIR = './checkpoints'

# ============================================================================
# TRAINING OPTIONS
# ============================================================================

# Save checkpoints during training
SAVE_CHECKPOINTS = True
CHECKPOINT_FREQUENCY = 1000  # Save every N products processed

# Verbose logging
VERBOSE = True

# Show progress bars
SHOW_PROGRESS = True

# ============================================================================
# ADVANCED OPTIONS
# ============================================================================

# Use mixed precision training (faster with GPU)
USE_MIXED_PRECISION = False

# Number of workers for data loading
NUM_WORKERS = 4

# Memory optimization
LOW_MEMORY_MODE = False  # Process in smaller batches if RAM is limited

# ============================================================================
# VALIDATION
# ============================================================================

# Validation split
VALIDATION_SPLIT = 0.1  # 10% of data for validation

# Test queries for evaluation
TEST_QUERIES = [
    "modern black leather dining chair",
    "comfortable office desk",
    "wooden coffee table",
    "bedroom storage cabinet",
    "ergonomic gaming chair",
    "minimalist bookshelf",
    "outdoor patio furniture",
    "kids bedroom set"
]

# ============================================================================
# LOGGING
# ============================================================================

# Log level
LOG_LEVEL = 'INFO'  # Options: DEBUG, INFO, WARNING, ERROR

# Log file path
LOG_FILE = './outputs/training.log'

# ============================================================================
# DEVICE CONFIGURATION
# ============================================================================

# Device selection (auto-detected by default)
# DEVICE = 'cuda'  # Force GPU
# DEVICE = 'cpu'   # Force CPU
DEVICE = 'auto'  # Auto-detect best device

# ============================================================================
# FEATURE FLAGS
# ============================================================================

# Enable/disable specific features
EXTRACT_TEXT_EMBEDDINGS = True
EXTRACT_IMAGE_FEATURES = True
CREATE_COMBINED_EMBEDDINGS = True
UPLOAD_TO_PINECONE = USE_PINECONE
GENERATE_VISUALIZATIONS = True
RUN_EVALUATION = True

# ============================================================================
# EXPERIMENT TRACKING
# ============================================================================

# Experiment name (for tracking different runs)
EXPERIMENT_NAME = 'default'

# Save experiment metadata
SAVE_EXPERIMENT_INFO = True

# ============================================================================
# NOTES
# ============================================================================

"""
Configuration Notes:

1. Text Model Selection:
   - all-MiniLM-L6-v2: Fast, good quality, 384 dims
   - all-mpnet-base-v2: Better quality, slower, 768 dims
   - Choose based on your speed vs. quality tradeoff

2. Hyperparameter Tuning:
   - ALPHA/BETA: Adjust based on your use case
   - Text-heavy: ALPHA=0.8, BETA=0.2
   - Visual-heavy: ALPHA=0.5, BETA=0.5
   - Balanced: ALPHA=0.7, BETA=0.3 (default)

3. Performance:
   - Use GPU for 5-10x speedup
   - Increase batch sizes with more RAM
   - Enable LOW_MEMORY_MODE if you hit OOM errors

4. Production:
   - Set USE_PINECONE=True for production deployments
   - Consider using better text models for higher quality
   - Monitor evaluation metrics to track improvements
"""
