const products = {
    /* example:
     id: {
            productName: name,
            price: price
        }             
*/
}


const addProduct = (name,price) => {
    // Validate the product data
    if (!name || typeof price !== 'number' || price <= 0) {
        return "Invalid product data.";
    }
    
    if (!noRepeat(name)) {
        return "Product name already exists.";
    }
    const id = generateRandomID();
    const newProduct = { productName: name, price: price}
    products[id] = newProduct; // add the new product to the products object

}

const deleteProduct = (id) =>{
    delete products[id];
}


const generateRandomID = () => {
  return Math.random().toString(16).slice(2);
}




const getIdByName = (name) => {
    for (const id in products) {
        if (products[id].productName === name) {
            return id;
        }
    }
    return null; // Return null if the product name is not found
}

function getProducts () {
    return products;
}


const noRepeat = (name) => {
    const setObject = new Set(Object.values(products).map(product => product.productName)); // Create a set of existing product names
    if (setObject.has(name)) {
        return false; // Name already exists
    }
    return true; // Name is unique
}



export { addProduct, deleteProduct, getProducts,getIdByName};