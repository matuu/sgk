function addFileInputIntoDiv(count, div){
    // Function that add a input file into a div.
    // count is a input hidden with a index and attr 'field-name' with the name of field of form.
    // div is a div element
  var fieldname = $(count).attr('field_name');
  var idx = parseInt($(count).val()) + 1;
  $(div).append("<div class='form-row'><label for='id_form-"+idx+"-"+fieldname+"'>Archivo:</label> <input id='id_form-"+idx+"-"+fieldname+"' name='form-"+idx+"-"+fieldname+"' type='file' /></div>");
  $(count).val(idx);
  // update the TOTAL forms
  $("#id_form-TOTAL_FORMS").val(idx+1);
}
