var add_new_card_button = document.getElementById("add-new-card-button");
var weather_card_container = document.getElementById("weather-card-container");
add_new_card_button.addEventListener("click", (event) => {
  let new_weather_card = document.createElement("div");
  new_weather_card.id = "card weather-card";
  weather_card_container.appendChild(new_weather_card);
});
