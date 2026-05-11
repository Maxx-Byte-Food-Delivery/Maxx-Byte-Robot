function ProductList({ productList, addToCart }) {
  return (
    <div>
      <h2>Food You Can Order</h2>

      <table>
        <thead>
          <tr>
            <th>Product Name</th>
            <th>Price</th>
            <th>Description</th>
            <th>Add to Cart</th>
          </tr>
        </thead>

        <tbody>
          {productList.map((item, index) => (
            <tr key={index}>
              <td>{item.name}</td>
              <td>${item.price}</td>
              <td>{item.description}</td>
              <td>
                <button value={index} onClick={addToCart}>
                  ➕🛒 Add 1 to Cart
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default ProductList;