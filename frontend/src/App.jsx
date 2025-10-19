import { BrowserRouter as Router, Routes, Route, Link, useLocation } from 'react-router-dom';
import ErrorBoundary from './components/ErrorBoundary';
import HomePage from './pages/HomePage';
import AnalyticsPage from './pages/AnalyticsPage';

function Navigation() {
  const location = useLocation();

  const isActive = (path) => {
    return location.pathname === path;
  };

  return (
    <nav className="glass sticky top-0 z-50 shadow-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link to="/" className="flex items-center space-x-2 hover:opacity-80 transition-opacity">
            <span className="text-3xl">📱</span>
            <span className="text-2xl font-bold font-display text-transparent bg-clip-text bg-gradient-to-r from-emerald-600 to-teal-600">
              SmartCart AI
            </span>
          </Link>

          {/* Navigation Pills */}
          <div className="flex items-center space-x-2">
            <Link
              to="/"
              className={`px-6 py-2 rounded-full font-semibold transition-all ${
                isActive('/')
                  ? 'bg-gradient-to-r from-emerald-500 to-teal-500 text-white shadow-lg'
                  : 'text-gray-600 hover:bg-gray-100'
              }`}
            >
              🏠 Home
            </Link>
            <Link
              to="/analytics"
              className={`px-6 py-2 rounded-full font-semibold transition-all ${
                isActive('/analytics')
                  ? 'bg-gradient-to-r from-emerald-500 to-teal-500 text-white shadow-lg'
                  : 'text-gray-600 hover:bg-gray-100'
              }`}
            >
              📊 Analytics
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
}

function Footer() {
  return (
    <footer className="glass mt-20 border-t border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div>
            <h3 className="text-lg font-bold text-transparent bg-clip-text bg-gradient-to-r from-emerald-600 to-teal-600 mb-2">
              SmartCart AI
            </h3>
            <p className="text-gray-600 text-sm">
              AI-powered product recommendations for the best electronics shopping experience.
            </p>
          </div>
          <div>
            <h4 className="font-semibold text-gray-800 mb-2">Features</h4>
            <ul className="space-y-1 text-sm text-gray-600">
              <li>🤖 AI Recommendations</li>
              <li>📊 Analytics Dashboard</li>
              <li>🔍 Smart Search</li>
              <li>⚡ Fast Performance</li>
            </ul>
          </div>
          <div>
            <h4 className="font-semibold text-gray-800 mb-2">Technologies</h4>
            <ul className="space-y-1 text-sm text-gray-600">
              <li>⚛️ React + Vite</li>
              <li>🎨 Tailwind CSS</li>
              <li>🐍 FastAPI Backend</li>
              <li>📈 Recharts</li>
            </ul>
          </div>
        </div>
        <div className="mt-8 pt-8 border-t border-gray-200 text-center text-sm text-gray-600">
          <p>© 2025 SmartCart AI. Built with ❤️ for the 2-day development challenge.</p>
        </div>
      </div>
    </footer>
  );
}

function App() {
  return (
    <ErrorBoundary>
      <Router>
        <div className="min-h-screen flex flex-col">
          <Navigation />
          <main className="flex-1">
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/analytics" element={<AnalyticsPage />} />
            </Routes>
          </main>
          <Footer />
        </div>
      </Router>
    </ErrorBoundary>
  );
}

export default App;
