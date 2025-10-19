import React, { useState, useEffect } from 'react';

const SearchBar = ({ onSearch, loading }) => {
  const [query, setQuery] = useState('');
  const [filters, setFilters] = useState({
    category: '',
    brand: '',
    minPrice: '',
    maxPrice: '',
    minRating: '',
  });

  const handleSearch = () => {
    onSearch({
      query: query.trim(),
      ...Object.fromEntries(
        Object.entries(filters).filter(([_, value]) => value !== '')
      ),
    });
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSearch();
    }
  };

  const handleReset = () => {
    setQuery('');
    setFilters({
      category: '',
      brand: '',
      minPrice: '',
      maxPrice: '',
      minRating: '',
    });
    onSearch({});
  };

  return (
    <div className="w-full space-y-4">
      {/* Main Search Bar */}
      <div className="relative">
        <div className="glass rounded-2xl shadow-lg hover:shadow-xl transition-all p-2">
          <div className="flex items-center gap-3">
            <div className="pl-3">
              <svg
                className="w-6 h-6 text-primary-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                />
              </svg>
            </div>
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Search for smartphones, laptops, headphones..."
              className="flex-1 bg-transparent border-none outline-none text-gray-800 placeholder-gray-500 text-lg py-3"
              disabled={loading}
            />
            <button
              onClick={handleSearch}
              disabled={loading}
              className="bg-gradient-to-r from-emerald-500 to-teal-500 text-white px-8 py-3 rounded-xl font-semibold hover:from-emerald-600 hover:to-teal-600 disabled:opacity-50 disabled:cursor-not-allowed transition-all shadow-md hover:shadow-lg"
            >
              {loading ? 'Searching...' : 'Search'}
            </button>
          </div>
        </div>
      </div>

      {/* Filters */}
      <div className="glass rounded-2xl shadow-md p-4">
        <div className="flex items-center justify-between mb-3">
          <h3 className="text-sm font-semibold text-gray-700 flex items-center gap-2">
            <svg
              className="w-5 h-5 text-primary-600"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"
              />
            </svg>
            Filters
          </h3>
          <button
            onClick={handleReset}
            className="text-sm text-primary-600 hover:text-primary-700 font-medium transition-colors"
          >
            Reset All
          </button>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-3">
          <div className="space-y-1">
            <label className="text-xs font-medium text-gray-600">Category</label>
            <select
              value={filters.category}
              onChange={(e) =>
                setFilters({ ...filters, category: e.target.value })
              }
              className="w-full px-3 py-2 bg-white border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-primary-500 transition-all"
            >
              <option value="">All Categories</option>
              <option value="Smartphones">Smartphones</option>
              <option value="Laptops">Laptops</option>
              <option value="Headphones">Headphones</option>
              <option value="Cameras">Cameras</option>
              <option value="Gaming">Gaming</option>
              <option value="Tablets">Tablets</option>
              <option value="Wearables">Wearables</option>
            </select>
          </div>

          <div className="space-y-1">
            <label className="text-xs font-medium text-gray-600">Brand</label>
            <select
              value={filters.brand}
              onChange={(e) => setFilters({ ...filters, brand: e.target.value })}
              className="w-full px-3 py-2 bg-white border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-primary-500 transition-all"
            >
              <option value="">All Brands</option>
              <option value="Apple">Apple</option>
              <option value="Samsung">Samsung</option>
              <option value="Sony">Sony</option>
              <option value="Google">Google</option>
              <option value="Dell">Dell</option>
              <option value="Lenovo">Lenovo</option>
              <option value="ASUS">ASUS</option>
              <option value="Microsoft">Microsoft</option>
            </select>
          </div>

          <div className="space-y-1">
            <label className="text-xs font-medium text-gray-600">Min Price</label>
            <input
              type="number"
              value={filters.minPrice}
              onChange={(e) =>
                setFilters({ ...filters, minPrice: e.target.value })
              }
              placeholder="$0"
              className="w-full px-3 py-2 bg-white border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-primary-500 transition-all"
            />
          </div>

          <div className="space-y-1">
            <label className="text-xs font-medium text-gray-600">Max Price</label>
            <input
              type="number"
              value={filters.maxPrice}
              onChange={(e) =>
                setFilters({ ...filters, maxPrice: e.target.value })
              }
              placeholder="$10000"
              className="w-full px-3 py-2 bg-white border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-primary-500 transition-all"
            />
          </div>

          <div className="space-y-1">
            <label className="text-xs font-medium text-gray-600">Min Rating</label>
            <select
              value={filters.minRating}
              onChange={(e) =>
                setFilters({ ...filters, minRating: e.target.value })
              }
              className="w-full px-3 py-2 bg-white border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-primary-500 transition-all"
            >
              <option value="">Any Rating</option>
              <option value="4.5">4.5+ ⭐</option>
              <option value="4.0">4.0+ ⭐</option>
              <option value="3.5">3.5+ ⭐</option>
            </select>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SearchBar;
