$(document).ready(function() {

  $("#hide").click(function(){
    $("#show").show()
    $("#hide").hide()
  })
  // $("#send").submit(function(event) {
  //   event.preventDefault()
  //   form=$("#send")
  //
  //   $.ajax({
  //     'url':'/ajax/review/',
  //     'type':'POST',
  //     'data':form.serialize(),
  //     'dataType':'json',
  //     'success':function(data) {
  //       $("#alert").text(data['success'])
  //
  //     },
  //
  //   })
  //   $(".form").hide()
  //   $("#alert").show()
  //
  //
  // })

})
