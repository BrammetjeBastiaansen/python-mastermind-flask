function includeJs(jsFilePath) {
    const js = document.createElement("script");
    js.type = "text/javascript";
    js.src = jsFilePath;
    js.defer = true;

    document.querySelector("head").appendChild(js);
}

includeJs("main/static/js/bootstrap/modal.js");