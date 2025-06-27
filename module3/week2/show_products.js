/* show products in index.html */

import {getAllProducts} from './gestion_datos.js'; 

const container = document.querySelector(".products-container");

const products = getAllProducts(); // call the import method

function displayProducts() {
    products.forEach(product => {
        const productDiv = document.createElement("div");
        productDiv.classList.add("box-product"); // add a class to the element
        productDiv.innerHTML = `
            <h3 class='title'>${product.productName}</h3>
            <p>Price: $${product.price}</p>
        `;
        container.appendChild(productDiv); // add products inside the element container(div)
    });
}


displayProducts();