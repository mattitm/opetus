var oikeaVastaus;
var virhe = 0;

function haeSanapari() {
	var vastaus = parseInt($("#kieli").val());
	var kysymys = 1 - vastaus;
	$.getJSON( '/api/sanapari', function( sanapari ) {
		if (sanapari.length == 2) {
			virhe = 0;
			oikeaVastaus = sanapari[vastaus];
			$("label[for='kysely']").text(sanapari[kysymys]);
			$("#kysely").val('').trigger('change');
		} else {
			alert('Virhe sanaparissa');
		}
	}).fail(function() {
		alert('Virhe haettaessa sanaparia');
	});
}

$(document).ready(function(){
	haeSanapari();
	$("#oikein").hide();
	$("#tarkista").submit(function( event ) {
		event.preventDefault();
		if ($("#kysely").val() == oikeaVastaus) {
			if (virhe < 3) {
				$("#oikein").show();
			}
			haeSanapari();
		} else {
			$("#oikein").hide();
			if (++virhe > 2) {
				$("#kysely").val(oikeaVastaus).trigger('change');
			}
		}
	});
	$("#kieli").change(function() {
		haeSanapari();
	});
	$("#kysely").keyup(function() {
		if(this.value.length > 0) {
			$("#oikein").hide();
		}
	});
});