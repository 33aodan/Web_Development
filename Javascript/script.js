// document.querySelector(".heading1").textContent = "crip walkaa";
// document.querySelector("#heading1").textContent = "crisp walkaa";
// console.log("Baodan");
// literals cant change value
// 34
// 56
// 45.8
// 'python'

// variables can change value
// let ageA = 15;
// console.log(ageA);

// naming conventions to name a variable:

// var age =15;
// age =15;
// console.log(age);

// we dont use data types to declare a variable in javascript as like c++

// type of is a keyword in javascript which is used to know the datatype of a variable

// var age =15;
// age =15;
// console.log(typeof age);

// number : decimals and integers
// // undefined : if im not putting any Value
// // null : empty value
// // bigint: too big and does not get adjusted in number data type
// // string: letters and words in qoutes
// // boolean: true/false

// //assignment operators
// let age=4;
// // age = 15 + 3;
// // age +=4;
// // age++;
// //age--;
// console.log(age)
// console.log(3**3);
// //
// let x;
// x=5000;
// console.log(x)

// if(2 == 3){
//     console.log("equal");
// }
// if(2 == 4){
//     console.log("not equal");
// }
// if(2 == 5){
//     console.log("dont know");
// }
// if(false == true){
//     console.log("not possible");
// }
// if(true){
//     console.log("true");
// }
// // else if(5 != 3){
// //     console.log("not equal 5 and 3");
// // }
// // else if(4 != 4){
// //     console.log("not equal 4 and 4");
// // }
// // else{
// //     console.log("Default value!!");
// // }
// x = 2;
// y = 30;
// z = 12;
// if(x >= 4 && x <= 2){
//     console.log(x);
// }
// if(x != -15){
//     console.log("whatever");
// }
// if(x == 5 && y <= 4){
//     console.log("its gonna happen");
// }
// if(z > x && x<y || x == 2){
//     console.log("you say");
// }
// if(!(y < 3)){
//     console.log(y);
// }
// else if(y < 10 || z < 5){
//     console.log("okkkkkkk");
// }
// else if(z < 10 || y <= 100){
//     console.log("pikachu");
// }
// else if(z == 0 && y ==5){
//     console.log("Pikaboo");
// }
// else{
//     console.log("Default value");
// }

//dom manipulation
// how to change the css styles using javascript

document.querySelector("body").style.backgroundImage = "url('https://j.gifs.com/KrWgwQ.gif')";
document.querySelector("body").style.backgroundSize = "cover"
document.querySelector(".heading").style.textAlign = "center";
document.querySelector(".heading").style.color = "lightBlue";
document.querySelector(".heading").style.fontSize = "36px";
document.querySelector(".heading").style.fontFamily = "Impact,Charcoal,sans-serif";
const images = document.querySelectorAll(".images")
for (let i = 0; i < images.length; i++) {
    images[i].style.width = "250px";
    images[i].style.height = "250px";
    images[i].style.padding = "25px";
  }
  document.querySelector(".hardcoreSmash").style.textAlign="center"
  const button = document.querySelectorAll("button")
for (let i = 0; i < button.length; i++) {
    button[i].style.margin = "25px";
    button[i].style.width = "250px";
    button[i].style.height = "50px";
    button[i].style.fontSize = "36px";
    button[i].style.fontFamily = "Impact,Charcoal,sans-serif";
  }
  document.querySelector(".buttons").style.textAlign="center"
  document.querySelector(".or").style.fontSize="24px"
  document.querySelector(".or").style.display="inline"
  document.querySelector(".or").style.fontFamily = "Impact,Charcoal,sans-serif";
  document.querySelector(".or").style.color="lightBlue"