document.addEventListener("DOMContentLoaded", () => {
    console.log("JS загружен!"); // Вывод при загрузке

    const container = document.querySelector(".carousel-container");
    const prev = document.querySelector(".prev");
    const next = document.querySelector(".next");

    let index = 0;

    next.addEventListener("click", () => {
        console.log("Клик по NEXT!"); // Проверка клика
        if (index < container.children.length - 4) {
            index++;
            container.style.transform = `translateX(-${index * 25}%)`;
        }
    });

    prev.addEventListener("click", () => {
        console.log("Клик по PREV!"); // Проверка клика
        if (index > 0) {
            index--;
            container.style.transform = `translateX(-${index * 25}%)`;
        }
    });
});
