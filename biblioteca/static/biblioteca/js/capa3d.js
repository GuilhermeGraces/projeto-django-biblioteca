const INCLINACAO = 25;

const capas = document.querySelectorAll(".capa-3d");

capas.forEach(function (capa) {
    capa.addEventListener("mousemove", function (evento) {
        const caixa = capa.getBoundingClientRect();
        const x = ((evento.clientX - caixa.left) / caixa.width) * 2 - 1;
        const y = ((evento.clientY - caixa.top) / caixa.height) * 2 - 1;
        capa.style.transform = `perspective(400px) rotateX(${-y * INCLINACAO}deg) rotateY(${x * INCLINACAO}deg) scale(1.05)`;
    });

    capa.addEventListener("mouseleave", function () {
        capa.style.transform = "";
    });
});