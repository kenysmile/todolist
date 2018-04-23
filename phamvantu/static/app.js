$(document).ready(function() {
    $('.updateButton').on('click', function() {

        var member_id = $(this).attr('todo_id');

        var todo = $('#todoInput'+todo_id).val();
        var ngay = $('#ngayInput'+todo_id).val();

        req = $.ajax({
            url : '/update',
            type : 'POST',
            data : { todo : todo, ngay : ngay, id : todo_id }
        });
    

    });

});