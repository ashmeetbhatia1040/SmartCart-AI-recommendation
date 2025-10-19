"""
SmartCart AI - Notebook Helper Utilities

This module provides helper functions for the model training notebook.
"""

import numpy as np
from typing import List, Dict, Any, Tuple
import pandas as pd
from sklearn.metrics import precision_score, recall_score, ndcg_score


class RecommendationEvaluator:
    """Evaluate recommendation quality"""
    
    def __init__(self, k_values: List[int] = [1, 3, 5, 10]):
        """
        Initialize evaluator
        
        Args:
            k_values: List of K values for Precision@K and Recall@K
        """
        self.k_values = k_values
    
    def precision_at_k(self, recommended: List[str], relevant: List[str], k: int) -> float:
        """
        Calculate Precision@K
        
        Args:
            recommended: List of recommended item IDs
            relevant: List of relevant item IDs
            k: Number of top recommendations to consider
        
        Returns:
            Precision@K score
        """
        if k == 0 or len(recommended) == 0:
            return 0.0
        
        recommended_k = recommended[:k]
        relevant_set = set(relevant)
        
        hits = sum(1 for item in recommended_k if item in relevant_set)
        return hits / k
    
    def recall_at_k(self, recommended: List[str], relevant: List[str], k: int) -> float:
        """
        Calculate Recall@K
        
        Args:
            recommended: List of recommended item IDs
            relevant: List of relevant item IDs
            k: Number of top recommendations to consider
        
        Returns:
            Recall@K score
        """
        if len(relevant) == 0:
            return 0.0
        
        recommended_k = recommended[:k]
        relevant_set = set(relevant)
        
        hits = sum(1 for item in recommended_k if item in relevant_set)
        return hits / len(relevant)
    
    def average_precision(self, recommended: List[str], relevant: List[str]) -> float:
        """
        Calculate Average Precision
        
        Args:
            recommended: List of recommended item IDs (ordered)
            relevant: List of relevant item IDs
        
        Returns:
            Average Precision score
        """
        if len(relevant) == 0:
            return 0.0
        
        relevant_set = set(relevant)
        hits = 0
        precision_sum = 0.0
        
        for i, item in enumerate(recommended, 1):
            if item in relevant_set:
                hits += 1
                precision_sum += hits / i
        
        return precision_sum / len(relevant) if len(relevant) > 0 else 0.0
    
    def ndcg_at_k(self, recommended: List[str], relevant: List[str], k: int) -> float:
        """
        Calculate Normalized Discounted Cumulative Gain @ K
        
        Args:
            recommended: List of recommended item IDs
            relevant: List of relevant item IDs
            k: Number of top recommendations to consider
        
        Returns:
            NDCG@K score
        """
        if len(relevant) == 0:
            return 0.0
        
        recommended_k = recommended[:k]
        relevant_set = set(relevant)
        
        # DCG
        dcg = 0.0
        for i, item in enumerate(recommended_k, 1):
            if item in relevant_set:
                dcg += 1.0 / np.log2(i + 1)
        
        # IDCG (ideal DCG)
        idcg = sum(1.0 / np.log2(i + 2) for i in range(min(len(relevant), k)))
        
        return dcg / idcg if idcg > 0 else 0.0
    
    def evaluate_all(
        self, 
        recommended: List[str], 
        relevant: List[str]
    ) -> Dict[str, float]:
        """
        Calculate all metrics
        
        Args:
            recommended: List of recommended item IDs
            relevant: List of relevant item IDs
        
        Returns:
            Dictionary with all metrics
        """
        metrics = {}
        
        for k in self.k_values:
            metrics[f'precision@{k}'] = self.precision_at_k(recommended, relevant, k)
            metrics[f'recall@{k}'] = self.recall_at_k(recommended, relevant, k)
            metrics[f'ndcg@{k}'] = self.ndcg_at_k(recommended, relevant, k)
        
        metrics['map'] = self.average_precision(recommended, relevant)
        
        return metrics


class EmbeddingAnalyzer:
    """Analyze embedding quality and distribution"""
    
    @staticmethod
    def calculate_diversity(embeddings: np.ndarray, sample_size: int = 1000) -> Dict[str, float]:
        """
        Calculate diversity metrics for embeddings
        
        Args:
            embeddings: Array of embeddings (n_samples, embedding_dim)
            sample_size: Number of samples to use for analysis
        
        Returns:
            Dictionary with diversity metrics
        """
        from sklearn.metrics.pairwise import cosine_similarity
        
        # Sample if too large
        if len(embeddings) > sample_size:
            indices = np.random.choice(len(embeddings), sample_size, replace=False)
            sample = embeddings[indices]
        else:
            sample = embeddings
        
        # Calculate pairwise similarities
        similarities = cosine_similarity(sample)
        
        # Remove diagonal
        mask = ~np.eye(similarities.shape[0], dtype=bool)
        similarities_no_diag = similarities[mask]
        
        return {
            'mean_similarity': float(np.mean(similarities_no_diag)),
            'std_similarity': float(np.std(similarities_no_diag)),
            'min_similarity': float(np.min(similarities_no_diag)),
            'max_similarity': float(np.max(similarities_no_diag)),
            'median_similarity': float(np.median(similarities_no_diag)),
            'q25_similarity': float(np.percentile(similarities_no_diag, 25)),
            'q75_similarity': float(np.percentile(similarities_no_diag, 75))
        }
    
    @staticmethod
    def analyze_clusters(
        embeddings: np.ndarray, 
        labels: np.ndarray,
        label_names: List[str] = None
    ) -> Dict[str, Any]:
        """
        Analyze cluster separation for labeled embeddings
        
        Args:
            embeddings: Array of embeddings
            labels: Array of cluster labels
            label_names: Optional names for labels
        
        Returns:
            Dictionary with cluster analysis
        """
        from sklearn.metrics import silhouette_score, davies_bouldin_score
        
        unique_labels = np.unique(labels)
        
        if len(unique_labels) < 2:
            return {'error': 'Need at least 2 clusters'}
        
        # Calculate metrics
        silhouette = silhouette_score(embeddings, labels)
        davies_bouldin = davies_bouldin_score(embeddings, labels)
        
        # Calculate inter-cluster distances
        from sklearn.metrics.pairwise import euclidean_distances
        
        cluster_centers = []
        for label in unique_labels:
            cluster_embeddings = embeddings[labels == label]
            center = cluster_embeddings.mean(axis=0)
            cluster_centers.append(center)
        
        cluster_centers = np.array(cluster_centers)
        inter_cluster_dists = euclidean_distances(cluster_centers)
        
        return {
            'silhouette_score': float(silhouette),
            'davies_bouldin_score': float(davies_bouldin),
            'n_clusters': len(unique_labels),
            'mean_inter_cluster_distance': float(inter_cluster_dists.mean()),
            'min_inter_cluster_distance': float(inter_cluster_dists[inter_cluster_dists > 0].min())
        }


