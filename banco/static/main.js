console.log('aqui!');

$(document).ready(function() {
  $("#extrato").on("click", function (event) {
    event.preventDefault();
    $('.active').removeClass('active')
    $.ajax({
      url: '/extrato',
      dataType: 'html',
      method: 'get',
      success: function(dados){
        $('#container-fluid').html(dados);
        $("#extrato").parents().addClass('active');
      },
      error: function(){
        console.log('erro ao pegar extrato');
      }
    });
  });
});