/*document.getElementById("boton").addEventListener("click",function(){

})
*/

const variable=function(mensaje){
      return mensaje;
}

//console.log(variable("hola"));

const sumar=a=>b=>a+b

const sumar1=function(a){
   return (function(b){
      return a+b;
   })
}
console.log([1,2,3,4,5].map(sumar1(1)))