class DataValidator:
    """Validate data quality before training"""
    
    @staticmethod
    def validate_dataframe(df: pd.DataFrame, required_columns: List[str]) -> Dict[str, Any]:
        """
        Validate dataframe structure and quality
        
        Args:
            df: Input dataframe
            required_columns: List of required column names
        
        Returns:
            Validation report
        """
        report = {
            'is_valid': True,
            'issues': [],
            'warnings': [],
            'stats': {}
        }
        
        # Check required columns
        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            report['is_valid'] = False
            report['issues'].append(f"Missing columns: {missing_cols}")
        
        # Check for empty dataframe
        if len(df) == 0:
            report['is_valid'] = False
            report['issues'].append("DataFrame is empty")
            return report
        
        # Check for duplicates
        n_duplicates = df.duplicated().sum()
        if n_duplicates > 0:
            report['warnings'].append(f"Found {n_duplicates} duplicate rows")
        
        # Check missing values
        missing_summary = {}
        for col in df.columns:
            n_missing = df[col].isnull().sum()
            if n_missing > 0:
                pct_missing = (n_missing / len(df)) * 100
                missing_summary[col] = {
                    'count': int(n_missing),
                    'percentage': round(pct_missing, 2)
                }
                
                if pct_missing > 50:
                    report['warnings'].append(
                        f"Column '{col}' has {pct_missing:.1f}% missing values"
                    )
        
        report['stats']['missing_values'] = missing_summary
        report['stats']['total_rows'] = len(df)
        report['stats']['total_columns'] = len(df.columns)
        
        return report
    
    @staticmethod
    def validate_embeddings(embeddings: np.ndarray) -> Dict[str, Any]:
        """
        Validate embedding quality
        
        Args:
            embeddings: Array of embeddings
        
        Returns:
            Validation report
        """
        report = {
            'is_valid': True,
            'issues': [],
            'warnings': []
        }
        
        # Check for NaN or Inf
        if np.isnan(embeddings).any():
            report['is_valid'] = False
            report['issues'].append("Embeddings contain NaN values")
        
        if np.isinf(embeddings).any():
            report['is_valid'] = False
            report['issues'].append("Embeddings contain Inf values")
        
        # Check for zero vectors
        zero_vectors = np.all(embeddings == 0, axis=1).sum()
        if zero_vectors > 0:
            pct_zero = (zero_vectors / len(embeddings)) * 100
            report['warnings'].append(
                f"{zero_vectors} ({pct_zero:.1f}%) zero vectors found"
            )
        
        # Check variance
        variance = embeddings.var(axis=0)
        low_variance_dims = (variance < 1e-6).sum()
        if low_variance_dims > 0:
            pct_low_var = (low_variance_dims / embeddings.shape[1]) * 100
            report['warnings'].append(
                f"{low_variance_dims} ({pct_low_var:.1f}%) dimensions have very low variance"
            )
        
        return report


def print_training_summary(
    model_config: Dict[str, Any],
    embeddings_info: Dict[str, Tuple[str, np.ndarray]],
    evaluation_metrics: Dict[str, Any] = None
) -> None:
    """
    Print a comprehensive training summary
    
    Args:
        model_config: Model configuration dictionary
        embeddings_info: Dictionary mapping embedding names to (path, array) tuples
        evaluation_metrics: Optional evaluation metrics
    """
    print("\n" + "=" * 80)
    print(" " * 25 + "TRAINING SUMMARY")
    print("=" * 80)
    
    print("\n📊 Model Configuration:")
    print("-" * 80)
    for key, value in model_config.items():
        print(f"  {key}: {value}")
    
    print("\n📦 Embeddings:")
    print("-" * 80)
    for name, (path, array) in embeddings_info.items():
        size_mb = array.nbytes / 1024 / 1024
        print(f"  {name}:")
        print(f"    - Shape: {array.shape}")
        print(f"    - Size: {size_mb:.2f} MB")
        print(f"    - Path: {path}")
    
    if evaluation_metrics:
        print("\n📈 Evaluation Metrics:")
        print("-" * 80)
        for metric, value in evaluation_metrics.items():
            if isinstance(value, float):
                print(f"  {metric}: {value:.4f}")
            else:
                print(f"  {metric}: {value}")
    
    print("\n" + "=" * 80 + "\n")
