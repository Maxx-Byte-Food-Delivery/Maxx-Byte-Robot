import { Link } from "react-router-dom";
import CartComponent from "./CartComponent";
import "./NavigationBar.css";

function NavigationBar({ cart }) {
  return (
    <nav className="navbar">
      <ul className="nav-links">
        <li><Link to="/products">Products</Link></li>
        <li><Link to="/tracker">Track Order</Link></li>
        <li><Link to="/orders">Order History</Link></li>
        <li><CartComponent cart={cart} /></li>
        <li><Link to="/checkout">Checkout</Link></li>
        <li><Link to="/logout">Logout</Link></li>
      </ul>
    </nav>
  );
}

export default NavigationBar;