// Importar utils como módulo JS

$("#idCiudadAdopcion").click(function(){
    $.get("https://apis.digital.gob.cl/dpa/comunas",
        function(data){
            $.each(data.nombre, function(i,item){
                let htmlCiudades = `<option>Quilpué</option>`;
                $("#containerCiudades").append(htmlCiudades);
            });

    });
});

//Utilizar ajax call para traer todas las comunas
$.ajax({
    url: "https://apis.digital.gob.cl/dpa/comunas",
    success: function (response) {
        // aquí ya tienes los datos en response
    },
    error:function(response){
        //aquí manejas un error.
    }
});