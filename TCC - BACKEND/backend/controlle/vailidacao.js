const {body, validationResult } =require("express-validator")
const Usuario = require("../model/Usuarios")

/*module.exports = { 
    async validarUsuario(request, response) {
        const (usuario) = new usuario(request.body)
        body(usuario).isEmail().notEmpty
        const resultado = validationResult(req)
        if (resultado.isEmpty() ) {
            return res.send(req.body.person)
        }
        res.send({ errors: resultado.array()})
    } 
}*/