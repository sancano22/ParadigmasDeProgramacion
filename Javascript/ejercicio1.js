class Animal{
    constructor (nombre, especie){
        this.nombre=nombre;
        this.especie=especie;
    }

    cantar(){
        return `${this.nombre} puede cantar`;
    }

    bailar(){
        return `${this.nombre} puede bailar`;
    }
}

let perro=new Animal("Ámbar","mamifero")
console.log(perro);