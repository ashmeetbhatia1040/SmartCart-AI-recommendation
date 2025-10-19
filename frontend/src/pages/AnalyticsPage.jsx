import React, { useState, useEffect } from 'react';
import {
  BarChart,
  Bar,
  PieChart,
  Pie,
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
  Cell,
} from 'recharts';
import LoadingSpinner from '../components/LoadingSpinner';
import { getAnalytics } from '../utils/api';

const AnalyticsPage = () => {
  const [analytics, setAnalytics] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    fetchAnalytics();
  }, []);

  const fetchAnalytics = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await getAnalytics();
      setAnalytics(data);
    } catch (err) {
      setError('Failed to load analytics data. Please try again.');
      console.error('Error fetching analytics:', err);
    } finally {
      setLoading(false);
    }
  };

  const COLORS = [
    '#10b981',
    '#14b8a6',
    '#06b6d4',
    '#0ea5e9',
    '#3b82f6',
    '#6366f1',
    '#8b5cf6',
    '#a855f7',
    '#d946ef',
    '#ec4899',
  ];

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <LoadingSpinner size="large" message="Loading analytics..." />
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen flex items-center justify-center p-4">
        <div className="glass rounded-2xl p-8 max-w-md w-full text-center">
          <div className="text-6xl mb-4">📊</div>
          <h3 className="text-xl font-bold text-gray-800 mb-2">{error}</h3>
          <button
            onClick={fetchAnalytics}
            className="mt-4 bg-gradient-to-r from-emerald-500 to-teal-500 text-white px-6 py-3 rounded-lg font-semibold hover:from-emerald-600 hover:to-teal-600 transition-all"
          >
            Retry
          </button>
        </div>
      </div>
    );
  }

  // Prepare chart data
  const priceRangeData = Object.entries(analytics.price_ranges).map(
    ([range, count]) => ({
      range,
      count,
    })
  );

  const topBrandsData = analytics.top_brands.slice(0, 8);

  const categoryPriceData = Object.entries(analytics.price_by_category)
    .slice(0, 10)
    .map(([category, price]) => ({
      category: category.length > 15 ? category.substring(0, 15) + '...' : category,
      price: parseFloat(price),
    }));

  const categoryDistData = Object.entries(analytics.category_distribution)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 8)
    .map(([category, count]) => ({
      name: category,
      value: count,
    }));

  return (
    <div
      className={`min-h-screen transition-colors duration-300 ${
        darkMode ? 'bg-gray-900' : ''
      }`}
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        {/* Header */}
        <div className="flex items-center justify-between mb-8">
          <div>
            <h1
              className={`text-4xl font-bold font-display ${
                darkMode ? 'text-white' : 'text-gray-800'
              }`}
            >
              📊 Analytics Dashboard
            </h1>
            <p
              className={`mt-2 ${
                darkMode ? 'text-gray-400' : 'text-gray-600'
              }`}
            >
              Comprehensive insights into our product catalog
            </p>
          </div>
          <button
            onClick={() => setDarkMode(!darkMode)}
            className={`glass px-4 py-2 rounded-lg font-medium transition-all ${
              darkMode
                ? 'bg-gray-800 text-white'
                : 'bg-white text-gray-800'
            }`}
          >
            {darkMode ? '☀️ Light' : '🌙 Dark'}
          </button>
        </div>

        {/* Summary Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <div
            className={`${
              darkMode ? 'glass-dark' : 'glass'
            } rounded-2xl p-6 hover-scale`}
          >
            <div className="flex items-center justify-between">
              <div>
                <p
                  className={`text-sm font-medium ${
                    darkMode ? 'text-gray-400' : 'text-gray-600'
                  }`}
                >
                  Total Products
                </p>
                <p
                  className={`text-3xl font-bold mt-2 ${
                    darkMode ? 'text-white' : 'text-gray-800'
                  }`}
                >
                  {analytics.total_products}
                </p>
              </div>
              <div className="text-4xl">📦</div>
            </div>
          </div>

          <div
            className={`${
              darkMode ? 'glass-dark' : 'glass'
            } rounded-2xl p-6 hover-scale`}
          >
            <div className="flex items-center justify-between">
              <div>
                <p
                  className={`text-sm font-medium ${
                    darkMode ? 'text-gray-400' : 'text-gray-600'
                  }`}
                >
                  Total Brands
                </p>
                <p
                  className={`text-3xl font-bold mt-2 ${
                    darkMode ? 'text-white' : 'text-gray-800'
                  }`}
                >
                  {analytics.total_brands}
                </p>
              </div>
              <div className="text-4xl">🏷️</div>
            </div>
          </div>

          <div
            className={`${
              darkMode ? 'glass-dark' : 'glass'
            } rounded-2xl p-6 hover-scale`}
          >
            <div className="flex items-center justify-between">
              <div>
                <p
                  className={`text-sm font-medium ${
                    darkMode ? 'text-gray-400' : 'text-gray-600'
                  }`}
                >
                  Categories
                </p>
                <p
                  className={`text-3xl font-bold mt-2 ${
                    darkMode ? 'text-white' : 'text-gray-800'
                  }`}
                >
                  {analytics.total_categories}
                </p>
              </div>
              <div className="text-4xl">📂</div>
            </div>
          </div>

          <div
            className={`${
              darkMode ? 'glass-dark' : 'glass'
            } rounded-2xl p-6 hover-scale`}
          >
            <div className="flex items-center justify-between">
              <div>
                <p
                  className={`text-sm font-medium ${
                    darkMode ? 'text-gray-400' : 'text-gray-600'
                  }`}
                >
                  Avg Price
                </p>
                <p
                  className={`text-3xl font-bold mt-2 ${
                    darkMode ? 'text-white' : 'text-gray-800'
                  }`}
                >
                  ${analytics.avg_price}
                </p>
              </div>
              <div className="text-4xl">💰</div>
            </div>
          </div>
        </div>

        {/* Charts Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
          {/* Price Distribution */}
          <div
            className={`${
              darkMode ? 'glass-dark' : 'glass'
            } rounded-2xl p-6`}
          >
            <h2
              className={`text-xl font-bold mb-4 ${
                darkMode ? 'text-white' : 'text-gray-800'
              }`}
            >
              Price Distribution
            </h2>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={priceRangeData}>
                <CartesianGrid
                  strokeDasharray="3 3"
                  stroke={darkMode ? '#374151' : '#e5e7eb'}
                />
                <XAxis
                  dataKey="range"
                  stroke={darkMode ? '#9ca3af' : '#6b7280'}
                  tick={{ fontSize: 12 }}
                />
                <YAxis stroke={darkMode ? '#9ca3af' : '#6b7280'} />
                <Tooltip
                  contentStyle={{
                    backgroundColor: darkMode ? '#1f2937' : '#ffffff',
                    border: 'none',
                    borderRadius: '8px',
                    boxShadow: '0 4px 6px rgba(0,0,0,0.1)',
                  }}
                />
                <Bar dataKey="count" fill="#10b981" radius={[8, 8, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>

          {/* Top Brands */}
          <div
            className={`${
              darkMode ? 'glass-dark' : 'glass'
            } rounded-2xl p-6`}
          >
            <h2
              className={`text-xl font-bold mb-4 ${
                darkMode ? 'text-white' : 'text-gray-800'
              }`}
            >
              Top Brands by Product Count
            </h2>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={topBrandsData} layout="horizontal">
                <CartesianGrid
                  strokeDasharray="3 3"
                  stroke={darkMode ? '#374151' : '#e5e7eb'}
                />
                <XAxis
                  type="number"
                  stroke={darkMode ? '#9ca3af' : '#6b7280'}
                />
                <YAxis
                  dataKey="brand"
                  type="category"
                  stroke={darkMode ? '#9ca3af' : '#6b7280'}
                  tick={{ fontSize: 12 }}
                  width={80}
                />
                <Tooltip
                  contentStyle={{
                    backgroundColor: darkMode ? '#1f2937' : '#ffffff',
                    border: 'none',
                    borderRadius: '8px',
                    boxShadow: '0 4px 6px rgba(0,0,0,0.1)',
                  }}
                />
                <Bar dataKey="count" fill="#14b8a6" radius={[0, 8, 8, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>

          {/* Category Distribution */}
          <div
            className={`${
              darkMode ? 'glass-dark' : 'glass'
            } rounded-2xl p-6`}
          >
            <h2
              className={`text-xl font-bold mb-4 ${
                darkMode ? 'text-white' : 'text-gray-800'
              }`}
            >
              Category Distribution
            </h2>
            <ResponsiveContainer width="100%" height={300}>
              <PieChart>
                <Pie
                  data={categoryDistData}
                  cx="50%"
                  cy="50%"
                  labelLine={false}
                  label={({ name, percent }) =>
                    `${name} ${(percent * 100).toFixed(0)}%`
                  }
                  outerRadius={100}
                  fill="#8884d8"
                  dataKey="value"
                >
                  {categoryDistData.map((entry, index) => (
                    <Cell
                      key={`cell-${index}`}
                      fill={COLORS[index % COLORS.length]}
                    />
                  ))}
                </Pie>
                <Tooltip
                  contentStyle={{
                    backgroundColor: darkMode ? '#1f2937' : '#ffffff',
                    border: 'none',
                    borderRadius: '8px',
                    boxShadow: '0 4px 6px rgba(0,0,0,0.1)',
                  }}
                />
              </PieChart>
            </ResponsiveContainer>
          </div>

          {/* Average Price by Category */}
          <div
            className={`${
              darkMode ? 'glass-dark' : 'glass'
            } rounded-2xl p-6`}
          >
            <h2
              className={`text-xl font-bold mb-4 ${
                darkMode ? 'text-white' : 'text-gray-800'
              }`}
            >
              Average Price by Category
            </h2>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={categoryPriceData}>
                <CartesianGrid
                  strokeDasharray="3 3"
                  stroke={darkMode ? '#374151' : '#e5e7eb'}
                />
                <XAxis
                  dataKey="category"
                  stroke={darkMode ? '#9ca3af' : '#6b7280'}
                  tick={{ fontSize: 10 }}
                  angle={-45}
                  textAnchor="end"
                  height={80}
                />
                <YAxis stroke={darkMode ? '#9ca3af' : '#6b7280'} />
                <Tooltip
                  contentStyle={{
                    backgroundColor: darkMode ? '#1f2937' : '#ffffff',
                    border: 'none',
                    borderRadius: '8px',
                    boxShadow: '0 4px 6px rgba(0,0,0,0.1)',
                  }}
                />
                <Line
                  type="monotone"
                  dataKey="price"
                  stroke="#10b981"
                  strokeWidth={3}
                  dot={{ fill: '#14b8a6', r: 5 }}
                  activeDot={{ r: 8 }}
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Insights Section */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div
            className={`${
              darkMode ? 'glass-dark' : 'glass'
            } rounded-2xl p-6`}
          >
            <div className="text-3xl mb-3">🎯</div>
            <h3
              className={`text-lg font-bold mb-2 ${
                darkMode ? 'text-white' : 'text-gray-800'
              }`}
            >
              Market Coverage
            </h3>
            <p
              className={`text-sm ${
                darkMode ? 'text-gray-400' : 'text-gray-600'
              }`}
            >
              Our catalog includes {analytics.total_products} products from{' '}
              {analytics.total_brands} leading brands
            </p>
          </div>

          <div
            className={`${
              darkMode ? 'glass-dark' : 'glass'
            } rounded-2xl p-6`}
          >
            <div className="text-3xl mb-3">💡</div>
            <h3
              className={`text-lg font-bold mb-2 ${
                darkMode ? 'text-white' : 'text-gray-800'
              }`}
            >
              Price Range
            </h3>
            <p
              className={`text-sm ${
                darkMode ? 'text-gray-400' : 'text-gray-600'
              }`}
            >
              Average product price: ${analytics.avg_price}, with options for
              every budget
            </p>
          </div>

          <div
            className={`${
              darkMode ? 'glass-dark' : 'glass'
            } rounded-2xl p-6`}
          >
            <div className="text-3xl mb-3">🚀</div>
            <h3
              className={`text-lg font-bold mb-2 ${
                darkMode ? 'text-white' : 'text-gray-800'
              }`}
            >
              AI-Powered
            </h3>
            <p
              className={`text-sm ${
                darkMode ? 'text-gray-400' : 'text-gray-600'
              }`}
            >
              Smart recommendations across {analytics.total_categories}{' '}
              categories
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AnalyticsPage;
