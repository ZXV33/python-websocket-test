$(function(){
    var socket = io('http://localhost:5000');
    $("form").submit(function(e){
        e.preventDefault();
        socket.emit('msg', $("#msg").val());
        $("#msg").val("");
        return false;
    });
    socket.on('msg', function(msg){
        $('#message').append($("<li>").text(msg));
    })
})