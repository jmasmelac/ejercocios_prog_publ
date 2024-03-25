let ataque_jugador 
let ataque_enemigo

let vidas_jugador = 3
let vidas_enemigo = 3

function iniciar_juego(){

    let secction_seleccionar_ataque=document.getElementById('seleccionar-ataque')
        secction_seleccionar_ataque.style.display='none'//con las funciones de editar estilo podemos esconder texto, con el none no retorna a pantalla

    let secction_seleccionar_reiniciar=document.getElementById('reiniciar')
        secction_seleccionar_reiniciar.style.display='none'

    let boton_mascota= document.getElementById('boton-seleccion_mascota')//comilla sensilla ojo con esto
        boton_mascota.addEventListener('click' , seleccionar_mascota_jugador)//evento que mira que paso con esa variable


    let boton_fuego=document.getElementById('boton-seleccion_fuego')
        boton_fuego.addEventListener('click', ataque_fuego)
    let boton_agua=document.getElementById('boton-seleccion_agua')
        boton_agua.addEventListener('click', ataque_agua)
    let boton_tierra=document.getElementById('boton-seleccion_tierra')
        boton_tierra.addEventListener('click', ataque_tierra)


    let boton_reiniciar=document.getElementById('boton-seleccion_reiniciar')
        boton_reiniciar.addEventListener('click', reiniciar_juego)

}

function aleatorio (min,max){
    return Math.floor(Math.random()*(max-min+1)+min)
}

function seleccionar_mascota_jugador(){
    let hipopotamo_input = document.getElementById('hipopotamo')
    let camello_input = document.getElementById('camello')
    let komodo_input = document.getElementById('komodo')
    let chiguiro_input = document.getElementById('chiguiro')
    let toro_input = document.getElementById('toro')
    let barracuda_input = document.getElementById('barracuda')

    let spam_mascota_jugador = document.getElementById('mascota_jugador')
    
    if(hipopotamo_input.checked){
        spam_mascota_jugador.innerHTML ='hipopotamo'
    }else if(camello_input.checked){
        spam_mascota_jugador.innerHTML ='camello'
    }else if(komodo_input.checked){
        spam_mascota_jugador.innerHTML ='komodo'
    }else if(chiguiro_input.checked){
        spam_mascota_jugador.innerHTML ='chiguiro'
    }else if(toro_input.checked){
        spam_mascota_jugador.innerHTML ='toro'
    }else if(barracuda_input.checked){
        spam_mascota_jugador.innerHTML ='barracuda'
    }else{
        alert("seleccion no valida")
    }

    seleccionar_mascota_enemigo()

    let secction_seleccionar_ataque=document.getElementById('seleccionar-ataque')
    secction_seleccionar_ataque.style.display='block'//con las funciones de editar estilo podemos esconder texto, con el block si retorna a pantalla

    let secction_seleccionar_mascota=document.getElementById('seleccionar-mascota')
    secction_seleccionar_mascota.style.display='none'
}
function seleccionar_mascota_enemigo(){
    let mascota_aleatoria =aleatorio (1,6)

    let spam_mascota_enemigo = document.getElementById('mascota_enemiga')

    if(mascota_aleatoria ==1){
        spam_mascota_enemigo.innerHTML ='hipopotamo'
        alert("enemigo selecciono a hipopotamo")
    }else if(mascota_aleatoria ==2){
        spam_mascota_enemigo.innerHTML ='camello'
        alert("enemigo selecciono a camello")
    }else if(mascota_aleatoria ==3){
        spam_mascota_enemigo.innerHTML ='komodo'
        alert("enemigo selecciono a komodo")
    }else if(mascota_aleatoria ==4){
        spam_mascota_enemigo.innerHTML ='chiguiro'
        alert("enemigo selecciono a chiguiro")
    }else if(mascota_aleatoria ==5){
        spam_mascota_enemigo.innerHTML ='toro'
        alert("enemigo selecciono a toro")
    }else if(mascota_aleatoria ==6){
        spam_mascota_enemigo.innerHTML ='barracuda'
        alert("enemigo selecciono a barracuda")
    }else{
        alert("seleccion no valida")
    }

}


