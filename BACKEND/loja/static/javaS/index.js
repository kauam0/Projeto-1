function scrollContainer(direction, containerSelector) {
    const container = document.querySelector(containerSelector);
    const scrollAmount = 305; // Ajuste a quantidade de rolagem se necessário
    container.scrollBy({
        left: direction * scrollAmount,
        behavior: 'smooth'
    });

}

