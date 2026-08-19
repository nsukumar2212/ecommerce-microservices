import { useEffect, useState } from "react";
import ProductCard from "../components/ProductCard";
import SearchBar from "../components/SearchBar";
import CategoryFilter from "../components/CategoryFilter";
import { getProducts, getCategories } from "../services/productApi";
import { useSearchParams } from "react-router-dom";

function Products() {
  const [searchParams] = useSearchParams();

  const categoryFromUrl = searchParams.get("category") || "All";

  const [products, setProducts] = useState([]);
  const [categories, setCategories] = useState([]);

  const [searchTerm, setSearchTerm] = useState("");

  const [selectedCategory, setSelectedCategory] = useState(categoryFromUrl);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  useEffect(() => {
    async function loadData() {
      try {
        setLoading(true);

        const [productsData, categoriesData] = await Promise.all([
          getProducts(),
          getCategories(),
        ]);

        const categoryMap = {};

        categoriesData.forEach((category) => {
          categoryMap[category.category_id] = category.category_name;
        });

        const formattedProducts = productsData.map((product) => ({
          id: product.product_id,

          name: product.product_name,

          brand: product.brand,

          price: Number(product.price),

          image: product.image,

          stock: product.stock,

          category: categoryMap[product.category_id] || "Other",
        }));

        setProducts(formattedProducts);

        setCategories(categoriesData);
      } catch (error) {
        console.error(error);

        setError("Unable to load products");
      } finally {
        setLoading(false);
      }
    }

    loadData();
  }, []);

  useEffect(() => {
    setSelectedCategory(categoryFromUrl);
  }, [categoryFromUrl]);

  const filteredProducts = products.filter((product) => {
    const search = searchTerm.toLowerCase();

    const matchesSearch =
      product.name.toLowerCase().includes(search) ||
      product.brand.toLowerCase().includes(search);

    const matchesCategory =
      selectedCategory === "All" || product.category === selectedCategory;

    return matchesSearch && matchesCategory;
  });

  if (loading) {
    return (
      <main className="products-page">
        <h2>Loading products...</h2>
      </main>
    );
  }

  if (error) {
    return (
      <main className="products-page">
        <h2>{error}</h2>
      </main>
    );
  }

  return (
    <main className="products-page">
      <h2>Electronics Products</h2>

      <p>{filteredProducts.length} products found</p>

      <SearchBar searchTerm={searchTerm} setSearchTerm={setSearchTerm} />

      <CategoryFilter
        selectedCategory={selectedCategory}
        setSelectedCategory={setSelectedCategory}
        categories={categories}
      />

      <div className="product-list">
        {filteredProducts.map((product) => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>

      {filteredProducts.length === 0 && (
        <p className="no-products">No products found.</p>
      )}
    </main>
  );
}

export default Products;
