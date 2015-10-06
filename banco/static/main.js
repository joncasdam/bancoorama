$(document).ready(function() {
  $("#dashboard").on("click", function (event) {
    event.preventDefault();
    $('.active').removeClass('active');
    $.ajax({
      url: '/dashboard/',
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
    $('.active').removeClass('active');
    $.ajax({
      url: '/extrato/',
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

  $("#extratoadmin").on("click", function (event) {
    event.preventDefault();
    $('.active').removeClass('active');
    $.ajax({
      url: '/extrato/',
      dataType: 'html',
      method: 'get',
      success: function(dados){
        $('#container-fluid').html(dados);
        $("#extratoadmin").parents().addClass('active');
      },
      error: function(){
        console.log('erro ao pegar extrato');
      }
    });
  });

  $("#saquesadmin").on("click", function (event) {
    event.preventDefault();
    $('.active').removeClass('active');
    $.ajax({
      url: '/extrato/',
      dataType: 'html',
      method: 'get',
      data: {'tipo': 1},
      success: function(dados){
        $('#container-fluid').html(dados);
        $("#saquesadmin").parents().addClass('active');
      },
      error: function(){
        console.log('erro ao pegar extrato');
      }
    });
  });

  $("#depositosadmin").on("click", function (event) {
    event.preventDefault();
    $('.active').removeClass('active');
    $.ajax({
      url: '/extrato/',
      dataType: 'html',
      method: 'get',
      data: {'tipo': 2},
      success: function(dados){
        $('#container-fluid').html(dados);
        $("#depositosadmin").parents().addClass('active');
      },
      error: function(){
        console.log('erro ao pegar extrato');
      }
    });
  });

  $("#listasaldos").on("click", function (event) {
    event.preventDefault();
    $('.active').removeClass('active');
    $.ajax({
      url: '/listasaldos/',
      dataType: 'html',
      method: 'get',
      success: function(dados){
        $('#container-fluid').html(dados);
        $("#listasaldos").parents().addClass('active');
      },
      error: function(){
        console.log('erro ao pegar extrato');
      }
    });
  });

  $("#saque").on("click", function (event) {
    event.preventDefault();
    $('.active').removeClass('active');
    $.ajax({
      url: '/saque/',
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

  $("#deposito").on("click", function (event) {
    event.preventDefault();
    $('.active').removeClass('active');
    $.ajax({
      url: '/deposito/',
      dataType: 'html',
      method: 'get',
      success: function(dados){
        $('#container-fluid').html(dados);
        $("#deposito").parents().addClass('active');
      },
      error: function(){
        console.log('erro no deposito');
      }
    });
  });

});

$(document).on("click", "#btSaque", function(){
    event.preventDefault();
    $.ajax({
      url: '/saque/',
      dataType: 'html',
      method: 'POST',
      data: $('form').serialize(),
      success: function(dados){
        $('#container-fluid').html(dados);
      },
      error: function(){
        console.log('erro no deposito');
      }
    });
});

$(document).on("click", "#btDeposito", function(){
    event.preventDefault();
    $.ajax({
      url: '/deposito/',
      dataType: 'html',
      method: 'POST',
      data: $('form').serialize(),
      success: function(dados){
        $('#container-fluid').html(dados);
      },
      error: function(){
        console.log('erro no deposito');
      }
    });
});