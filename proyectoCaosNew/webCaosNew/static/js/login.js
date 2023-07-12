window.addEventListener('load', ()=> {
    const form = document.querySelector('#formulario')

    const usuario = document.getElementById('usuario')
    const pass = document.getElementById('pass')


    form.addEventListener('submit', (e) => {
        // e.preventDefault()
        validaCampos()
    })

    const validaCampos = ()=> {
        //capturar los valores ingresados por el usuario

        const usuarioValor = usuario.value.trim()
        const passValor = pass.value.trim();




        //validando campo email
        if(!usuarioValor){
            //console.log('CAMPO VACIO')
            validaFalla(usuario, 'Campo vacío')
        }else{
            validaOk(usuario)
        }
         //validando campo password
        const er = /^(?=.\d)(?=.[a-z])(?=.*[A-Z]).{6,18}$/
        if(!passValor) {
            validaFalla(pass, 'Campo vacío')
        } else if (passValor.length < 8) {
            validaFalla(pass, 'Debe tener 8 caracteres cómo mínimo.')
        } 

         else {
            validaOk(pass)
        }


    }

    const validaFalla = (input, msje) => {
        const formControl = input.parentElement
        const aviso = document.getElementById("msgError");
        aviso.innerText = msje
        formControl.className = 'form-control falla'
    }
    const validaOk = (input, msje) => {
        const formControl = input.parentElement
        formControl.className = 'form-control ok'
        // enviar al index
        // location.href ='http://127.0.0.1:8000/';

    }



  })