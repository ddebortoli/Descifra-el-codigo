$(document).ready(function () {
    const $select = $("#miSelect");
  
    const opcionCambiada = () => {
      console.log("Cambio");
    };
  
    $select.change(opcionCambiada);
    const agregar = () => {
      const valor = new Date().getTime();
      $select.append($("<option>", {
        value: valor,
        text: valor
      }));
      loadData()
    };
  
    const limpiar = () => {
      $select.empty();
    };
  
    const mostrar = () => {
      const valor = $("#miSelect :selected").val(),
        texto = $("#miSelect :selected").text();
      alert(`Texto: ${texto}. Valor: ${valor}`);
    };
  
    $("#btnAgregar").click(agregar);
    $("#btnLimpiar").click(limpiar);
    $("#btnMostrar").click(mostrar);
  });

function loadData(){
    console.log($(".pets :selected").val())
}