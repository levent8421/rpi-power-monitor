$(function () {
    function setPinValue(id, value) {
        const postData = JSON.stringify({id: id, value: value});
        $.ajax({
            url: '/panel/out-pin/value',
            type: 'post',
            data: postData,
            contentType: 'application/json',
            success: function (res) {
                window.showMessage('Set value success,' + res.data)
            }
        });
    }

    $('.sub-power-switch').bootstrapSwitch({
        state: true,
        onText: "ON",
        offText: "OFF",
        onColor: "success",
        offColor: "info",
        size: "large",
        onSwitchChange: function (event, state) {
            const id = $(this).attr('data-id');
            setPinValue(id, state)
        }
    });

    function setMainPowerStatus(value) {
        $.ajax({
            url: '/panel/main-power/value',
            type: 'post',
            data: JSON.stringify({value: value}),
            contentType: 'application/json',
            success: function (res) {
                if (res.code === 200) {
                    showMessage('Set main power value success!');
                } else {
                    showMessage('Set main power value error!' + res.msg);
                }
            }
        });
    }

    $.ajax({
        url: '/panel/main-power/',
        type: 'get',
        success: function (res) {
            if (res.code === 200) {
                $('#main-power-switch').bootstrapSwitch({
                    state: res.data.value,
                    onText: "ON",
                    offText: "OFF",
                    onColor: "success",
                    offColor: "info",
                    size: "large",
                    onSwitchChange: function (event, state) {
                        setMainPowerStatus(state);
                    }
                });
            } else {
                window.showMessage('Error on get mai power status!');
            }
        }
    });


});