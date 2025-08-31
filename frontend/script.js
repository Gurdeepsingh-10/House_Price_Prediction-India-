const API_URL = "http://localhost:8000";  // Update if needed

// Load locations on page load
window.onload = async () => {
    try {
        const response = await fetch(`${API_URL}/locations`);
        const data = await response.json();
        const locationSelect = document.getElementById("location");

        data.locations.forEach(loc => {
            const option = document.createElement("option");
            option.value = loc;
            option.textContent = loc;
            locationSelect.appendChild(option);
        });
    } catch (error) {
        console.error("Error fetching locations:", error);
    }
};

// Handle form submission
document.getElementById("prediction-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = {
        location: document.getElementById("location").value,
        bhk: parseInt(document.getElementById("bhk").value),
        bathrooms: parseInt(document.getElementById("bathrooms").value),
        area: parseFloat(document.getElementById("area").value),
        status: document.getElementById("status").value,
        furnishing: document.getElementById("furnishing").value,
        transaction: document.getElementById("transaction").value,
        type: document.getElementById("type").value,
    };

    try {
        const response = await fetch(`${API_URL}/predict`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
        });

        const result = await response.json();
        document.getElementById("result").innerHTML = `<h2>🏷️ Predicted Price: ₹ ${Math.round(result.prediction).toLocaleString()}</h2>`;
    } catch (error) {
        document.getElementById("result").innerHTML = `<p style="color: red;">❌ Failed to predict: ${error.message}</p>`;
    }
});
