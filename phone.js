window.setInterval(function(){
    var refreshHours = new Date().getHours();
    var refreshMin = new Date().getMinutes();
    var refreshSec = new Date().getSeconds();
    if(refreshHours=='11' && refreshMin=='55' && refreshSec=='0'){
        a = function click(){
        for (var i=0;i<2 ;i++){
        var bt=document.getElementById('submitOrderId');
        bt.click()
        }
        };
        setInterval(a,500)
    }
}, 1000);
