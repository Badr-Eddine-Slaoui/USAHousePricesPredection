const form = document.getElementById("predictionForm");

const button = document.getElementById("predictButton");
const buttonText = document.getElementById("buttonText");
const buttonArrow = document.getElementById("buttonArrow");
const spinner = document.getElementById("spinner");

const errorMessage = document.getElementById("errorMessage");

const resultPlaceholder =
    document.getElementById("resultPlaceholder");

const result =
    document.getElementById("result");

const predictedPrice =
    document.getElementById("predictedPrice");


const API_URL = "http://127.0.0.1:8000/predict";


function getValue(id) {
    return document.getElementById(id).value;
}


function getNumber(id) {
    return Number(getValue(id));
}


function setLoading(loading) {
    button.disabled = loading;

    if (loading) {
        buttonText.textContent = "Predicting...";
        buttonArrow.classList.add("hidden");
        spinner.classList.remove("hidden");
        button.classList.add("opacity-70", "cursor-not-allowed");
    } else {
        buttonText.textContent = "Predict house price";
        buttonArrow.classList.remove("hidden");
        spinner.classList.add("hidden");
        button.classList.remove("opacity-70", "cursor-not-allowed");
    }
}


function showError(message) {
    errorMessage.textContent = message;
    errorMessage.classList.remove("hidden");
}


function hideError() {
    errorMessage.classList.add("hidden");
}


function showPrediction(price) {
    resultPlaceholder.classList.add("hidden");

    result.classList.remove("hidden");

    result.classList.remove("result-animation");

    // Restart animation
    void result.offsetWidth;

    result.classList.add("result-animation");

    predictedPrice.textContent =
        new Intl.NumberFormat("en-US", {
            style: "currency",
            currency: "USD",
            maximumFractionDigits: 0
        }).format(price);
}


form.addEventListener("submit", async (event) => {
    event.preventDefault();

    hideError();
    setLoading(true);

    try {
        const data = {
            bedrooms: getNumber("bedrooms"),
            bathrooms: getNumber("bathrooms"),

            sqft_living: getNumber("sqft_living"),
            sqft_lot: getNumber("sqft_lot"),

            floors: getNumber("floors"),

            waterfront: getNumber("waterfront"),
            view: getNumber("view"),
            condition: getNumber("condition"),
            grade: getNumber("grade"),

            sqft_above: getNumber("sqft_above"),
            sqft_basement: getNumber("sqft_basement"),

            yr_built: getNumber("yr_built"),
            yr_renovated: getNumber("yr_renovated"),

            zipcode: getNumber("zipcode"),

            lat: getNumber("lat"),
            long: getNumber("long"),

            sqft_living15: getNumber("sqft_living15"),
            sqft_lot15: getNumber("sqft_lot15"),

            date: `${getValue("date")}T00:00:00`
        };


        const response = await fetch(API_URL, {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(data)
        });


        if (!response.ok) {
            const error = await response.json();

            throw new Error(
                error.detail || "Prediction request failed."
            );
        }


        const prediction = await response.json();

        showPrediction(prediction.predicted_price);

    } catch (error) {

        console.error(error);

        showError(
            error.message ||
            "Unable to connect to the prediction API."
        );

    } finally {
        setLoading(false);
    }
});