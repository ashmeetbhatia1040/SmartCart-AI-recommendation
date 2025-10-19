import axios from 'axios';

// API base URL - update for production
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Health check
export const checkHealth = async () => {
  try {
    const response = await api.get('/api/health');
    return response.data;
  } catch (error) {
    console.error('Health check failed:', error);
    throw error;
  }
};

// Get product recommendations
export const getRecommendations = async (params = {}) => {
  try {
    const response = await api.get('/api/recommend', { params });
    return response.data;
  } catch (error) {
    console.error('Failed to fetch recommendations:', error);
    throw error;
  }
};

// Get analytics data
export const getAnalytics = async () => {
  try {
    const response = await api.get('/api/analytics');
    return response.data;
  } catch (error) {
    console.error('Failed to fetch analytics:', error);
    throw error;
  }
};

// Get categories
export const getCategories = async () => {
  try {
    const response = await api.get('/api/categories');
    return response.data;
  } catch (error) {
    console.error('Failed to fetch categories:', error);
    throw error;
  }
};

// Get brands
export const getBrands = async () => {
  try {
    const response = await api.get('/api/brands');
    return response.data;
  } catch (error) {
    console.error('Failed to fetch brands:', error);
    throw error;
  }
};

export default api;
