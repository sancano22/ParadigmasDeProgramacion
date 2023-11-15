const ctx = document.getElementById('myChart');
datos=[];
url="http://127.0.0.1:5000/estadisticos";
$.ajax({
    contentType: "application/json",
    type: "GET",
    url:url,
})
.done(function( data, textStatus, jqXHR ) {
   //console.log();
   datos=data;
   new Chart(ctx, {
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
  });
});
