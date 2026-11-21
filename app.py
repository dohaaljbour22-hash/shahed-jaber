
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Pink XO",
    page_icon="♡",
    layout="centered"
)

html = """
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');

* {
    box-sizing: border-box;
}

html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    font-family: 'Cairo', sans-serif;
    background: transparent;
    color: #704568;
}

.game {
    width: 100%;
    max-width: 480px;
    margin: 15px auto;
    padding: 25px 18px;
    text-align: center;
    border-radius: 28px;
    background: linear-gradient(145deg, #fff0f7, #f2e5ff);
    border: 2px solid #ffffff;
    box-shadow: 0 10px 35px #d9a9ce55;
    position: relative;
    overflow: hidden;
}

.decor {
    color: #d99acb;
    font-size: 23px;
    letter-spacing: 12px;
    margin-bottom: 5px;
}

h1 {
    color: #b65c9e;
    font-size: 43px;
    margin: 0;
    font-weight: 800;
    letter-spacing: 5px;
}

.subtitle {
    color: #a77b9e;
    font-size: 15px;
    margin: 5px 0 22px;
}

/* خيارات اللعب بالنص */
.modes {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 12px;
    margin: 25px auto;
    flex-wrap: wrap;
}

.mode-btn {
    border: 2px solid #e6b6d8;
    background: #fff8fc;
    color: #a65391;
    padding: 13px 17px;
    border-radius: 16px;
    font-family: inherit;
    font-size: 15px;
    font-weight: 700;
    cursor: pointer;
    transition: .2s;
}

.mode-btn:hover,
.mode-btn.active {
    background: #d98bc2;
    color: white;
    transform: translateY(-2px);
}

.status {
    background: #ffffffb8;
    border-radius: 15px;
    padding: 12px;
    margin: 15px 0;
    font-size: 17px;
    font-weight: 700;
    color: #9e5791;
}

/* لوحة اللعب: 3 أعمدة ثابتة حتى على الهاتف */
.board {
    display: grid !important;
    grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
    grid-template-rows: repeat(3, auto);
    gap: 10px;
    width: 100%;
    max-width: 330px;
    margin: 20px auto;
}

.cell {
    width: 100%;
    min-width: 0;
    aspect-ratio: 1 / 1;
    border: 2px solid #e8b8d9;
    border-radius: 18px;
    background: #fffafd;
    color: #bd6ca9;
    font-family: inherit;
    font-size: clamp(35px, 11vw, 55px);
    font-weight: 800;
    cursor: pointer;
    box-shadow: 0 4px 8px #d8a9ce35;
    transition: .2s;
}

.cell:hover {
    background: #fce6f5;
    transform: scale(1.03);
}

.cell.x {
    color: #bd69aa;
}

.cell.o {
    color: #8e78c8;
}

.cell:disabled {
    cursor: default;
}

/* زر لعبة جديدة بدون أيقونة */
.new-btn {
    border: none;
    border-radius: 14px;
    padding: 12px 25px;
    margin: 7px 4px;
    font-family: inherit;
    font-size: 15px;
    font-weight: 700;
    cursor: pointer;
    background: linear-gradient(135deg, #d985bd, #ae78c9);
    color: white;
    box-shadow: 0 5px 12px #c98aba55;
}

.music-btn {
    background: #fff;
    color: #a85c98;
    border: 1px solid #e6b6d8;
    border-radius: 14px;
    padding: 12px 25px;
    margin: 7px 4px;
    font-family: inherit;
    font-size: 15px;
    font-weight: 700;
    cursor: pointer;
}

.footer {
    margin-top: 25px;
    color: #a76c9b;
    font-size: 13px;
    letter-spacing: 1px;
}

.hidden {
    display: none;
}

/* ضبط الشكل على شاشات الهاتف */
@media(max-width: 380px) {
    .game {
        padding: 20px 12px;
    }

    .board {
        gap: 7px;
        max-width: 100%;
    }

    .mode-btn {
        padding: 11px 12px;
        font-size: 13px;
    }
}
</style>
</head>

<body>

<div class="game">

    <div class="decor">♡ ✿ ♡ ✿ ♡</div>

    <h1>XO</h1>

    <div class="subtitle">Let's play together ♡</div>

    <div class="modes" id="modes">
        <button class="mode-btn" onclick="startGame('two', this)">
            لعبة ثنائية
        </button>

        <button class="mode-btn" onclick="startGame('computer', this)">
            لعبة ضد الكمبيوتر
        </button>
    </div>

    <div id="gameArea" class="hidden">

        <div class="status" id="status">
            دور اللاعب X
        </div>

        <div class="board" id="board">
            <button class="cell" onclick="play(0)"></button>
            <button class="cell" onclick="play(1)"></button>
            <button class="cell" onclick="play(2)"></button>
            <button class="cell" onclick="play(3)"></button>
            <button class="cell" onclick="play(4)"></button>
            <button class="cell" onclick="play(5)"></button>
            <button class="cell" onclick="play(6)"></button>
            <button class="cell" onclick="play(7)"></button>
            <button class="cell" onclick="play(8)"></button>
        </div>

        <button class="new-btn" onclick="resetGame()">
            لعبة جديدة
        </button>

        <br>

        <button class="music-btn" onclick="toggleMusic()" id="musicBtn">
            ♫ تشغيل الموسيقى
        </button>

    </div>

    <div class="footer">
        Made with love ♡ Shahed Jaber
    </div>

</div>

<script>

let board = ["","","","","","","","",""];
let current = "X";
let mode = "two";
let finished = false;

const wins = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
];

let audioContext = null;
let musicTimer = null;
let musicOn = false;
let noteIndex = 0;


/* المؤثرات الصوتية */

function sound(frequency, duration=0.16, type="sine", volume=0.07) {

    try {

        audioContext = audioContext ||
            new (window.AudioContext || window.webkitAudioContext)();

        if (audioContext.state === "suspended") {
            audioContext.resume();
        }

        const oscillator = audioContext.createOscillator();
        const gain = audioContext.createGain();

        oscillator.type = type;
        oscillator.frequency.value = frequency;

        gain.gain.setValueAtTime(
            volume,
            audioContext.currentTime
        );

        gain.gain.exponentialRampToValueAtTime(
            0.001,
            audioContext.currentTime + duration
        );

        oscillator.connect(gain);
        gain.connect(audioContext.destination);

        oscillator.start();
        oscillator.stop(audioContext.currentTime + duration);

    } catch(e) {}

}


/* اختيار نوع اللعبة */

function startGame(selectedMode, button) {

    mode = selectedMode;

    document.querySelectorAll(".mode-btn").forEach(b => {
        b.classList.remove("active");
    });

    button.classList.add("active");

    document.getElementById("gameArea").classList.remove("hidden");

    resetGame();
}


/* لعبة جديدة */

function resetGame() {

    board = ["","","","","","","","",""];

    current = "X";
    finished = false;

    document.querySelectorAll(".cell").forEach(cell => {

        cell.textContent = "";
        cell.disabled = false;
        cell.className = "cell";

    });

    document.getElementById("status").textContent =
        "دور اللاعب X";

}


/* حركة اللاعب */

function play(index) {

    if (finished || board[index] !== "") {
        return;
    }

    if (mode === "computer" && current === "O") {
        return;
    }

    makeMove(index, current);

    if (!finished && mode === "computer" && current === "O") {

        setTimeout(computerMove, 450);

    }

}


/* تنفيذ الحركة */

function makeMove(index, player) {

    board[index] = player;

    const cells = document.querySelectorAll(".cell");

    cells[index].textContent = player;

    cells[index].classList.add(player.toLowerCase());

    cells[index].disabled = true;

    sound(
        player === "X" ? 560 : 430,
        0.13,
        "sine"
    );

    const winner = checkWinner();

    if (winner) {

        finished = true;

        document.getElementById("status").textContent =
            winner === "X"
            ? "مبروك! اللاعب X فاز ♡"
            : winner === "O"
            ? (mode === "computer"
                ? "الكمبيوتر فاز ♡"
                : "مبروك! اللاعب O فاز ♡")
            : "تعادل! جربوا مرة ثانية ♡";

        sound(700, 0.25, "sine");

        setTimeout(() => {
            sound(880, 0.35, "sine");
        }, 180);

        cells.forEach(c => {
            c.disabled = true;
        });

        return;

    }

    if (board.every(cell => cell !== "")) {

        finished = true;

        document.getElementById("status").textContent =
            "تعادل! جربوا مرة ثانية ♡";

        sound(350, 0.3);

        return;

    }

    current = player === "X" ? "O" : "X";

    document.getElementById("status").textContent =
        mode === "computer" && current === "O"
        ? "دور الكمبيوتر..."
        : "دور اللاعب " + current;

}


/* فحص الفوز */

function checkWinner() {

    for (const combo of wins) {

        const [a,b,c] = combo;

        if (
            board[a] &&
            board[a] === board[b] &&
            board[a] === board[c]
        ) {

            return board[a];

        }

    }

    return null;

}


/* حركة الكمبيوتر */

function computerMove() {

    if (finished) {
        return;
    }

    let move = findBestMove("O");

    if (move === -1) {
        move = findBestMove("X");
    }

    if (move === -1 && board[4] === "") {
        move = 4;
    }

    if (move === -1) {

        const empty = board
            .map((v,i) => v === "" ? i : -1)
            .filter(i => i !== -1);

        move = empty[
            Math.floor(Math.random() * empty.length)
        ];

    }

    if (move !== undefined && move >= 0) {
        makeMove(move, "O");
    }

}


/* البحث عن حركة رابحة */

function findBestMove(player) {

    for (let i = 0; i < 9; i++) {

        if (board[i] !== "") {
            continue;
        }

        board[i] = player;

        const won = checkWinner() === player;

        board[i] = "";

        if (won) {
            return i;
        }

    }

    return -1;

}


/* تشغيل وإيقاف الموسيقى */

function toggleMusic() {

    if (musicOn) {

        clearInterval(musicTimer);

        musicOn = false;

        document.getElementById("musicBtn").textContent =
            "♫ تشغيل الموسيقى";

        return;

    }

    audioContext = audioContext ||
        new (window.AudioContext || window.webkitAudioContext)();

    if (audioContext.state === "suspended") {
        audioContext.resume();
    }

    musicOn = true;

    document.getElementById("musicBtn").textContent =
        "♫ إيقاف الموسيقى";

    const melody = [
        523, 659, 784, 659,
        587, 698, 880, 698
    ];

    function playNote() {

        sound(
            melody[noteIndex % melody.length],
            0.32,
            "sine",
            0.035
        );

        noteIndex++;

    }

    playNote();

    musicTimer = setInterval(playNote, 420);

}

</script>

</body>
</html>
"""

components.html(
    html,
    height=790,
    scrolling=False
)
