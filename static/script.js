const form = document.getElementById("form")
const hwContainer = document.getElementById("hw");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const name = form.elements.name.value;
    const schoolClass = form.elements.class.value;

    await fetch("/hw", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "name": name,
            "class": schoolClass
        })
    });

    form.reset();
    await loadThings();
});

async function loadThings() {
    const res = await fetch("/hw");
    const hw = await res.json();

    hwContainer.innerHTML = "";
    
    hw.array.forEach(element => {
        const item = document.createElement("p");
        item.textContent = `${element.class}: ${element.name}`;
        hwContainer.appendChild(item);
    });
};

loadThings();