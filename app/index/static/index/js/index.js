function mouse_click(event) {
    if(false) {
        console.log()
    }
    else if (event.altKey) {
        let ho = event.currentTarget;
        event.preventDefault();
        let mo = ho.getAttribute("data-hale");
        mo += "dala/"
        window.open(mo,'_blank');
    }
    else if (event.shiftKey) {
        let ho = event.currentTarget;
        event.preventDefault();
        let mo = ho.getAttribute("data-hale")
        mo += "hapa/"
        window.open(mo,'_blank');
    }
    else if (event.ctrlKey) {
        let ho = event.currentTarget;
        event.preventDefault();
        let mo = ho.getAttribute("data-hale")
        let hepa = new RegExp('(.*)\\/(\\w*)\\/$', 'ig');
        mo = mo.replace(hepa,"$1/kara/");
        window.open(mo,'_blank');
    }
}

let as = document.querySelectorAll("a");
for(let a of as) {
    a.addEventListener("click",mouse_click);
}