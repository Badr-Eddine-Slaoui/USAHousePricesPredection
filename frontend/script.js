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
