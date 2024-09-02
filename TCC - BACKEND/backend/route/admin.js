//carregando modulos
const express  = require("express")
const route = express.Router()
const usuarioControlle = require("../controlle/usuarioControlle")
const vailidacao = require("../controlle/vailidacao")
const login = require = require("../controlle/vailidacao")
//rotas
//route.get("/login", vailidacao.validarUsuario )

route.post("/gravar", usuarioControlle.cadastrarUsuario)

module.exports = route
