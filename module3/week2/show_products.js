import {getAllProducts} from './gestion_datos.js';

const container = document.querySelector(".products-container");

const products = getAllProducts();

function displayProducts() {
    products.forEach(product => {
        const productDiv = document.createElement("div");
        productDiv.classList.add("box-product");
        productDiv.innerHTML = `
            <h3 class='title'>${product.productName}</h3>
            <p>Price: $${product.price}</p>
        `;
        container.appendChild(productDiv);
    });
}


displayProducts();