import { useState } from "react";
import { CartModel } from "../models/CartModel";
import { CartEntry } from "../models/CartEntry";

function CartComponent() {

    const [currentCart, setCurrentCart] = useState(() => new CartModel());
    const [productList] = useState([]);

    function addToCart(event) {

        const index = Number(event.target.value);
        const product = productList[index];

        if (index >= 0 && index < productList.length) {

            setCurrentCart(prevCart => {

                const updated = new Map(prevCart.entries);

                if (updated.has(product.name)) {

                    const qty = updated.get(product.name).quantity;

                    updated.set(
                        product.name,
                        new CartEntry(product.name, product.price, qty + 1)
                    );

                } else {
                    updated.set(
                        product.name,
                        new CartEntry(product.name, product.price, 1)
                    );
                }

                return {
                    entries: updated,
                    totalQty: prevCart.totalQty + 1,
                    totalCost: prevCart.totalCost + product.price
                };
            });
        }
    }

    return (
        <div>
            <h2>Cart Component</h2>
        </div>
    );
}

export default CartComponent;