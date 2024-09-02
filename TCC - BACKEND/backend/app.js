//carregando modulos
const express = require("express")
const app = express()
const admin = require("./route/admin")

//configuração

app.use(express.urlencoded({extended: true}))
//sessao


//middleware

    //rotas
app.use("/admin", admin )

    app.listen(8080, function(){
    console.log("servidor rodando")

    })


