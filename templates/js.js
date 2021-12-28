var text;
     window.onload = (event) => {
    document.getElementById('mainpage').style.display = 'none';
      $('#select').select2({
        placeholder:"Select product",
           allowClear:true}); 
};
    var search = document.getElementById('ss');
       search.addEventListener('click', (event) => {
      var  mylist = document.getElementById('search');
  var name  = mylist.options[mylist.selectedIndex].text;
  console.log(name)
  var qq = name.match(/(\d+)/);
  console.log(qq);
  var data = {
    customer:"Hai",
    message:'Success'
  };
  console.log(data);
     function div() {
       var  mylist = document.getElementById('search');
  var name  = mylist.options[mylist.selectedIndex].text;
//<-------------------------------------Trying an ajax--------------------------------------------------->
        fetch('/login/alternatecust', {

// Declare what type of data we're sending
headers: {
  'Content-Type': 'application/json'
},

// Specify the method
method: 'POST',

// A JSON payload
body: JSON.stringify({
    "Customercode": name
})
}).then(function (response) { // At this point, Flask has printed our JSON
return response.text();
}).then(function (text) {

console.log('POST response: ');

//Should be 'OK' if everything was successful
console.log(text);
//<--------------------------------------------------------------------------------------------------------->
var avail = document.getElementById('Avail').innerHTML = "Avail: "+text;

//<--------------------------------------------------Trying to do an ajax call call-------------------->

  $('hahahahaha').click(function(){
		var user = $('#inputUsername').val();
		var pass = $('#inputPassword').val();
		$.ajax({
			url: '/signUpUser',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});

});
// fetch('/login/select')
//     .then(function (response) {
//         return response.text();
//     }).then(function (text) {
//         console.log('GET response text:');
//         console.log(text); // Print the greeting as text
        
//     });

// // Send the same request
// fetch('/login/select')
//     .then(function (response) {
//         return response.json(); // But parse it as JSON this time
//     })
//     .then(function (json) {
//         console.log('GET response as JSON:');
//         console.log(json); // Here’s our JSON object
//     })

  //     mylist = document.getElementById('select');
  // var name  = mylist.options[mylist.selectedIndex].text;
  // console.log(name);
 
  // console.log(data);
  // var  mylist = document.getElementById('search');
  // var name  = mylist.options[mylist.selectedIndex].text;
  // console.log(name)
  // var qq = name.match(/(\d+)/);
  // console.log(qq);
  // var data = {
  //   c:'hai',
  //   message:'Success'
  // };
//<------------------------------------------------------------------------------------------------------->

  var x = document.getElementById('s');
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
    document.getElementById('mainpage').style.display = 'block';
  }
}  
   var counter = 1;
   let btnAdd = document.querySelector('#add');
btnAdd.addEventListener('click', () => {
  
   let table = document.querySelector('table');
  
   var cust_type = document.getElementById('Avail').innerHTML.replace('Avail:','')
   console.log(cust_type)
   var price = 100; 
var mylist = document.getElementById('select');
  var name  = mylist.options[mylist.selectedIndex].text;
  var inp = document.getElementById('qty').value;
  var entry = {
    "Productname":name
  }
  fetch(`${window.origin}/login/alternate`, {
      method: "POST",
      credentials: "include",
      body: JSON.stringify(entry),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json"
      })
    })
      .then(function (response) {
        if (response.status !== 200) {
          console.log(`Looks like there was a problem. Status code: ${response.status}`);
          return;
        }
        response.json().then(function (data) {
          console.log(data);
        });
      })
      .catch(function (error) {
        console.log("Fetch error: " + error);
      });

  
//Orginal fetch method used when successfully created call with fetch function
//   fetch('/login/product', {

// // Declare what type of data we're sending
// headers: {
//   'Content-Type': 'application/json'
// },

// // Specify the method
// method: 'POST',

// // A JSON payload
// body: JSON.stringify({
//     "Productname": name,
//     "Customertype":cust_type
// })
// }).then(function (response) { // At this point, Flask has printed our JSON
// return response.text();
// }).then(function (text) {

// //console.log('POST response: ');
// })
// // Send the same request
// fetch('/login/product')
//     .then(function (res) {
//         return res.json(); // But parse it as JSON this time
//     })
//     .then(function (json) {
//         console.log('GET response as JSON:');
//        console.log(typeof(json)); // Here’s our JSON object
//  console.log(inp);
//end of code snippets
    let template = `
                <tr>
                    <td>${counter}</td>
                    <td>${name}</td>
                    <td>${inp}</td>
                    <td>${JSON.stringify(json['Price'])}</td>
                </tr>`
 
    table.innerHTML += template;

    counter = counter + 1;
    console.log(inp);
    console.log(json);
  })

function increment() {
  // this function is executed whenever the user clicks the increment button
  document.getElementById("qty").stepUp();
}
function decrement(){
document.getElementById("qty").stepDown();
}
function add(){ 
  document.getElementByClass('cars').innerHTML;
 document.getElementByClass('productname').innerHTML = a;}
function product_price(){
  var a = document.getElementById('qty').value;
  console.log(a)
}
function myFunction() {
  var mylist = document.getElementById('w');
  var selected = mylist.options[mylist.selectedIndex].text;
  document.getElementById('productname').innerHTML = selected;
  var input = document.getElementById('qty');
  var input_selected =input.value;
  document.getElementById('customercode').innerHTML = input_selected;
}
function myfunction(){

var table = document.getElementById('table');
for (let i in table.rows) {
   let row = table.rows[i]
   //iterate through rows
   //rows would be accessed using the "row" variable assigned in the for loop
   for (let j in row.cells) {
     let col = row.cells[j]
     //iterate through columns
     console.log(col);
     console.log(row);//columns would be accessed using the "col" variable assigned in the for loop
   } 
   console.log(row);
   console.log(col);
  }   
}