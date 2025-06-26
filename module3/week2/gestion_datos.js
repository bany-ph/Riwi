
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


const newMap = new Map ([
    ["Electronics", "cellPhone"],
    ["Accessories", "Mouse"],
    ["Accessories", "keyboard"]
]);



export function getAllProducts(){ // get all products
    return Object.values(products);
}


function formatProduct(){ // show products
    for(const id in products){
        console.log(`PRODUCT ID: ${id}, Details :` , products[id]);
    }     
}

function formatMapProducts(){
    newMap.forEach((product, category) =>{
        console.log(`Category: ${category}, Products: ${product}`)
    });

}



const setProducts = new Set(Object.values(products).map(element =>  console.log("unique product: ", element)) ); // check if products have duplicate items

formatProduct();
formatMapProducts();


