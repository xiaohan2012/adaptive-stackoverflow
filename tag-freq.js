//Chrome and F12, copy&pasta and enter! you get the idea

JSON.stringify($.map($(".post-tag"), function(v,i){
    var v= $(v);
    var freq=v.next(".item-multiplier").children(".item-multiplier-count").text();
    return {name: v.text(), freq: freq && parseInt(freq) || 1};
}))
