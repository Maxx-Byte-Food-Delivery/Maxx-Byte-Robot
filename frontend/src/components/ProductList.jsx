            <div>
                {(
                        <>
                            {/*The product list view.  A table containing all items to buy.*/}
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
                                    {
                                        productList.map((item, index) => (
                                            <tr key={index}>
                                                <td>{item.name}</td>
                                                <td>${item.price}</td>
                                                <td>{item.description}</td>
                                                {/*The button to add the item to the cart.*/}
                                                <td><button type="button" value={index} onClick={addToCart}>➕🛒 Add 1 to Cart</button></td>
                                            </tr>
                                        ))
                                    }
                                </tbody>
                            </table>
                        </>
                    )
                }
            </div>