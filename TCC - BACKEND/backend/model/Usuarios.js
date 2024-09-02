const conectar = require("../database/conexao")//modulo de conexão
const {body, validationResult } =require("express-validator")

class Usuarios {
    constructor({nome, nascimento, telefone, email, senha}) {
        this.nome = nome;
        this.nascimento = nascimento;
        this.telefone = telefone;
        this.email = email
        this.senha = senha
    
    }
  
async cadastrar() {
    try {
      const [cadastro] = await conectar("usuario")
      .insert({
          nome: this.nome,
          nascimento: this.nascimento,
          telefone: this.telefone,
          email: this.email,
          senha: this.senha
        })
        .returning("nome" , "telefone", "nascimento", "email", "senha");
      return cadastro;
    } 
    catch (error) {
      return error;
    } finally {
      conectar.destroy;
    }
  }
}
module.exports = Usuarios;