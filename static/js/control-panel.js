$(function () {
    $('#main-power-switch').bootstrapSwitch({
        state: true,
        onText: "ON",
        offText: "OFF",
        onColor: "success",
        offColor: "info",
        size: "large",
        onSwitchChange: function (event, state) {
            if (state === true) {
                console.log("开启");
            } else {
                console.log("关闭");
            }
        }
    });
});