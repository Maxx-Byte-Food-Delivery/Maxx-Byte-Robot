import { Link } from "react-router-dom";
import CartComponent from "./CartComponent";

function NavigationBar({ cart }) {
  return (
    <nav>
      <Link to="/products">Products</Link>
      <CartComponent cart={cart} />
      <Link to="/checkout">Checkout</Link>
    </nav>
  );
}

export default NavigationBar;