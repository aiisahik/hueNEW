(function($){

    $.fn.autoPaste = function() {
        this.bind('paste', function(event) {
            var self_td = this;
            event.stopPropagation();
            // determine column index
            var column_index = $(self_td).parent().children().index(self_td);
            // Short pause to wait for paste to complete
            setTimeout( function() {
                var pasted_rows = self_td.firstChild.value.split("\n");
                var currentJqueryObject = self_td;
                for (var i in pasted_rows) {
                    var arr_row = pasted_rows[i].split("\t");
                    if (arr_row.length > 0) {
                        // cycle through the remaining cells in row (including current cell)
                        $.map($(currentJqueryObject).nextAll().andSelf(), function(column_object, i) {
                            $(column_object).children().first().val(arr_row[i]);
                        })
                    }
                    // check to see if next row exists
                    if ($(currentJqueryObject).parent().next().length == 0) {
                        // add a new row
                        $(currentJqueryObject).parent().addParticipantRow();
                    }
                    // define currentJqueryObject as the same cell in the new row
                    currentJqueryObject = $(currentJqueryObject).parent().next().children()[column_index];
                }
            }, 100);
        });

        // Alternative control & paste handling - keep this in case current method has compatibility issues. 
        // var ctrlDown = false;
        // var ctrlKey = 17, vKey = 86, cKey = 67;
        // // windows 
        // $(document).keydown(function(e)
        // {
        //     if (e.metaKey || e.keyCode == ctrlKey) ctrlDown = true;
        // }).keyup(function(e)
        // {
        //     if (e.metaKey || e.keyCode == ctrlKey) ctrlDown = false;
        // });

        // $('#spreadsheet .spreadsheet-row td').keydown(function(e)
        // {

        //     if (ctrlDown && (e.keyCode == vKey || e.keyCode == cKey)){
        //         //this.firstChild.value;
        //         var self = this;
        //         // Short pause to wait for paste to complete
        //         setTimeout( function() {
        //             var text = self.firstChild.value;
        //             //$(".display").html(text);
        //         }, 100);
        //     }
        // });
        return this;
    };

    // takes textarea as input object and selects text upon click
    $.fn.focusOnClick = function() { 
        this.focus(function(e){
            $this = $(this);
            $this.select();
            $this.mouseup(function() {
                // Prevent further mouseup intervention
                $this.unbind("mouseup");
                return false;
            });
            
        });
    };

    // takes textarea as input object and adds new row upon any keypress
    $.fn.newRowOnType = function() { 
        this.keydown(function(e){
            if ($(this).parent().parent().next().length == 0) {
                // add a new row 
                $(this).parent().parent().addParticipantRow();
            }
        });
    };

    $.fn.addParticipantRow = function() {
        var t_row = _.template(t_.get('leftNav','add-participant-row'));
        // the following is a workaround because the html templating system currently does not support incomplete html snippets for some reason
        this.filter('tr').last().after($(t_row()).children().children());
        
        var new_row_object = this.parent().children().last();
        // bind the new row textarea with select on focus

        var textarea_objects = new_row_object.children().find("textarea");
        textarea_objects.focusOnClick();
        // bind the new row textarea with add new row on enter text
        textarea_objects.newRowOnType();
        // bind remove row button

        new_row_object.find("a.remove-btn").click(function(e){
            e.preventDefault();
            // if not first row
            if (new_row_object.siblings().andSelf().index(new_row_object)>1) {
                // the delete entire row if not first row
                new_row_object.remove();
            } else { 
                // if first row, remove all contents
                new_row_object.find("textarea").val("");

            }
        });
        // bind the new row with autoPaste functionality 
        setTimeout( function() {
            new_row_object.children().autoPaste();
        }, 100);
    };

})(jQuery);