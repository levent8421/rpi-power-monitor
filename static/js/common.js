$(function () {
    window.topMessage = $('#top-message');

    function showMessage(msg) {
        topMessage.text(msg);
        topMessage.slideDown(100);
        setTimeout(function () {
            topMessage.slideUp(100);
        }, 2000);
    }

    window.showMessage = showMessage;
});

