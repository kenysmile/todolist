$(document).ready(function() {
    $(document).on('click','.updateButton', function() {
    // $('.updateButton').on('click', function() {

        var todo_id = $(this).attr('todo_id');

        var todo = $('#todoInput'+todo_id).val();
        var ngay = $('#ngayInput'+todo_id).val();

        req = $.ajax({
            url : '/update',
            type : 'POST',
            data : { todo : todo, ngay : ngay, id : todo_id },
            
        }).done(function(data) {
            $('#todoSection'+todo_id).html(data)
        });
    

    });

});