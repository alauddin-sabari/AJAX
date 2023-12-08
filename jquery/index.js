// //js example
// document.querySelector("h1").innerHTML = "Good Bye";
// // by jquery
// $("h1").text("Good Byes");


// //#index2.html
// $(".my-div h1").text("hi");
// $('#p1,h1').css("color", "blue"); //mutiple attribute selection by tag name and id or class name
// $('#p1,.my-div h1').css("color", "red");

// $("#p1").html("<b>Bold text</b>"); //have to use html tag to render html tag
// $("#p1").append("Godbye");
// $("#p1").prepend("Godbye");

// var mypara1 = $("<p></p>").text("this is paragraph 0")
// $("#p1").after(mypara1);
// // $("#p1").before(mypara1);




// //attribute-manipulation.html 
// //by js 
// var myattr = document.querySelector("a").getAttribute("href");
// console.log(myattr);

// //by jquery
// $("a").attr("href");
// $("a").removeAttr("href");

// //by js attribute set 
// document.querySelector("a").setAttribute('href', 'https://www.bengolai.com');
// // by jquery
// $("a").attr("href", "https://www.bengolai.com");





// //css style-manipulation.html
// $("h1").css("color",'red');
// $("h1").css("font-size",'5rem');
// //multiple css style change by json
// $("h1").css({"color":"red","font-size":"5rem"}); //
// //by js 
// d//ocument.querySelector("h1").style.color = "red";
// document.querySelector("h1").classList.add("style1"); //style1 defined in css file style1.css
// document.querySelector("h1").classList.add("style2"); //style2 defined in css file style2.css
// document.querySelector("h1").classList.add("style1");
// // add style1 and style2 by single line 
// document.querySelector("h1").classList.add("style1","style2");
// // // by jquery
// $("h1").addClass("style1 style2");  // in javascript need comma separated string(class name ) but in jquery need space separated string









// //event-listener.html
// document.querySelector("button").addEventListener("click", function (){ // "click" and anonymous function inside addEventListener is callback function

//     document.querySelector("h1").innerHTML = "You have clicked the button";
// })
// //by jquery
// $("button").click(function(){       // in jquery click  event listener is click() function but in javascript click event listener is addEventListener("click", function (){})
//     $("h1").text("You have clicked the button (listen by jquery)");
// })

// // toggle class by jquery  || toggle means if class is not present then add class and if class is present then remove class
// $("button").click( function(){
//     $("h1").toggleClass("style1");
// })


// // // with javascript
// var totalButton = document.querySelectorAll(".myButton").length;
// for (i = 0; i < totalButton; i++){
//     document.querySelectorAll(".myButton")[i].addEventListener("click", function (){

//         var text = this.innerHTML;
//         document.querySelector("h1").innerHTML = text + " is clicked";
//     })
// };

// $(".myButton").click( function () {

//     var text = this.innerHTML;
//     $("h1").text(text + " is clicked")
// })
// $(".myButton").on( "mouseover", function () {

//     var text = this.innerHTML;
//     $("h1").text(text + " is clicked")
// }) 




//// password maching example
// $("#logInButton").click( function (){

//     var password1 = $("#password1").val();
//     var password2 = $("#password2").val();
//     if(password1 != "" && password2 != "") {
//         if (password1 == password2){
//             alert("password matched")
//         }
//         else{
//             alert("password mismatched")
//         }
//     }
//     else{
//         alert("please enter password")
//     }
// })





// $("#animButton").click( function (){
//    $("#div1").animate({opacity: 0.5}, 3000);
// })

// $("#animButton").click( function (){
//     $("#div1").animate({
//         width: '500px',
//          height:'900px',
//         margin:'90px',
//     marginLeft:'100px',}, 
//          3000);
//  })
 








