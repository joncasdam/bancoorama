$(document).ready(function() {
  $("#dashboard").on("click", function (event) {
    event.preventDefault();
    $('.active').removeClass('active')
    $.ajax({
      url: '/dashboard',
      dataType: 'html',
      method: 'get',
      success: function(dados){
        $('#container-fluid').html(dados);
        $("#dashboard").parents().addClass('active');
        console.log('dash');
      },
      error: function(){
        console.log('erro no dashboard');
      }
    });
  });

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

  $("#saque").on("click", function (event) {
    event.preventDefault();
    $('.active').removeClass('active')
    $.ajax({
      url: '/saque',
      dataType: 'html',
      method: 'get',
      success: function(dados){
        $('#container-fluid').html(dados);
        $("#saque").parents().addClass('active');
      },
      error: function(){
        console.log('erro ao pegar extrato');
      }
    });
  });
});