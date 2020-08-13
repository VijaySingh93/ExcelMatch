function highlight(newElem, oldElem) {
    var oldText = oldElem.text(),
        text = '';
    newElem.text().split('').forEach(function(val, i) {
        if (val != oldText.charAt(i))
            text += "<span class='highlight'>" + val + "</span>";
        else
            text += val;
    });
    newElem.html(text);
}