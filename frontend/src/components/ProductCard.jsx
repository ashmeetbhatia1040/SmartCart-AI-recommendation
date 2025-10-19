import React from 'react';

const ProductCard = ({ product }) => {
  const { title, brand, price, categories, description, image_url, rating, features } =
    product;

  const getRatingStars = (rating) => {
    const fullStars = Math.floor(rating);
    const hasHalfStar = rating % 1 >= 0.5;
    const stars = [];

    for (let i = 0; i < fullStars; i++) {
      stars.push('⭐');
    }
    if (hasHalfStar) {
      stars.push('✨');
    }

    return stars.join('');
  };

  return (
    <div className="glass rounded-2xl overflow-hidden hover-scale shadow-lg">
      {/* Product Image */}
      <div className="relative h-64 bg-gradient-to-br from-gray-100 to-gray-200 overflow-hidden">
        <img
          src={image_url}
          alt={title}
          className="w-full h-full object-cover transition-transform duration-300 hover:scale-110"
          onError={(e) => {
            e.target.src = 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400';
          }}
        />
        {/* Rating Badge */}
        <div className="absolute top-3 right-3 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-full shadow-md">
          <span className="text-sm font-semibold text-gray-800">
            {rating} {getRatingStars(rating)}
          </span>
        </div>
        {/* Brand Badge */}
        <div className="absolute top-3 left-3 bg-gradient-to-r from-emerald-500 to-teal-500 text-white px-3 py-1 rounded-full shadow-md">
          <span className="text-xs font-semibold">{brand}</span>
        </div>
      </div>

      {/* Product Info */}
      <div className="p-5 space-y-3">
        {/* Title */}
        <h3 className="text-lg font-bold text-gray-800 line-clamp-2 hover:text-primary-600 transition-colors">
          {title}
        </h3>

        {/* Categories */}
        <div className="flex flex-wrap gap-2">
          {categories.slice(0, 3).map((category, index) => (
            <span
              key={index}
              className="text-xs px-2 py-1 bg-primary-50 text-primary-700 rounded-full font-medium"
            >
              {category}
            </span>
          ))}
        </div>

        {/* Description */}
        <p className="text-sm text-gray-600 line-clamp-2">{description}</p>

        {/* Features */}
        <div className="flex flex-wrap gap-1">
          {features.slice(0, 3).map((feature, index) => (
            <span
              key={index}
              className="text-xs px-2 py-1 bg-gray-100 text-gray-600 rounded-md"
            >
              {feature}
            </span>
          ))}
        </div>

        {/* Price and Action */}
        <div className="flex items-center justify-between pt-3 border-t border-gray-200">
          <div>
            <p className="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-emerald-600 to-teal-600">
              ${price.toLocaleString()}
            </p>
          </div>
          <button className="bg-gradient-to-r from-emerald-500 to-teal-500 text-white px-4 py-2 rounded-lg font-semibold hover:from-emerald-600 hover:to-teal-600 transition-all shadow-md hover:shadow-lg text-sm">
            View Details
          </button>
        </div>
      </div>
    </div>
  );
};

export default ProductCard;
