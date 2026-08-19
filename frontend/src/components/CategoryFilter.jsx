function CategoryFilter({ selectedCategory, setSelectedCategory, categories }) {
  return (
    <div className="category-filter">
      <button
        onClick={() => setSelectedCategory("All")}
        className={selectedCategory === "All" ? "active-category" : ""}
      >
        All
      </button>

      {categories.map((category) => (
        <button
          key={category.category_id}
          onClick={() => setSelectedCategory(category.category_name)}
          className={
            selectedCategory === category.category_name ? "active-category" : ""
          }
        >
          {category.category_name}
        </button>
      ))}
    </div>
  );
}

export default CategoryFilter;
