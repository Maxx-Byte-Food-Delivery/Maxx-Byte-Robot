import { useEffect, useState } from "react";
import Login from "./Login";
import CheckoutPage from "./CheckoutPage";
import { useNavigate } from "react-router-dom";
import CartComponent from "../components/CartComponent";

function Page(){
    
    const [message, setMessage] = useState("");

     useEffect(() => {
        fetch("http://127.0.0.1:8000/api/all_products")
        .then(res => res.json())
        .then(data => {
            console.log(data.products);
            setProductList(data.products);
        })
        .catch(err => console.error(err));
    }, []);
    

    const navigate = useNavigate();

    return (
        <>
            <div>
                <h1> {message} </h1>
            </div>
            <table>
                <tbody>
                    <tr>
                        <td><button type="button" 
                        onClick={() => navigate("/products")}>🏪 PRODUCTS</button></td>
                        <td><button type="button" 
                        onClick={() => navigate("/cart")}>🛒 CART ({currentCart.totalQty})</button></td>
                        <td><button type="button"                         
                        onClick={() => navigate("/checkout")}>💳 CHECKOUT</button></td>
                    </tr>
                </tbody>
            </table>
            
        </>
    )
}

export default Page;