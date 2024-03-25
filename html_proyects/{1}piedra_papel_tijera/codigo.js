 // 1 piedra 2 papel 3 tijera
 let jugador = 0
 let min=1
 let max=3
 let pc_ = 0
 let triunfo =0
 let perdida =0

 while(triunfo<=3 && perdida <3 ){
  pc_ = Math.floor(Math.random()*(max-min+1)+min)
 jugador = prompt("Elige: piedra(1) papel(2) o tijera(3)")
 
 if(jugador==1){
     alert("elegiste piedra")
 }else if(jugador==2){
     alert("elegiste papel")
 }else if(jugador==3){
     alert("elegiste tijera")
 }else{
     alert("elegiste mal")
 }

 if(pc_==1){
     alert("pc eligio piedra")
 }else if(jugador==2){
     alert("pc eligio papel")
 }else if(jugador==3){
     alert("pc eligio tijera")
 }else{
     alert("pc eligio mal")
 }

 if(pc_==jugador){
     alert("empate")
 }else if(jugador==1 && pc_==3){
     alert("ganador")
     triunfo=triunfo+1
 }else if(jugador==2 && pc_==1){
     alert("ganador")
     triunfo=triunfo+1
 }else if(jugador==3 && pc_==2){
     alert("ganador")
     triunfo=triunfo+1
 }else{
     alert("perdedor")
     perdida=perdida+1
 }

}