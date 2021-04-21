/* The add new card button */
var add_new_card_button = document.getElementById("add-new-card-button");

/* The whole container for the add new card button */
var add_new_card_button_container = document.getElementById("add-new-card");

/* The list of weather cards */
var weather_card_list = document.getElementById("weather-card-list");

/* Add and event listener to the add new card button
 * so that we can add new weather cards on click */
add_new_card_button.addEventListener("click", (event) => {
  let weather_card = new_weather_card();
  weather_card_list.appendChild(weather_card);
  move_add_new_card_button(weather_card_list, add_new_card_button_container);
});

/**
 * This function returns a full weather card.
 * @returns a weather card with the right css and child elements
 */
function new_weather_card() {
  let new_list_item = document.createElement("li");
  let new_card_container = document.createElement("div");
  let new_card_body = document.createElement("div");
  let new_card_paragraph = document.createElement("p");

  new_card_container.classList.add("card");
  new_card_container.classList.add("weather-card");
  new_card_body.classList.add("card-body");

  let text = document.createTextNode("some text");
  new_card_paragraph.appendChild(text);

  new_card_body.appendChild(new_card_paragraph);
  new_card_container.appendChild(new_card_body);
  new_list_item.appendChild(new_card_container);

  return new_list_item;
}

function move_add_new_card_button(card_list, add_new_card_button) {
  card_list.appendChild(add_new_card_button);
}
