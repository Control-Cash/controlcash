function criarClienteViewCarregarCep() {
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
        inputRua.value = data.logradouro;
        inputBairro.value = data.bairro;
        inputCidade.value = data.localidade;
        inputEstado.value = data.uf;
        inputComplemento.value = data.complemento;
      });
  });
}

criarClienteViewCarregarCep();
