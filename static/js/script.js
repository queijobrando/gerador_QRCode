function downloadQRCode() {
    let imgElement = document.getElementById("qrcode");
    let imageURL = imgElement.src;

    let fileName = prompt("Digite o nome do arquivo:", "qrcode");
    if (!fileName) return; // Se o usuário cancelar, não faz nada.

    let link = document.createElement("a");
    link.href = imageURL;
    link.download = fileName + ".png"; // Define o nome do arquivo
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}