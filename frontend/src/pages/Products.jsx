import { useState, useEffect } from "react";
import { showToast } from "../utils/toast";
import { CartEntry } from "../models/CartEntry";

function Products({ cart, setCart }) {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("/api/all_products/")
      .then((res) => {
        if (!res.ok) throw new Error("Failed to fetch products");
        return res.json();
      })
      .then((data) => {
        setProducts(data.products);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  function addToCart(product) {
    setCart(prevCart => {
      const updated = new Map(prevCart.entries);

      if (updated.has(product.name)) {
        const qty = updated.get(product.name).quantity;
        updated.set(product.name, new CartEntry(product.name, product.price, qty + 1));
      } else {
        updated.set(product.name, new CartEntry(product.name, product.price, 1));
      }

      return {
        entries: updated,
        totalQty: prevCart.totalQty + 1,
        totalCost: prevCart.totalCost + product.price
      };
    });

    showToast(`${product.name} added to cart!`, true);
  }

  if (loading) return <p>Loading products...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div>
      <h1>Products Page</h1>
      {products.map((product) => (
        <div key={product.id}>
          <h2>{product.name}</h2>
          <p>{product.description}</p>
          <p>${product.price}</p>
          <button onClick={() => addToCart(product)}>Add to Cart</button>
        </div>
      ))}
    </div>
  );
}

export default Products;