(function() {

  Window.toasts = (text) => {
    let elem = document.createElement('div');
    elem.innerHTML = text;
    elem.style.position = 'absolute';
    elem.style.top = '-500px';
    elem.style.right = '60px';
    elem.style.maxWidth = '600px';
    elem.style.padding = '20px';
    elem.style.background = '#fff';
    elem.style.fontSize = '16px';
    elem.style.boxShadow = '0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22)';
    elem.style.transition = 'top .5s';

    document.body.append(elem);

    setTimeout(() => {
      elem.style.top = '60px';
    }, 0)

    setTimeout(() => {
      elem.style.top = '-500px';
      setTimeout(() => {
        document.body.removeChild(elem);
      }, 200);
    }, 3500)
  }

})();