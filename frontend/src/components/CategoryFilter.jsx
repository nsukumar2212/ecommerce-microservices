function CategoryFilter({ selectedCategory, setSelectedCategory }) {
  const categories = [
    'All',
    'Smartphones',
    'Laptops',
    'Headphones',
    'Tablets',
    'Televisions',
    'Speakers'
  ]

  return (
    <div className="category-filter">
      {categories.map((category) => (
        <button
          key={category}
          onClick={() => setSelectedCategory(category)}
          className={
            selectedCategory === category
              ? 'active-category'
              : ''
          }
        >
          {category}
        </button>
      ))}
    </div>
  )
}

export default CategoryFilter