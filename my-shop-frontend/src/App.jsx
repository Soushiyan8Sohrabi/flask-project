import { useState, useEffect } from "react"

function App() {
  const [cartItems, setCartItems] = useState([])
  const [customerName, setCustomerName] = useState("")
  const [cartCount, setCartCount] = useState(0)

  const loadCart = () => {
    fetch("http://127.0.0.1:5000/cart")
      .then((res) => res.json())
      .then((data) => {
        setCartItems(data.cart)
        setCartCount(data.cart.length)
      })
  }

  useEffect(() => {
    loadCart()
  }, [])

  const createOrder = () => {
    if (!customerName) {
      alert("Please enter your name")
      return
    }

    fetch("http://127.0.0.1:5000/order/create", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ customer_name: customerName }),
    })
    .then(() => {
      loadCart()
      setCartCount(0)
      setCustomerName("")
      alert(" Order received! But RIP to your wallet!")
    })
  }

  return (
    <>
      <h3>Items Number: {cartCount}</h3>

      <h1>Cart Items:</h1>
      <ul>
        {cartItems.map((item, index) => (
          <li key={index}>
            {item.name} - ${item.price} - Quantity: {item.quantity}
          </li>
        ))}
      </ul>

      <hr />

      <div>
        <label>Customer Name: </label>
        <input 
          type="text" 
          value={customerName} 
          onChange={(e) => setCustomerName(e.target.value)} 
          placeholder="Enter name"
        />
      </div>

      <button onClick={createOrder}>
        Confirm Order
      </button>
    </>
  )
}

export default App
