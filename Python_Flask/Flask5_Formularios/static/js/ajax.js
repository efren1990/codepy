$(document).ready(function(){
	console.log("Ajax desde python y flask")
	// Funcion para envio del ajax
	function ajax_login(){
		$.ajax({
			type:'POST',
			url:'/ajax-login',//ruta que debe ser generada en el servidor flask-python
			data:$("#form-log").serialize(),
			dataType:'json',//Los datos de cada campo se traeran por los nombres asignados en la clase FormularioLoguin
			success:function(response){
				alert(response.user);
			},
			error:function(error){
				console.log(error);
			}	
		});
	}
	// Evitar el envio del formulario
	$("#form-logs").submit(function(event){
		// Cancelar el evento por default de envio
		event.preventDefault();
		// Ejecutar Funcion De ajax 
		ajax_login();
	});
});
