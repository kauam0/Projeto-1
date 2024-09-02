function process_geral(quant, indice){ 
    const todosProdutos = document.getElementsByClassName('produto_qnt_princ');
    
    var i,len;
    var produtoFiltrado; 

        for (i = 0,len=todosProdutos.length;i<len; i++) {
            //console.log(todosProdutos[i].getAttribute('data-product'));
            if (todosProdutos[i].getAttribute('data-product') === indice) {
                //console.log(todosProdutos[i].getAttribute('data-product'));
                produtoFiltrado = todosProdutos[i];
            }
        }
    
    var classValue = parseInt(produtoFiltrado.querySelector('input.quanti').value);
    classValue+=quant; 

    if(classValue < 1){
        produtoFiltrado.querySelector("input.quanti").value = 1;
    }else{  
        produtoFiltrado.querySelector("input.quanti").value = classValue;     
    } 
        const preco = parseInt( document.getElementById("precoo").value);
        const quantidade = parseInt(produtoFiltrado.querySelector('input.quanti').value);
        const valorTotal = preco * quantidade;
        document.getElementById("resultado").innerHTML = ` R$ ${valorTotal}`;
        
}    