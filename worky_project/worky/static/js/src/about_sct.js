const maxCounts = [358, 28, 18, 724];
const speeds = [3, 60, 100, 1];
let counters = [0, 0, 0, 0];
let intervalIds = [];

const yellowBlockAbout = document.getElementById("yellow_block_about");
const topPositionYellowBlockAbout = yellowBlockAbout.offsetTop;

function count(index) {
    counters[index]++;
    document.getElementById(`counter${index + 1}`).innerHTML = counters[index];

    if (counters[index] === maxCounts[index]) {
        clearInterval(intervalIds[index]);
    }
}

function startCounter(index) {
    clearInterval(intervalIds[index]);
    counters[index] = 0;
    document.getElementById(`counter${index + 1}`).innerHTML = counters[index];
    
    intervalIds[index] = setInterval(() => count(index), speeds[index]);
}

document.addEventListener('DOMContentLoaded', () => {
    let countersStarted = false;

    window.addEventListener('scroll', () => {
        if (!countersStarted && window.innerHeight + window.scrollY >= topPositionYellowBlockAbout) {
            for (let i = 0; i < maxCounts.length; i++) {
                startCounter(i);
            }
            countersStarted = true;  // Встановлюємо флаг, щоб лічильники не запускались знову
        }
    });
});
