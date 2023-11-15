let grafica;
const url="http://127.0.0.1:5000/estadisticos";
$("#boton1").on("click",function(){
     $("#grafico1").css("display","block");

    const ctx = document.getElementById('myChart');
    datos=[];
    $.ajax({
        contentType: "application/json",
        type: "GET",
        url:url,
    })
    .done(function( data, textStatus, jqXHR ) {
     datos=data;
     configuracion={
            type: 'bar',
            data: {
              labels: ['Benigno', 'Maligno','sinDiagnostico'],
              datasets: [{
                label: 'Personas con tumor',
                data: [data[0]["benigno"], data[0]["maligno"],data[0]["sinDiagnostico"]],
                borderWidth: 1
              }]
            },
            options: {
              scales: {
                y: {
                  beginAtZero: true
                }
              }
            }
        }
        if (grafica) grafica.destroy();
        
        grafica=new Chart(ctx, configuracion);
    });
});

$("#genero").on("change",function(){
  $.ajax({
      contentType: "application/json",
      type: "POST",
      dataType: "json",
      data:JSON.stringify({"genero":$(this).find(":selected").text()}),
      url: url,
  }).done(function( data, textStatus, jqXHR ) {
    const ctx = document.getElementById('myChart');
    datos=data;
    configuracion={
           type: 'bar',
           data: {
             labels: ['Benigno', 'Maligno','sinDiagnostico'],
             datasets: [{
               label: 'Personas con tumor',
               data: [data[0]["benigno"], data[0]["maligno"],data[0]["sinDiagnostico"]],
               borderWidth: 1
             }]
           },
           options: {
             scales: {
               y: {
                 beginAtZero: true
               }
             }
           }
       }
       if (grafica) grafica.destroy();
       
       grafica=new Chart(ctx, configuracion);
   
 })
    

     
});
