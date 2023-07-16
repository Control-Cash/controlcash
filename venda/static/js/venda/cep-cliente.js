function carregarCep() {
  const inputCEP = document.getElementById('id_cep');
  const inputRua = document.getElementById('id_rua');
  const inputBairro = document.getElementById('id_bairro');
  const inputCidade = document.getElementById('id_cidade');
  const inputEstado = document.getElementById('id_estado');
  const inputComplemento = document.getElementById('id_complemento');

  inputCEP.addEventListener('blur', (e) => {
    const url = `https://viacep.com.br/ws/${e.target.value}/json/`;
    fetch(url)
      .then((res) => res.json())
      .then((data) => {
        if (!data.erro) {
          inputRua.value = data.logradouro || inputRua.value;
          inputBairro.value = data.bairro || inputBairro.value;
          inputCidade.value = data.localidade || inputCidade.value;
          inputEstado.value = data.uf || inputEstado.value;
          inputComplemento.value = data.complemento || inputComplemento.value;
        }
      });
  });
}

carregarCep();
