function includeJs(jsFilePath) {
    const js = document.createElement("script");
    js.type = "text/javascript";
    js.src = jsFilePath;
    js.defer = true;

    document.querySelector("head").appendChild(js);
}

includeJs("main/static/js/game_screen_autoselector.js");
includeJs("main/static/js/drag_and_drop.js");
