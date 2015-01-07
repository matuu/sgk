(function($){
    $(document).ready(function(){
        //Checkbox event handler in header table
        $("input[type=checkbox].toggle-all").change(function(){
            var check = $(this).is(':checked');
            $(".id-check").each(function(){
                $(this).prop('checked', check);
                if(check){
                  $(this).parents('tr').addClass('selected');
                }else{
                  $(this).parents('tr').removeClass('selected');
                }
            });
            if(!check){
                $('#select-all-rows').prop('checked', check);
            }
        });
        //Event handler from Individual checkbox when change status
        $("td.ids input[type=checkbox]").on('change', function(){
            var checkbox = $(this),
                tr = checkbox.parents('tr');

            if(checkbox.is(':checked')){
                tr.addClass('selected');
            }else{
              tr.removeClass('selected');
            }
            verifyAllCheckbox();
        }).change();

        $('#select-all-rows').change(function(event){
            if($(this).is(':checked')){
                if(!$('input.toggle-all').is(':checked')){
                    $('input.toggle-all').click();
                }
            }else{
                if($('input.toggle-all').is(':checked')){
                    $('input.toggle-all').click();
                }
            }
        });

        // Ask confirm actions
        //
        $("input[confirmFormAction]").click(function(e){
            e.preventDefault();
            confirmFormAction($(this));
        });
        
        $("a[confirmAction]").click(function(e){
            e.preventDefault();
            confirmAction($(this));
        });

        // Clear forms
        //
        $("#id_clearfilter").click(function(e){
            $("#selectionCustom").find('select').each(function(){
                $(this).val($(this).find("option:first").val()).change();
            });
            $("#selectionCustom").find('input').not(':button,input[type=button],input[type=submit]').each(function() {
                $(this).val("");
            });
        });

        $('div.container-overflow table tr').click(function(event) {
            if (event.target.type !== 'checkbox') {
                if(!get_jQ(event.target).is('a')){
                    $(':checkbox', this).trigger('click');
                }
            }
        });

        function collapseFilter(toogle) {
            var activeFilters = new Array(),
                idx = 0,
                titleFilter = $('#filter-title-toggle'),
                filterInfo = titleFilter.next(),
                filterFrame = $("div[class=filter-frame]");
            if (toogle) {
                filterInfo.slideToggle(400, function(){ });
                filterFrame.slideToggle(400, function () {
                    (filterFrame.is(":visible")) ? titleFilter.removeClass("collapsed") :
                        titleFilter.addClass("collapsed");
                });
            }
            location.queryString = {};
            location.search.substr(1).split("&").forEach(function (pair) {
                if (pair === "") return;
                var parts = pair.split("=");
                var value = location.queryString[parts[0]] = parts[1] &&
                    decodeURIComponent(parts[1].replace(/\+/g, " "));
                if(value != ""){
                    activeFilters[idx] = parts[0];
                    idx++;
                }
            });
            var text = getFieldFilterInfo(activeFilters);
            filterInfo.html(text);
        }

        $("#filter-title-toggle").click(function(e){
            collapseFilter(true);
        });

        // Fill the active filters indicator
        collapseFilter(false);
    });

    function verifyAllCheckbox(){
        var allCheck = true;
        $(".id-check").each(function(){
            if(!$(this).is(':checked')){
                allCheck = false;
            }
        });
        if(allCheck){
            $('input.toggle-all').prop('checked', true);
        }else{
            $('input.toggle-all').prop('checked', false);
            $('input#select-all-rows').prop('checked', false);
        }
    }

    function getFieldFilterInfo(fields){
        var text = "Filtros activos: ",
            textArray = new Array(),
            index = 0;
        if(fields.length == 0) return "Ningún filtro activo."
        for(var idx in fields){
            var help_text = $("[name="+ fields[idx]+"]")
                .parents(".filter-field")
                .children(".collapse-field-info")
                .html().trim();
            if(textArray.indexOf(help_text) == -1){
                textArray[index] = help_text;
                text += " <b>"+ help_text + "</b>,";
            }
        }
        text = text.substr(0, text.length-1) + ".";
        return text;
    }

})(jQuery);


//Requires mdialog https://github.com/matuu/mdialog
//Elem is a Element HTML with msg and url attributes.
//<a href="#" url="editar/2" msg="Se va a editar el ítem 2." onclick="confirmAction(this);" >Editar</a>
function confirmAction(elem){
    var mconfirm = new mDialogConfirm({
        title: '¿Desea continuar?',
            message: get_jQ(elem).attr('msg'),
            yes: function() {
            window.location = get_jQ(elem).attr('url') ;
            }
        }
    ).show();
}

//Requires mdialog https://github.com/matuu/mdialog
//Elem is a Element HTML with 'msg' and 'form_name' attributes.
//<input msg="Se enviará el formulario." form_name="form1" onclick="confirmFormAction(this);" value="Ok" />
function confirmFormAction(elem){
    var mconfirm = new mDialogConfirm({
            title: '¿Desea continuar?',
            message: get_jQ(elem).attr('msg'),
            yes: function() {
                form = get_jQ(elem).attr('form_name');
                document.forms[form].submit();
            }
        }
    ).show();
}

function get_jQ(elem){
    if(elem instanceof jQuery){
        return elem;
    }
    return $(elem);
}

