async function localhost() {
    const response = await
    fetch("http://localhost:8080/gravar");
    const localhost = await response.json();
    console.log(localhost);
}