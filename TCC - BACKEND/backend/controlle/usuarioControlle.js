const Usuario = require("../model/Usuarios.js") // OBRIGADO DEUS POR FAZER FUNCIONAR, MESMO NAO SABENDO COMO, MESMO DANDO "ERRO" EU SEI QUE FUNCIONOU GRAÇAS A VOCE E NUNA NA VIDA VOU SABER COMO ESSE MILAGRE ACONTECEU 
//modulo de conexao

//modulo de validaçao
module.exports = {
async cadastrarUsuario(request, response) {
    const Usuario = new Usuario(request.body)
    const validar = await usuario.cadastrar()

    return response.json(validar)}
}
//modulo de inserçao
module.exports = {
    async cadastrarUsuario(request, response) {
        const usuario = new Usuario(request.body)
        const cadastrar = await usuario.cadastrar()

        return response.json(cadastrar)
    }}