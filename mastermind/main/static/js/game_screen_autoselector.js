let doubleColorsEnabled = false;
let currentAmountOfColorsNode = document.querySelector(".amount-of-colors-container input[checked]");
let currentAmountOfPinsNode = document.querySelector(".amount-of-pins-container input[checked]");
const doubleColors = document.querySelectorAll(".doubleColorOption");
doubleColors.forEach(node => {
    node.addEventListener("click", e => {
        doubleColorsEnabled = e.currentTarget.value != 0;
        this.handleChange();
    });
});

const amountOfColorsClickable = document.querySelectorAll(".amount-of-colors-container .amountOfColorsOption");
amountOfColorsClickable.forEach(node => {
    node.addEventListener("click", e => {
        currentAmountOfColorsNode = e.currentTarget;
        this.handleChange();
    });
});

document.querySelectorAll(".amount-of-pins-container .amountOfPins").forEach(node => {
    node.addEventListener("click", e => {
        currentAmountOfPinsNode = e.currentTarget;
        this.handleChange();
    });
});

handleChange = () => {
    if(doubleColorsEnabled) {
        return;
    }

    const colors = parseInt(currentAmountOfColorsNode.value);
    const pins = parseInt(currentAmountOfPinsNode.value);

    if(colors < pins) {
        for(let i = 0; i < amountOfColorsClickable.length; i++) {
            if(parseInt(amountOfColorsClickable[i].value) === pins) {
                amountOfColorsClickable[i].checked = true
                currentAmountOfColorsNode = amountOfColorsClickable[i];
            }
        }
    }
}
