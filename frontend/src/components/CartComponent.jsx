// import { BsCart4 } from "react-icons/bs";
import { Link } from "react-router-dom";


function CartComponent({ cart }) {
  return (
    <div>
        <Link to="/cart">
            <h2><BsCart4 /> {cart.totalQty}</h2>
        </Link>
    </div>
  );
}

export default CartComponent;