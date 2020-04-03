 class DragAndDropService {
    /**
     * Constructor
     */
    constructor() {
        this.element = null;
        this.dragZones = [];
        this.dragStarted = false;
        this.double_colors_enabled = false;

        fetch("/api/double_colors_enabled").then(data => data.json()).then(data => this.double_colors_enabled = data.double_colors_enabled)

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
        for(const dragZone of this.dragZones) {
            dragZone.classList.add("drag-zone-delete");
        }
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
            console.log(this.double_colors_enabled);
            if(this.double_colors_enabled) {
                this.element = e.target.cloneNode(true);
                this._applyDraggableEvents(this.element);
            } else {
                this.element = e.target;
            }
        }
        e.dataTransfer.setData("text", e.target.id);

        for(const dragZone of this.dragZones) {
            dragZone.classList.add("drag-zone-delete");
        }
    }

    /**
     * Method that is called when the dragend event is called.
     * @param e
     * @private
     */
    _dragEnd() {
        for(const dragZone of this.dragZones) {
            dragZone.classList.remove("drag-zone-delete");
        }
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
            e.target.append(this.element);
            this.audio.play();
        }

        if(e.target.classList.contains("dragZone") && this.element !== null) {
            this.element.remove();

            for(const dragZone of this.dragZones) {
                dragZone.classList.remove("drag-zone-delete");
            }
        }

        this.element = null;
    }
}

new DragAndDropService();