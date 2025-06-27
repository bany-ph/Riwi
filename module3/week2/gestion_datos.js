
const products = {
    1: {
        id: 1,
        productName: "Cell Phone",
        price : 800000
    },
    2: {
        id: 2,
        productName: "Mouse",
        price : 80000
    },
    3:{
        id: 3,
        productName: "keyboard",
        price: 54000
    }
     
}


const newMap = new Map ([ // map categories and product
    ["Electronics", "cellPhone"],
    ["Accessories", "Mouse"],
    ["Accessories", "keyboard"]
]);



export function getAllProducts(){ // export to show all products on a page
    return Object.values(products);
}


function formatProduct(){ // show products
    for(const id in products){
        console.log(`PRODUCT ID: ${id}, Details :` , products[id]); // show the the id and them el object inside it
    }     
}

function formatMapProducts(){
    newMap.forEach((product, category) =>{
        console.log(`Category: ${category}, Products: ${product}`)
    });

}


// check if products have duplicate items
const setProducts = new Set(Object.values(products).map(element =>  console.log("unique product: ", element)) ); 


/* show products in console */
formatProduct();
formatMapProducts();


