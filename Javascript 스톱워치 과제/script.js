const watch = document.getElementById("watch");
let timer = null;
let startTime = 0;
let runningTime = 0;
let Running = false;

function start() {
    if(!Running){
        startTime = Date.now() - runningTime;
        timer = setInterval(update, 10);
        Running = true;
    }
}
function deletebtn() {
    const containers = document.querySelectorAll('.records div');
    containers.forEach(container => {
        const checkbox = container.querySelector('.record-checkbox');
        if (checkbox.checked) {
            container.remove();
        }
    });
}
function stop() {
    if(Running){
        const record = document.querySelector(".records");
        const p = document.createElement("div");

        let seconds = Math.floor(runningTime / 1000 % 60);
        let milliseconds = Math.floor(runningTime % 1000 / 10);

        seconds = String(seconds).padStart(2, "0");
        milliseconds = String(milliseconds).padStart(2, "0");

        p.innerHTML = `<input type="checkbox" class="record-checkbox"> ${seconds}:${milliseconds}`;
        record.appendChild(p);

        clearInterval(timer);
        runningTime = Date.now() - startTime;
        Running = false;
    }
}
function reset(){
    clearInterval(timer);
    startTime = 0;
    runningTime = 0;
    Running = false;

    watch.textContent = `00:00`;
}
function update() {
    const currentTime = Date.now();
    runningTime = currentTime - startTime;

    let hours = Math.floor(runningTime / (1000 * 60 * 60));
    let minutes = Math.floor(runningTime / (1000 * 60) % 60);
    let seconds = Math.floor(runningTime / 1000 % 60);
    let milliseconds = Math.floor(runningTime % 1000 / 10);

    seconds = String(seconds).padStart(2, "0");
    milliseconds = String(milliseconds).padStart(2, "0");

    watch.textContent = `${seconds}:${milliseconds}`;
}