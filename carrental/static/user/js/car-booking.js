// Data Limit Set Starts
var dateStartInput=document.getElementById("book_pick")
var dateEndInput=document.getElementById("book_off")
var date= new Date()
y = date.getFullYear();
m = date.getMonth() + 1;
d = date.getDate();
if(m<10){
    m=`0`+m
}
if(d<10){
    d=`0`+d
}
var todayDate=`${y}-${m}-${d}`
var tomorrowDate=`${y}-${m}-${d+1}`
dateStartInput.min=todayDate
dateEndInput.min=tomorrowDate
// Date Limit Set Ends

//Pickup location
// let pickupSelection=document.getElementById("custom-pickup")
// pickupSelection.addEventListener('change',()=>{
//     if (pickupSelection.checked){
//         document.getElementById("pick-location").style="display:block"
//     }
//     else{
//         document.getElementById("pick-location").style="display:none"
//     }
// })

let bookingForm=document.getElementById("booking-form")
bookingForm.addEventListener("submit",(e)=>{
    e.preventDefault()
    let formData=new FormData(bookingForm)
    if(formData.get("start_date")>formData.get("end_date")){
        showPopup("Sorry!","Invalid selection, please check the pick-up date and drop-date before trying again","Try Again")
    }
    else{
        checkReservation(formData)
    }
    
})

async function checkReservation(form){
    await fetch(reservationCheckUrl, {
        method: "POST",
        headers: {
            'X-CSRFToken': getCookie("csrftoken"),
            'Content-type': 'application/json; charset=UTF-8'
        },
        body: JSON.stringify({
            start_date: form.get("start_date"),
            end_date:form.get("end_date"),
            cid:cId,
            pickup:form.get("custom-pickup")
        }),
      }).then(res=>res.json()).then(response=>{
        console.log(response);
        if(response.status == 'available'){
            createCookie("cid",response.cid,45)
            createCookie("sd",response.start_date,45)
            createCookie("ed",response.end_date,45)
            let content=`Selected vehicle available to book from ${response.start_date} - ${response.end_date} and estimated total cost is ₹ ${response.price}`
            showPopup("Hooray!",content,"Book Now")
        }
        else{
            showPopup("Sorry!","Selected vehicle is un-available for the selected dates","OK")
        }
    })
}


function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }

function createCookie(name,value,minutes) {
    if (minutes) {
        var date = new Date();
        date.setTime(date.getTime()+(minutes*60*1000));
        var expires = "; expires="+date.toGMTString();
    } else {
        var expires = "";
    }
    document.cookie = name+"="+value+expires+"; path=/booking";
}


function showPopup(title,content,button){
    // Modal Controls 
    const modalContent=document.getElementById("modal-content")
    const modalTitle=document.getElementById("modal-title")
    const modalButton=document.getElementById("modal-button")
    modalTitle.innerText=title
    modalContent.innerText=content
    modalButton.innerText=button
    if(button=='Book Now'){
        modalButton.href=`/booking`
    }
    $('#myModal').modal('show');
}