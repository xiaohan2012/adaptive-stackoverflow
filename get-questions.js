var host="http://stackoverflow.com/";

var questions = $.map($(".question-summary"), function(elem){
    //get the title, tags, url
    var $elem = $(elem);

    return {
	url: host + $elem.find("a.question-hyperlink:eq(0)").attr("href"),
	title: $elem.find("a.question-hyperlink:eq(0)").text(),
	tags: $.map($elem.find(".tags a.post-tag"), function(elem){
	    return $(elem).text();
	}),
    };
});

console.log(JSON.stringify(questions));
console.log(questions.length)
