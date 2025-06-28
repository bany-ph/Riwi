import { deleteProduct,getProducts, addProduct, getIdByName} from "./management.js";


const container = document.getElementById("show-products-container");



/* add */
document.getElementById("send").addEventListener('click', () => {
    const productName = document.getElementById("productName");
    const productPrice = document.getElementById("productPrice");
    if(!productName.value || !productPrice.value) return;
    
    const ifMessage = addProduct(productName.value, parseFloat(productPrice.value));
    if(ifMessage){errorAlert(ifMessage); return;}
   

    productName.value = "";
    productPrice.value = "";
    displayProducts(); // update the display
});


document.getElementById("show-products-container").addEventListener('click', (e) => {
    if(e.target.classList.contains("icon")){
        const productDiv = e.target.parentElement;
        const productName = productDiv.querySelector("p").textContent;
        const productId = getIdByName(productName);
        console.log(productName);
        if (productId) {
            deleteProduct(productId);
            productDiv.remove(); // Remove the product div from the container
        } else {
            console.error("Product not found for deletion.");
        }
        
    }
});

function displayProducts(){
    container.innerHTML = ""; // Clear the container before displaying products
   const products = getProducts();
    Object.values(products).forEach(product=> {
        const productdiv = document.createElement("div");
        productdiv.classList.add("products-box")
        productdiv.innerHTML = `
            <p>${product.productName}</p>
            <span>${product.price}</span>
            <i class='fa-solid fa-trash icon'></i>
        `; 
        container.appendChild(productdiv);
    });
}

  const errorAlert = (mess) => {
      
    alert(mess);
      
}; 


