const maxCounts = [358, 28, 18, 724];
const speeds = [3, 60, 100, 1];  // Масив зі швидкостями для кожного лічильника
let counters = [0, 0, 0, 0];
let intervalIds = [];

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
    
    intervalIds[index] = setInterval(() => count(index), speeds[index]);  // Використовуємо відповідну швидкість
}

document.addEventListener('DOMContentLoaded', () => {
    for (let i = 0; i < maxCounts.length; i++) {
        startCounter(i);
    }
});