function ataque_fuego (){
    ataque_jugador='FUEGO'
    ataque_aleatorio_enemigo()
}
function ataque_agua (){
    ataque_jugador='AGUA'
    ataque_aleatorio_enemigo()
}
function ataque_tierra (){
    ataque_jugador='TIERRA'
    ataque_aleatorio_enemigo()
}


function evaluacion_combate (){
    let span_vidas_jugador=document.getElementById('vida_jugador')
    let span_vidas_enemigo=document.getElementById('vida_enemigo')
    if(ataque_enemigo==ataque_jugador){
        crear_mensaje_combate("empataste")
    }else if(ataque_jugador=='FUEGO' && ataque_enemigo=='TIERRA'){
        vidas_enemigo--
        span_vidas_enemigo.innerHTML=vidas_enemigo
        crear_mensaje_combate("ganaste")
    }else if(ataque_jugador=='AGUA' && ataque_enemigo=='FUEGO'){
        vidas_enemigo--
        span_vidas_enemigo.innerHTML=vidas_enemigo
        crear_mensaje_combate("ganaste")
    }else if(ataque_jugador=='TIERRA' && ataque_enemigo=='AGUA'){
        vidas_enemigo--
        span_vidas_enemigo.innerHTML=vidas_enemigo
        crear_mensaje_combate("GANASTE")
    }else{
        crear_mensaje_combate("PERDISTE")
        vidas_jugador--
        span_vidas_jugador.innerHTML = vidas_jugador
    }


    revisor_vidas()
   
}

function revisor_vidas(){
    if(vidas_enemigo == 0){
        let secction_seleccionar_reiniciar=document.getElementById('reiniciar')
        secction_seleccionar_reiniciar.style.display='block'
        crear_mensaje_result_bat("GANASTE LA PARTIDA")

    }else if(vidas_jugador==0){
        let secction_seleccionar_reiniciar=document.getElementById('reiniciar')
        secction_seleccionar_reiniciar.style.display='block'
        crear_mensaje_result_bat("PERDISTE LA PARTIDA")

    }
}

function crear_mensaje_combate(resultado_bat){
    let section_mensajes_combate =document.getElementById('mensajes_combate')
    let parrafo_combate = document.createElement('p')//el create elelmente crea algo en el html, en este caso un parrafo
    parrafo_combate.innerHTML= 'Tu mascota ataca con ' +ataque_jugador+ ' y la mascota del enemigo ataca con '+ataque_enemigo+' y '+ resultado_bat

    section_mensajes_combate.appendChild(parrafo_combate)

}

function crear_mensaje_result_bat(resultado_final){
    let section_mensajes_combate =document.getElementById('mensajes_combate')
    let parrafo_combate = document.createElement('p')
    parrafo_combate.innerHTML= resultado_final

    section_mensajes_combate.appendChild(parrafo_combate)


    let boton_fuego=document.getElementById('boton-seleccion_fuego')
        boton_fuego.disabled = true
    let boton_agua=document.getElementById('boton-seleccion_agua')
        boton_agua.disabled = true
    let boton_tierra=document.getElementById('boton-seleccion_tierra')
        boton_tierra.disabled = true

}

function ataque_aleatorio_enemigo(){
    let ataque_aleatorio = aleatorio(1,3)
    if(ataque_aleatorio==1){
        ataque_enemigo='FUEGO'
    }else if(ataque_aleatorio==2){
        ataque_enemigo='AGUA'
    }else if(ataque_aleatorio==3){
        ataque_enemigo='TIERRA'
    }
    evaluacion_combate ()
}

function reiniciar_juego(){

    if(vidas_enemigo==0 || vidas_jugador==0){
        location.reload()
    }

}

    window.addEventListener('load', iniciar_juego)//si se verifica si el html ya cargo se ejecuta el resto