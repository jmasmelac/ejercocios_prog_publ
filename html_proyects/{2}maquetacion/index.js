console.log('hola papu')

const express_c = require("express")
const app = express_c()
const jugadores =[]

class Jugador{
    constructor(id_m){
        this.id_m = id_m
    }
}
app.get("/unirse",(req,res)=>{
    const id_m = `${Math.random()}`//esa comilla es la alt+96
    const jugador = new Jugador(id_m)
    jugadores.push(jugador)
    res.send(id_m)
})
app.listen(8080,()=>{
    console.log("servidor funcionando")
})