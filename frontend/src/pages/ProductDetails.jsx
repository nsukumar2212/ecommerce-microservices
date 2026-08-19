import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getProductById } from "../services/productApi";

function ProductDetails() {
  const { id } = useParams();

  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadProduct() {
      try {
        const data = await getProductById(id);

        setProduct(data);
      } catch (error) {
        console.error(error);

        setError("Unable to load product");
      } finally {
        setLoading(false);
      }
    }

    loadProduct();
  }, [id]);

  if (loading) {
    return <h2>Loading product...</h2>;
  }

  if (error) {
    return <h2>{error}</h2>;
  }

  if (!product) {
    return <h2>Product not found</h2>;
  }

  return (
    <main className="product-details">
      <div className="product-details-image">
        <img src={product.image} alt={product.product_name} />
      </div>

      <div className="product-details-info">
        <h1>{product.product_name}</h1>

        <p>Brand: {product.brand}</p>

        <h2>₹{product.price}</h2>

        <p>Stock available: {product.stock}</p>

        {product.description && <p>{product.description}</p>}

        <button>Add to Cart</button>
      </div>
    </main>
  );
}

export default ProductDetails;
