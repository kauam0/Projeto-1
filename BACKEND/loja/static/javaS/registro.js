const cep = document.querySelector('#cep');
const address = document.querySelector('#address'); // Corrigido para #address
const bairro = document.querySelector('#bairro');
const cidade = document.querySelector('#cidade');
const message = document.querySelector('#message');

cep.addEventListener('focusout', async () => {
    const onlyNumbers = /^[0-9]+$/;
    const cepValid = /^[0-9]{8}$/;

    try {
        if (!onlyNumbers.test(cep.value) || !cepValid.test(cep.value)) {
            throw { cep_error: 'CEP inválido' };
        }

        const response = await fetch(`https://viacep.com.br/ws/${cep.value}/json/`);
        
        if (!response.ok) {
            throw new Error('Erro ao buscar o CEP');
        }

        const responseCep = await response.json();

        if (responseCep.erro) {
            throw { cep_error: 'CEP não encontrado' };
        }

        address.value = responseCep.logradouro;
        bairro.value = responseCep.bairro;
        cidade.value = responseCep.localidade;

    } catch (error) {
        if (error?.cep_error) {
            message.textContent = error.cep_error;
            setTimeout(() => {
                message.textContent = '';
            }, 5000);
        } else {
            console.error(error);
        }
    }
});
