import React, { useEffect, useState } from "react";
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/hello")
      .then(res => res.json())
      .then(data => {
        setMessage(data.message);
        console.log(data);
      })
      .catch(err => console.error(err));
  }, []);

  //The product data structure used for listing products for sale.  
  class Product {
    name = "";
    price = 0;
    description = "";

    constructor(name, price, description) {
      this.name = name;
      this.price = price;
      this.description = description;
    }
  }

  /**
   * This is the data structure for the cart. 
   * It contains a dynamic total quantity and total cost variable
   * that is rapidly updated with each addition or removal of items from the cart,
   * and can thus be quickly checked to allow the user to readily view total qty
   * and cost of order.
   * 
   * A JavaScript Map is used to keep track of the unique items ordered and their quantity,
   * each represented by CartEntry objects.
   * New Maps must be created during adding or removal to keep the updating process pure.
   */
  class Cart {
    totalQty = 0;
    totalCost = 0;
    entries = new Map();

    constructor() {
      this.totalQty = 0;
      this.totalCost = 0;
      this.entries = new Map();
    }
  }

  /**
   * This is the data structure for a unique cart entry.  Contains name, price
   * and current quantity count.  Quantity must be above zero for a valid cart
   * entry.
   */
  class CartEntry {
    name = ""
    price = 0;
    quantity = 0;
    constructor(name, price, quantity) {
      this.name = name;
      this.price = price;
      this.quantity = quantity;
    }
  }

  class Address { //Address input displayed during checkout view.  Maintained by inputAddress state variable.  
    addressLine1 = "";
    addressLine2 = "";
    city = "";
    state = "Alabama";
    zipCode = 0;
    constructor() {
      this.addressLine1 = "";
      this.addressLine2 = "";
      this.city = "";
      this.state = "Alabama";
      this.zipCode = 0;
    }
  }

  const emptyCart = new Cart();

  const emptyAddress = new Address();

  const dummyProducts = [
    new Product("Hamburger and fries", 9.99, "Juicy hamburger with crispy fries"),
    new Product("Pizza", 11.99, "Delicious pizza with your favorite toppings"),
    new Product("Salad", 6.99, "Fresh salad with a variety of vegetables"),
    new Product("Soda", 2.99, "Refreshing carbonated beverage")
  ];

  const states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
    "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
    "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
    "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
  ]

  let [currentCart, setCurrentCart] = useState(emptyCart);
  let [productList, setProductList] = useState(dummyProducts); // This would be populated from the backend in a real application
  let [inputAddress, setInputAddress] = useState(emptyAddress); //Regulates the input fields for the address form
  let [view, setView] = useState("productList"); // Can be "productList", "cart", or "checkout"
  const CART_COLUMNS = 4;
  //In a real application, this would be done in a useEffect hook that fetches the product list from the backend when the component mounts.
  //Function that fires when adding a product from the product list.  
  function addToCart(event) {
    const product = productList[event.target.value];
    //The key for the add to cart is their index position in the array of products for sale.
    if (event.target.value >= 0 && event.target.value < productList.length) {
      setCurrentCart(prevCart => {
        const updatedCartEntries = new Map(prevCart.entries); //You must create a new map to ensure pure change of Maps.
        if (updatedCartEntries.has(product.name)) { //If the product is already in the cart, update its quantity by 1.
          const quantity = prevCart.entries.get(product.name).quantity;
          updatedCartEntries.set(product.name, new CartEntry(product.name, product.price, quantity + 1));
        }
        else {//Otherwise, add it to the cart's entries map with a starting quantity of 1.
          updatedCartEntries.set(product.name, new CartEntry(product.name, product.price, 1));
        }
        const updatedTotalQty = prevCart.totalQty + 1;//Update grand total quantity.
        const updatedTotalCost = prevCart.totalCost + product.price;//Update grand total price.
        showToast("One "+product.name+" has been added to the cart!  You now have "+updatedCartEntries.get(product.name).quantity+".", true);
        return { entries: updatedCartEntries, totalQty: updatedTotalQty, totalCost: updatedTotalCost };
      });
    }
  }

  //Function for adding one more of an item in your cart.
  function addMoreToCart(event) {
    setCurrentCart(prevCart => {
      const updatedCartEntries = new Map(prevCart.entries);// You must create a new map to ensure pure change of Maps.
      const product = updatedCartEntries.get(event.target.value);//Look up the product to add on to, is it in the Cart?
      if (product != undefined) {//If it's in the cart, proceed. 
        //Create a new CartEntry with the quantity incremented.
        updatedCartEntries.set(product.name, new CartEntry(product.name, product.price, product.quantity + 1));
        const updatedTotalQty = prevCart.totalQty + 1;//Update grand total quantity.
        const updatedTotalCost = prevCart.totalCost + product.price;//Update grand total price.
        showToast("One more "+product.name+" has been added to the cart!  You now have "+updatedCartEntries.get(product.name).quantity+".", true);
        return { entries: updatedCartEntries, totalQty: updatedTotalQty, totalCost: updatedTotalCost };
      }
      else //As a failsafe, if you're adding an item to what you think is in the cart, but isn't, gracefully abort the function.
        return prevCart;
    });
  }

  //Function for removing an item from the cart.  
  function removeFromCart(event) {
    setCurrentCart(prevCart => {
      const productName = event.target.value;
      const updatedCartEntries = new Map(prevCart.entries);// You must create a new map to ensure pure change of Maps.
      const productToRemove = updatedCartEntries.get(productName);//Look up the product to remove from, is it in the Cart?
      if (productToRemove != undefined) {//If it's in the cart, proceed. 
        const decQty = productToRemove.quantity - 1;//Decrease the quantity of the item to remove from.
        if (decQty < 0)//If quantity is below zero, peg it to zero.  
          decQty = 0;
        if (decQty > 0) {//If the quantity is still 1 or higher, create a new CartEntry with the decremented quantity.  
          updatedCartEntries.set(productName, new CartEntry(productName, productToRemove.price, decQty));
          showToast("You removed one "+productName+" from the cart.  There are now "+updatedCartEntries.get(productName).quantity+" left.", false);
        }
        else {
          updatedCartEntries.delete(productName);//If none remain, just delete the CartEntry.
          showToast("You removed "+productName+" from the cart.", false);
        }
        const reducedQty = prevCart.totalQty - 1; //Update grand total quantity.
        const updatedTotalQty = reducedQty < 0 ? 0 : reducedQty; //If reduced quantity is below zero, peg it to zero.  
        const reducedPrice = prevCart.totalCost - productToRemove.price; //Update grand total price.
        const updatedTotalCost = reducedPrice < 0 ? 0 : reducedPrice; //If reduced price is below zero, peg it to zero.
        return { entries: updatedCartEntries, totalQty: updatedTotalQty, totalCost: updatedTotalCost };
      }
      else //As a failsafe, if you're removing from item to what you think is in the cart, but isn't, gracefully abort the function.
        return prevCart
    });
  }

  function removeCompletelyFromCart(event) {
    if (confirm("Do you want to remove " + event.target.value + " altogether from your cart?")) {
      setCurrentCart(prevCart => {
        const productName = event.target.value;
        const updatedCartEntries = new Map(prevCart.entries);// You must create a new map to ensure pure change of Maps.
        const productToRemove = updatedCartEntries.get(productName);//Look up the product to remove from, is it in the Cart?
        if (productToRemove != undefined) {//If it's in the cart, proceed. 
          updatedCartEntries.delete(productName);//Remove the item from the cart entirely.
          const reducedQty = prevCart.totalQty - productToRemove.quantity;  //Update grand total quantity.
          const updatedTotalQty = reducedQty < 0 ? 0 : reducedQty; //If reduced quantity is below zero, peg it to zero.
          const reducedPrice = prevCart.totalCost - (productToRemove.price * productToRemove.quantity); //Update grand total price.
          const updatedTotalCost = reducedPrice < 0 ? 0 : reducedPrice; //If reduced price is below zero, peg it to zero.
          showToast("You removed "+productName+" from the cart.", false);
          return { entries: updatedCartEntries, totalQty: updatedTotalQty, totalCost: updatedTotalCost };
        }
        else //As a failsafe, if you're removing from item to what you think is in the cart, but isn't, gracefully abort the function.
          return prevCart
      });
    }
  }

  function showToast(message, positive) {
    const toast = document.createElement("div");
    toast.id = positive ? "snackbar" : "neg_snackbar";
    toast.className = "show";
    toast.innerText = message;
    document.body.appendChild(toast);

    // Remove after 3 seconds
    setTimeout(() => {
      toast.className = toast.className.replace("show", "");
      document.body.removeChild(toast);
    }, 3000);
  }

  //Functions for responding to changes to any part of the address input class.
  function onChangeAddress1(event) {
    setInputAddress({
      ...inputAddress,
      addressLine1: event.target.value
    }
    )
  }

  function onChangeAddress2(event) {
    setInputAddress({
      ...inputAddress,
      addressLine2: event.target.value
    }
    )
  }

  function onChangeCity(event) {
    setInputAddress({
      ...inputAddress,
      city: event.target.value
    }
    )
  }

  function onChangeState(event) {
    setInputAddress({
      ...inputAddress,
      state: event.target.value
    }
    )
  }

  function onChangeZip(event) {
    setInputAddress({
      ...inputAddress,
      zipCode: event.target.value
    }
    )
  }

  //Clear the cart.  Confirm with user before proceeding.
  function clearCart() {
    if (confirm("Do you want to clear your cart?")) {
      setCurrentCart(emptyCart);
      showToast("You have cleared the cart.", false);
    }
  }

  //Clear the address form.  Confirm with user before proceeding.
  function clearAddress() {
    if (confirm("Do you want to reset the address form?")) {
      setInputAddress(emptyAddress);
    }
  }

  //Switch the view between the products, cart and checkout.  
  function switchView(event) {
    setView(event.target.value);
  }

  return (
    <>
      <div>
        <h1> {message} </h1>
      </div>
      <table>
        <tbody>
          {/*The viewing tabs that let you cycle beteen products to buy, your cart and a checkout page.*/}
          <tr>
            <td><button type="button" value="productList" onClick={switchView} disabled={view === "productList"} >🏪 PRODUCTS</button></td>
            <td><button type="button" value="cart" onClick={switchView} disabled={view === "cart"} >🛒 CART ({currentCart.totalQty})</button></td>
            <td><button type="button" value="checkout" onClick={switchView} disabled={view === "checkout" || currentCart.totalQty <= 0} >💳 CHECKOUT</button></td>
          </tr>
        </tbody>
      </table>
      <div>
        {
          view === "productList" && (
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
      <div>
        {
          view === "cart" && (
            <>
              {/*The cart view.  A table containing items you've added to the cart.*/}
              <h2>Your Cart</h2>
              <p>You have {currentCart.totalQty} item(s) in the cart.</p>
              <table>
                <thead>
                  <tr>
                    <th>Product Name</th>
                    <th>Price</th>
                    <th>Total Price</th>
                    <th>Quantity</th>
                  </tr>
                </thead>
                <tbody>
                  {
                    currentCart.totalQty > 0 ?
                      (
                        <>
                          {/*If you have at least one item in the cart, display a table of unique products you've bought and their quantities.  Otherwise, indicate that the cart is empty.*/}
                          {
                            Array.from(currentCart.entries.values()).map((item, index) => (
                              <tr key={index}>
                                <td>{item.name}</td>
                                <td>${item.price}</td>
                                <td>${item.price * item.quantity}</td>
                                {/*Buttons to remove or add to the current quantity of the item.*/}
                                <td><button type="button" value={item.name} onClick={removeCompletelyFromCart}>🗑️</button><button type="button" value={item.name} onClick={removeFromCart}>➖</button> {item.quantity} <button type="button" value={item.name} onClick={addMoreToCart}>➕</button></td>
                              </tr>
                            ))
                          }
                          {/*A final row that shows your grand total of quantity and cost for your current order.*/}
                          <tr key="FINAL_TOTAL">
                            <td><b>TOTAL</b></td>
                            <td>➡️</td>
                            <td><b>${Math.trunc(currentCart.totalCost * 100) / 100}</b></td>
                            <td><b>{currentCart.totalQty} item(s)</b></td>
                          </tr>
                        </>
                      )
                      :
                      (
                        <tr colSpan={CART_COLUMNS} key="NO_ITEMS"><td><i>Your cart is empty.</i></td></tr>
                      )
                  }
                </tbody>
              </table>
              {/*The button to empty the cart.  Make sure to confirm to prevent accidentally clearing the cart!*/}
              <button onClick={clearCart} disabled={currentCart.totalQty <= 0}>❌🛒 Clear Cart</button>
            </>
          )
        }
      </div>
      <div>
        {
          view === "checkout" && (
            <>
              {/*The checkout view.  Unlocked when there's at least 1 item in the cart.*/}
              <h2>Checkout</h2>
              <p>Confirm your order and where you want it delivered here.</p>
              {/*Reproduce the cart table; but this time, it's not editable.*/}
              <table>
                <thead>
                  <tr>
                    <th>Product Name</th>
                    <th>Price</th>
                    <th>Quantity</th>
                    <th>Total Price</th>
                  </tr>
                </thead>
                <tbody>
                  {
                    Array.from(currentCart.entries.values()).map((item, index) => (
                      <tr key={index}>
                        <td>{item.name}</td>
                        <td>${item.price}</td>
                        <td>{item.quantity}</td>
                        <td>${item.price * item.quantity}</td>
                      </tr>
                    ))
                  }
                  <tr key="FINAL_TOTAL">
                    <td><b>TOTAL</b></td>
                    <td>➡️</td>
                    <td><b>{currentCart.totalQty} item(s)</b></td>
                    <td><b>${Math.trunc(currentCart.totalCost * 100) / 100}</b></td>
                  </tr>
                </tbody>
              </table>
              {/*The address entry form.*/}
              <div>Street Address 1: <input type="text" value={inputAddress.addressLine1} onChange={onChangeAddress1} /></div>
              <div>Street Address 2: <input type="text" value={inputAddress.addressLine2} onChange={onChangeAddress2} /></div>
              <div>City: <input type="text" value={inputAddress.city} onChange={onChangeCity} /></div>
              <div>State:
                <select value={inputAddress.state} onChange={onChangeState}>
                  {states.map(state => (
                    <option key={state} value={state}>{state}</option>
                  ))}
                </select>
              </div>
              <div>Zip Code: <input type="text" maxLength="5" pattern="^[0-9]+$" value={inputAddress.zipCode} onChange={onChangeZip} /></div>
              <button onClick={clearAddress}>❌ Clear Address</button>
              <button>✔️ Submit Order</button>
            </>
          )
        }
      </div>
    </>
  )
}

export default App
