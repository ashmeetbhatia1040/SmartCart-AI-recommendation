import React from 'react';

const LoadingSpinner = ({ size = 'medium', message = 'Loading...' }) => {
  const sizeClasses = {
    small: 'w-8 h-8',
    medium: 'w-12 h-12',
    large: 'w-16 h-16',
  };

  return (
    <div className="flex flex-col items-center justify-center p-8 space-y-4">
      <div className="relative">
        <div
          className={`${sizeClasses[size]} border-4 border-gray-200 border-t-emerald-500 rounded-full spinner`}
        ></div>
        <div
          className={`${sizeClasses[size]} border-4 border-transparent border-t-primary-400 rounded-full spinner absolute top-0 left-0`}
          style={{ animationDuration: '1.5s' }}
        ></div>
      </div>
      {message && (
        <p className="text-gray-600 text-sm font-medium animate-pulse">{message}</p>
      )}
    </div>
  );
};

export default LoadingSpinner;
