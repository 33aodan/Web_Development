const aboutMeOnClick=document.querySelector(".aboutMeHighlight")
const aboutMeBox=document.querySelector(".aboutMe")

aboutMeOnClick.addEventListener("click", highlighter1)
aboutMeOnClick.addEventListener("click", returnHighlighter2)
aboutMeOnClick.addEventListener("click", returnHighlighter3)

function highlighter1(){
    aboutMeBox.style.backgroundColor="lightblue"
}
function returnHighlighter1(){
    aboutMeBox.style.backgroundColor="white"
}

const projectOnClick=document.querySelector(".projectHighlight")
const projectBox2=document.querySelector(".projectBox")

projectOnClick.addEventListener("click", highlighter2)
projectOnClick.addEventListener("click", returnHighlighter1)
projectOnClick.addEventListener("click", returnHighlighter3)

function highlighter2(){
    projectBox2.style.backgroundColor="lightblue"
}
function returnHighlighter2(){
    projectBox2.style.backgroundColor="white"
}
const ecOnClick=document.querySelector(".ecHighlight")
const ecBox2=document.querySelector(".ecBox")

ecOnClick.addEventListener("click", highlighter3)
ecOnClick.addEventListener("click", returnHighlighter1)
ecOnClick.addEventListener("click", returnHighlighter2)

function highlighter3(){
    ecBox2.style.backgroundColor="lightblue"
}
function returnHighlighter3(){
    ecBox2.style.backgroundColor="white"
}