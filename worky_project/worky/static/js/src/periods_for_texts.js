document.addEventListener("DOMContentLoaded", function() {
    var postsTexts = document.getElementsByClassName("post_text");
    for(var i = 0; i < postsTexts.length; i++){
        var postText = postsTexts[i].textContent;
        var words = postText.split(" ");
        if (words.length > 48) {
            var limitedText = words.slice(0, 48).join(" ");
            var newText = limitedText + "...";
            postsTexts[i].innerHTML = newText;
        }
    }
});