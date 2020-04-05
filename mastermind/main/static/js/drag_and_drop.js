 class DragAndDropService {
    /**
     * Constructor
     */
    constructor() {
        this.element = null;
        this.dragStarted = false;
        this.double_colors_enabled = false;
        this.amount_of_positions = 4;

        fetch("/api/game/data").then(data => data.json()).then(data => {
            this.double_colors_enabled = data.double_colors_enabled;
            this.amount_of_positions = data.amount_of_positions;
        });

        /**
         * Get draggable nodes
         * @type {NodeListOf<Element>}
         */
        this.draggableNodes = document.querySelectorAll(".draggable");

        /**
         * Get drop zone nodes
         * @type {NodeListOf<Element>}
         */
        this.dropZoneNodes = document.querySelectorAll(".dropZone");

        /**
         * Get dragZone node
         * @type {Element}
         */
        this.dragZone = document.querySelector(".dragZone")

        /**
         * Get colors container
         * @type {Element}
         */
        this.colors_container = document.querySelector(".colors");

        /**
         * Get apply button
         * @type {Element}
         */
        this.button = document.querySelector("#game-apply-button");

        /**
         * Get game form
         * @type {Element}
         */
        this.form = document.querySelector("#game-form");

        /**
         * Add event listeners to draggable nodes
         */
        this.draggableNodes.forEach(node => {
            this._applyDraggableEvents(node);
        });

        /**
         * Add event listeners to dropZone nodes
         */
        this.dropZoneNodes.forEach(node => {
            this._applyDropZoneEvents(node);
        });

        /**
         * Add event listener to dragZone
         */
        this._applyDropZoneEvents(this.dragZone);

        /**
         * Set button event listeners
         */

        this.button.addEventListener("click", e => {
            e.preventDefault();
            this.button.disabled = true;
            this.form.submit();
        })

        /**
         * Audio that will be played whenever a drop occurs.
         * @type {HTMLAudioElement}
         */
        this.audio = new Audio("/main/static/sound/BlOOP.mp3");
    }
    /**
     * Method to provide the passed node with event listeners.
     * @param node
     * @private
     */
    _applyDropZoneEvents(node) {
        node.addEventListener("dragover", e => this._dragOver(e));
        node.addEventListener("dragenter", e => this._dragEnter(e));
        node.addEventListener("dragleave", e => this._dragLeave(e));
        node.addEventListener("drop", e => this._dragDrop(e));
    }

        /**
     * Method to add draggable event listeners.
     * @param node
     * @private
     */
    _applyDraggableEvents(node) {
        node.addEventListener("dragstart", e => this._dragStart(e));
        node.addEventListener("dragend", e => this._dragEnd(e));
    }

    /**
     * Method that is called when the dragover event is called.
     * @param e
     * @private
     */
    _dragOver(e) {
        e.preventDefault();
        this.dragZone.classList.add("drag-zone-delete");
    }

    /**
     * Method that is called when the dragenter event is called.
     * @param e
     * @private
     */
    _dragEnter(e) {
        e.preventDefault();
    }

    /**
     * Method that is called when the dragleave event is called.
     * @private
     */
    _dragLeave() {
        // Empty
    }

    /**
     * Method that is called when the dragstart event is called.
     * @param e
     * @private
     */
    _dragStart(e) {
        // We use this check te prevent the issue that multiple
        // Event handlers are attached to the copied element.
        if(this.dragStarted) {
            return;
        }

        this.dragStarted = true;

        if(e.target.parentElement.classList.contains("dropZone")) {
            this.element = e.target;
        } else {
            if(this.double_colors_enabled) {
                this.element = e.target.cloneNode(true);
                this._applyDraggableEvents(this.element);
            } else {
                this.element = e.target;
            }
        }
        e.dataTransfer.setData("text", e.target.id);

        this.dragZone.classList.add("drag-zone-delete");
    }

    /**
     * Method that is called when the dragend event is called.
     * @param e
     * @private
     */
    _dragEnd() {
        this.dragZone.classList.remove("drag-zone-delete");
        this.dragStarted = false;
    }

    /**
     * Method that is called when the drop event is called.
     * @param e
     * @private
     */
    _dragDrop(e) {
        e.preventDefault();

        if(e.target.classList.contains("dropZone") && this.element !== null) {
            if(e.target.attributes.disabled.value !== "false") {
                return;
            }
            this.element.name = `dragged`;

            e.target.append(this.element);
            this.audio.play();
        }

        if(e.target.classList.contains("dragZone") && this.element !== null) {
            if(this.double_colors_enabled) {
                this.element.remove();
                this.dragZone.classList.remove("drag-zone-delete");
            } else {
                this.colors_container.append(this.element)
                this.element.name = `draggable`;
            }
        }
        this._toggleSubmitButton();
        this.element = null;
    }

    _toggleSubmitButton() {
        const draggedColors = document.querySelectorAll("input[name='dragged']");

        if(!this.button || !draggedColors) {
            return
        }

        this.button.disabled = draggedColors.length !== this.amount_of_positions;
    }
}

new DragAndDropService();