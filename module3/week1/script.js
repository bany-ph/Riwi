const form = document.getElementById("form")

form.addEventListener("submit", function(event){ // if the button from form is clicked then: 
    event.preventDefault(); // prevent to send form

    const userName = document.getElementById("name").value 
    let userAge = document.getElementById("age").value
    
    if(userAge.trim() == '' || userName.trim() == ''){ // check if the inputs are empty
        ShowMessage("Please fill the inputs",false);
        return // close the eventListener
    }
 
    
    if(userAge < 0 || isNaN(userAge)){
        ShowMessage("The age can't be less than 0 or letters",false) // second parameter is false cuz is only a error message
        return
    }else if(userAge < 18){
        ShowMessage(`Hi! ${userName}, you're a minor. Keep learning while you have fun coding`, true)
        
    }else{
        ShowMessage(`Hi! ${userName}, you're an adult. Prepare for big opportunities in programming's world`,true)
    }
    
    this.submit(); // send the data
}); 



function ShowMessage(showMessage, isAlert){ 
   let message =  document.getElementById("message")
    if(isAlert){
        alert(showMessage)
    }else{
        message.style.color = "red" // style the color red
        message.textContent = showMessage;
    }
}