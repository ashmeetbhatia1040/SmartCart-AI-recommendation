import React, { useState, useEffect } from 'react';
import SearchBar from '../components/SearchBar';
import ProductCard from '../components/ProductCard';
import LoadingSpinner from '../components/LoadingSpinner';
import { getRecommendations } from '../utils/api';

const HomePage = () => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchParams, setSearchParams] = useState({});
  const [total, setTotal] = useState(0);

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async (params = {}) => {
    setLoading(true);
    setError(null);
    try {
      const data = await getRecommendations(params);
      setProducts(data.products);
      setTotal(data.total);
    } catch (err) {
      setError('Failed to load products. Please try again.');
      console.error('Error fetching products:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = (params) => {
    setSearchParams(params);
    fetchProducts(params);
  };

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <div className="relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-emerald-100 via-teal-50 to-cyan-100 opacity-50"></div>
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
          <div className="text-center space-y-4 mb-8">
            <div className="inline-block">
              <h1 className="text-5xl md:text-6xl font-bold font-display">
                <span className="text-transparent bg-clip-text bg-gradient-to-r from-emerald-600 to-teal-600">
                  SmartCart AI
                </span>{' '}
                <span className="text-4xl">📱</span>
              </h1>
            </div>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Discover the perfect electronics with AI-powered recommendations
            </p>
          </div>

          {/* Search Bar */}
          <div className="max-w-5xl mx-auto">
            <SearchBar onSearch={handleSearch} loading={loading} />
          </div>
        </div>
      </div>

      {/* Products Section */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        {/* Results Header */}
        {!loading && (
          <div className="mb-8 flex items-center justify-between">
            <div>
              <h2 className="text-2xl font-bold text-gray-800">
                {searchParams.query
                  ? `Search Results for "${searchParams.query}"`
                  : 'Recommended Products'}
              </h2>
              <p className="text-gray-600 mt-1">
                Found {total} products
              </p>
            </div>
            <div className="glass px-4 py-2 rounded-lg">
              <p className="text-sm text-gray-600">
                Powered by <span className="font-semibold text-primary-600">AI</span>
              </p>
            </div>
          </div>
        )}

        {/* Loading State */}
        {loading && (
          <div className="flex justify-center py-20">
            <LoadingSpinner size="large" message="Finding the best products for you..." />
          </div>
        )}

        {/* Error State */}
        {error && (
          <div className="glass rounded-2xl p-8 text-center">
            <div className="text-6xl mb-4">😕</div>
            <h3 className="text-xl font-bold text-gray-800 mb-2">
              Oops! Something went wrong
            </h3>
            <p className="text-gray-600 mb-4">{error}</p>
            <button
              onClick={() => fetchProducts(searchParams)}
              className="bg-gradient-to-r from-emerald-500 to-teal-500 text-white px-6 py-3 rounded-lg font-semibold hover:from-emerald-600 hover:to-teal-600 transition-all shadow-lg hover:shadow-xl"
            >
              Try Again
            </button>
          </div>
        )}

        {/* Products Grid */}
        {!loading && !error && products.length > 0 && (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 fade-in">
            {products.map((product) => (
              <ProductCard key={product.id} product={product} />
            ))}
          </div>
        )}

        {/* No Results */}
        {!loading && !error && products.length === 0 && (
          <div className="glass rounded-2xl p-12 text-center">
            <div className="text-6xl mb-4">🔍</div>
            <h3 className="text-2xl font-bold text-gray-800 mb-2">
              No products found
            </h3>
            <p className="text-gray-600 mb-6">
              Try adjusting your search or filters to find what you're looking for
            </p>
            <button
              onClick={() => handleSearch({})}
              className="bg-gradient-to-r from-emerald-500 to-teal-500 text-white px-6 py-3 rounded-lg font-semibold hover:from-emerald-600 hover:to-teal-600 transition-all shadow-lg hover:shadow-xl"
            >
              Show All Products
            </button>
          </div>
        )}
      </div>

      {/* Features Section */}
      {!loading && products.length > 0 && (
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="glass rounded-2xl p-6 text-center hover-scale">
              <div className="text-4xl mb-3">🤖</div>
              <h3 className="text-lg font-bold text-gray-800 mb-2">
                AI-Powered Search
              </h3>
              <p className="text-gray-600 text-sm">
                Advanced algorithms find the perfect products for your needs
              </p>
            </div>
            <div className="glass rounded-2xl p-6 text-center hover-scale">
              <div className="text-4xl mb-3">⚡</div>
              <h3 className="text-lg font-bold text-gray-800 mb-2">
                Lightning Fast
              </h3>
              <p className="text-gray-600 text-sm">
                Get instant recommendations from our extensive catalog
              </p>
            </div>
            <div className="glass rounded-2xl p-6 text-center hover-scale">
              <div className="text-4xl mb-3">🎯</div>
              <h3 className="text-lg font-bold text-gray-800 mb-2">
                Smart Filters
              </h3>
              <p className="text-gray-600 text-sm">
                Refine your search with intelligent filtering options
              </p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default HomePage;
