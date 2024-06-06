const copyToClipboard = async () => {
    try {
        const element = document.querySelector(".user-select-all");
        await navigator.clipboard.writeText(element.value);
    } catch (error) {
        console.error("Failed to copy to clipboard:", error);
    }
    alert("Link copied, shawty!");
};