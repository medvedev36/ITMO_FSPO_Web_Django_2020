function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}

String.prototype.format = function() {
    var a = this;
    for (var k in arguments) {
        a = a.replace("{" + k + "}", arguments[k])
    }
    return a
}

var from = getParameterByName("from");
var to = getParameterByName("to");
var date = getParameterByName("date");

var d = new Date(date);
var weekday = new Array(7);
weekday[0] = "воскресенье";
weekday[1] = "понедельник";
weekday[2] = "вторник";
weekday[3] = "среда";
weekday[4] = "четверг";
weekday[5] = "пятница";
weekday[6] = "суббота";
const ye = new Intl.DateTimeFormat('en', { year: 'numeric' }).format(d)
const mo = new Intl.DateTimeFormat('en', { month: 'short' }).format(d)
const da = new Intl.DateTimeFormat('en', { day: '2-digit' }).format(d)
var fullDate = `${da} ${mo} ${ye}`

document.getElementById("ticket-info").textContent = document.getElementById("ticket-info").textContent.format(from, to, fullDate, weekday[d.getDay()])